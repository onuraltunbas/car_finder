import cv2
import os
from ultralytics import YOLO

# Eğittiğimiz E46 modelini yüklüyoruz
model = YOLO('/home/onur/Desktop/car_finder/models/best.pt')

# Kullanılacak klasörlerin isimleri
girdi_klasoru = "/home/onur/Desktop/car_finder/extracted_frames/e60"
cikti_klasoru = "/home/onur/Desktop/car_finder/e60_islenmis"

# Eğer bu klasörler yoksa, kod otomatik olarak oluşturacak
os.makedirs(girdi_klasoru, exist_ok=True)
os.makedirs(cikti_klasoru, exist_ok=True)

# Girdi klasöründeki tüm resim dosyalarını bul
fotograflar = [f for f in os.listdir(girdi_klasoru) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not fotograflar:
    print(f"Uyarı: '{girdi_klasoru}' klasörünün içi boş!")
    print(f"Lütfen içine birkaç fotoğraf atıp kodu tekrar çalıştırın.")
else:
    print(f"Toplam {len(fotograflar)} fotoğraf bulundu. İşlem başlıyor...\n")
    
    for foto_adi in fotograflar:
        foto_yolu = os.path.join(girdi_klasoru, foto_adi)
        
        # Modeli fotoğrafın üzerinde çalıştır
        results = model(foto_yolu)
        
        # İşaretlenmiş (Bounding Box çizilmiş) görüntüyü al
        isaretli_foto = results[0].plot()
        
        # Yeni ismiyle çıktı klasörüne kaydet
        kayit_yolu = os.path.join(cikti_klasoru, f"isaretli_{foto_adi}")
        cv2.imwrite(kayit_yolu, isaretli_foto)
        
        print(f"✔ Başarılı: {foto_adi} işaretlendi ve kaydedildi.")

    print(f"\nHarika! Tüm fotoğraflar işaretlendi. Lütfen '{cikti_klasoru}' klasörünü kontrol edin.")