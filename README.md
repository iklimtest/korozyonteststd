Korozyon Test Standartları Uygulaması

Bu Python uygulaması, kullanıcıların korozyon test standartlarına erişebileceği, ayrıca kendi özel test standartlarını ekleyebileceği bir platform sunmaktadır. Uygulama, Tkinter kütüphanesi kullanılarak geliştirilmiştir ve basit bir grafik arayüz ile kullanıcı dostu bir deneyim sağlar.

Özellikler

Korozyon Test Standartları Listesi: Uygulama, çeşitli korozyon test standartlarını (örneğin, ASTM, DIN, JIS, ISO vb.) içerir.

Standart Ekleme: Kullanıcılar, kendi test standartlarını ekleyebilir ve mevcut verilere kolayca erişebilir.

Tkinter GUI: Basit ve kullanımı kolay bir grafiksel kullanıcı arayüzü ile çalışır.

Kullanıcı Arayüzü

Ana Ekran: Uygulama başlatıldığında, mevcut korozyon test standartları listelenir. Kullanıcılar, bu standartları inceleyebilir veya yeni standartlar ekleyebilir.

Yeni Standart Ekleme: Kullanıcılar, bir form aracılığıyla yeni test standartları ekleyebilir. Standart adı, açıklama, prosedür ve diğer detaylar girilebilir.

Test Standardı Görüntüleme: Kullanıcılar, listelenen test standartlarından herhangi birini seçerek detaylarına ulaşabilir.

Gereksinimler
Python 3.x
Tkinter (Python ile birlikte gelir)
Diğer bağımlılıklar: tkinter dışında ek bir bağımlılık bulunmamaktadır.
Kurulum

GitHub reposunu klonlayın:

bash
Copy code
git clone https://github.com/iklimtest/korozyonteststd.git
Python 3 yüklü olduğundan emin olun. Tkinter, Python ile birlikte gelir, ancak bazı durumlarda ekstra yükleme yapılması gerekebilir.

Uygulamayı çalıştırın:

korozyonstd.py
standards.csv 

Kullanım

Uygulama açıldığında, standartların listelendiği ana ekranı göreceksiniz.
Yeni bir standart eklemek için "Yeni Standart Ekle" butonuna tıklayın.
Test standartlarının detaylarını girin ve kaydedin.
Mevcut standartları görmek veya düzenlemek için listeden bir tanesini seçin.
standards.csv dosyası ile python uygulaması aynı klasör içinde olmalıdır.
