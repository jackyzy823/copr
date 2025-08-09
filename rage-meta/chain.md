rage
Problem 1: nothing provides requested (crate(age/armor) >= 0.11.1 with crate(age/armor) < 0.12.0~)                                     
 Problem 2: nothing provides requested (crate(age/cli-common) >= 0.11.1 with crate(age/cli-common) < 0.12.0~)                          
 Problem 3: nothing provides requested (crate(age/default) >= 0.11.1 with crate(age/default) < 0.12.0~)                                                                                                                                                                       
 Problem 4: nothing provides requested (crate(age/plugin) >= 0.11.1 with crate(age/plugin) < 0.12.0~)                                  
 Problem 5: nothing provides requested (crate(age/ssh) >= 0.11.1 with crate(age/ssh) < 0.12.0~)                                        
 Problem 6: nothing provides requested (crate(fuse_mt/default) >= 0.6.0 with crate(fuse_mt/default) < 0.7.0~)                                                                                                                                                                 
 Problem 7: nothing provides requested (crate(fuser/default) >= 0.13.0 with crate(fuser/default) < 0.14.0~)
 Problem 8: nothing provides requested (crate(i18n-embed-fl/default) >= 0.9.0 with crate(i18n-embed-fl/default) < 0.10.0~)
 Problem 9: nothing provides requested (crate(i18n-embed/default) >= 0.15.0 with crate(i18n-embed/default) < 0.16.0~)
 Problem 10: nothing provides requested (crate(i18n-embed/desktop-requester) >= 0.15.0 with crate(i18n-embed/desktop-requester) < 0.16.0~)
 Problem 11: nothing provides requested (crate(i18n-embed/fluent-system) >= 0.15.0 with crate(i18n-embed/fluent-system) < 0.16.0~)
OK Problem 12: nothing provides requested (crate(pinentry/default) >= 0.6.0 with crate(pinentry/default) < 0.7.0~)                       
 Problem 13: nothing provides requested (crate(time/default) >= 0.3.7 with crate(time/default) < 0.3.24~)                              
have compat rust-trycmd0.14 but dead package
NEED TO DOWNGRADE FEDORA HAS 0.15 BUT WE REQUIRE 0.14 Problem 14: nothing provides requested (crate(trycmd/default) >= 0.14.0 with crate(trycmd/default) < 0.15.0~)

for fedora-rawhide
Problem 1: nothing provides requested (crate(console) >= 0.15.0 with crate(console) < 0.16.0~)
 Problem 2: package rust-age+cli-common-devel-0.11.1-1.fc43.noarch from copr_base requires crate(age/console) = 0.11.1, but none of the providers can be installed
  - conflicting requests
  - nothing provides (crate(console) >= 0.15.0 with crate(console) < 0.16.0~) needed by rust-age+console-devel-0.11.1-1.fc43.noarch from copr_base

age
 dnf install noarch/* --skip-broken (for wsl web-sys plugin)
  plugin is  required by rage , which depends on wsl

 OK Problem 1: nothing provides requested (crate(age-core/default) >= 0.11.0 with crate(age-core/default) < 0.12.0~)                       
 OK NOT THE LATEST 0.11 BUT 0.9 Problem 2: nothing provides requested (crate(bech32/default) >= 0.9.0 with crate(bech32/default) < 0.10.0~)                           
 OK SUB Problem 3: nothing provides requested (crate(chacha20poly1305) >= 0.10.0 with crate(chacha20poly1305) < 0.11.0~)                      
 OK SUB Problem 4: nothing provides requested (crate(chacha20poly1305/alloc) >= 0.10.0 with crate(chacha20poly1305/alloc) < 0.11.0~)          
 OK Problem 2: nothing provides requested (crate(i18n-embed-fl/default) >= 0.9.0 with crate(i18n-embed-fl/default) < 0.10.0~)
 OK Problem 3: nothing provides requested (crate(i18n-embed/default) >= 0.15.0 with crate(i18n-embed/default) < 0.16.0~)
 OK Problem 4: nothing provides requested (crate(i18n-embed/desktop-requester) >= 0.15.0 with crate(i18n-embed/desktop-requester) < 0.16.0~)
 OK Problem 5: nothing provides requested (crate(i18n-embed/fluent-system) >= 0.15.0 with crate(i18n-embed/fluent-system) < 0.16.0~)

 ONLY INSTALL NECESSARY PACKAGES dnf install noarch/rust-i18n-embed+default-devel-0.15.4-1.fc43.noarch.rpm noarch/rust-i18n-embed-devel-0.15.4-1.fc43.noarch.rpm noarch/rust-i18n-embed+rust-embed-devel-0.15.4-1.fc43.noarch.rpm noarch/rust-i18n-embed+fluent-system-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+desktop-requester-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+arc-swap-devel-0.15.4-1.fc43.noarch.rpm noarch/rust-i18n-embed+fluent-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+fluent-syntax-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+i18n-embed-impl-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+parking_lot-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+locale_config-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+filesystem-assets-devel-0.15.4-1.fc43.noarch.rpm  noarch/rust-i18n-embed+walkdir-devel-0.15.4-1.fc43.noarch.rpm 

SKIP TESTS
 Problem 6: nothing provides requested (crate(pprof/default) >= 0.13.0 with crate(pprof/default) < 0.14.0~)
 Problem 7: nothing provides requested (crate(pprof/flamegraph) >= 0.13.0 with crate(pprof/flamegraph) < 0.14.0~)


age-core
 OK Problem 1: nothing provides requested (crate(chacha20poly1305) >= 0.10.0 with crate(chacha20poly1305) < 0.11.0~) 
 OK Problem 2: nothing provides requested (crate(chacha20poly1305/alloc) >= 0.10.0 with crate(chacha20poly1305/alloc) < 0.11.0~)
 OK Problem 3: nothing provides requested (crate(io_tee/default) >= 0.1.1 with crate(io_tee/default) < 0.2.0~)
 UPGRADE Problem 4: nothing provides requested (crate(secrecy/default) >= 0.10.0 with crate(secrecy/default) < 0.11.0~)

pinentry
 secrecy/default

i18n-embed-fl
test failed due to nightly features
Problem 1: nothing provides requested (crate(i18n-embed/default) >= 0.15.4 with crate(i18n-embed/default) < 0.16.0~)
 Problem 2: nothing provides requested (crate(i18n-embed/filesystem-assets) >= 0.15.4 with crate(i18n-embed/filesystem-assets) < 0.16.0~)
 Problem 3: nothing provides requested (crate(i18n-embed/fluent-system) >= 0.15.4 with crate(i18n-embed/fluent-system) < 0.16.0~)


fuse_mt
 LATEST 0.15 , REQUIRE 0.13        (crate(fuser/default) >= 0.13.0 with crate(fuser/default) < 0.14.0~) is needed by rust-fuse_mt-0.6.1-1.fc43.x86_64
        (crate(threadpool/default) >= 1.8.0 with crate(threadpool/default) < 2.0.0~) is needed by rust-fuse_mt-0.6.1-1.fc43.x86_64

fuser
edit dep
Problem: nothing provides requested (crate(page_size/default) >= 0.5.0 with crate(page_size/default) < 0.6.0~)


since 
fuser requires pkgconfig(fuse3) so fuse_mt requires pkgconfig(fuse3) too , so rage requires too
