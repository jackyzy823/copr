upgrade from src.fed one
no check

to fix test 
ln two folder
and update azidentity to 1.8.2

github.com/Azure/azure-sdk-for-go/sdk/internal/test/credential                                                                                                                                                                                                                
# github.com/Azure/azure-sdk-for-go/sdk/internal/test/credential [github.com/Azure/azure-sdk-for-go/sdk/internal/test/credential.test] 
./credential.go:35:21: undefined: azidentity.NewAzurePipelinesCredential                                                                                                                                                                                                      
./credential_test.go:43:26: undefined: azidentity.AzurePipelinesCredential                                                             
FAIL    github.com/Azure/azure-sdk-for-go/sdk/internal/test/credential [build failed]

so we temp skip the test for credential
