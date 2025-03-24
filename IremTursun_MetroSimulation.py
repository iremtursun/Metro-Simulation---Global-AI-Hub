#Algoritma boyunca kullanılacak olan methodlar için ilgili kütüphaneleri yüklemek ile başlıyoruz. 
#Proje kapsamının amacına uygun en önemli 2 kütüphane heapq ve deque'dir.

from collections import defaultdict, deque  #BFS Algoritması için önemli olan deque yüklemesi import ediliyor.
import heapq #A* algoritması için önemli olan heapq import ediliyor.
from typing import Dict, List, Set, Tuple, Optional

class Istasyon: #Istasyon sınıfı oluşturuluyor ve "idx,ad,hat" nesneleri ile "komsular" tuple'ları bir listede toplanarak oluşturuluyor.
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int): #Istasyon class'ında "istasyon" değişkeni ile "sure" integer değişkeni komsu_ekle fonksiyonunda sıralı ikili olarak "komsular" tuple'ına ekleniyor.
        self.komsular.append((istasyon, sure))

class MetroAgi: #Yeni bir MetroAgi sınıfı oluşturuluyor. Burada "hatlar" ve "istasyonlar" nesneleri sözlük olarak tanımlanıyor.
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        if id not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)  #Istasyon sınıfına 3 adet string değişken ataması yapılıyor.
            self.istasyonlar[idx] = istasyon  #idx, istasyon olarak tutuluyor.
            self.hatlar[hat].append(istasyon)  #istasyon bilgisi hatlar sözlüğüne ekleniyor.

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None: #en az iki istasyon arasında bir "baglanti_ekle" fonksiyonu kuruluyor.
        istasyon1 = self.istasyonlar[istasyon1_id]  #Bu iki satırda 2 istasyona ait id tanımlamaları gerçekleştiliyor, string değerinde.
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)  #Yukarıda bulunan "komsu_ekle" fonksiyonuna, yazılan 2 adet istasyon ve süre ("sure" integer değeri) değişkenleri sıralı ikili olarak atanıyor. 
        istasyon2.komsu_ekle(istasyon1, sure)

#Global AI Hub, Metro Simülasyonu proje örneği için en önemli kısım iki istasyon arasındaki en az aktarmalı, en hızlı rotayı bulup bir çıktı olarak kullanıcıya sunabilmektir.
#Dolayısıyla en az aktarma ve en hızlı rotayı bulabilmek için 2 farklı fonksiyon üzerinden çalışılmalıdır.
#BFS algoritması kullanarak en az aktarmalı rota bulunur.
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        baslangic= self.istasyonlar[baslangic_id]
        hedef= self.istasyonlar[hedef_id]

        #Başlangıç ve hedef istasyonların varlığına bakılır ve eğer bulunamazsa None döndürür.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        #Başlangıç ve ulaşılmak istenen hedef istasyonu var olduğuna devam ederek BFS algoritmasına geçilir.

        queue = deque([(baslangic, [baslangic])]) #Collections'dan deque modülü çekilir ve başlangıç noktasına, diğer ziyaret edilecek olan yeni komşu istasyonlar eklenir. Bir listede tutulur.
    
        ziyaret_edildi = set()
        ziyaret_edildi.add(baslangic) 
        
        while queue:
            suanki_istasyon, yol = queue.popleft()  #Döngüye yol üzerinden devam edileceği için başlangıç noktası çıkartılır. Böylece hedefe devam edebilme şartını inceleyebiliriz.
            
            if suanki_istasyon == hedef:
                return yol  #Eğer gelinen hedef noktası, ulaşılmak istenen istasyon ise burada işlem bitmiştir ve döngü tamamlanmıştır.
            
            for (komsu, _) in suanki_istasyon.komsular:  #Herhangi bir integer süresi alınmadan string hedeflerde devam edilir. 
                #Eğer henüz istenen istasyona varamadı ise, komşulara bakmaya devam edecek; eğer komşular ziyaret edilmedi ise, listeye ekleyecektir. (komsular tuple olarak tanımlandığı için (istasyon,süre) değiştirilemez; bu yüzden integer değer olarak _ kullanıldı)
                if komsu not in ziyaret_edildi:
                    ziyaret_edildi.add(komsu) # add() fonksiyonu ekleme görevinde bulunur.
                    queue.append((komsu, yol + [komsu]))  #Devamında komsu istasyonda dahil edilerek yola devam edilir.
        return queue

#2. önemli fonksiyon ise yola bağlı maliyet hesabıdır. En hızlı sürede istasyona varabilmek için A* algoritması kullanılır ve yukarıda indirilmiş olan heapq modülü esas alınır.

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        #En hızlı rotayı bulmak için BFS başlangıçına benzer şekilde baslangic,hedef,ziyaret_edildi nesnelerini tanımlayacağız.
        baslangic= self.istasyonlar[baslangic_id]
        hedef= self.istasyonlar[hedef_id]
        ziyaret_edildi = set()

        #Benzer şekilde başlangıç ve hedef istasyonların varlığına bakılır ve bulunamazsa None döndürür.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        pq = [(0, id(baslangic), baslangic, [baslangic])] #Burada heapq modülünden 4 parametre alan bir kuyruk oluşturulur. 
        # pq kuyruğu 0 süreye, başlangıç id'sine, başlangıç adına ve rotadan oluşan bir liste değişkenlerine sahiptir. Yani başlanan ilk istasyon bilgisine sahiptir.
        
        while pq:
            toplam_sure, _, suanki_istasyon, istasyon_listesi = heapq.heappop(pq)  #heappop() fonksiyonu pq kuyruğunda en küçük elemanı çıkartır.
            if suanki_istasyon == hedef: #Eklenen yeni değerler, şu an ki istasyonun aslında hedef nokta olduğunu söyler ve ilerleme burada tamamlanarak (rota, süre) bilgisini döndürür. 
                return (istasyon_listesi, toplam_sure)
                               
            for (komsu, sure) in suanki_istasyon.komsular: #Komşu noktanın komsular listesinde olup olmadığı bakılır. Komsular listesi tuple'lardan oluştuğu için (komşu, süre) şeklinde listede aratmak gerekir.
                if komsu not in ziyaret_edildi: #Bu komşu noktanın ziyaret edilmeyen nokta olması istenir. Çünkü yukarıdaki koşul ile aynı olmadan, ziyaretlerini farklı noktaları kontrol ederek devam etmesi beklenir.
                    yeni_sure = toplam_sure + sure  #Komşu nokta, yeni istasyon durağı olduğu için maliyeti, yani süresi, hesaba katılır. Toplam süre içerisine yeni durağa gidilecek süre eklenir.
                    yeni_rota = rota + [komsu]  #Benzer şekilde bu komlu nokta, rotaya dahil edilir ve yol oluşmaya başlar. (while olarak döneceği için)
                    heapq.heappush(pq, (yeni_sure, id(komsu), komsu, yeni_rota)) #Yeni değerler pq kuyruğuna tuple olarak eklenir.

        return None
        

if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    #Burada istasyon durakları MetroAgi class'ına eklenerek tanımlamalar gerçekleştiriliyor.
    #Kırmızı, Mavi ve Turuncu olmak üzere üç metro hattı var. Her birinde id'leri tanımlanmış duraklar bulunmakta
 
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    #İstasyon durakları eklendiğine göre, graf oluşturmak için bağlandıkları durakların da eklenmesi gerekir. Böylece id'den id'ye istasyonların bağlantılarını gösteren hatlar yazılmıştır

    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 

    #Test Senaryolarını daha iyi anlamak için bir örnekte ben ekledim:
    #Demetevler -> Kızılay
    print("\n4. Demetevler'den Kızılay'a:")
    rota = metro.en_az_aktarma_bul("T2", "K1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T2", "K1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 

