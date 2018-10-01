from bs4 import BeautifulSoup
from credentials import *
import tweepy
import requests
import re
import schedule
import time

url = 'http://apostolicfaithweca.org/'


def retrieval(website_url):
    page = requests.get(website_url)
    souped = BeautifulSoup(page.text, 'html.parser')
    lesson_bible_ref = ""

    lesson_title = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[0]
    lesson_bible_ref_list = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[1].find_all(class_='bls')
    lesson_number = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[2]
    lesson_type = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[3]
    memory_verse = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[4]
    lesson_link = \
        souped.find_all(
            class_="view view-week-sunlessons view-id-week_sunlessons view-display-id-block_1 view-dom-id-3")[
            0].find_all(class_='field-content')[5].find('a', attrs={'href': re.compile("^/")})

    for ref in lesson_bible_ref_list:
        lesson_bible_ref += "[{}] ".format(ref.text.strip())

    tweet_line_0 = url[:-1] + lesson_link.get('href')
    tweet_line_1 = "Sunday School Weekly Lesson\n#AFMSundaySchool.\nFind out more at " + tweet_line_0 + \
                   "\nThe Sunday School lesson for this week is:"
    tweet_line_2 = lesson_title.text.strip()
    tweet_line_3 = lesson_bible_ref.strip()
    tweet_line_4 = lesson_number.text.strip() + " - " + lesson_type.text.strip()
    tweet_line_5 = "Memory Verse: " + memory_verse.text.strip()

    tweet_lines = [tweet_line_1, tweet_line_2, tweet_line_3, tweet_line_4, tweet_line_5]

    return tweet_lines


def tweet_lesson():
    # Access and authorize our Twitter credentials from credentials.py
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweet_lines = retrieval(url)

    print(tweet_lines[0])
    last_tweet = api.update_status(tweet_lines[0])

    # create a loop to iterate over lines
    for tweet_line in tweet_lines[1:]:
        try:
            print(tweet_line)
            last_tweet = api.update_status(tweet_line, last_tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)
        time.sleep(5)


schedule.every().day.at("09:00").do(tweet_lesson)
while True:
    schedule.run_pending()
    time.sleep(60)
