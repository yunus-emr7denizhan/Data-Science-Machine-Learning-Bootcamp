"""
Amaç:
    - Müşteri ayrılma tahmini (Churn Prediction) senaryosu ile uçtan uca temel makine öğrenmesi akışı oluşturma
    - Logistic Regression, KNN ve Decision Tree modellerini eğitme, doğrulama (validation) ve karşılaştırma
    - En iyi modeli seçip test veri seti üzerinde sınıflandırma metrikleriyle (Accuracy, F1, vb.) değerlendirme

Veri seti:
    - Numpy ve Pandas kullanılarak oluşturulmuş sentetik müşteri veri seti (150 örnek)
    - features: yaş, gelir, abonelik_suresi, destek_talebi_sayisi, sehir, uyelik_tipi
    - hedef değişken (churn):
        - 0: kalır
        - 1: ayrılır

Plan:
    1. Gerekli kütüphanelerin yüklenmesi ve sentetik veri setinin oluşturulması
    2. Veri seti incelemesi ve eksik değer kontrolü/temizliği
    3. Öznitelik üretimi (Feature Engineering)
    4. Kategorik değişkenlerin One-Hot Encoding ile dönüştürülmesi
    5. Hedef değişken ve özniteliklerin ayrılması
    6. Eğitim, doğrulama (validation) ve test veri setlerinin oluşturulması
    7. Özelliklerin ölçeklendirilmesi (StandardScaler)
    8. Modellerin (Logistic Regression, KNN, Decision Tree) tanımlanması ve eğitilmesi
    9. Validation sonuçlarına göre modellerin karşılaştırılması
    10. En iyi modelin test seti ile değerlendirilmesi ve sonuç yorumu

Kurulumlar:
pip install pandas numpy scikit-learn
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

# Gerekli kütüphanelerin yüklenmesi ve sentetik veri setinin oluşturulması
np.random.seed(42) # Sonuçların her çalıştırıldığında aynı çıkması için
n = 150

yas = np.random.randint(18, 70, n)
gelir = np.random.randint(30000, 150000, n)
abonelik_suresi = np.random.randint(1, 60, n)
destek_talebi_sayisi = np.random.randint(0, 10, n)
sehir = np.random.choice(["İstanbul", "Ankara", "İzmir"], n)
uyelik_tipi = np.random.choice(["Standart", "Premium"], n)

# Churn (Ayrılma) durumunu mantıksal bir kurala bağlayalım
# Çok destek talebi açan ve aboneliği kısa olanların ayrılma ihtimali daha yüksek olsun
churn_prob = (destek_talebi_sayisi / 10) + (1 - abonelik_suresi / 60)
churn = np.where(churn_prob > 1.0, 1, 0)

df = pd.DataFrame({
    "yas": yas,
    "gelir": gelir,
    "abonelik_suresi": abonelik_suresi,
    "destek_talebi_sayisi": destek_talebi_sayisi,
    "sehir": sehir,
    "uyelik_tipi": uyelik_tipi,
    "churn": churn
})

# Kodun çalışmasını test etmek için bilerek eksik (NaN) veriler ekliyoruz
df.loc[10:15, 'gelir'] = np.nan
df.loc[45:50, 'yas'] = np.nan

# Veri seti incelemesi ve eksik değer kontrolü/temizliği
print("--- Veri Seti İlk 5 Satır ---")
print(df.head())
print(f"\nHedef değişken dağılımı:\n{df['churn'].value_counts()}")

if df.isna().any().any():
    print("\n[BİLGİ] Veri setinde eksik (NaN) değerler tespit edildi. Temizleniyor...")
    df.dropna(inplace=True)
    print("Eksik değerler temizlendi. Yeni boyut:", df.shape)
else:
    print("\nEksik değer bulunmuyor.")

# Öznitelik üretimi (Feature Engineering)
# Gelir düzeyini kategorilere ayırarak yeni bir özellik üretiyoruz
df["gelir_grubu"] = pd.cut(df["gelir"], bins=[0, 50000, 100000, 200000], labels=["Dusuk", "Orta", "Yuksek"])
print("\nYeni öznitelik (gelir_grubu) eklendi:\n", df[["gelir", "gelir_grubu"]].head())

# Kategorik değişkenlerin One-Hot Encoding ile dönüştürülmesi
df = pd.get_dummies(df, columns=["sehir", "uyelik_tipi", "gelir_grubu"], drop_first=True)

# Hedef değişken ve özniteliklerin ayrılması
X = df.drop(["churn"], axis=1).values
y = df["churn"].values

# Eğitim, doğrulama (validation) ve test veri setlerinin oluşturulması
# Önce Train+Val ve Test olarak ayırıyoruz (%80 - %20)
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Sonra Train+Val setini kendi içinde Train ve Validation olarak ayırıyoruz
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp)

# Özelliklerin ölçeklendirilmesi (StandardScaler)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Modellerin (Logistic Regression, KNN, Decision Tree) tanımlanması ve eğitilmesi
log_reg = LogisticRegression(random_state=42)
knn = KNeighborsClassifier(n_neighbors=5)
tree_clf = DecisionTreeClassifier(max_depth=3, random_state=42)

log_reg.fit(X_train_scaled, y_train)
knn.fit(X_train_scaled, y_train)
tree_clf.fit(X_train_scaled, y_train)

# Validation sonuçlarına göre modellerin karşılaştırılması
val_acc_log = accuracy_score(y_val, log_reg.predict(X_val_scaled))
val_acc_knn = accuracy_score(y_val, knn.predict(X_val_scaled))
val_acc_tree = accuracy_score(y_val, tree_clf.predict(X_val_scaled))

print("\n--- Doğrulama (Validation) Seti Başarımları ---")
print(f"Logistic Regression Accuracy: {val_acc_log:.4f}")
print(f"KNN Accuracy                : {val_acc_knn:.4f}")
print(f"Decision Tree Accuracy      : {val_acc_tree:.4f}")

# En iyi modeli seçme
models = {"Logistic Regression": log_reg, "KNN": knn, "Decision Tree": tree_clf}
best_model_name = max({"Logistic Regression": val_acc_log, "KNN": val_acc_knn, "Decision Tree": val_acc_tree}, key=lambda k: {"Logistic Regression": val_acc_log, "KNN": val_acc_knn, "Decision Tree": val_acc_tree}[k])
best_model = models[best_model_name]

print(f"\n[SEÇİLEN EN İYİ MODEL] -> {best_model_name}")

# En iyi modelin test seti ile değerlendirilmesi ve sonuç yorumu
y_pred = best_model.predict(X_test_scaled)

print("\n--- Test Seti Sonuçları ---")
print(f"Accuracy         : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision        : {precision_score(y_test, y_pred):.4f}")
print(f"Recall           : {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score         : {f1_score(y_test, y_pred):.4f}")
print(f"Confusion Matrix :\n{confusion_matrix(y_test, y_pred)}")

print("\n--- Yorum Çıktısı ---")
print(f"Validation setinde en yüksek başarım oranını veren {best_model_name} modeli, final testi için seçilmiştir.")
print("Sentetik verimizde churn olma ihtimalini destek_talebi ve abonelik_suresi üzerinden şekillendirdiğimiz için")
print("modellerimiz (özellikle doğrusal ayrımlar yapabilen modeller) mantıklı ve yüksek bir test performansı sergilemiştir.")