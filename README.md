# Hukuk AI - Gemini Destekli Hukuk Asistanı 🤖⚖️

Bu proje, Google Gemini API'si ile entegre çalışan ve hukuk alanında (boşanma, alacak, ticaret) temel emsal kararlar, ilgili kanun maddeleri ve dilekçe örnekleri sunan bir yapay zeka asistanıdır. Hem web arayüzü (Flask) hem de masaüstü uygulaması (PyQt5) ile kullanılabilir.

---

## 🔧 Özellikler

- 📚 **Boşanma, Alacak ve Ticaret davalarına özel destek**
- 🧠 **Gemini (Google Generative AI) ile doğal dil işleme**
- 🧾 **Kanun ve Yargıtay kararları önerileri**
- 📝 **Hazır dilekçe örnekleri**
- 🌐 **Web API (Flask)**
- 🖥️ **Masaüstü Arayüz (PyQt5)**

---

## 📦 Gereksinimler

### Ortak Gereksinimler

- Python 3.8+
- `.env` dosyasına [Google Gemini API Anahtarınız](https://aistudio.google.com/app/apikey) eklenmelidir:


### Gereken Python Paketleri

```bash
pip install -r requirements.txt

Flask
flask-cors
python-dotenv
google-generativeai
PyQt5


Dosya Yapısı
.
├── flask_app.py         # Web API uygulaması
├── pyqt_app.py          # PyQt5 masaüstü uygulaması
├── .env                 # API anahtarı burada saklanır
├── templates/
│   └── index.html       # Web arayüzü (Flask)
└── README.md            # Bu dosya

!!!!Uyarı
Bu yapay zeka asistanı gerçek bir avukat yerine geçemez. Verilen bilgiler sadece bilgilendirme amaçlıdır ve herhangi bir yasal işlem öncesinde profesyonel hukuki danışmanlık alınmalıdır.

