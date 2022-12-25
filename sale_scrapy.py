from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import json


options = Options()
# options.add_argument('--headless')
# options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

url = 'https://netsuper.san-a.co.jp/'

driver.get(url)
sleep(3)

select_btn = driver.find_element(By.CSS_SELECTOR,"form.shopSelectForm input.btn")
select_btn.click()
sleep(3)

time_btn = driver.find_element(By.CSS_SELECTOR,"td.deriveryTimeSelectTD5 > form > div > div > span > input")
time_btn.submit()
sleep(3)

sale_link = driver.find_element(By.PARTIAL_LINK_TEXT,"本日の目玉商品")
sale_link.click()
sleep(3)

itme_detail = driver.find_element(By.XPATH,'//*[@id="three_ColumnContents"]/form/div[1]/div[2]/div[3]/p/a[2]')
itme_detail.click()
sleep(3)

item_list = []
item = {}
while True:
  item_elems = driver.find_elements(By.CSS_SELECTOR,"div.ItemListDetail")
  for item_elem in item_elems:
    item['title'] = item_elem.find_element(By.CSS_SELECTOR,"p.ListDetailName > a").text.strip('※・').replace('　',' ')
    item['url'] = item_elem.find_element(By.CSS_SELECTOR,"p.ListDetailPic > a > img").get_attribute('src')
    item['price'] = item_elem.find_element(By.CSS_SELECTOR,"span.ListDetailPriceTDSub").text.strip('(税込:円)')
    item_list.append(item.copy())
    
  try:
    next_page = driver.find_element(By.LINK_TEXT,"次→")
    next_page.click()
    sleep(3)
    
  except Exception:
    break

item_json = json.dumps(item_list, indent=4, ensure_ascii=False)
print(item_json)
