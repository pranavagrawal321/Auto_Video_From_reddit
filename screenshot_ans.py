from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

post_id = '1dxsv4q'
comment_id = 'lc4q6hy'
url = f'https://www.reddit.com/comments/{post_id}/comment/{comment_id}'
driver.get(url)

time.sleep(5)

comment_summary = driver.find_element(By.XPATH, '//*[@id="main-content"]/shreddit-comment-tree/shreddit-comment')

driver.execute_script("arguments[0].scrollIntoView();", comment_summary)

time.sleep(2)

screenshot_path = 'comment_summary_screenshot.png'
comment_summary.screenshot(screenshot_path)

driver.quit()

print(f'Screenshot saved to {screenshot_path}')
