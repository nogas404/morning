import covid_stats

from send_email import send_email

from get_feed import main, get_urls

import asyncio

urls = get_urls('rss-feed.txt')

results = asyncio.run(main(urls))

print(results)

send_email(results)