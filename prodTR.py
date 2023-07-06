import os
import json
import requests
import schedule
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

slack_webhook_url = "https://hooks.slack.com/services/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"
json_filenames = ["prodTR.json", "preprodEng.json"]
service = Service('path_to_chromedriver')
driver = webdriver.Chrome(service=service)

def test_url_check(url):
    response = requests.get(url)
    status_code = response.status_code

    if status_code >= 400 and status_code < 600:
        print(f"URL kontrolü başarısız: {url} - HTTP durum kodu: {status_code}")
        send_slack_notification(url, status_code)
        return

    driver.get(url)

    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    try:
        wait.until(EC.url_to_be(url))
        print(f"URL kontrolü başarılı: {url}")
    except:
        print(f"URL kontrolü başarısız: {url}")
        send_slack_notification(url, status_code)

def send_slack_notification(url, status_code):
    message = f"URL kontrolü başarısız: {url} - HTTP durum kodu: {status_code}"
    payload = {
        "text": message
    }
    response = requests.post(slack_webhook_url, json=payload)
    if response.status_code == 200:
        print("Slack bildirimi gönderildi.")
    else:
        print("Slack bildirimi gönderilemedi.")

wait = WebDriverWait(driver, 10)

def run_job():
    for json_filename in json_filenames:
        # Load URLs from JSON file
        with open(json_filename) as f:
            urls = json.load(f)

        for url in urls:
            test_url_check(url)

def repeat_job():
    while True:
        schedule.run_pending()
        time.sleep(1)
        schedule.every(1).hours.do(run_job)




run_job()
repeat_job()

driver.quit()