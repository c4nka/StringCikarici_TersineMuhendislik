# 🧝‍♂️ Goblin Toolbox - String Extractor

**Tersine Mühendislik (Reverse Engineering) Eğitim Projesi**

Goblin Toolbox, derlenmiş binary (ikili) dosyaların veya zararlı yazılımların (malware) bellek dökümlerinin içinde gizlenmiş anlamlı metinleri (strings) ayıklamak için tasarlanmış hafif ve etkili bir Python aracıdır. Dosyaları bayt bayt okuyarak motor bloğunun arasına sıkışmış "kağıt parçalarını" bulur ve üzerlerinde Düzenli İfadeler (Regex) ile hassas veri avına çıkar.

## 🚀 Özellikler

- **Bayt-Bayt Analiz:** Dosya formatından bağımsız olarak ham veriyi okur ve İngilizce/ASCII karakter dizilerini cımbızla çeker.
- **Obfuscation (Gizleme) Direnci:** Bitişik veya arasına boşluk/yeni satır eklenmiş gizli metinleri yakalayacak şekilde esnek Regex mimarisine sahiptir.
- **Hassas Veri Avcısı:** Çıkarılan metinler içinde şu kritik verileri otomatik olarak tespit eder:
  - C2 (Command & Control) Sunucu URL'leri
  - C2 IP Adresleri
  - API Anahtarları (API Keys / Tokens)
  - Parolalar (Passwords)

## 🛠️ Kurulum

Bu araç tamamen standart Python kütüphaneleri kullanılarak yazılmıştır. Herhangi bir harici modül (pip install) gerektirmez.

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/Goblin-String-Extractor.git](https://github.com/KULLANICI_ADIN/Goblin-String-Extractor.git)

2. Proje dizinine gidin:

Bash
cd Goblin-String-Extractor

💻 Kullanım
Aracı komut satırı (CLI) üzerinden çalıştırabilirsiniz. Hedef dosyanın yolunu parametre olarak vermeniz yeterlidir.

Temel Kullanım:

python goblin.py hedef_dosya.bin

Gelişmiş Kullanım (Minimum String Uzunluğunu Belirleme):

Varsayılan olarak minimum 4 karakter uzunluğundaki metinler çıkarılır. Bunu -m veya --min parametresi ile değiştirebilirsiniz:

python goblin.py hedef_dosya.bin -m 6

📊 Örnek Çıktı

=======================================
    GOBLIN TOOLBOX - String Extractor  
=======================================
[*] Hedef Dosya: hedef_dosya.bin
[*] Bayt bayt tarama yapılıyor... (Minimum 4 karakter)
[+] Toplam 7 adet potansiyel string bulundu.

[+] Regex Analizi Başlıyor...

--- C2 Sunucu URL'si BULUNDU! ---
 -> [https://malicious-c2-server.com/payload.exe](https://malicious-c2-server.com/payload.exe)

--- C2 IP Adresi BULUNDU! ---
 -> 192.168.1.105

--- Hassas Veri (API KEY) BULUNDU! ---
 -> AKIAIOSFODNN7EXAMPLE

--- Hassas Veri (PASSWORD) BULUNDU! ---
 -> SuperSecretAdmin123!

 Bu araç Tersine Mühendislik dersi kapsamında ve tamamen eğitim/araştırma amaçlı geliştirilmiştir. Yalnızca yasal yetkiniz olan dosyalar üzerinde analiz yapınız.
