import pandas as pd

# İlk dosyayı kontrol et
print("gsm8k_tr_classified_merged_results.csv dosyası:")
df1 = pd.read_csv('gsm8k_tr_classified_merged_results.csv')
print(f"Satır sayısı: {len(df1)}")
print(f"Kolonlar: {list(df1.columns)}")
print("\nİlk 3 satır:")
print(df1[['question', 'answer'] + ['tr_llama_result', 'is_tr_llama_correct', 'gg_gemma_result', 'is_gg_gemma_correct']].head(3))

print("\n" + "="*50 + "\n")

# İkinci dosyayı kontrol et
print("gsm8k_tr_classified_merged.csv dosyası:")
df2 = pd.read_csv('gsm8k_tr_classified_merged.csv')
print(f"Satır sayısı: {len(df2)}")
print(f"Kolonlar: {list(df2.columns)}")
print("\nİlk 3 satır:")
print(df2[['question', 'answer']].head(3)) 