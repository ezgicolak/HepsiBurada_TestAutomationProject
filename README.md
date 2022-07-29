# HepsiBuradaproject

@Proje EzgiColak tarafından hazırlanmıştır.

1) Kullanıcı girişi yapılarak sepete ürün eklenmesi
#Projenin gereksinimleri:
 - Python yüklü olması.
 - pip yüklü olması ve yukarıda belirtilen librarylerin yüklü olması gerekmektedir.
    -> pip install selenium
    -> pip install behave
    -> pip install allure-behave
    -> pip install webdriver_manager
 - Proje klasöründe bulunan Allure-2.18.1 içerisindeki 'bin' klasörü dosya yolunun sistem path kısmına eklenmesi.

#Aşağıdaki komutlar "cmd" üzerinde sırasıyla derlendiğinde ilk olarak tarayıcı üzerinde testler gerçekleştirilip
"reports" klasörü üzerine ".json" formatında rapor dosyası yazılır sonrasında ise rapor dosyası allure server
aracılığı ile generate edilip tarayıcı üzerinde rapor görüntülenir.

    - Projeyi çalıştırmak için gereken komut:
        -> behave -f allure_behave.formatter:AllureFormatter -o reports/ features
    - Rapor dosyasının servis edilmesi için gereken komut:
        -> allure serve reports/

#Python dili ve PyCharm 2021.3 IDE kullanılarak hazırlanmıştır.

#Selenium, behave, webdriver_manager, allure-behave ve allure frameworkleri kullanılmıştır.

#BDD prensipleri doğrultusunda hazırlanmıştır.
    -objects_repository klasörü web sitesine göre hiyerarşik olarak dizan edilmiş olup element xpath lerini içerir.
    -features klasörü satin_alma feature ve python dosyasını içerir.
    -reports klasörü koşu sonrası oluşan json formatındaki rapor dosyasını içerir.

#Chrome ve Edge tarayıcıları için feature dosyası üzerinden parametrik çalışacak şekilde ayarlanmıştır.

2) Api testi yapılması

#Test adımları :
- Yeni pet eklenmesi - POST 
- ID ye göre pet aranması - GET 
- Petin silinmesi - DELETE 
- Aynı ID ile petin aranması - GET 

- Silinen Petin listelenmediği görülmektedir.






