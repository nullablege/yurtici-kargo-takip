from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = Options()
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

url = "https://www.yurticikargo.com/tr/online-servisler/gonderi-sorgula?code="
takipKodu = input("Takip Kodu Giriniz : ")
url = url + takipKodu

driver.get(url)

try:
    element = WebDriverWait(driver, 100).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "info-graphic-content"))
    )
except Exception as e:
    print("Element bulunamadı:", e)


try:
    durum = driver.find_element(By.ID,"shipmentStatus") #
except:
    print("Durum bilgisi alınırken problem yaşandı.")
try:
    yollayan = driver.find_element(By.ID,"sender") #
except:
    print("Durum bilgisi alınırken problem yaşandı.")
try:
    alici = driver.find_element(By.ID,"receiver") #
except:
    print("Alici bilgisi alınırken problem yaşandı.")
try:
    cikisTarihi = driver.find_element(By.ID,"shipmentDate") #
except:
    print("Cikis Tarihi bilgisi alınırken problem yaşandı.")
try:
    tahminiTeslimTarihi = driver.find_element(By.ID,"estimatedDeliveryDate") #
except:
    print("Tahmini Teslim Tarihi bilgisi alınırken problem yaşandı.")
try:
    teslimBirimi = driver.find_element(By.ID,"deliveryUnitName")#
except:
    print("Teslim Birini bilgisi alınırken problem yaşandı.")
try:
    odemeTuru = driver.find_element(By.ID,"ProductName") #
    odemeTuru = str(odemeTuru.text).split("<br>") #
except:
    print("Odeme Turu bilgisi alınırken problem yaşandı.")
try:
    nereden = driver.find_element(By.ID,"departureCityCounty") #
except:
    print("Nereden bilgisi alınırken problem yaşandı.")
try:
    nereye = driver.find_element(By.ID,"deliveryCityCounty") #
except:
    print("Nereye bilgisi alınırken problem yaşandı.")
try:
    kargoHareketleriBtn = driver.find_element(By.ID, "btn-shipment-movement")
except:
    print("Kargo Hareketleri Button tespit edilirken problem yaşandı.")
try:
    driver.execute_script("arguments[0].click();", kargoHareketleriBtn)
except:
    print("Kargo Hareketleri Button'una basılmaya çalışılırken problem yaşandı.")
try:
    tablo = driver.find_element(By.ID,"table-shipment-movement")
except:
    print("Gönderi detaylarını barındıran tablo alınırken hata yaşandı.")
try:
    tdler = driver.find_elements(By.TAG_NAME,"td")
except:
    print("Tablo elementleri alınırken hata yaşandı.")




print(f"\t\t{durum.text}\t\t")
odeme = odemeTuru[0].replace("\n"," ")
print(f"{odeme} ,{nereden.text} Adresinden {nereye.text} Adresindeki {teslimBirimi.text} Subesinden teslim alınacak olan kargo ; ")
print(f"{yollayan.text[0:10]} Kisisinden {alici.text[0:10]} Kisine Tahminen {tahminiTeslimTarihi.text} Tarihinde Teslim edimek uzere {cikisTarihi.text} Tarihinde Subeye Teslim Edilmistir. ")
print("Sıra No\t\tTarih\t\tŞube\t\tDurumu\t\tAçıklama")


sayac = 1
for td in tdler:
    print(td.text,end="\t\t")
    if sayac%5==0:
        print("")
    sayac+=1