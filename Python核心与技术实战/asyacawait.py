"""
协程
"""
import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
    end_time = time.perf_counter()
    print('cost {} seconds'.format(end_time - start_time))


