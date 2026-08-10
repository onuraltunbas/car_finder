import cv2
import os

# Ana klasör yollarımız
video_ana_klasoru = "videos"
cikti_ana_klasoru = "extracted_frames"
saniyedeki_kare_hedefi = 8

# 1 saniye = 1000 milisaniye. 5 kare için her 200 milisaniyede 1 kayıt yapacağız.
milisaniye_hedefi = 1000 / saniyedeki_kare_hedefi  

if not os.path.exists(cikti_ana_klasoru):
    os.makedirs(cikti_ana_klasoru)

for kasa_kodu in os.listdir(video_ana_klasoru):
    kasa_yolu = os.path.join(video_ana_klasoru, kasa_kodu)
    
    if os.path.isdir(kasa_yolu):
        print(f"\n--- {kasa_kodu.upper()} klasörü işleniyor ---")
        cikti_kasa_yolu = os.path.join(cikti_ana_klasoru, kasa_kodu)
        os.makedirs(cikti_kasa_yolu, exist_ok=True)
        
        for video_dosyasi in os.listdir(kasa_yolu):
            if video_dosyasi.endswith((".webm", ".mp4")):
                video_tam_yol = os.path.join(kasa_yolu, video_dosyasi)
                video_adi_temiz = video_dosyasi.split('.')[0]
                
                cap = cv2.VideoCapture(video_tam_yol)
                
                kaydedilen = 0
                # İlk kareyi en başta alması için eksi değerden başlatıyoruz
                son_kayit_zamani = -milisaniye_hedefi 
                
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    
                    # Mevcut karenin videonun neresinde olduğunu milisaniye olarak alıyoruz
                    suan_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
                    
                    # Eğer son kayıt üzerinden hedef süremiz (200ms) geçtiyse kaydet
                    if suan_ms - son_kayit_zamani >= milisaniye_hedefi:
                        dosya_adi = f"{kasa_kodu}_{video_adi_temiz}_frame_{kaydedilen}.jpg"
                        kayit_yolu = os.path.join(cikti_kasa_yolu, dosya_adi)
                        
                        cv2.imwrite(kayit_yolu, frame)
                        kaydedilen += 1
                        son_kayit_zamani = suan_ms
                        
                cap.release()
                print(f"{video_dosyasi} dosyasından tam {kaydedilen} adet kare çıkartıldı.")

print("\nTüm işlemler tamamlandı! Kronometre mantığıyla resimler kusursuzca çıkarıldı.")