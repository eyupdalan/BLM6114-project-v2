import pandas as pd
import os

def merge_csv_files():
    """
    Merge 4 CSV files containing question types data into a single CSV file.
    """
    # List of CSV files to merge
    csv_files = [
        'gsm8k_tr_answer_methods_first.csv',
        'gsm8k_tr_answer_methods_second.csv', 
        'gsm8k_tr_answer_methods_third.csv',
        'gsm8k_tr_answer_methods_fourth.csv'
    ]
    
    # Read and merge all CSV files
    dataframes = []
    total_rows = 0
    
    for i, file in enumerate(csv_files, 1):
        print(f"Dosya {i}/4 okunuyor: {file}")
        try:
            df = pd.read_csv(file)
            dataframes.append(df)
            total_rows += len(df)
            print(f"  - {len(df)} satır okundu")
        except Exception as e:
            print(f"  - Hata: {file} dosyası okunamadı: {e}")
            return
    
    # Concatenate all dataframes
    print("\nDosyalar birleştiriliyor...")
    merged_df = pd.concat(dataframes, ignore_index=True)
    
    # Save merged data to a new CSV file
    output_file = 'gsm8k_tr_answer_methods_merged.csv'
    merged_df.to_csv(output_file, index=False)
    
    print(f"\n✅ Birleştirme tamamlandı!")
    print(f"📊 Toplam satır sayısı: {len(merged_df)}")
    print(f"💾 Birleştirilmiş dosya: {output_file}")
    
    # Display some statistics
    print(f"\n📈 İstatistikler:")
    print(f"  - İlk dosya: {len(dataframes[0])} satır")
    print(f"  - İkinci dosya: {len(dataframes[1])} satır") 
    print(f"  - Üçüncü dosya: {len(dataframes[2])} satır")
    print(f"  - Dördüncü dosya: {len(dataframes[3])} satır")
    print(f"  - Toplam: {total_rows} satır")
    
    # Check for any duplicates
    duplicates = merged_df.duplicated().sum()
    if duplicates > 0:
        print(f"⚠️  {duplicates} adet tekrarlanan satır bulundu")
    else:
        print("✅ Tekrarlanan satır bulunmadı")
    
    # Display column information
    print(f"\n📋 Sütun bilgileri:")
    for col in merged_df.columns:
        print(f"  - {col}: {merged_df[col].dtype}")

if __name__ == "__main__":
    merge_csv_files()
