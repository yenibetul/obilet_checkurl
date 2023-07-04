import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


slack_webhook_url = "https://hooks.slack.com/services/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"


service = Service('path_to_chromedriver')  # ChromeDriver'ın yolunu belirtin
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

# Slack bildirimi gönderme
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


urls = [
"https://www.obilet.com/seferler/7248-16322/2023-07-04",
"https://www.obilet.com/",
"https://www.obilet.com/ucak-bileti",
"https://www.obilet.com/otobus-bileti-sorgulama-ve-iptali",
"https://www.obilet.com/ucak-bileti-sorgulama",
"https://www.obilet.com/otogarlar",
"https://www.obilet.com/duraklar",
"https://www.obilet.com/ucus-noktalari",
"https://www.obilet.com/otobus-seferleri/populer-seyahat-noktalari",
"https://www.obilet.com/otobus-bileti-al",
"https://www.obilet.com/otobus-seferleri",
"https://www.obilet.com/aydinlatma-metni",
"https://www.obilet.com/kisisel-verilerin-korunmasi",
"https://www.obilet.com/kullanim-sartlari",
"https://www.obilet.com/online-otobus-bileti",
"https://www.obilet.com/en-ucuz-otobus-bileti",
"https://www.obilet.com/indirimli-otobus-bileti",
"https://www.obilet.com/mobil-uygulamalar",
"https://www.obilet.com/otobus-bileti-kampanyalari",
"https://www.obilet.com/ucak-bileti-kampanyalari",
"https://www.obilet.com/ucak-bileti-kampanyalari/hediye-internet-paketi",
"https://www.obilet.com/havaalanlari",
"https://www.obilet.com/ucak-seferleri",
"https://www.obilet.com/yurtdisi-ucak-bileti",
"https://www.obilet.com/otobus-firmalari/nilufer-turizm",
"https://www.obilet.com/otobus-firmalari",
"https://www.obilet.com/otobus-firmalari/istanbul-seyahat/edirne",
"https://www.obilet.com/otobus-bileti/ankara/asti-otogari",
"https://www.obilet.com/otobus-bileti/edirne",
"https://www.obilet.com/otobus-bileti/edirne-istanbul",
"https://www.obilet.com/otobus-seferleri/populer-edirne-seferleri",
"https://www.obilet.com/ucak-firmalari/pegasus-airlines",
"https://www.obilet.com/havaalanlari/izmir-adnan-menderes-uluslararasi-havalimani",
"https://www.obilet.com/ucak-bileti/izmir",
"https://www.obilet.com/ucak-bileti/izmir-istanbul",
"https://www.obilet.com/kredi-ve-banka-karti-duzenlemesi",
"https://www.obilet.com/ucuslar/251_18-250_0/20230822-20230830/1a/economy/all",
"https://www.obilet.com/ucuslar/251_18-250_0/20230822-20230830/2a-1c/economy/all",
"https://www.obilet.com/ucuslar/251_18-250_0/20230822/1a/economy/all",
"https://www.obilet.com/ucuslar/251_18-250_0/20230822/2a-1c/economy/all",
"https://www.obilet.com/ucuslar/2836_1227-250_0/20230822/1a/economy/all",
"https://www.obilet.com/ucuslar/2836_1227-250_0/20230822/2a-1c/economy/all",
"https://www.obilet.com/ucuslar/2836_1227-250_0/20230822-20230830/1a/economy/all",
"https://www.obilet.com/ucuslar/2836_1227-250_0/20230822-20230830/2a-1c/economy/all",
"https://www.obilet.com/seferler/349-372/2023-08-22",
"https://www.obilet.com/uye/giris?returnUrl=%2Fuye%2Fprofil",
"https://yardim.obilet.com/hc/tr/categories/360001240994-Otob%c3%bcs-Bileti",
"https://yardim.obilet.com/hc/tr/categories/360001266133-U%c3%a7ak-Bileti",
"https://blog.obilet.com/kurumsal/obilet-guvenli-mi",
"https://blog.obilet.com/kurumsal/otobus-bileti-satin-alma-rehberi",
"https://blog.obilet.com/kurumsal/seferlere-nasil-oy-verilir/",
"https://blog.obilet.com/kurumsal/odullerimiz",
"https://blog.obilet.com/kurumsal/hakkimizda",
"https://careers.obilet.com/",
]

wait = WebDriverWait(driver, 10)
for url in urls:
    test_url_check(url)

driver.quit()
