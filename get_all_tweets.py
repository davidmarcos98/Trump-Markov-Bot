from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.firefox.options import Options

import json
import datetime

# Modified - Original script by bpb27 https://github.com/bpb27/twitter_scraping

# edit this variable
user = 'realdonaldtrump'
max_tweets = 15000 #maximum number of tweets to be retrieved

def format_day(date):
    day = '0' + str(date.day) if len(str(date.day)) == 1 else str(date.day)
    month = '0' + str(date.month) if len(str(date.month)) == 1 else str(date.month)
    year = str(date.year)
    return '-'.join([year, month, day])

def form_url(since, until):
    p1 = 'https://twitter.com/search?f=tweets&vertical=default&q=from%3A'
    p2 =  user + '%20since%3A' + since + '%20until%3A' + until + 'include%3Aretweets&src=typd'
    print(p1+p2)
    return p1 + p2

def increment_day(date, i):
    return date - datetime.timedelta(days=i)

def get_tweets():
    #you can also edit the time interval in which you want to look for tweets
    start = datetime.datetime(2010, 1, 1)  # year, month, day
    end = datetime.datetime(2018, 8, 30)  # year, month, day
    global user
    # only edit these if you're having problems
    opts = Options()
    opts.set_headless()
    assert opts.headless  # Operating in headless mode
    driver = webdriver.Firefox(options=opts)  # options are Chrome() Firefox() Safari()

    # don't mess with this stuff
    twitter_ids_filename = 'all_ids.json'
    days = (end - start).days + 1
    id_selector = '.time a.tweet-timestamp'
    tweet_selector = 'li.js-stream-item'
    user = user.lower()
    ids = []


    while end > start and len(ids) < max_tweets:
        d1 = format_day(increment_day(end, 15))
        d2 = format_day(increment_day(end, 0))
        print(d1)
        url = form_url(d1, d2)
        driver.get(url)
        try:
            found_tweets = driver.find_elements_by_css_selector(tweet_selector)
            increment = 10

            while len(found_tweets) >= increment:
                print('scrolling down to load more tweets')
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                found_tweets = driver.find_elements_by_css_selector(tweet_selector)
                increment += 10

            print('{} tweets found, {} total'.format(len(found_tweets), len(ids)))

            for tweet in found_tweets:
                try:
                    id = tweet.find_element_by_css_selector(id_selector).get_attribute('href').split('/')[-1]
                    ids.append(id)
                except StaleElementReferenceException as e:
                    print('lost element reference', tweet)

        except NoSuchElementException:
            print('no tweets on this day')

        end = increment_day(end, 15)

    try:
        with open(twitter_ids_filename) as f:
            all_ids = ids + json.load(f)
            data_to_write = list(set(all_ids))
            print('tweets found on this scrape: ', len(ids))
            print('total tweet count: ', len(data_to_write))
    except FileNotFoundError:
        with open(twitter_ids_filename, 'w') as f:
            all_ids = ids
            data_to_write = list(set(all_ids))
            print('tweets found on this scrape: ', len(ids))
            print('total tweet count: ', len(data_to_write))

    with open(twitter_ids_filename, 'w') as outfile:
        json.dump(data_to_write, outfile)

    print('all done here')
    driver.close()


get_tweets()
