use <= 0.12.7

use 0.12.6 
since https://github.com/mitmproxy/mitmproxy_rs/commit/41c202ea1b14fa1c4153bf4824c01fafa6e1fc87#diff-e44d46086614c4a0a7219497cfc85ca7c670855a41c088075ad52d4f25a04fee


error[E0308]: mismatched types
  --> src/packet_sources/wireguard.rs:77:17
   |
77 |                 tunnel,
   |                 ^^^^^^ expected `Tunn`, found `Result<Tunn, &str>`
   |
   = note: expected struct `Tunn`
                found enum `Result<Tunn, &str>`
help: use the `?` operator to extract the `Result<Tunn, &str>` value, propagating a `Result::Err` value to the caller
   |
77 |                 tunnel: tunnel?,
   |                       +++++++++



