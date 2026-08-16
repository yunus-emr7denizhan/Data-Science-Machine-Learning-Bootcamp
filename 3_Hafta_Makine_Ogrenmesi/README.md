# Müşteri Ayrılma (Churn) Tahmini - Makine Öğrenmesi Akışı

**Projenin Amacı:**
Bu proje, makine öğrenmesi akışını uçtan uca pratik etmek amacıyla küçük ve anlaşılır bir sınıflandırma problemi üzerinde uygulanmıştır. Çalışmanın temel hedefi; veri oluşturma, temel veri ön işleme, öznitelik üretme, veriyi eğitim-doğrulama-test (train-validation-test) olarak bölme, model eğitimi gerçekleştirme ve sınıflandırma metrikleriyle değerlendirme adımlarını tek bir Python dosyasında başarıyla tamamlamaktır.

### Veri Seti Hakkında
Projede, dışarıdan hazır bir veri kullanmak yerine, Python (NumPy ve Pandas) kullanılarak 150 satırlık basit ve sentetik bir müşteri veri seti oluşturulmuştur. 
*   **Öznitelikler (Features):** Müşterilere ait yaş, gelir, abonelik_suresi, destek_talebi_sayisi, şehir ve üyelik_tipi bilgilerini içermektedir.
*   **Hedef Değişken (Target):** `churn` (0 = müşteri kalır, 1 = müşteri ayrılır) olarak belirlenmiştir.

### Uygulanan Süreç ve İş Akışı
Proje kapsamında aşağıdaki makine öğrenmesi adımları sırasıyla uygulanmıştır:
1.  **Veri Ön İşleme:** Sentetik veriye kasıtlı olarak eklenen eksik değerler (NaN) tespit edilip temizlenmiş, kategorik değişkenler (şehir, üyelik_tipi) One-Hot Encoding yöntemiyle sayısal forma dönüştürülmüştür.
2.  **Öznitelik Üretimi (Feature Engineering):** Gelir verilerinden faydalanılarak müşteriler için "gelir_grubu" adında yeni ve basit bir öznitelik üretilmiştir.
3.  **Veri Bölme & Ölçeklendirme:** Sınıflandırma problemi olduğu için veri seti `stratify` parametresi kullanılarak train, validation ve test kümelerine ayrılmış; ardından sayısal değişkenlere standartlaştırma (StandardScaler) uygulanmıştır.
4.  **Model Eğitimi:** Önerilen Logistic Regression ve KNN modellerine ek olarak, bonus olarak Decision Tree (Karar Ağacı) modeli de eğitilmiştir.


**Nasıl Çalıştırılır:**
1. Gerekli kütüphaneleri yükleyin: `pip install -r requirements.txt`
2. Python dosyasını çalıştırın: `python churn_prediction.py`