from ultralytics import YOLO
import cv2

# Önceden eğitilmiş standart modeli yükle (ilk çalışmada otomatik indirecek)
model = YOLO('yolov8n.pt')

# 0 numaralı kamerayı (webcam) başlat
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Görüntüyü modele ver ve tahminleri al
        results = model(frame)
        
        # Tahmin çizimlerini (kutu ve etiketleri) içeren kareyi al
        annotated_frame = results[0].plot()

        # Ekranda göster
        cv2.imshow("YOLO Canli Test", annotated_frame)

        # 'q' tuşuna basıldığında çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()