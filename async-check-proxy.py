#!/usr/bin/python3.8

import argparse
import ipaddress
import asyncio
import httpx

parser = argparse.ArgumentParser(description='Import subnet, IP and credentials')

parser.add_argument("-s", "--subnet", type=str, help="Subnet for check", default=None)
parser.add_argument("-ip", type=str, help="IP for check", default=None)
parser.add_argument("-p", "--port", type=str, help="Proxy port")
parser.add_argument("-c", "--credentials", type=str, help="Credentials for check")

args = parser.parse_args()

port = args.port
ip = args.ip
subnet = args.subnet
credentials = args.credentials

net = []
fail = 0

if subnet:
    net_raw = ipaddress.ip_network(subnet)
    for x in net_raw:
        z = f'http://{credentials}@{x}:{port}'
        net.append(z)

if ip:
    net.append(f'http://{credentials}@{ip}:{port}')

async def call_url(url, proxy):
    global fail
    try:
        session = httpx.AsyncClient(proxies=proxy)
        response = await session.request(method='GET', url=url)
        #print(proxy, response.status_code)
        return response
    except (httpx.HTTPError, httpx.StreamError)  as exc:
        print (proxy, "- Bad proxy!")
        fail+=1
    finally:
        await session.aclose()

async def check_proxies():
    global fail
    url = "http://google.com/"
    await asyncio.gather(*[call_url(url, proxy) for proxy in net])
    print(fail)

asyncio.run(check_proxies())