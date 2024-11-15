# OpenAI Article Processor

## Opis aplikacji

OpenAI Article Processor to narzędzie stworzone w Pythonie, które umożliwia automatyczne przekształcanie artykułów w formacie tekstowym do formatu HTML przy użyciu API OpenAI. Aplikacja generuje zarówno surowy kod HTML artykułu, jak i kompletny podgląd artykułu w przygotowanym szablonie HTML, co pozwala na łatwą wizualizację i dalsze wykorzystanie treści.

## Funkcje

- **Konwersja tekstu do HTML:** Automatyczne przekształcanie artykułów z pliku tekstowego (`artykul.txt`) do formatu HTML.
- **Generowanie podglądu:** Tworzenie pełnego podglądu artykułu w pliku `podglad.html` z zastosowanym szablonem `szablon.html`.
- **Obsługa obrazków:** Wstawianie placeholderów dla obrazków z atrybutami `src` i `alt`, co ułatwia późniejsze dodawanie grafik.
- **Automatyczne otwieranie plików:** Po wygenerowaniu, pliki HTML są automatycznie otwierane w domyślnej przeglądarce użytkownika.
- **Styling przy użyciu Bootstrap:** Użycie biblioteki Bootstrap CSS do responsywnego i estetycznego wyglądu podglądu artykułu.
- **Bezpieczeństwo klucza API:** Klucz API jest przechowywany w pliku `config.py`, który jest wyłączony z repozytorium dzięki wpisowi w `.gitignore`.

## Użytkowanie

### 1. Przygotowanie artykułu

Upewnij się, że plik `artykul.txt` zawiera treść artykułu, który chcesz przekształcić do formatu HTML. Możesz edytować ten plik za pomocą dowolnego edytora tekstu.

### 2. Konfiguracja klucza API

Przed uruchomieniem aplikacji, skonfiguruj swój klucz API OpenAI:

1. Otwórz plik `config.py` w głównym katalogu projektu.
2. Wprowadź swój klucz API w zmiennej `OPENAI_API_KEY`:

   ```python
   # config.py
   OPENAI_API_KEY = 'TWÓJ_KLUCZ_API'
   ```

### 3. Uruchomienie aplikacji

Aby przetworzyć artykuł i wygenerować pliki HTML, uruchom główny skrypt aplikacji:

```
python main.py
```

Po wykonaniu tego polecenia, aplikacja:

Odczyta treść z pliku `artykul.txt`.
Przetworzy tekst za pomocą API OpenAI, generując kod HTML artykułu.
Zapisze wygenerowany kod HTML w pliku `artykul.html`.
Stworzy pełny podgląd artykułu w pliku `podglad.html` na podstawie szablonu `szablon.html`.
Automatycznie otworzy oba pliki HTML w domyślnej przeglądarce.

### 4. Przeglądanie wyników

`artykul.html`: Zawiera tylko treść artykułu w formacie HTML, bez zewnętrznych tagów takich jak <!DOCTYPE html>, <html>, <head>, czy <body>. Jest to surowy kod HTML, który możesz wykorzystać według własnych potrzeb.

`podglad.html`: Zawiera pełny dokument HTML z wstawionym artykułem, sformatowany zgodnie z szablonem `szablon.html`. Otwórz ten plik w przeglądarce, aby zobaczyć sformatowany artykuł z zastosowanymi stylami i placeholderami dla obrazków.
