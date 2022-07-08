import covid_stats

from send_email import send_email

from get_feed import main, get_urls

import asyncio, os

urls = get_urls('rss-feed.txt')

print(urls)

results = asyncio.run(main(urls))

print(results)

files = ['covid_cases.jpeg', 'covid_tests.jpeg']

send_email(results, files)