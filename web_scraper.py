from bs4 import BeautifulSoup
import requests
import re


def lesson_content_retrieval(website_url):
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

