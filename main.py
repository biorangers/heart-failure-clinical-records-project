from pathlib import Path
from ucimlrepo import fetch_ucirepo
import pandas as pd

def fetch_and_save_data():
    # Veri setini çek
    heart_failure_clinical_records = fetch_ucirepo(id=519)

    # Özellikleri ve hedef değişkenini al
    X = heart_failure_clinical_records.data.features  # Özellikler
    y = heart_failure_clinical_records.data.targets   # Hedef değişken

    # Özellikleri pandas DataFrame olarak al
    data = pd.DataFrame(X)

    # Hedef değişkenini ekle
    data['death_state'] = y

    # Projenin ana dizinini belirleyin
    project_root = Path(__file__).parent.parent  # Ana dizine ulaşmak için iki kat yukarı çıkıyoruz

    # 'data' klasörünün tam yolunu oluştur
    data_path = project_root / 'data' / 'heart_failure_clinical_records_dataset.csv'

    # Veriyi kaydet
    data.to_csv(data_path, index=False)
    print(f"Veri başarıyla kaydedildi! Dosya yolu: {data_path}")

if __name__ == "__main__":
    fetch_and_save_data()
