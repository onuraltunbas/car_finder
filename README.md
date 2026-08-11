# Car Finder

Minimal YOLO-based vehicle detection project for local setup and testing.

## Türkçe

### Kurulum

1. Python 3.10 veya 3.11 kurun.
2. Proje klasörüne girin:

```bash
cd /home/onur/Desktop/car_finder
```

3. Sanal ortam oluşturun:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Gerekli paketleri kurun:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Alternatif manuel kurulum:

```bash
pip install ultralytics opencv-python numpy mss bing-image-downloader torch
```

5. Model dosyasının mevcut olduğundan emin olun:

```bash
ls models
```

6. Çalıştırma:

```bash
python veri_topla.py
python kareleri_cikar.py
python foto_test.py
python ekran_test.py
```

### Gereksinimler
- Python 3.10+
- pip
- OpenCV
- Ultralytics
- NumPy
- MSS
- Bing Image Downloader
- PyTorch

### Notlar
- Bazı script'lerde mutlak yol kullanıldığı için kendi bilgisayarınızın yolu ile uyumlu hale getirmeniz gerekebilir.
- `models/best.pt` dosyası proje içinde bulunmalıdır.

---

## English

### Installation

1. Install Python 3.10 or 3.11.
2. Go to the project folder:

```bash
cd /home/onur/Desktop/car_finder
```

3. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Manual install alternative:

```bash
pip install ultralytics opencv-python numpy mss bing-image-downloader torch
```

5. Make sure the model file exists:

```bash
ls models
```

6. Run the project:

```bash
python veri_topla.py
python kareleri_cikar.py
python foto_test.py
python ekran_test.py
```

### Requirements
- Python 3.10+
- pip
- OpenCV
- Ultralytics
- NumPy
- MSS
- Bing Image Downloader
- PyTorch

### Notes
- Some scripts use absolute paths, so you may need to update them for your own machine.
- The file `models/best.pt` must be present in the project.

---

## Project Structure

```text
car_finder/
├── README.md
├── requirements.txt
├── veri_topla.py
├── kareleri_cikar.py
├── foto_test.py
├── ekran_test.py
├── models/
│   └── best.pt
├── extracted_frames/
├── videos/
├── ham_veriseti/
└── yolo_test/
```

---

## Quick Start

```bash
cd /home/onur/Desktop/car_finder
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python ekran_test.py
```

This is enough to set up the project and start testing locally.

### Path error / Yol hatası
Some scripts use absolute paths like `/home/onur/Desktop/car_finder`. Update them according to your environment.

Bazı script'lerde `/home/onur/Desktop/car_finder` gibi mutlak yollar kullanılmıştır. Bunları kendi sisteminize göre güncelleyin.

### ffmpeg not found / ffmpeg bulunamadı
```bash
sudo apt install ffmpeg -y
```

---

## Notes / Notlar

- This project is designed for research and prototyping.
- Results depend heavily on dataset quality, annotation consistency, and model tuning.
- For production-grade use, it is recommended to validate on a larger and cleaner dataset.

- Bu proje araştırma ve prototip geliştirme için tasarlanmıştır.
- Sonuçlar veri kalitesine, etiketleme doğruluğuna ve model ayarlarına bağlıdır.
- Daha güvenilir sonuç için daha geniş ve temiz bir veri kümesiyle doğrulama yapılması önerilir.

---

## License / Lisans

This project is intended for educational and experimental use.

Bu proje eğitim ve deneysel kullanım için hazırlanmıştır.

---

## Future Improvements / Gelecek Geliştirmeler

- Add a cleaner dataset directory structure
- Add automatic image filtering and labeling pipeline
- Improve performance for detection in different lighting conditions
- Add CLI arguments for easier customization
- Add badge, screenshots, and release notes

- Daha düzenli veri seti yapısı ekleme
- Otomatik görsel filtreleme ve etiketleme akışı
- Farklı ışık koşullarında tespit performansını iyileştirme
- Daha kolay özelleştirme için CLI argümanları ekleme
- Rozetler, ekran görüntüleri ve sürüm notları ekleme

---

## Contact / İletişim

For questions or improvement suggestions, feel free to open an issue or contact the project maintainer.

Sorular veya geliştirme önerileri için sorun açabilir veya proje sahibiyle iletişime geçebilirsiniz.
