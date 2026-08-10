from bing_image_downloader import downloader

# Aramak istediğimiz anahtar kelimeler (İngilizce aratmak daha iyi sonuç verir)
arama_terimleri = [
    "BMW F30 rear",
    "BMW F10 rear",
    "BMW E46 rear",
    "BMW E60 rear",
    "BMW F30 taillights",
    "BMW F10 back"
]

print("Görsel indirme işlemi başlıyor...")

for terim in arama_terimleri:
    # limit=150: Her arama için kaç fotoğraf indirileceği
    # output_dir: Fotoğrafların kaydedileceği ana klasör
    downloader.download(terim, 
                        limit=150,  
                        output_dir='ham_veriseti', 
                        adult_filter_off=True, 
                        force_replace=False, 
                        timeout=60, 
                        verbose=True)

print("Tüm görseller indirildi! 'ham_veriseti' klasörünü kontrol et.")