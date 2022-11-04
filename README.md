Fast (7-9 sec) proxy subnet check implemented with asyncio and httpx.

Made to check entire subnets /24, /25 etc

## Usage
```
./async-check-proxy.py -c login:pass -p port -s 10.10.10.0/24 -ip 192.168.1.1
```
-c - login and password http proxy

-p - proxy port

-s - subnet

-ip - ip for single proxy

Username and password must be the same for everyone.

Example of output
```
http://login:pass@10.10.10.0:8080 - Bad proxy!
http://login:pass@10.10.10.255:8080 - Bad proxy!
2
```
This means there is no proxy for ip .0 and .255 or they don't work

2 - how many non-working proxies

To display only the number of non-working proxies, comment string
```
        print (proxy, "- Bad proxy!")
```

If you need to print response code, uncomment string
```
        #print(proxy, response.status_code)
```

Script uses google site for checking. You can change this
```
    url = "http://google.com/"
```

## Issues
Doesn't work well with network anymore /23. Use in parts /24.