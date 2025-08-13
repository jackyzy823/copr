1 no check
# github.com/charmbracelet/x/ansi/sixel [github.com/charmbracelet/x/ansi/sixel.test]                                                                                                                                                                                          
./encoder.go:187:26: s.pixelBands.GetWord64AtBit undefined (type bitset.BitSet has no field or method GetWord64AtBit)

maybe mismatched bitset dep version


https://github.com/bits-and-blooms/bitset/commit/8e4fa4952b25054fb5594e839b63c6a0639e0763
x-ansi 0.10.1 require bitset at least 1.15 (but we have 1.2 only)
latest 1.24 , and x-ansi require 1.22

we upgrade bitset to 1.24


x-ansi 0.8 do not require bitset's upgrade
glamour require 0.8 but chezmoi requires 0.10.1, so we must upgrade bitset 

2.  go monorepo 


