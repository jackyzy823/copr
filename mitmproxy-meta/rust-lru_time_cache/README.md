---- test::iter::it_yields_the_most_recent_items_first stdout ----

thread 'test::iter::it_yields_the_most_recent_items_first' (34015) panicked at src/lib.rs:735:13:
assertion `left == right` failed
  left: [(3, 1), (3, 3), (0, 0), (2, 2)]
 right: [(1, 1), (3, 3), (0, 0), (2, 2)]
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

---- test::notify_iter::it_yields_the_most_recent_items_first stdout ----

thread 'test::notify_iter::it_yields_the_most_recent_items_first' (34021) panicked at src/lib.rs:783:13:
assertion `left == right` failed
  left: [(3, 1), (3, 3), (0, 0), (2, 2)]
 right: [(1, 1), (3, 3), (0, 0), (2, 2)]


failures:
    test::iter::it_yields_the_most_recent_items_first
    test::notify_iter::it_yields_the_most_recent_items_first

test result: FAILED. 22 passed; 2 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.90s



This looks like should not skip checking, it is a fatal fail

However 
when do 
`lru_cache.iter().for_each(|x| println!("{:#?}",x));` the result is ok?


----- Answer from Gemini ---

Question: In  https://github.com/maidsafe/lru_time_cache 's test test::iter::it_yields_the_most_recent_items_first , result assertion `left == right` failed

 left: [(3, 1), (3, 3), (0, 0), (2, 2)]

right: [(1, 1), (3, 3), (0, 0), (2, 2)]

, but if you use `lru_cache.iter().for_each(|x| println!("{:#?}",x));` instead of ` let cached = lru_cache.iter().collect::<Vec<_>>();` , the result is correct. 


so The problem is 1) why the first object's key is modified?  2) Why it pass the test with rustc 1.65.0 but not with rustc 1.96.0, find what changed internally in rustc


Answer:

This is a fascinating issue that directly highlights a subtle quirk regarding how Rust's iterators work under the hood, coupled with an optimization change introduced in newer `rustc` versions.

Here is exactly what is happening to cause this disparity.

---

## 1. Why is the first object's key modified in `collect()`?

The first element's key isn't *actually* modified during the iteration itself. What you are witnessing is a side effect of **`lru_time_cache::Iter` updating internal metadata** while you advance the iterator.

According to `lru_time_cache`'s documentation:

> `Iter`: An iterator over an `LruCache`'s entries that **updates the timestamps as values are traversed**. Values are produced in the most recently used order.

Because the cache elements contain pointers or internal references tracking their "freshness", calling `.next()` updates the internal structure of the cache to reflect that the item was just touched.

### Why `collect()` breaks but `for_each(println!)` works

* **When using `for_each` + `println!`, elements are evaluated and printed eagerly one by one.** When the iterator reaches the first element, it yields references to it, you print it immediately (showing `(1, 1)`), and *then* the iterator advances to the next item. Any structural reordering or side effects caused by moving to the next item happen *after* you have already printed the current one.
* **When using `collect::<Vec<_>>()**`, you are compiling a collection of references to elements inside the cache. Because `rustc` 1.96.0 optimizes memory layouts and loops differently (via `BTreeMap` or internal heap adjustments), the iterator triggers internal updates (mutating structural pointers/timestamps under the hood) *while* you are still collecting references to the rest of the elements. Because your `Vec` holds references to the data inside the cache, mutating the cache's structure can retrospectively change what those references point to by the time the `Vec` is fully built and asserted.

---

## 2. Why did it pass in `rustc 1.65.0` but fail in `rustc 1.96.0`?

The root cause lies in how **`Iterator::collect` is optimized internally** between these two compiler versions.

### In `rustc 1.65.0` (Eager/Sequential Evaluation)

Older versions of Rust compiled `collect::<Vec<_>>()` as a straightforward loop that essentially did:

```rust
let mut vec = Vec::with_capacity(hint);
while let Some(item) = iter.next() {
    vec.push(item);
}

```

Because it was entirely linear, the item `(1, 1)` was read, pushed into the vector, and its state was captured before the subsequent `.next()` calls could retroactively mangle its reference space.

### In `rustc 1.96.0` (Internal Specialization & TrustedLen)

Newer versions of the standard library heavily utilize `InPlaceIterable`, `TrustedLen`, and **Internal Iterator Specialization** (like `fold`-based or `next_chunk`-based collection).

Instead of treating `collect()` as a naive `while let` loop, `rustc 1.96.0` frequently optimizes `collect()` by utilizing `Iterator::try_fold` or processing elements in unrolled blocks/chunks to maximize CPU register efficiency.

* This causes the compiler to evaluate or "look ahead" at iterator steps differently.
* Because `lru_time_cache` relies on side effects during traversal (updating timestamps/LRU tracking on every `.next()` call), changing the sequence or batching of how those evaluations are rolled out causes the underlying cache memory layout to shift *before* the references inside your `Vec` are completely finalized.

### The Underlying Bug in `lru_time_cache`

The `lru_time_cache` crate is quite old and contains internal architecture that implicitly relies on a strict execution order of `.next()`. By upgrading the compiler, you gave `rustc` permission to optimize the assembly loop of `collect()`, which inadvertently triggered the crate's internal timestamp updates out of the exact sequential order the original test expected.

### The Fix

If you want to view or test the contents of the cache without mutating its internal state during the iteration, you should use **`PeekIter`** instead of `Iter`:

```rust
// Use peek_iter() instead of iter() so timestamps/structures don't change during collection
let cached = lru_cache.peek_iter().collect::<Vec<_>>();

```
