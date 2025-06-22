import pandas as pd

# İlk dosyayı oku (model sonuçları)
df_results = pd.read_csv('gsm8k_tr_classified_merged_results.csv')

# İkinci dosyayı oku (mevcut veri)
df_merged = pd.read_csv('gsm8k_tr_classified_merged.csv')

# Seçili kolonları al
selected_columns = ['question', 'answer', 'tr_llama_result', 'is_tr_llama_correct', 'gg_gemma_result', 'is_gg_gemma_correct']
df_selected = df_results[selected_columns]

# İki dosyayı question ve answer kolonlarına göre birleştir
merged_df = pd.merge(df_merged, df_selected[['tr_llama_result', 'is_tr_llama_correct', 'gg_gemma_result', 'is_gg_gemma_correct']], 
                     left_index=True, right_index=True, how='left')

# Sonucu kaydet
merged_df.to_csv('gsm8k_tr_classified_merged.csv', index=False)

print("Birleştirme tamamlandı!")
print(f"Yeni dosya satır sayısı: {len(merged_df)}")
print(f"Yeni kolonlar: {list(merged_df.columns)}")
print(f"Tüm kolonlar: {merged_df.columns}")
print("\nİlk 3 satır:")
print(merged_df.head(3))



