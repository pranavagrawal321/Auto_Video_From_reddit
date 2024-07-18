import reddit
import screenshot
import constants
import voiceover

data = eval(reddit.scrape_reddit())

print(len(data))

for dict in data:
    question_id = list(dict.keys())[0]

    ques_value = dict[question_id]
    ques_title = ques_value['title']

    voiceover.create_voiceover(ques_title, f"Questions/{question_id}")

    screenshot.screenshot_reddit_question(constants.SUBREDDIT, question_id)

    comments = ques_value['comments']

    for i in comments:
        comment_id = list(i.keys())[0]
        comment_value = i[comment_id]

        print(comment_id)

        screenshot.screenshot_reddit_comment(question_id, comment_id)
        voiceover.create_voiceover(comment_value, f"Answers/{question_id}_{comment_id}")
