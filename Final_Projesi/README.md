# 🏦 Kredi Riski Sınıflandırması (Credit Risk Classification)

Bu proje, **Huawei Student Developers (HSD) & Türkiye Yapay Zeka Akademisi (TRAI) Veri Bilimi ve Makine Öğrenmesi Bootcamp** bitirme projesi olarak geliştirilmiştir.

## 🎯 Projenin Amacı
Bankacılık sektöründe kredi temerrütlerini (kredi riskini) Karar Ağaçları ve Random Forest algoritmalarıyla önceden tahmin etmek ve risk yönetimine veri odaklı stratejik içgörüler sunmaktır.

---

## 📊 Veri Seti ve Ön İşleme
* **customer_data.csv:** Müşterilere ait maskelenmiş demografik veriler.
* **payment_data.csv:** Müşterilerin geçmiş ödeme ve gecikme (OVD) kayıtları.
* Müşteri ID'si bazında ödeme geçmişleri gruplanmış (**Aggregation**), demografik tablo ile birleştirilmiş (**Merge**) ve eksik değerler medyan yöntemiyle doldurulmuştur.
* Veri seti `%80 Eğitim` ve `%20 Test` olarak `stratify=y` ile ayrılmış, sayısal özellikler `StandardScaler` ile ölçeklendirilmiştir.

---

## ⚙️ Model Performansları

| Model | Accuracy (Doğruluk) | AUC Skoru |
| :--- | :---: | :---: |
| **Decision Tree** | %77.78 | - |
| **Random Forest** | **%79.56** | **0.67** |

---

## 🚀 Kurulum ve Çalıştırma

Bağımlılıkları yüklemek için:
```bash
pip install -r requirements.txt


## 📝 Medium Makalesi
Projenin detaylı iş zekası analizi, aykırı değer yaklaşımı ve görselleştirmelerine Medium üzerinden ulaşabilirsiniz:

## 🔗 **Medium:** [Kime Kredi Verme(me)liyiz? Karar Ağaçları ve Random Forest ile Bankacılıkta Kredi Riski Analizi](https://medium.com/@yunusemredenizhan07/kime-kredi-verme-me-liyiz-01a8e65f7220)