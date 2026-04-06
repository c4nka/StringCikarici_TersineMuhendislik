# Temel imaj olarak hafif bir Python 3.10 sürümü seçiyoruz
FROM python:3.10-slim

# Konteyner içindeki çalışma dizinimizi (klasörümüzü) ayarlıyoruz
WORKDIR /app

# Bilgisayarımızdaki src klasörünü ve test dosyamızı konteynerin içine kopyalıyoruz
COPY src/ ./src/
COPY hedef_dosya.bin .

# İsteğe bağlı: Aracın çalıştığını göstermek için varsayılan bir komut belirliyoruz
CMD ["python", "src/goblin.py", "hedef_dosya.bin"]
