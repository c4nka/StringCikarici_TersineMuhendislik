# TODO: İleriki sürümlerde Base64 şifreleme çözücü (deobfuscation) yeteneği eklenecek.
# TODO: Çıktıları terminal yerine otomatik olarak rapor.json dosyasına aktarma parametresi eklenecek.

import os
import re
import string
import argparse

def extract_strings_from_binary(file_path, min_length=4):
    """
    Dosyayı bayt bayt okuyarak içindeki anlamlı ASCII (İngilizce) kelimeleri çıkarır.
    (Motor bloğunun içindeki kağıt parçalarını bulma aşaması)
    """
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print(f"[-] Hata: {file_path} bulunamadı!")
        return []

    # Sadece yazdırılabilir İngilizce/ASCII karakterleri filtrele
    printable = set(string.printable.encode('ascii'))
    current_string = bytearray()
    extracted_strings = []

    for byte in data:
        if byte in printable:
            current_string.append(byte)
        else:
            if len(current_string) >= min_length:
                # Bulunan bayt dizisini string'e çevir ve listeye ekle
                extracted_strings.append(current_string.decode('ascii', errors='ignore').strip())
            current_string = bytearray()
            
    # Dosya sonundaki olası son string'i de ekle
    if len(current_string) >= min_length:
        extracted_strings.append(current_string.decode('ascii', errors='ignore').strip())

    return extracted_strings

def analyze_for_sensitive_data(strings_list):
    """
    Çıkarılan metinlerin içinde Regex ile hassas veri (C2, API, Password) avlar.
    """
    print("\n[+] Regex Analizi Başlıyor...\n")
    
    # Avlanacak hassas verilerin Regex (Düzenli İfade) kuralları
    patterns = {
        "C2 Sunucu URL'si": r"https?://[a-zA-Z0-9./\-_?=]+",
        "C2 IP Adresi": r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", # Sınır ihlali kaldırıldı!
        "Hassas Veri (API KEY)": r"(?i)(?:api_key|apikey|token|secret)[\s:=]+['\"]?([A-Za-z0-9_\-]{16,})['\"]?",
        "Hassas Veri (PASSWORD)": r"(?i)(?:password|pass|pwd)[\s:=]+['\"]?([A-Za-z0-9@#$%^&+=]+)['\"]?"
    }

    found_items = {key: [] for key in patterns}

    for s in strings_list:
        for key, pattern in patterns.items():
            matches = re.findall(pattern, s)
            for match in matches:
                # Bulunan eşleşmeyi temizle ve kaydet
                item = match if isinstance(match, str) else "".join(match)
                if item not in found_items[key]:  # Kopyaları engelle
                    found_items[key].append(item)

    # Sonuçları ekrana şık bir şekilde yazdır
    for category, items in found_items.items():
        if items:
            print(f"--- {category} BULUNDU! ---")
            for item in items:
                print(f" -> {item}")
            print()

def main():
    print("=======================================")
    print("    GOBLIN TOOLBOX - String Extractor  ")
    print("=======================================")
    
    parser = argparse.ArgumentParser(description="Binary dosyalardan string çıkarıp hassas veri arayan analiz aracı.")
    parser.add_argument("file", help="Analiz edilecek hedefin dosya yolu (örn: malware.exe)")
    parser.add_argument("-m", "--min", type=int, default=4, help="Minimum string uzunluğu (varsayılan: 4)")
    
    args = parser.parse_args()

    print(f"[*] Hedef Dosya: {args.file}")
    print(f"[*] Bayt bayt tarama yapılıyor... (Minimum {args.min} karakter)")
    
    strings = extract_strings_from_binary(args.file, args.min)
    
    if strings:
        print(f"[+] Toplam {len(strings)} adet potansiyel string bulundu.")
        analyze_for_sensitive_data(strings)
    else:
        print("[-] Analiz edilecek geçerli bir veri bulunamadı.")

if __name__ == "__main__":
    main()
