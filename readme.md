# Proje

## Kullanılan veri seti

- <https://huggingface.co/datasets/ytu-ce-cosmos/gsm8k_tr> veri seti kullanıldı.
- Bu veri setinde
  - İki kolon var: "question" ve "answer"
  - 8792 kayıt yer alıyor

## Modellerin çözümleri

- İlk aşağıdaki modellere veri setindeki sorular verilerek cevapları alımıştır.
  - <https://huggingface.co/ytu-ce-cosmos/Turkish-Llama-8b-DPO-v0.1>
  - <https://huggingface.co/google/gemma-2-9b-it>
- Burada kullanılan prompt:
  
  ```python
    prompt = (
    f"Soru: {question}\n"
    "Soruya tek bir yanıt ver, adım adım çözme, sadece sonuç olsun.",
    "Yanıtlarında ‘24 \times \frac’ gibi notasyonlar kullanma.",
    "Bunu da ‘Sonuç: <değer>’ formatında göster."
  )
  ```

- Mevcuttaki cevaplarda cevaplar hep en son sayı
- Bu iki modelde de benzer şekilde olması sağlandı.
- Mevcuttaki cevap ile gelen cevap karşılaştırılarak, modelin bu soruları doğru cevaplayıp cevaplamadığı işaretlendi.
- Buna göre sonuçlar şu şekilde:
    Llama Doğru Sayısı: 1001
    Gemma Doğru Sayısı: 1558
    Llama Yanlış Sayısı: 7791
    Gemma Yanlış Sayısı: 7234

## Soru tipi ve cevap yöntemi tespitleri

- gpt-4o kullanıldı.
- Aşağıdaki prompt ile soru tiplerini tespiti yapıldı:

  ```python
    prompt = f"""
        Aşağıdaki matematik sorusunun hangi türde olduğunu belirle.
        
        Soru: {question}
        
        Türü belirle ve kısa bir açıklama yaz. 
        Format: {{"type": "tür", "explanation": "açıklama"}}
        """
  ```

- Aşağıdaki prompt ile de cevap yöntemleri yapıldı:

  ```python
    prompt = f"""
        Aşağıdaki matematik sorusunun cevabının hangi yöntemle elde edildiğini belirle.
        
        Cevap: {answer}
        
        Cevabın hangi yöntemle elde edildiğini belirle ve kısa bir açıklama yaz. 
        Format: {{"method": "yöntem", "explanation": "açıklama"}}
        """
  ```

- Burada en çok gelen soru tipleri şu şekilde:
aritmetik problem	1606
word problem	1075
problem solving	638
problem çözme	480
Aritmetik Problemi	312
Aritmetik Problem	290
problem-solving	222
algebra	201
Algebra	133
aritmetik problemleri	127

- Burada en çok gelen cevap yöntemleri şu şekilde:
aritmetik hesaplama	843
adım adım hesaplama	547
doğrudan hesaplama	506
hesaplama	181
aritmetik işlemler	129
bölme	106
doğrudan bilgi	98
Aritmetik Hesaplama	95
aritmetik	82
direct calculation	81

- Artık elimizde bu veri için 4 metin verisi var: question, answer, question_type, solution_method
- Bu 4 metnin <https://huggingface.co/ytu-ce-cosmos/turkish-e5-large> ile embeddingleri oluşturuldu.

## Lojstik Regresyon

- Elimizde 4 metne ait embedding'ler var.
- İki modele ait de çözdü/çözemedi şeklinde sınıflandırma verisi var.
- Buna göre soru/cevap/soru tipi/çözüm metodu embedding'leri ayrı ayrı kullanılarak yapılacak lojistik regresyon sınıflandırması sonrası TR-Llama'nın ve Gemma'nın sonuçlarının tahmin edilip edilemediğinin karşılaştırılması
- Lojistik regresyon için veri set'leri %50 eğitim, %50 test olarak kullanılıyor.
