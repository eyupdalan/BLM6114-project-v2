import pandas as pd
import os
def merge_question_types_and_answer_methods():
    """
    Merge question types and answer methods data from two CSV files.
    """
    # Read both CSV files
    print("Soru tipleri dosyası okunuyor...")
    try:
        question_types_df = pd.read_csv('gsm8k_tr_question_types_merged.csv')
        print(f"✅ {len(question_types_df)} satır okundu")
    except Exception as e:
        print(f"❌ Hata: Soru tipleri dosyası okunamadı: {e}")
        return

    print("\nCevap yöntemleri dosyası okunuyor...")
    try:
        answer_methods_df = pd.read_csv('gsm8k_tr_answer_methods_merged.csv')
        print(f"✅ {len(answer_methods_df)} satır okundu")
    except Exception as e:
        print(f"❌ Hata: Cevap yöntemleri dosyası okunamadı: {e}")
        return

    # Merge dataframes
    print("\nDosyalar birleştiriliyor...")
    merged_df = pd.merge(question_types_df, answer_methods_df, on=['question', 'answer'], how='inner')

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
    merge_question_types_and_answer_methods()
