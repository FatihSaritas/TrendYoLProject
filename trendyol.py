
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def giris():
    driver = webdriver.Chrome()
    driver.get('https://www.trendyol.com/')
    #SİTEYE BAĞLANTI İŞLEMİNİ GERÇEKLEŞTİR ŞUANDA
    time.sleep(10)

    searchButton = driver.find_element(By.XPATH,"//*[@id='sfx-discovery-search-suggestions']/div/div[1]/input ")
    #SEARCH YANİ ARAMA KISMINA ERİŞTİK 
    searchButton.click()
    #VERİ GİRMEK YANİ ARMAK YAPABİLMEK İÇİN TIKLAMA İŞLEMİ GERÇEKLEŞTİRDİK .
   
    search_query = "Telefon"
    #ARATTIGIMIZ VERİ 
    
    searchButton.send_keys(search_query)
    #BUTONA TIKLATTIK
    searchButton.send_keys(Keys.ENTER)
    #VE ENTER DEDİK 
    time.sleep(5)
    #SAYFADA SORUN CIKMAMSI ADINA BİRAZ BEKLETTİK 
    
    
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    #BU KISIMDA SCROL BAR YANİ SAYFADA AŞŞA YUKARI BUTONUNA ERİŞİP SAYFANIN EN ALTINA İNDİK TÜM TELEFONLARI GÖRÜNTÜLEMEK İÇİN
    
    
    #BU KISIMDA İSE TABLOYA ERİŞTİK VE ONUN ALTINDA DİV CLASS DEDİĞİMİZ TABLONUN YANİ TELEFONLARIN CLASSLARINA ERİŞTİK TEK TEK ELE ALICAGIMIZ KISIM 
    telefon_listesi = driver.find_elements(By.XPATH, "//div[@class='prdct-cntnr-wrppr']//div[@class='product-down']")

    # Telefonları içeren div'leri bir liste olarak saklayalım
    telefonlar = [telefon.text for telefon in telefon_listesi]
    #BU DÖNGÜDE TELEFON İÇERİSİNE TELEFON LİSTESİ GELEN BÜTÜN TELEFONLARI ATTIK VE TELEFON ADINDA DEĞİŞKENE ATAYIP
    #ORADA DA TEXT YANİ İÇERİK BİLGİSİNİ ELE ALDIK

    # Verileri bir veri çerçevesine dönüştürdük
    df = pd.DataFrame(telefonlar, columns=["Telefon Bilgisi"])

    # Veriyi Excel'e kaydediyoruz.
    df.to_excel("telefonlar.xlsx", index=False)

    driver.quit()

giris()

#BU YAPTIGIMIZ KODDA TRENDYOL SİTESİNE ULAŞTIK ARAMA BUTONU KISMINA GİDEREK TELEFON YAZDIRDIK
#KARŞIMIZA ÇIKAN BUTUN TELEFONLARIN HTML KODLARINA ERİŞİP HEPSİNİ BİR LİSTE İÇERİSİNE ALDIK VE 
#BU TELEFONLARIN İSİMLERİNİ FİYATLARINI HER BİRİNİ TEKER TEKER ELE ALDIK BUNU YAPARKEN BÜTÜN SAYFAYI KASTEDİYORUM
#BU İŞLEMDE SCROLLBARDAN FAYDALANDIK ALDIGIMIZ VERİLERİ EXCEL DOSYASINA KAYIT ETTİK EN SONUNDA KISACASI BİR 
#WEB SİTESİ ÜZERİNDEN VERİLER ÇEKTİK VE BUNLARI EXCEL DOSYASINA KAYIT ETTİK.