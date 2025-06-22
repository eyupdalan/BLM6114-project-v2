import pandas as pd

def merge_with_old_results():
    """
    Merge old question types and answer methods with new ones.
    """
    # Read both CSV files
    print("Eski sınıflandırma dosyası okunuyor...")
    try:
        old_df = pd.read_csv('gsm8k_tr_classified.csv')
        print(f"✅ {len(old_df)} satır okundu")
    except Exception as e:
        print(f"❌ Hata: Eski sınıflandırma dosyası okunamadı: {e}")
        return

    print("\nYeni sınıflandırma dosyası okunuyor...")
    try:
        new_df = pd.read_csv('gsm8k_tr_classified_merged.csv')
        print(f"✅ {len(new_df)} satır okundu")
    except Exception as e:
        print(f"❌ Hata: Yeni sınıflandırma dosyası okunamadı: {e}")
        return

    # Add old values as new columns
    print("\nEski değerler yeni sütunlar olarak ekleniyor...")
    merged_df = pd.merge(new_df, old_df[['question', 'question_type', 'solution_method']], 
                        on='question', how='left',
                        suffixes=('', '_old'))

    # Save merged data
    output_file = 'gsm8k_tr_classified_merged.csv'
    merged_df.to_csv(output_file, index=False)

    print(f"\n✅ Birleştirme tamamlandı!")
    print(f"📊 Toplam satır sayısı: {len(merged_df)}")
    print(f"💾 Birleştirilmiş dosya: {output_file}")

    # Display column information
    print(f"\n📋 Sütun bilgileri:")
    for col in merged_df.columns:
        print(f"  - {col}: {merged_df[col].dtype}")

if __name__ == "__main__":
    merge_with_old_results()
