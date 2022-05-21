import feedparser
import asyncio
import time


# VARIABLES
## in how many hours does your script update
UPDATE_PERIOD = 49

# what time was the time of last update
#                               UNIX TIME       - X hours
time_of_last_sync = time.gmtime(int(time.time() - UPDATE_PERIOD * 3600))

# get urls from file
def get_urls(file_name):
    urls = []
    with open(file_name, 'r') as f:
        for x in f:
            if x.split()[0].startswith('http'):
                urls.append(x.split()[0])
    return urls


# get feeds from web and filter them (by date)
async def get_feeds(x):
    a = feedparser.parse(x)
    results_feed = []
    
    for i, x in enumerate(a.entries):
        if i > 10:
            pass
        else:
            entry_time = x.published_parsed
        
            # if time of publishing is sonner than of last sync then get results
            if entry_time > time_of_last_sync:
                results_feed.append(x['link'])
                print(x['link'])
    
    # return results
    if results_feed is not []:
        return results_feed

# this function executes get_feeds function in async
async def main(urls):
    results = []
    for x in urls:
        results += ( await asyncio.create_task(get_feeds(x)) )
    return results


if __name__=='__main__':
    urls = get_urls('rss-feed.txt')

    a = asyncio.run(main(urls))
    print(a)
