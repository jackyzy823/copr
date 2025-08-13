1. edit -> disable check

or bypass vet check with `%global gotestflags -vet=off %{gotestflags}`


# [github.com/dustin/gojson]
./decode.go:602:17: fmt.Errorf call needs 1 arg but has 2 args
./decode_test.go:1088:3: (*testing.common).Fatalf format %v reads arg #1, but call has 0 args
./scanner.go:608:21: conversion from int to string yields a string of one rune, not a string of digits
FAIL    github.com/dustin/gojson [build failed]

First two line could be fixed with
https://github.com/golang/go/commit/2c987e16937a6abf907ab230b04d42c071a388f5

Last one could be fixed with
https://github.com/golang/go/commit/fcf8143d638dbc34fdd418f45f8e8b45de802916



