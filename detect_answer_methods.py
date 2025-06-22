import os
import openai
from dotenv import load_dotenv
import pandas as pd
from tqdm import tqdm
import argparse

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv('OPEN_AI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.") 

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def detect_answer_methods(answer):
    prompt = f"""
    Aşağıdaki matematik sorusunun cevabının hangi yöntemle elde edildiğini belirle.
    
    Cevap: {answer}
    
    Cevabın hangi yöntemle elde edildiğini belirle ve kısa bir açıklama yaz. 
    Format: {{"method": "yöntem", "explanation": "açıklama"}}
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": answer}
        ]
    )
    return response.choices[0].message.content

df = pd.read_csv('gsm8k_tr.csv')
print(df.head())
print(df.columns)
print(df.shape)

# Enable tqdm for pandas
tqdm.pandas(desc="Cevap yöntemleri tespit ediliyor")

first_quarter = df.head(int(df.shape[0] * 0.25))
second_quarter = df.iloc[int(df.shape[0] * 0.25):int(df.shape[0] * 0.5)]
third_quarter = df.iloc[int(df.shape[0] * 0.5):int(df.shape[0] * 0.75)]
fourth_quarter = df.iloc[int(df.shape[0] * 0.75):]

def process_chunk(df, quarter):
    """Belirtilen quarter'ı işler"""
    total_rows = len(df)
    chunk_size = total_rows // 4
    
    if quarter == "first":
        chunk = df.head(chunk_size)
    elif quarter == "second":
        chunk = df.iloc[chunk_size:chunk_size*2]
    elif quarter == "third":
        chunk = df.iloc[chunk_size*2:chunk_size*3]
    elif quarter == "fourth":
        chunk = df.iloc[chunk_size*3:]
    else:
        raise ValueError("Quarter 'first', 'second', 'third' veya 'fourth' olmalıdır")
    
    print(f"{quarter.upper()} quarter işleniyor... ({len(chunk)} soru)")
    
    # Enable tqdm for pandas
    tqdm.pandas(desc=f"{quarter.upper()} quarter")
    
    chunk["answer_method"] = chunk["answer"].progress_apply(detect_answer_methods)
    
    # Sadece işlenen chunk'ı kaydet
    output_filename = f'gsm8k_tr_answer_methods_{quarter}.csv'
    chunk.to_csv(output_filename, index=False)
    print(f"{output_filename} dosyasına kaydedildi.")

if __name__ == "__main__":
    # Command line argument parser
    parser = argparse.ArgumentParser(description='Matematik sorularının cevap yöntemlerini tespit et')
    parser.add_argument('quarter', choices=['first', 'second', 'third', 'fourth'], 
                       help='İşlenecek quarter (first, second, third, fourth)')
    
    args = parser.parse_args()
    
    # CSV dosyasını oku
    df = pd.read_csv('gsm8k_tr.csv')
    print(f"Toplam {len(df)} soru bulundu.")
    print(f"İşlenecek quarter: {args.quarter}")
    
    # Belirtilen quarter'ı işle
    process_chunk(df, args.quarter)