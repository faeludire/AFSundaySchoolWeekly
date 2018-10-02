from twitter_bot import tweet_lesson
import schedule
import time


def main():
    schedule.every().day.at("09:00").do(tweet_lesson)
    while True:
        schedule.run_pending()
        time.sleep(60)


main()
