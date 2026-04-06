<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/tr/archive/3/36/20200813164817%21Istinye_University_Logo.png" alt="İstinye Üniversitesi Logosu" width="200"/>
</p>

# 🧝‍♂️ Goblin Toolbox - String Extractor

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Status-Active-success.svg)
![Topic](https://img.shields.io/badge/Topic-Reverse%20Engineering-orange.svg)

**Ders:** Tersine Mühendislik (Reverse Engineering)
**Danışman:** [Danışman Hocanın Adı ve Soyadı Buraya]
**Geliştiren:** Raşit Çankaya

---

## 📑 İçindekiler
- [Geliştirilme Amacı](#-geliştirilme-amacı)
- [Proje Yapısı](#-proje-yapısı)
- [Özellikler](#-özellikler)
- [Kurulum](#️-kurulum)
- [Kullanım](#-kullanım)
- [Çalışma Kanıtı](#-projenin-çalıştığına-dair-görsel-kanıt)

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
│
├── goblin.py                      # Aracın ana kaynak kodu (Python betiği)
├── hedef_dosya.bin                # Analiz edilen örnek/test binary dosyası
└── README.md                      # Proje dökümantasyonu
```

🚀 Özellikler
Bayt-Bayt Analiz: Dosya formatından bağımsız olarak ham veriyi okur ve İngilizce/ASCII karakter dizilerini cımbızla çeker.

Esnek Regex Mimarisi: Geliştirilmiş regex kuralları sayesinde hem ayrık hem de bitişik (obfuscate edilmiş) metinleri tespit edebilir.

Hassas Veri Avcısı: Çıkarılan metinler içinde şu kritik verileri otomatik olarak tespit eder:

C2 (Command & Control) Sunucu URL'leri (örneğin: https://)

C2 IP Adresleri (harf arasına sıkışsa dahi)

API Anahtarları (API Keys / Tokens)

Parolalar (Passwords)

🛠️ Kurulum
Bu araç tamamen standart Python kütüphaneleri kullanılarak yazılmıştır. Herhangi bir harici modül (pip install) gerektirmez.
