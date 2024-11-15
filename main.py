# main.py
import openai
from config import OPENAI_API_KEY

def read_article(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
def process_with_openai(article_text):
    openai.api_key = OPENAI_API_KEY
    prompt = (
        "Przekształć poniższy artykuł do formatu HTML zgodnie z następującymi wytycznymi:\n"
        "1. Użyj odpowiednich tagów HTML do strukturyzacji treści.\n"
        "2. Określ miejsca na grafiki za pomocą tagu <img> z atrybutem src='image_placeholder.jpg'.\n"
        "   Dodaj atrybut alt z dokładnym promptem do generowania grafiki.\n"
        "   Umieść podpisy pod grafikami używając odpowiedniego tagu HTML.\n"
        "3. Nie używaj CSS ani JavaScript.\n"
        "4. Zwrócony kod powinien zawierać wyłącznie zawartość pomiędzy <body> a </body>.\n"
        "Nie dołączaj znaczników <html>, <head> ani <body>.\n\n"
        "Artykuł:\n"
        f"{article_text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś asystentem pomagającym w konwersji tekstu do HTML."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.7,
    )

    return response.choices[0].message['content']    
