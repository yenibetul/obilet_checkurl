import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

slack_webhook_url ="https://hooks.slack.com/services/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"
json_filenames = ["prodTR.json", "preprodEng.json"]
service = Service('path_to_chromedriver')
driver = webdriver.Chrome(service=service)
def create_session_with_header(header_name, header_value):
    session = requests.Session()
    session.headers[header_name] = header_name
    session.headers[header_value] = header_value
    return session

def test_url_check(url):
    session = create_session_with_header('bypass-rate-limit', '126371a4-bf11-4225-80ea-26c173c32571')
    response = session.get(url)
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

wait = WebDriverWait(driver, 5)

def run_job():
    for json_filename in json_filenames:

        with open(json_filename) as f:
            urls = json.load(f)
        for url in urls:
            test_url_check(url)
run_job()
driver.quit()