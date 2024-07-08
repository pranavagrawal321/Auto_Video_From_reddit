from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageOps
from io import BytesIO
import os

screenshot_dir = "Screenshots"


def screenshot_reddit_question(subreddit, question_id, spacing_height=20):
    os.makedirs(screenshot_dir, exist_ok=True)

    combined_screenshot_path = os.path.join(screenshot_dir, f"{question_id}.png")

    driver = webdriver.Chrome()

    url = f'https://www.reddit.com/r/{subreddit}/comments/{question_id}/'

    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    try:
        title_element = driver.find_element(By.CSS_SELECTOR, 'h1[slot="title"]')
        title_screenshot = BytesIO(title_element.screenshot_as_png)

        profile_element = driver.find_element(By.CSS_SELECTOR, 'div[slot="credit-bar"] span.flex.gap-xs.items-center.pr-xs.truncate')
        profile_screenshot = BytesIO(profile_element.screenshot_as_png)

        title_image = Image.open(title_screenshot)
        profile_image = Image.open(profile_screenshot)

        title_width, title_height = title_image.size
        profile_width, profile_height = profile_image.size

        background_color = (15, 16, 19)

        max_width = max(title_width, profile_width)
        if title_width < max_width:
            title_image = ImageOps.expand(title_image, border=(0, 0, max_width - title_width, 0), fill=background_color)
        if profile_width < max_width:
            profile_image = ImageOps.expand(profile_image, border=(0, 0, max_width - profile_width, 0), fill=background_color)

        blank_space = Image.new('RGB', (max_width, spacing_height), background_color)

        title_width, title_height = title_image.size
        profile_width, profile_height = profile_image.size
        space_width, space_height = blank_space.size

        combined_image = Image.new('RGB', (max_width, title_height + profile_height + space_height), background_color)

        combined_image.paste(profile_image, (0, 0))
        combined_image.paste(blank_space, (0, profile_height))
        combined_image.paste(title_image, (0, profile_height + space_height))

        combined_image.save(combined_screenshot_path)

        print(f'Combined screenshot saved to {combined_screenshot_path}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        driver.quit()


if __name__ == '__main__':
    subreddit_name = 'AskReddit'
    question_id = '1dw9m1a'
    screenshot_reddit_question(subreddit_name, question_id)
