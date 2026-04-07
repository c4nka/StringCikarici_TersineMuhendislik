<div align="center">
  <img src="https://images.seeklogo.com/logo-png/61/1/istinye-universitesi-logo-png_seeklogo-610039.png" width="300" alt="İstinye Üniversitesi Logosu">
</div>

# 🧝‍♂️ Goblin Toolbox - String Extractor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Status-Active-success.svg)
![Topic](https://img.shields.io/badge/Topic-Reverse%20Engineering-orange.svg)

**Öğrenci:** Raşit ÇANKAYA (2420191006)  
**Üniversite / Bölüm:** İstinye Üniversitesi - Bilişim Güvenliği Teknolojisi (İÖ)  
**Ders:** Tersine Mühendislik (Reverse Engineering)  
**Danışman:** Keyvan Arasteh Abbasabad

---

## 📑 İçindekiler
- [Geliştirilme Amacı](#-geliştirilme-amacı)
- [Proje Yapısı](#-proje-yapısı)
- [Özellikler](#-özellikler)
- [Kurulum](#️-kurulum)
- [Kullanım](#-kullanım)
- [Çalışma Kanıtı](#-projenin-çalıştığına-dair-görsel-kanıt)
- [Ayıklanan Veri Özeti](#-ayiklanan-veri-ozeti)
- [Lisans](#-lisans)

---

## 🎯 Geliştirilme Amacı

Bu proje, **Tersine Mühendislik (Reverse Engineering)** ve **Zararlı Yazılım Analizi (Malware Analysis)** alanlarındaki temel "Statik Analiz" kavramlarını pratik bir düzeyde uygulamak ve pekiştirmek amacıyla eğitim odaklı geliştirilmiştir. 

Projenin temel hedefi; derlenmiş çalıştırılabilir dosyaların (binaries) veya bellek dökümlerinin içinde genellikle gözden kaçan, zayıf obfuskasyon uygulanan veya şifrelenmeyi unutulan açık metin (plain-text) kalıntılarını tespit etmektir. Bir siber güvenlik analistinin bakış açısıyla tasarlanan bu araç, yapısal olmayan ham veriler (unstructured raw data) içerisinden düzenli ifadeler (Regex) yardımıyla anlamlı siber istihbarat (C2 sunucu bağlantıları, API anahtarları ve kimlik bilgileri) çıkarma mantığını kavramayı sağlamaktadır.

## 📁 Proje Yapısı

```text
StringCikarici_TersineMuhendislik/
│
├── docs/                          # Proje dokümantasyon klasörü
│   └── aciklama.txt
│
├── screenshots/
│   └── goblin_analiz_sonucu.png   # Projenin çalıştığını gösteren terminal çıktısı
├── src/
    └── goblin.py                      # Aracın ana kaynak kodu (Python betiği)
    └── hedef_dosya.bin                # Analiz edilen örnek/test binary dosyası
└── README.md                      # Proje dökümantasyonu
```

## 🚀 Özellikler
Bayt-Bayt Analiz: Dosya formatından bağımsız olarak ham veriyi okur ve İngilizce/ASCII karakter dizilerini cımbızla çeker.

Esnek Regex Mimarisi: Geliştirilmiş regex kuralları sayesinde hem ayrık hem de bitişik (obfuscate edilmiş) metinleri tespit edebilir.

Hassas Veri Avcısı: Çıkarılan metinler içinde şu kritik verileri otomatik olarak tespit eder:

C2 (Command & Control) Sunucu URL'leri (örneğin: https://)

C2 IP Adresleri (harf arasına sıkışsa dahi)

API Anahtarları (API Keys / Tokens)

Parolalar (Passwords)

## 🛠️ Kurulum

Bu araç tamamen standart Python kütüphaneleri kullanılarak yazılmıştır. Herhangi bir harici modül (pip install) gerektirmez.

Repoyu bilgisayarınıza klonlayın:

```bash
git clone [https://github.com/c4nka/StringCikarici_TersineMuhendislik.git](https://github.com/c4nka/StringCikarici_TersineMuhendislik.git)
```

Proje dizinine gidin:

```bash
cd StringCikarici_TersineMuhendislik
```

## 💻 Kullanım

Aracı komut satırı (CLI) üzerinden çalıştırabilirsiniz. Hedef dosyanın yolunu parametre olarak vermeniz yeterlidir.

Örnek Çalıştırma Komutu:

```bash
python src/goblin.py hedef_dosya.bin
```

## 🎬 Demo

Aşağıdaki ekran kaydında projenin kurulum, kullanım, hata yakalama (invalid input), temel analiz süreci ve entegre test süreçlerinin adım adım nasıl çalıştığını görebilirsiniz:

[Demo](./demo/demo.html)
<br>
[Demo MP4](./demo/demo.mp4)
<br>
<a href="https://youtu.be/X5OuelGrnPk" target="_blank">Youtube Demo Videosunu İzlemek İçin Tıklayın</a>

<video src="demo/demo.H264" width="100%" controls>
</video>

## 📊 Projenin Çalıştığına Dair Görsel Kanıt

Bu görsel, aracın `hedef_dosya.bin` üzerinde yaptığı analizin gerçek terminal çıktısını göstermektedir. Geliştirilen esnek regex kuralları sayesinde, veriler harf arasına sıkışmış olsa dahi (IP adresi ve temiz URL) cımbızla çekilerek başarıyla tespit edilmiştir.

![Proje Çıktısı](./screenshots/ss1.png)

## Ayıklanan Veri Özeti

Yukarıdaki ekran görüntüsünde görüldüğü gibi, araç aşağıdaki hassas verileri başarıyla tespit etmiş ve ayıklamıştır:

| Hassas Veri Türü | Ayıklanan Veri Değeri |
| :--- | :--- |
| **C2 Sunucu URL'si** | `https://malicious-c2-server.com/payload.exe` |
| **C2 IP Adresi** | `192.168.1.105` |
| **API Anahtarı** | `AKIAIOSFODNN7EXAMPLE` |
| **Parola** | `SuperSecretAdmin123` |

## 📜 Lisans

Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) altında lisanslanmıştır. 

## ⚠️ Yasal Uyarı

Bu araç **Tersine Mühendislik** dersi kapsamında ve tamamen **eğitim/araştırma amaçlı** geliştirilmiştir. Yalnızca yasal yetkiniz olan dosyalar üzerinde analiz yapınız.
