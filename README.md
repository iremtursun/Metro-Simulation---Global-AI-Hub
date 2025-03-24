**Global AI Hub - Akbank Python ile Yapay Zekaya Giriş Bootcamp Projesi**

**TANIM**

Akbank ve Global AI Hub işbirliğinde hazırlanan, Metro Simülasyonu olarak adlandırabileceğimiz bir metro ağında hedeflenen bu proje; test ortamlarında iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulmak amaçlanmaktadır.

Dosyanın python koduna **IremTursun_MetroSimulation.py** dosyasından erişebilir ve tasarısı şahsıma ait **metro-simulation-grafs.png** görselinden duraklar arasındaki ilişkilendirmeleri inceleyebilirsiniz.

**Proje Simülasyon Uygulaması**

Kullanıcılar hedeflenen belirli istasyon noktalarından hedefledikleri istasyon durağına erişebilmek için belli başlı metro hatlarını kullanmaktadır. Kırmızı metro ağı sırasıyla Kızılay, Ulus, Demetevler, OSB istasyon duraklarını içermektedir. Her durağın algoritmada dikkatli kullanılmasını sağlamak için "id" isimlendirmesi yapılır. Sırasıyla takip eden metro duraklarının id'leri; K1, K2, K3, K4 olarak isimlendirilmiştir.

Benzer şekilde iki metro ağı daha vardır. Öncelikli olarak Mavi metro ağı için sırasıyla duraklar AŞTİ, Kızılay, Sıhhiye ve Gar'dır. Bu durakların id isimlendirmeleri ise M1, M2, M3, M4 olarak isimlendirilmiştir. Bir diğer metro ağı ise Turuncu metro ağıdır. Sırasıyla Batıkent, Demetevler, Gar, Keçiören olmakla birlikte id isimlendirmeleri T1, T2, T3, T4'dür.

İstasyonlar arasındaki bağlantıların süreleri, **baglanti_ekle()** fonksiyonu üzerinden takip edilerek alındı ve görsel tasarısı içine yazıldı.

Hedefimiz en hızlı yol aktarma/rotasını bulup; kısa sürede erişebileceğimiz şekilde hedeflenen istasyon duraklarına erişebilmektir. Bu problemi bir algoritma problemi olarak değerlendirip kullanmamız gereken kütüphaneleri tanımamız beklenir. Duraklar için komşular arası ziyaret yapan bir graf tasarısında en kısa rotayı hesaplamada BFS (Breadth-First Search) algoritmasını kullanmak; hedefe ulaşmak için maliyet fonksiyonunu da hesaplamak ve en az sürede ulaşabilmeyi gerçekleştiren A* algoritmasının kullanmaktır.

Proje dosyasında **en_az_aktarma_bul()** ve **en_hizli_rota_bul()** fonksiyonları içinde kullanacağımız BFS ve A* algoritmalarını açıkladığımıza göre nelere ihtiyacımız olduğunu daha iyi kontrol edelim:

Kütüphaneleri indirerek öncelikli olarak işlemlerimize başlayabiliriz. BFS algoritmasının çalışmasını için **collections** modülünden **deque** kütüphanesini import edebiliriz. Devamında A* algoritmasını kullanmak için ise **heapq** modülünü import edebiliriz. Tüm kod üzerinde belirli Python gerekliliklerini kullanmak için lazım olan **Dict, List, Set, Tuple, Optional** tiplerini indirebilir ve yeniden **collections** modülünden **defaultdict** sözlüğünü (bu sözlük varsayılan değer için anahtar yoksa hata döndürmez) indirebiliriz.

**istasyon_ekle()** ve **baglanti_ekle()** fonksiyonlarının girdilerini kontrol ederek **MetroAgi()** sınıfında nesneler tanımlanır ve **Istasyon()** sınıfı da dahil olmak üzere tasarlanan fonksiyonlar üzerinden istasyon ad bilgisi, zaman bilgisi tanımlanmış olur.

Sınıflar ve fonksiyonlar tanımlandıktan sonra rota oluşturulur ve iki durak arasındaki en hızlı rota ile en az aktarmalı yolların çıktısı kullanıcıya sunulmuş olur.

Özet halinde anlattığım metro simülasyonu kodlarına erişebilir ve test senaryolarını inceleyebilirsiniz.

**Kaynakça:**
1. https://www.geeksforgeeks.org/a-search-algorithm/
2. https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
