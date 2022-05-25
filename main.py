import covid_stats

from send_email import send_email

from get_feed import main, get_urls

import asyncio, os

OTHER_URLS = os.getenv('OTHER_URLS')

urls = get_urls('rss-feed.txt')

urls += OTHER_URLS

print(urls)

results = asyncio.run(main(urls))

print(results)

files = ['covid_cases.jpeg', 'covid_tests.jpeg']

send_email(results, files)