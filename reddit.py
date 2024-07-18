import praw
import json
import re
from constants import *
from bs4 import BeautifulSoup
import os
import warnings
from markdown import markdown
from text.cleaners import english_cleaners
warnings.filterwarnings("ignore")


def reddit_obj():
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
    )

    return reddit


def scrape_reddit():
    reddit = reddit_obj()
    subreddit = reddit.subreddit(SUBREDDIT).top(time_filter='day', limit=5)

    results = []

    created_ids = os.listdir('videos')

    for submission in subreddit:
        if submission.over_18 or submission.id + ".mp4" in created_ids:
            continue

        submission.comments.replace_more(limit=2)
        all_comments = submission.comments.list()

        filtered_comments = []
        for comment in all_comments:
            word_count = len(comment.body.split())
            if 25 <= word_count <= 100:
                cleaned_comment = english_cleaners(comment.body)
                filtered_comments.append({comment.id: cleaned_comment})

        result = {
            submission.id: {
                'title': english_cleaners(submission.title),
                'comments': filtered_comments[:2]
            }
        }

        results.append(result)

    json_results = json.dumps(results, indent=4)

    return json_results


if __name__ == '__main__':
    print(scrape_reddit())