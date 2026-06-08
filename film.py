# Hocam merhaba, ödevin 2. kriteri olan veri tabanı işlemleri için derste işlediğimiz sqlite3 kütüphanesini projeme dahil ettim.
import sqlite3


def veritabanini_hazirla():
    # Hocam burada dosya oluştururken veya bağlanırken bir hata olursa program çökmesin diye try-except bloğu kullandım.
    try:
        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()

        # CREATE TABLE IF NOT EXISTS komutunu kullandım ki programı her çalıştırdığımda tabloyu yeniden oluşturmaya çalışıp hata vermesin.
        # İstatistiklerde (SUM fonksiyonu ile) toplam süreyi hesaplatacağım için 'sure_dk' sütununu INTEGER yaptım.
        imlec.execute("""
            CREATE TABLE IF NOT EXISTS filmler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL,
                yil INTEGER,
                tur TEXT,
                sure_dk INTEGER,
                izlenme_durumu TEXT,
                favori_mi TEXT,
                kisisel_puan REAL
            )
        """)

        # Hocam programı her çalıştırdığımda filmlerimi tekrar tekrar (çift kayıt olarak) eklemesin diye önce tablonun dolu mu boş mu olduğuna baktırdım.
        imlec.execute("SELECT COUNT(id) FROM filmler")
        kayit_sayisi = 0
        for satir in imlec:
            kayit_sayisi = satir[0]

        # Eğer kayıt sayısı 0 ise (yani tablo sıfırdan açıldıysa), test ederken kolaylık olsun diye kendi favori film listemi otomatik ekletiyorum.
        if kayit_sayisi == 0:
            print("Arşiv boş tespit edildi. Özel film listeniz veri tabanına yükleniyor, lütfen bekleyiniz...")

            #Hazırladığım süreleri dakika cinsinden girilmiş film listem
            film_listem = [
                ("Weapons", 2025, "Korku", 130, "İzlendi", "Evet", 9.4),
                ("Ölü Mevsim", 2024, "Dram", 114, "İzlendi", "Hayır", 6.0),
                ("Late Night With The Devil", 2023, "Korku", 93, "İzlendi", "Evet", 9.0),
                ("Decision To Leave", 2022, "Gizem", 138, "İzlendi", "Evet", 8.0),
                ("The Power Of The Dog", 2021, "Western, Drama", 126, "İzlendi", "Evet", 8.5),
                ("Sound Of Metal", 2019, "Drama, Music", 120, "İzlendi", "Evet", 8.0),
                ("Uncut Gems", 2019, "Suç, Dram", 135, "İzlendi", "Evet", 9.5),
                ("Kutsal Geyiğin Ölümü", 2017, "Gizem, Dram", 121, "İzlendi", "Evet", 8.5),
                ("No Other Choise", 2025, "Suç, Komedi, Gerilim", 115, "İzlenecek", "Hayır", 0.0),
                ("I Swear", 2025, "Tarih, Drama", 120, "İzlenecek", "Hayır", 0.0),
                ("Anora", 2024, "Romantik, Komedi", 139, "İzlenecek", "Hayır", 0.0),
                ("Anatomy Of A Fall", 2023, "Gerilim, Suç", 152, "İzlenecek", "Hayır", 0.0),
                ("The Usual Suspects", 1995, "Gerilim, Dram, Suç", 106, "İzlenecek", "Hayır", 0.0),
                ("In The Mood For Love", 2000, "Romantik, Dram", 98, "İzlenecek", "Hayır", 0.0),
                ("Gun Girl", 2014, "Dram, Gizem, Gerilim", 149, "İzlenecek", "Hayır", 0.0),
                ("Spirit Away", 2001, "Anime", 125, "İzlenecek", "Hayır", 0.0),
                ("I Want Eat Your Pancreas", 2018, "Dram, Romantik", 108, "İzlendi", "Evet", 9),
                ("Your Name", 2017, "Dram, Fantastik", 106, "İzlenecek", "Hayır", 0.0),
                ("Scream", 1996, "Gerilim, Gizem, Korku", 111, "İzlendi", "Hayır", 4.7),
                ("Spider-Man: Across the Spider-Verse", 2023, "Aksiyon, Komedi, Süper Kahraman", 140, "İzlendi", "Evet",
                 8.5),
                ("The Light House", 2019, "Gerilim, Korku, Drama", 109, "İzlendi", "Evet", 9.2),
                ("No Country For Old Men", 2007, "Suç, Gerilim, Western", 122, "İzlendi", "Evet", 9.3),
                ("Challengers", 2024, "Romantik, Dram", 131, "İzlendi", "Evet", 8.8),
                ("Blade Runner 2049", 2017, "Bilim Kurgu, Aksiyon", 164, "İzlendi", "Evet", 9.9)
            ]

            #Ders notlarında gösterdiğiniz gibi for döngüsü ile listedeki tüm filmleri veritabanına işliyorum.
            for film in film_listem:
                imlec.execute("""
                    INSERT INTO filmler (ad, yil, tur, sure_dk, izlenme_durumu, favori_mi, kisisel_puan)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, film)

            print("✅ Film listeniz arşive başarıyla eklendi!\n")

        # Hocam verilerin fiziksel dosyaya tam olarak yazılması için commit komutu.
        baglanti.commit()
        # Bağlantıyı kapatarak sistem kaynaklarını serbest bırakıyorum.
        baglanti.close()

    except sqlite3.Error as hata:
        # Veritabanı oluşturulurken hata çıkarsa konsola yazdırıyorum (ÖDEV1 Kriteri).
        print("Hocam veri tabanı oluşturulurken bir hata meydana geldi:", hata)


def film_ekle():
    print("\n--- 🎬 YENİ FİLM EKLE ---")
    try:
        # Önce sadece filmin adını alıyoruz ki, eğer film zaten varsa kullanıcıyı diğer sorularla yormayalım.
        ad = input("Filmin Adı: ")

        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()

        # EKLENEN SAVUNMA 0: Veri tabanında bu isimde bir film var mı diye kontrol ediyoruz.
        imlec.execute("SELECT id FROM filmler WHERE ad = ?", (ad,))
        film_zaten_var = False
        for satir in imlec:
            film_zaten_var = True

        # Eğer film bulunduysa kullanıcıyı uyarıp (return ile) fonksiyondan hemen çıkıyoruz.
        if film_zaten_var:
            print(f"\n❌ Uyarı: '{ad}' isimli film zaten arşivinizde mevcut! Tekrar ekleyemezsiniz.")
            baglanti.close()
            return

        # Film veri tabanında yoksa, gönül rahatlığıyla diğer bilgileri sormaya devam edebiliriz.
        yil = int(input("Çıkış Yılı (Örn: 2023): "))
        tur = input("Türü (Birden fazlaysa virgülle ayırın Örn: Dram, Aksiyon): ")
        sure_dk = int(input("Filmin Süresi (Dakika cinsinden, Örn: 120): "))
        izlenme_durumu = input("İzlenme Durumu (İzlendi / İzlenecek): ")
        favori_mi = input("Favorilere eklensin mi? (Evet/Hayır): ")
        kisisel_puan = float(input("Kişisel Puanınız (1-10 arası, izlemediyseniz 0 giriniz): "))

        # Her şey tamamsa veriyi tabloya ekliyoruz.
        imlec.execute("""
            INSERT INTO filmler (ad, yil, tur, sure_dk, izlenme_durumu, favori_mi, kisisel_puan)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (ad, yil, tur, sure_dk, izlenme_durumu, favori_mi, kisisel_puan))

        baglanti.commit()
        baglanti.close()
        print(f"\n✅ Başarılı: '{ad}' arşivinize eklendi!")

    except ValueError:
        print("\n❌ Hata: Yıl, süre veya puan girerken lütfen sadece RAKAM kullanınız!")
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)

def filmleri_listele(sorgu="SELECT * FROM filmler"):
    # Hocam bu fonksiyonu birden fazla yerde kullanabilmek için dinamik sorgu alacak şekilde tasarladım.
    try:
        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()
        imlec.execute(sorgu)

        # HOCAM DİKKAT: 13. Hafta 31. Slaytta belirttiğiniz üzere fetchall() veya fetchone() kullanmadım.
        # Bunun yerine verileri doğrudan imleç üzerinden for döngüsü ile çektim.
        kayit_var_mi = False
        for film in imlec:
            kayit_var_mi = True  # Döngü bir kere bile dönerse demek ki kayıt vardır.
            print(
                f"ID: {film[0]} | Ad: {film[1]} ({film[2]}) | Tür: {film[3]} | Süre: {film[4]}dk | Durum: {film[5]} | Puan: {film[7]}")

        # Eğer döngü hiç çalışmadıysa aranan film yok demektir, program hata vermesin diye kullanıcıyı uyarıyorum.
        if not kayit_var_mi:
            print("Bu kritere uygun film bulunamadı.")

        baglanti.close()
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)


def isimle_ara():
    # Hocam kullanıcının girdiği kelimenin filmin isminin içinde geçip geçmediğini SQL'deki LIKE operatörü ile bulduruyorum.
    print("\n--- 🔍 FİLM ARA ---")
    kelime = input("Aramak istediğiniz filmin adını (veya bir kısmını) giriniz: ")
    sorgu = f"SELECT * FROM filmler WHERE ad LIKE '%{kelime}%'"
    filmleri_listele(sorgu)  # Sorguyu listeleme fonksiyonuma gönderip sonuçları yazdırıyorum.


def ture_gore_listele():
    # Hocam bir filmin birden fazla türü olabiliyor (Örn: Suç, Komedi, Gerilim). Bunları tek tek ayırıp listelemek için bu gelişmiş yapıyı kurdum.
    print("\n--- 📂 TÜR SEÇİMİ ---")
    try:
        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()
        imlec.execute("SELECT tur FROM filmler")

        # Aynı türlerin menüde tekrar tekrar listelenmemesi için Python'ın Küme (Set) veri yapısını kullandım. Kümeler aynı elemanı 1 kez tutar.
        benzersiz_turler = set()

        kayit_var = False
        for satir in imlec:
            kayit_var = True
            tur_metni = satir[0]
            if tur_metni:
                # Virgülle ayrılmış türleri split ile bölüyorum ("Suç, Komedi" -> "Suç" ve "Komedi" oluyor).
                parcalar = tur_metni.split(",")
                for parca in parcalar:
                    # strip() ile başındaki sonundaki boşlukları siliyor, capitalize() ile baş harfini büyütüp kümeye ekliyorum.
                    benzersiz_turler.add(parca.strip().capitalize())

        if not kayit_var or len(benzersiz_turler) == 0:
            print("Arşivinizde henüz hiç film yok.")
            baglanti.close()
            return

        print("Arşivinizdeki Film Türleri:")
        # Menüde güzel görünmesi için kümeyi listeye çevirip alfabetik sıralattım hocam.
        tur_listesi = sorted(list(benzersiz_turler))

        sayac = 1
        for t in tur_listesi:
            print(f"{sayac}. {t}")
            sayac += 1

        secim = int(input(f"\nLütfen listelemek istediğiniz türün numarasını seçin (1-{len(tur_listesi)}): "))

        if 1 <= secim <= len(tur_listesi):
            secilen_tur = tur_listesi[secim - 1]
            print(f"\n--- 🍿 İÇİNDE '{secilen_tur.upper()}' GEÇEN FİLMLER ---")

            # Seçilen tek türü, LIKE komutuyla çoklu türler barındıran filmlerin içinde aratıyorum.
            sorgu = f"SELECT * FROM filmler WHERE tur LIKE '%{secilen_tur}%'"
            filmleri_listele(sorgu)
        else:
            print("\n❌ Hata: Geçersiz bir numara seçtiniz.")

        baglanti.close()

    except ValueError:
        print("\n❌ Hata: Lütfen seçim yapmak için sadece RAKAM giriniz.")
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)


def rastgele_film_oner():
    # Hocam izlenecekler listesindeki filmlerden şansa birini önermesi için SQL'in RANDOM() komutunu kullandım.
    print("\n--- 🎲 BUGÜN NE İZLESEM? ---")
    try:
        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()

        # ORDER BY RANDOM() tabloyu rastgele karıştırıyor, LIMIT 1 ise en üstteki tek filmi getiriyor.
        imlec.execute(
            "SELECT ad, tur, sure_dk FROM filmler WHERE izlenme_durumu = 'İzlenecek' ORDER BY RANDOM() LIMIT 1")

        film_onerildi = False
        for film in imlec:
            film_onerildi = True
            print(f"Sistem sizin için seçti: '{film[0]}'")
            print(f"Tür: {film[1]} | Süre: {film[2]} dakika. İyi seyirler!")

        #Burada geleceği düşünmezsem bug oluşabilirdi. İzlenecek filmlerin hepsini ileride izlendi olarak düzenlersem diye ekledim.
        if not film_onerildi:
            print("İzlenecekler listeniz şu an boş. Arşive yeni filmler eklemelisiniz!")

        baglanti.close()
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)


def istatistikleri_goster():
    # Hocam burada verileri Python'a çekip hesaplamak yerine, doğrudan SQL'in yerleşik matematik fonksiyonlarına hesaplattım.
    print("\n--- 📊 ARŞİV İSTATİSTİKLERİ ---")
    try:
        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()

        # 1. COUNT() ile tablodaki toplam kayıtlı (id) film sayısını saydırıyorum.
        imlec.execute("SELECT COUNT(id) FROM filmler")
        toplam_film = 0
        for satir in imlec:
            toplam_film = satir[0]

        if toplam_film == 0:
            print("Arşivinizde henüz film bulunmuyor.")
            baglanti.close()
            return

        # 2. SUM() ile sadece izlediğim filmlerin (sure_dk) sürelerini toplayıp hayatta sinemaya ne kadar vakit ayırdığımı bulduruyorum.
        imlec.execute("SELECT SUM(sure_dk) FROM filmler WHERE izlenme_durumu = 'İzlendi'")
        toplam_sure = 0
        for satir in imlec:
            if satir[0] is not None:
                toplam_sure = satir[0]

        # 3. AVG() ile de izlediğim ve puan verdiğim filmlerin puan ortalamasını hesaplatıyorum.
        imlec.execute("SELECT AVG(kisisel_puan) FROM filmler WHERE kisisel_puan > 0")
        ortalama_puan = 0.0
        for satir in imlec:
            if satir[0] is not None:
                ortalama_puan = satir[0]

        print(f"Toplam Kayıtlı Film: {toplam_film} adet")
        print(f"İzlenen Toplam Süre: {toplam_sure} dakika (Yaklaşık {toplam_sure / 60:.1f} saat)")
        print(f"Arşiv Puan Ortalaması: {ortalama_puan:.1f}/10")

        baglanti.close()
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)


def film_sil():
    # Hocam veritabanından veri silme işlemini bu fonksiyonda kurguladım.
    print("\n--- 🗑️ FİLM SİL ---")
    try:
        silinecek_id = int(input("Silmek istediğiniz filmin ID numarasını giriniz: "))

        baglanti = sqlite3.connect("film_arsivim.db")
        imlec = baglanti.cursor()

        # Kullanıcının sildiği film ekranda görünsün diye önce o ID'ye sahip filmin adını çekiyorum.
        imlec.execute("SELECT ad FROM filmler WHERE id = ?", (silinecek_id,))

        film_bulundu = False
        film_adi = ""
        for satir in imlec:
            film_bulundu = True
            film_adi = satir[0]

            # Eğer kullanıcının girdiği ID'de bir film varsa silme (DELETE) işlemini başlatıyorum.
        if film_bulundu:
            imlec.execute("DELETE FROM filmler WHERE id = ?", (silinecek_id,))
            baglanti.commit()
            print(f"✅ Başarılı: '{film_adi}' arşivden silindi!")
        else:
            print("❌ Hata: Bu ID numarasına sahip bir film bulunamadı.")

        baglanti.close()
    except ValueError:
        print("\n❌ Hata: Lütfen ID numarasını tam sayı olarak giriniz!")
    except sqlite3.Error as hata:
        print("\n❌ Veri tabanı Hatası:", hata)


def ana_menu():
    # Hocam programın tek sefer çalışıp bitmemesi, kullanıcı çıkış yapana kadar menünün dönmesi için while True döngüsü kurdum.
    while True:
        print("\n✧ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ 🎬 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ✧")
        print("            KİŞİSEL FİLM ARŞİVİM            ")
        print("✧ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ 🍿 ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ✧")
        print("1. Yeni Film Ekle")
        print("2. Tüm Filmleri Listele")
        print("3. İsimle Film Ara")
        print("4. Türe Göre Filmleri Gör")
        print("5. İzleneceklerden Rastgele Film Öner")
        print("6. Arşiv İstatistiklerini Gör")
        print("7. Film Sil")
        print("8. Çıkış")
        print("✧ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ✧")

        try:
            secim = int(input("Lütfen yapmak istediğiniz işlemi seçin (1-8): "))

            # Kullanıcının seçimine göre ilgili fonksiyonlara yönlendirme (karar yapısı) kullanıyorum hocam.
            if secim == 1:
                film_ekle()
            elif secim == 2:
                print("\n--- 📋 TÜM FİLM ARŞİVİ ---")
                filmleri_listele()
            elif secim == 3:
                isimle_ara()
            elif secim == 4:
                ture_gore_listele()
            elif secim == 5:
                rastgele_film_oner()
            elif secim == 6:
                istatistikleri_goster()
            elif secim == 7:
                film_sil()
            elif secim == 8:
                print("Programdan çıkılıyor. İyi seyirler!")
                break
            else:
                print("\n❌ Hata: Lütfen 1 ile 8 arasında bir rakam giriniz.")

        except ValueError:
            # Kullanıcı menüde numara yerine harf girerse diye hata yakalama ekledim.
            print("\n❌ Hata: Geçersiz giriş! Lütfen sadece RAKAM giriniz.")

# Proje ana dosya olarak çalıştırıldığında ilk buralar çalışır hocam.
if __name__ == "__main__":
    veritabanini_hazirla()  # Önce tablom ve listem hazırlanıyor.
    ana_menu()  # Sonra menü açılıyor.