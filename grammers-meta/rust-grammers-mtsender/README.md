Problem 1: nothing provides requested (crate(locate-locale/default) >= 0.2.0 with crate(locate-locale/default) < 0.3.0~)
 Problem 2: nothing provides requested (crate(os_info) >= 3.14.0 with crate(os_info) < 4.0.0~)
	Update Fedora's one from 3.12 to
 Problem 3: nothing provides requested (crate(simple_logger) >= 5.2.0 with crate(simple_logger) < 6.0.0~)
 Problem 4: nothing provides requested (crate(simple_logger/colors) >= 5.2.0 with crate(simple_logger/colors) < 6.0.0~)

	Update Fedora's one from 4.3 to
	Just skip , see grammers-mtsender/DEPS.md: Used in the tests in order to debug with more information when things go wrong.
 Problem 5: nothing provides requested (crate(socks5-server/default) >= 0.10.1 with crate(socks5-server/default) < 0.11.0~)
	Just skip, see grammers-mtsender/DEPS.md: Used to test for SOCKS5 proxy support.


Runtime:
Problem 1: conflicting requests
  - nothing provides (crate(async-http-proxy/basic-auth) >= 1.2.5 with crate(async-http-proxy/basic-auth) < 2.0.0~) needed by rust-grammers-mtsender+async-http-proxy-devel-0.9.0-1.fc45.noarch from @commandline
  - nothing provides (crate(async-http-proxy/default) >= 1.2.5 with crate(async-http-proxy/default) < 2.0.0~) needed by rust-grammers-mtsender+async-http-proxy-devel-0.9.0-1.fc45.noarch from @commandline
  - nothing provides (crate(async-http-proxy/runtime-tokio) >= 1.2.5 with crate(async-http-proxy/runtime-tokio) < 2.0.0~) needed by rust-grammers-mtsender+async-http-proxy-devel-0.9.0-1.fc45.noarch from @commandline
 Problem 2: conflicting requests
  - nothing provides (crate(url/default) >= 2.5.8 with crate(url/default) < 3.0.0~) needed by rust-grammers-mtsender+url-devel-0.9.0-1.fc45.noarch from @commandline
 Problem 3: package rust-grammers-mtsender+proxy-devel-0.9.0-1.fc45.noarch from @commandline requires crate(grammers-mtsender/url) = 0.9.0, but none of the providers can be installed
  - conflicting requests
  - nothing provides (crate(url/default) >= 2.5.8 with crate(url/default) < 3.0.0~) needed by rust-grammers-mtsender+url-devel-0.9.0-1.fc45.noarch from @commandline
You can try to add to command line:
  --skip-broken to skip uninstallable packages

since we requires proxy feature, so ....
Update Fedora's rust-url from 2.5.7 to 2.5.8
package async-http-proxy
