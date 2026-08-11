import cv2
import numpy as np
import time
from mss import mss
from ultralytics import YOLO

# Eğittiğimiz E46 modelini yüklüyoruz
model = YOLO('/home/onur/Desktop/car_finder/models/best.pt')

# Ekran yakalama aracını başlat
sct = mss()
monitor = sct.monitors[1] 

print("Ekran yakalama başladı! Çıkmak için ekrandaki pencere seçiliyken 'q' tuşuna bas.")

# FPS hesaplamak için zaman tutucu
onceki_zaman = 0

while True:
    sct_img = sct.grab(monitor)
    frame = np.array(sct_img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    # Modeli çalıştır (Sınıf adı ve doğruluk skoru burada otomatik hesaplanır)
    results = model(frame)
    
    # Kutu, sınıf adı ve doğruluk skorunu görüntünün üzerine çiz
    annotated_frame = results[0].plot()

    # --- FPS HESAPLAMA VE EKRANA YAZDIRMA ---
    su_anki_zaman = time.time()
    fps = 1 / (su_anki_zaman - onceki_zaman)
    onceki_zaman = su_anki_zaman

    # FPS değerini sol üst köşeye yeşil renkli olarak yazdır
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    # Ekrana sığması için yeniden boyutlandır
    annotated_frame = cv2.resize(annotated_frame, (1280, 720))

    cv2.imshow("YOLO Canli Ekran Tespiti", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()