1. edit -> disable check

# [github.com/Shopify/ejson/crypto]
./crypto_test.go:66:1: ExampleEncrypt should be niladic
./crypto_test.go:66:1: ExampleEncrypt refers to unknown identifier: Encrypt
./crypto_test.go:77:1: ExampleDecrypt should be niladic
./crypto_test.go:77:1: ExampleDecrypt refers to unknown identifier: Decrypt
FAIL    github.com/Shopify/ejson/crypto [build failed]

Because crypto_test.go 's example: ExampleEncrypt/ExampleDecrypt function name and arguments didn't fit govet requirement.
https://github.com/golangci/govet/blob/master/tests.go#L83
https://stackoverflow.com/questions/62627924/go-vet-warns-that-example-refers-to-unknown-identifier-but-why


So we should patch to delete these two functions


diff --git a/crypto/crypto_test.go b/crypto/crypto_test.go
index 3261ced..00d4e1c 100644
--- a/crypto/crypto_test.go
+++ b/crypto/crypto_test.go
@@ -62,25 +62,3 @@ func TestRoundtrip(t *testing.T) {
 		So(len(ct), ShouldBeGreaterThan, len(pt))
 	})
 }
-
-func ExampleEncrypt(peerPublic [32]byte) {
-	var kp Keypair
-	if err := kp.Generate(); err != nil {
-		panic(err)
-	}
-
-	encrypter := kp.Encrypter(peerPublic)
-	boxed, err := encrypter.Encrypt([]byte("this is my message"))
-	fmt.Println(boxed, err)
-}
-
-func ExampleDecrypt(myPublic, myPrivate [32]byte, encrypted []byte) {
-	kp := Keypair{
-		Public:  myPublic,
-		Private: myPrivate,
-	}
-
-	decrypter := kp.Decrypter()
-	plaintext, err := decrypter.Decrypt(encrypted)
-	fmt.Println(plaintext, err)
-}



Or use 
%global gotestflags -vet=off %{gotestflags}
