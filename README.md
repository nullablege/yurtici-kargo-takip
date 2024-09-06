Kargo Takip ve Bilgi Çekme Uygulaması
Bu proje, Yurtici Kargo'nun çevrimiçi takip servisi üzerinden kargo bilgilerini çekmek ve detayları ekranda göstermek için Python ve Selenium kullanarak geliştirilmiş bir uygulamadır. Uygulama, kargo takip kodunu girerek kargonun durumunu, gönderici ve alıcı bilgilerini, teslim tarihlerini ve kargo hareketlerini kullanıcıya sunar.

Özellikler
Kargo Bilgileri Çekme: Kargo takip kodunu kullanarak, kargonun mevcut durumunu, gönderici ve alıcı bilgilerini, teslim tarihlerini ve teslim birimini alır.
Kargo Hareketleri: Kargo hareketlerinin detaylarını içeren tabloyu alır ve her hareketin bilgilerini ekrana yazdırır.
Web Scraping: Selenium kütüphanesi kullanılarak web sayfasından veri çekme işlemleri yapılır.
Kullanım
Gereksinimler: Aşağıdaki Python kütüphanelerine ihtiyaç duyulmaktadır:

selenium
webdriver_manager
Bu kütüphaneleri yüklemek için şu komutları çalıştırabilirsiniz:
pip install selenium webdriver_manager

Kodun Çalıştırılması:
Python ortamınızı açın.
Aşağıdaki kodu bir Python dosyasına (örneğin yurtici-kargo-takip.py) yapıştırın ve kaydedin.

Kodun Çalıştırılması: Terminal veya komut satırında aşağıdaki komutu çalıştırarak uygulamanızı başlatabilirsiniz:
python yurtici-kargo-takip.py
Takip kodunu girdikten sonra, kargo bilgileri ve hareketleri ekranda görüntülenecektir.

Kod Açıklamaları
Selenium Kullanımı: Web tarayıcısını kontrol etmek ve web sayfasından veri çekmek için Selenium kütüphanesi kullanılır.
WebDriver Ayarları: Chrome tarayıcısının başlık ve kullanıcı ajanı gibi ayarları yapılandırılır.
Veri Çekme: Kargo takip kodu ile kargo bilgileri çekilir ve ekrana yazdırılır.
Hata Yönetimi: Kodun çeşitli aşamalarında oluşabilecek hatalar try-except blokları ile ele alınır.

NOT : Kod sadece Seleinum, python ve algoritma geliştirme tekniklerinde antrenman yapabilmek için yazılmıştır. Kullanımlarınızın sorumluluğu tamamen kendinizdedir, paylaşım amacım sadece eğitimdir.
