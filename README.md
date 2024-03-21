# TrendYoLProject

İlk olarak, selenium ve pandas kütüphanelerini projemize dahil ediyoruz.

Bu kütüphaneler web tarayıcısı otomasyonu ve veri işleme için kullanılırız.

giris() fonksiyonunuz içerisinde, webdriver.Chrome() ile Chrome tarayıcısını başlatıyoruz.

Trendyol sitesine gidiyoruz, (driver.get('https://www.trendyol.com/')).

Ardından, arama kutusuna erişmek için searchButton değişkenini buluyoruz ve üzerine tıklıyoruz. 
Daha sonra, arama sorgusu olan "Telefon" kelimesini gönderiyoruz, (searchButton.send_keys(search_query)).

Sonrasında sayfayı aşağı kaydırıyoruz ve telefonları içeren bölümleri bulmak için XPath kullanarak telefon_listesi adlı bir liste oluşturuyoruz.

Bu listedeki her bir telefonun metnini alıyoruz ve telefonlar adlı bir listede saklıyoruz.

Ardından, telefonlar listesini bir pandas DataFrame'e dönüştürerek df adlı bir değişkene atıyoruz. 
DataFrame, verilerimizi düzenli bir tablo halinde tutmanızı sağlar.

Son olarak, df.to_excel("telefonlar.xlsx", index=False) komutuyla DataFrame'i "telefonlar.xlsx" adlı bir Excel dosyasına kaydediyoruz. 
index=False parametresi, DataFrame'in indeks sütununu Excel dosyasına dahil etmemek için kullanılır.

Kodumuzun sonunda, tarayıcıyı kapatıyoruz. (driver.quit()).

Bu şekilde, Trendyol sitesinden "Telefon" araması yaparak bulunan telefonların bilgilerini Excel dosyasına kaydetmiş oluyoruz. Kodumu oldukça iyi bir şekilde yapılandırdım anlaşılması ve okunması açısından :)
