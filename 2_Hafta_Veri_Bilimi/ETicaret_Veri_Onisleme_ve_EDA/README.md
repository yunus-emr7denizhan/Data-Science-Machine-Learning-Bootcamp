# 🛒 E-Ticaret Veri Ön İşleme ve Keşifsel Veri Analizi (EDA)

Bu proje, e-ticaret satış verileri üzerindeki eksik verilerin doldurulması, kategorik ve metinsel tutarsızlıkların temizlenmesi, aykırı değerlerin (outlier) tespiti ve temel iş analizi sorularının yanıtlanmasını içermektedir.

---

## 🛠️ Kullanılan Teknolojiler & Kütüphaneler
- **Python 3.x**
- **Pandas:** Veri işleme, temizleme ve analiz
- **NumPy:** Sayısal işlemler
- **Matplotlib & Seaborn:** Veri görselleştirme

---

## 📊 Öne Çıkan İşlemler ve Veri Temizliği
1. **Eksik Veri İmpütasyonu:** `sehir` sütunundaki eksik değerler mod ile, sayısal değişkenler ise medyan yöntemiyle tamamlandı.
2. **Metin & Tip Standartlaştırma:** 
   - `kategori` ve `odeme_turu` sütunlarındaki Türkçe karakter hataları (ör. *Kozmetık* ➔ *Kozmetik*, *Banka Karti* ➔ *Banka Kartı*) ve görünmez boşluklar düzeltildi.
   - Benzer ödeme türleri (*Havale*, *EFT* ➔ *Havale/EFT*) tekilleştirildi.
   - `siparis_tarihi` sütunu `datetime` formatına dönüştürüldü.
3. **Mantıksal Hataların Ayıklanması:** Eksi/sıfır fiyatlı ürünler, negatif teslimat günleri ve 5'ten büyük müşteri puanları filtrelendi.
4. **İstatistiksel Aykırı Değer Analizi:** `birim_fiyat` değişkeni için IQR (Çeyrekler Arası Açıklık) yöntemiyle alt ve üst sınırlar belirlenerek aykırı değerler tespit edildi.
5. **Görselleştirme & İş Analizi:**
   - `toplam_tutar` dağılımı Histogram ve Boxplot grafikleriyle incelendi.
   - Ödeme türü dağılımları Countplot ile görselleştirildi.
   - En yüksek ortalama sepet tutarına sahip kategori ve en yüksek müşteri memnuniyeti sağlayan müşteri tipi belirlendi.

---

## 🚀 Çalıştırma
Projeyi kendi ortamınızda çalıştırmak için:

```bash
# Bağımlılıkları yükleyin
pip install -r requirements.txt