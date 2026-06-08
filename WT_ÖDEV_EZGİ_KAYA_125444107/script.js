document.addEventListener('DOMContentLoaded', function () {

    var btnKaranlik = document.getElementById('btn-karanlik');
    var btnAydinlik = document.getElementById('btn-aydinlik');
    var btnMavi = document.getElementById('btn-mavi');
    var btnYesil = document.getElementById('btn-yesil');
    var temaMesaj = document.getElementById('tema-mesaj');

    function temalariTemizle() {
        document.body.classList.remove('karanlik-tema', 'mavi-tema', 'yesil-tema');
        document.body.style.backgroundColor = '';
        document.body.style.color = '';
    }

    function temaKaydet(tema) {
        localStorage.setItem('seciliTema', tema);
    }

    function temaYukle() {
        var kayitliTema = localStorage.getItem('seciliTema');
        if (kayitliTema) {
            temalariTemizle();
            if (kayitliTema !== 'aydinlik') {
                document.body.classList.add(kayitliTema);
            }
        }
    }

    temaYukle();

    if (btnKaranlik) {
        btnKaranlik.addEventListener('click', function () {
            temalariTemizle();
            document.body.classList.add('karanlik-tema');
            temaKaydet('karanlik-tema');
            if (temaMesaj) { temaMesaj.textContent = '🌙 Karanlık tema aktif'; temaMesaj.style.color = '#3498db'; }
        });
    }

    if (btnAydinlik) {
        btnAydinlik.addEventListener('click', function () {
            temalariTemizle();
            temaKaydet('aydinlik');
            if (temaMesaj) { temaMesaj.textContent = '☀️ Aydınlık tema aktif'; temaMesaj.style.color = '#f39c12'; }
        });
    }

    if (btnMavi) {
        btnMavi.addEventListener('click', function () {
            temalariTemizle();
            document.body.classList.add('mavi-tema');
            temaKaydet('mavi-tema');
            if (temaMesaj) { temaMesaj.textContent = '🔵 Mavi tema aktif'; temaMesaj.style.color = '#3498db'; }
        });
    }

    if (btnYesil) {
        btnYesil.addEventListener('click', function () {
            temalariTemizle();
            document.body.classList.add('yesil-tema');
            temaKaydet('yesil-tema');
            if (temaMesaj) { temaMesaj.textContent = '🟢 Yeşil tema aktif'; temaMesaj.style.color = '#27ae60'; }
        });
    }

    var ipuclari = [
        "💡 Beyaz haç yaparken önce kenar parçalarını bulun, sonra merkez renklerle eşleştirin.",
        "💡 R U R' U' algoritması küp çözmenin temel yapı taşıdır!",
        "💡 Aceleniz olmasın. Önce yavaş ve doğru yapmayı öğrenin.",
        "💡 F2L tekniğini öğrenmek sürenizi yarıya indirebilir.",
        "💡 Pratik yaparken küpü her seferinde farklı karıştırın.",
        "💡 Parmak hareketlerinizi optimize edin. Küpü sıkı tutmayın.",
        "💡 Son katman algoritmalarını en az 50 kez tekrar edin.",
        "💡 Küpünüzü düzenli yağlayın. Pürüzsüz dönüş hızı artırır.",
        "💡 Mirror Cube çözerken parçaların kalınlığına dokunarak bakın.",
        "💡 Megaminx çözmek 3x3 algoritmalarınızı pekiştirir.",
        "💡 Pyraminx çözerken uçları önce hizalayın — çok kolaylaşır.",
        "💡 Her gün en az 10 çözüm yaparak alışkanlık oluşturun.",
        "💡 4x4'te parite algoritmalarını ezberlemeniz şart!",
        "💡 Kilominx, Megaminx'in basit versiyonudur. Onunla başlayın.",
        "💡 Sabırlı olun! Dünya rekortmenleri bile yıllar pratik yapmıştır."
    ];

    var btnIpucu = document.getElementById('btn-ipucu');
    var ipucuMetin = document.getElementById('ipucu-metin');

    if (btnIpucu && ipucuMetin) {
        btnIpucu.addEventListener('click', function () {
            var rastgele = Math.floor(Math.random() * ipuclari.length);
            ipucuMetin.textContent = ipuclari[rastgele];
            ipucuMetin.style.opacity = '0';
            setTimeout(function () {
                ipucuMetin.style.transition = 'opacity 0.5s ease';
                ipucuMetin.style.opacity = '1';
            }, 100);
        });
    }

    var canliSaat = document.getElementById('canli-saat');
    var canliTarih = document.getElementById('canli-tarih');

    function saatGuncelle() {
        var simdi = new Date();
        var saat = String(simdi.getHours()).padStart(2, '0');
        var dakika = String(simdi.getMinutes()).padStart(2, '0');
        var saniye = String(simdi.getSeconds()).padStart(2, '0');
        if (canliSaat) { canliSaat.textContent = saat + ':' + dakika + ':' + saniye; }

        if (canliTarih) {
            var gunler = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];
            var aylar = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
            canliTarih.textContent = gunler[simdi.getDay()] + ', ' + simdi.getDate() + ' ' + aylar[simdi.getMonth()] + ' ' + simdi.getFullYear();
        }
    }

    if (canliSaat) { saatGuncelle(); setInterval(saatGuncelle, 1000); }

    var kronEkran = document.getElementById('kronometre-ekran');
    var btnBaslat = document.getElementById('btn-baslat');
    var btnDurdur = document.getElementById('btn-durdur');
    var btnKronSifirla = document.getElementById('btn-sifirla');
    var kronInterval = null;
    var kronSaniye = 0;

    function kronGoster() {
        var s = Math.floor(kronSaniye / 3600);
        var d = Math.floor((kronSaniye % 3600) / 60);
        var sn = kronSaniye % 60;
        if (kronEkran) {
            kronEkran.textContent = String(s).padStart(2, '0') + ':' + String(d).padStart(2, '0') + ':' + String(sn).padStart(2, '0');
        }
    }

    if (btnBaslat) {
        btnBaslat.addEventListener('click', function () {
            if (kronInterval === null) { kronInterval = setInterval(function () { kronSaniye++; kronGoster(); }, 1000); }
        });
    }
    if (btnDurdur) { btnDurdur.addEventListener('click', function () { clearInterval(kronInterval); kronInterval = null; }); }
    if (btnKronSifirla) {
        btnKronSifirla.addEventListener('click', function () { clearInterval(kronInterval); kronInterval = null; kronSaniye = 0; kronGoster(); });
    }

    var btnPratik = document.getElementById('btn-pratik');
    var pratikSayi = document.getElementById('pratik-sayi');
    var btnPratikSifirla = document.getElementById('btn-pratik-sifirla');
    var cozumSayisi = 0;

    if (btnPratik && pratikSayi) {
        btnPratik.addEventListener('click', function () {
            cozumSayisi++;
            pratikSayi.textContent = 'Toplam çözüm: ' + cozumSayisi;
            if (cozumSayisi === 10) alert('🎉 10 çözüme ulaştınız!');
            if (cozumSayisi === 50) alert('🏆 50 çözüm! Harika!');
            if (cozumSayisi === 100) alert('👑 100 çözüm! Speedcuber oluyorsunuz!');
        });
    }
    if (btnPratikSifirla && pratikSayi) {
        btnPratikSifirla.addEventListener('click', function () { cozumSayisi = 0; pratikSayi.textContent = 'Toplam çözüm: 0'; });
    }

});

function toggleSSS(id) {
    var el = document.getElementById(id);
    if (el) { el.style.display = el.style.display === 'block' ? 'none' : 'block'; }
}
function formKontrol() {
    var ad = document.getElementById('ad-soyad');
    var email = document.getElementById('email');
    var mesaj = document.getElementById('mesaj');
    var sifre = document.getElementById('sifre');
    var sonuc = document.getElementById('form-sonuc');

    if (ad && ad.value.trim().length < 3) { alert('⚠️ Ad soyad en az 3 karakter olmalı.'); ad.focus(); return false; }
    if (email && !email.value.includes('@')) { alert('⚠️ Geçerli e-posta giriniz.'); email.focus(); return false; }
    if (sifre && sifre.value.length > 0 && sifre.value.length < 6) { alert('⚠️ Şifre en az 6 karakter olmalı.'); sifre.focus(); return false; }
    if (!document.querySelector('input[name="deneyim"]:checked')) { alert('⚠️ Deneyim seviyesi seçiniz.'); return false; }
    if (mesaj && mesaj.value.trim().length < 10) { alert('⚠️ Mesaj en az 10 karakter olmalı.'); mesaj.focus(); return false; }

    if (sonuc) {
        sonuc.textContent = '✅ Formunuz gönderildi! En kısa sürede dönüş yapacağız.';
        sonuc.style.color = '#27ae60';
        sonuc.style.padding = '12px';
        sonuc.style.backgroundColor = '#eafaf1';
        sonuc.style.borderRadius = '10px';
    }
    var form = document.getElementById('iletisim-formu');
    if (form) form.reset();
    return false;
}
function degerlendir(mesaj) {
    var el = document.getElementById('deger-sonuc');
    if (el) { el.textContent = '📝 ' + mesaj + ' — Teşekkürler!'; el.style.color = '#27ae60'; }
}