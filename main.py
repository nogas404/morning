import covid_stats

from send_email import send_email

from get_feed import main, get_urls

import asyncio
import os

urls = get_urls('rss-feed.txt')

print(urls)

results = asyncio.run(main(urls))

print(results)



files = ['covid_daily.jpeg', 'mgram_pict.png']

send_email(results, files)
