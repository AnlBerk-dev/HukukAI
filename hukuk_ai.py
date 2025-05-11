import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QLabel, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt
import google.generativeai as genai

class LegalAssistant:
    # Boşanma, Alacak ve Ticaret davalarına yönelik emsal kararlar ve kanunlar
    def get_case_laws(self, dava_turu):
        # 1. Boşanma davasına yönelik emsal kararlar ve kanunlar
        if dava_turu == "boşanma":
            yargi_kararlari = [
                "Yargıtay 2. Hukuk Dairesi, E. 2017/25825, K. 2018/10362: Şiddetli geçimsizlik nedeniyle boşanma kararı verilmiştir.",
                "Yargıtay 2. Hukuk Dairesi, E. 2018/27911, K. 2019/3416: Evlilik birliğinin temelinden sarsılması nedeniyle boşanma kararı verilmiştir."
            ]
            kanunlar = [
                "Türk Medeni Kanunu, Madde 166: Boşanma sebepleri (Şiddetli geçimsizlik, zina, hayata kast, vb.)",
                "Türk Medeni Kanunu, Madde 171: Boşanma davası açılabilmesi için hukuki nedenlerin varlığı gereklidir."
            ]
            return {"yargi_kararlari": yargi_kararlari, "kanunlar": kanunlar}
        
        # 2. Alacak davasına yönelik emsal kararlar ve kanunlar
        elif dava_turu == "alacak":
            yargi_kararlari = [
                "Yargıtay 13. Hukuk Dairesi, E. 2019/7555, K. 2020/11527: Alacak davasında sözleşmeye dayalı ödeme yükümlülüğü kabul edilmiştir."
            ]
            kanunlar = [
                "Borçlar Kanunu, Madde 83: Alacaklı ile borçlu arasındaki sözleşme ilişkisi.",
                "Borçlar Kanunu, Madde 98: Alacakların tahsili ve ödeme süreleri."
            ]
            return {"yargi_kararlari": yargi_kararlari, "kanunlar": kanunlar}
        
        # 3. Ticaret davasına yönelik emsal kararlar ve kanunlar
        elif dava_turu == "ticaret":
            yargi_kararlari = [
                "Yargıtay 11. Hukuk Dairesi, E. 2020/16823, K. 2021/22132: Ticaret hukuku çerçevesinde haksız rekabet davası verilmiştir."
            ]
            kanunlar = [
                "Türk Ticaret Kanunu, Madde 56: Ticari işletme sahiplerinin yükümlülükleri.",
                "Türk Ticaret Kanunu, Madde 58: Haksız rekabetin tanımı ve cezai yaptırımlar."
            ]
            return {"yargi_kararlari": yargi_kararlari, "kanunlar": kanunlar}
        
        else:
            return "Bu dava türü için emsal kararlar veya kanunlar bulunmamaktadır."

    # Her dava türü için dilekçe örneği hazırlama
    def prepare_petition(self, dava_turu):
        # 1. Boşanma davası için dilekçe örneği
        if dava_turu == "boşanma":
            return """\
**Boşanma Dilekçesi Örneği:**

[Mahkemenin Adı]

DAVACI: [Adınız Soyadınız, T.C. Kimlik Numaranız, Adresiniz, Telefon Numaranız]  
DAVALI: [Eşinizin Adı Soyadı, T.C. Kimlik No, Adresi]

KONU: Boşanma Davası

AÇIKLAMALAR:
1. [Evlilik tarihi] tarihinde evlendik.  
2. Evliliğimizde sürekli geçimsizlik yaşanmakta olup, eşim [Eşinizin kusurlu davranışları].

HUKUKİ SEBEPLER:
Türk Medeni Kanunu, Madde 166: Şiddetli geçimsizlik nedeniyle boşanma.

DELİLLER:
1. Tanık beyanları  
2. Diğer deliller

TALEPLER:
1. Tarafların boşanmasına,  
2. Velayetin davacıya verilmesine,  
3. Nafaka talebinin kabulüne

[Tarih]  
[Adınız Soyadınız]  
[İmza]
"""
        # 2. Alacak davası için dilekçe örneği
        elif dava_turu == "alacak":
            return """\
**Alacak Davası Dilekçesi Örneği:**

[Mahkemenin Adı]

DAVACI: [Adınız Soyadınız, T.C. Kimlik Numaranız, Adresiniz, Telefon Numaranız]  
DAVALI: [Adı Soyadı, T.C. Kimlik No, Adresi]

KONU: Alacak Davası

AÇIKLAMALAR:
1. 2021 tarihli sözleşme uyarınca 10.000 TL alacağım bulunmaktadır.  
2. Ödeme yapılmamış ve borç halen ödenmemiştir.

HUKUKİ SEBEPLER:
Borçlar Kanunu, Madde 83 ve 98.

DELİLLER:
1. Sözleşme örneği  
2. Tanık beyanları

TALEPLER:
1. Alacağın tahsiline  
2. Yasal faizine

[Tarih]  
[Adınız Soyadınız]  
[İmza]
"""
        # 3. Ticaret davası için dilekçe örneği
        elif dava_turu == "ticaret":
            return """\
**Ticaret Davası Dilekçesi Örneği:**

[Mahkemenin Adı]

DAVACI: [Adınız Soyadınız, T.C. Kimlik Numaranız, Adresiniz, Telefon Numaranız]  
DAVALI: [Ticaret Unvanı, Adresi]

KONU: Haksız Rekabet Davası

AÇIKLAMALAR:
1. [Ticaretin yapıldığı tarih] tarihinde, davalı firma haksız rekabete dayalı olarak piyasa davranışlarını bozan bir faaliyet yürütmüştür.
2. Davalı firma, [açıklama: hangi ürün, hizmet, davranışlar haksız rekabeti oluşturmuş?]

HUKUKİ SEBEPLER:
Türk Ticaret Kanunu, Madde 56 ve 58.

DELİLLER:
1. Tanık beyanları  
2. Diğer ticaret belgeleri

TALEPLER:
1. Haksız rekabetin durdurulmasına,  
2. Zararın tazminine

[Tarih]  
[Adınız Soyadınız]  
[İmza]
"""
        else:
            return "Belirttiğiniz dava türüne uygun dilekçe örneği bulunmamaktadır."

    # Kullanıcıdan gelen soruya göre dava türüne göre işlem yapma
    def handle_query(self, query):
        if "boşanma" in query.lower():
            petition = self.prepare_petition("boşanma")
            case_laws = self.get_case_laws("boşanma")
            return self.format_output(petition, case_laws)
        
        elif "alacak" in query.lower():
            petition = self.prepare_petition("alacak")
            case_laws = self.get_case_laws("alacak")
            return self.format_output(petition, case_laws)
        
        elif "ticaret" in query.lower():
            petition = self.prepare_petition("ticaret")
            case_laws = self.get_case_laws("ticaret")
            return self.format_output(petition, case_laws)
        
        else:
            return "Lütfen geçerli bir dava türü girin (Boşanma, Alacak, Ticaret vb.)."
    
    # Çıktıyı uygun formatta sunma
    def format_output(self, petition, case_laws):
        if isinstance(case_laws, dict):
            case_laws_output = "\n".join([f"{kanun}: {text}" for kanun, text in zip(case_laws['kanunlar'], case_laws['yargi_kararlari'])])
        else:
            case_laws_output = case_laws

        return f"{petition}\n\n**Kanunlar ve Kararlar:**\n{case_laws_output}"

class ChatBotApp(QWidget):
    def __init__(self):  
        super().__init__()
        self.setWindowTitle("Hukuk AI - Gemini Destekli")
        self.setMinimumSize(600, 500)
        self.setStyleSheet("""
            QWidget { font-family: Arial; background-color: #F4F4F4; }
            QTextEdit, QLineEdit { background-color: #FFFFFF; border: 1px solid #D3D3D3; padding: 10px; font-size: 14px; }
            QPushButton { background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px; }
            QPushButton:hover { background-color: #45a049; }
            QLabel#status_label { color: #4CAF50; font-weight: bold; }
        """)
        
        load_dotenv()
        self.api_key = os.getenv("Gemini_Api_Key")
        if not self.api_key:
            raise ValueError("Gemini_Api_Key .env dosyasında bulunamadı.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.legal = LegalAssistant()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Mesajınızı yazın ve Enter'a basın")
        self.user_input.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("Gönder")
        self.send_button.clicked.connect(self.send_message)

        self.status_label = QLabel("Hukuk AI — Gemini destekli hukuk asistanınız.")
        self.status_label.setObjectName("status_label")
        self.status_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.chat_display)
        layout.addWidget(self.user_input)
        layout.addWidget(self.send_button)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def send_message(self):
        user_message = self.user_input.text().strip()
        if not user_message:
            return

        self.chat_display.append(f"Kullanıcı: {user_message}")
        self.user_input.clear()

        try:
            if any(k in user_message.lower() for k in ["boşanma", "alacak", "ticaret"]):
                response = self.legal.handle_query(user_message)
            else:
                response = "Geçerli bir dava türü giriniz. Örnek: 'Boşanma' veya 'Alacak'."
        except Exception as e:
            response = f"Hata oluştu: {str(e)}"

        self.chat_display.append(f"Hukuk AI: {response}")
        self.chat_display.verticalScrollBar().setValue(self.chat_display.verticalScrollBar().maximum())
        self.status_label.setText("Mesaj gönderildi.")

if __name__ == "__main__":
    app = QApplication([])
    window = ChatBotApp()
    window.show()
    app.exec_()
