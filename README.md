# Filtrowanie CSV - Usuwanie Duplikatów

Ten projekt to prosty skrypt w Pythonie, który przetwarza plik CSV zawierający tłumaczenia. Skrypt identyfikuje duplikaty w danych, zapisuje znalezione duplikaty do osobnego pliku `duplikaty.csv`, a następnie tworzy nowy plik `Translation.csv` z unikalnymi wierszami.

## Funkcjonalności

- **Wczytywanie danych:** Skrypt wczytuje dane z pliku CSV przy użyciu modułu `csv` oraz `DictReader`.
- **Wykrywanie duplikatów:** Sprawdza, czy istnieją wiersze z identycznymi polami `source_text` oraz `translated_text`.
- **Zapis duplikatów:** Duplikaty są zapisywane do pliku `duplikaty.csv` w czytelnym formacie.
- **Usuwanie duplikatów:** Tworzony jest nowy plik `Translation.csv` zawierający tylko unikalne wpisy.

## Wymagania

- Python 3.x
- Standardowa biblioteka Pythona (moduły: `csv`, `collections`)

## Instalacja

1. Upewnij się, że masz zainstalowanego Pythona 3.
2. Skopiuj pliki projektu do wybranego katalogu.

## Uruchomienie

1. Przygotuj plik CSV o nazwie `Translation.csv` z przynajmniej dwoma kolumnami: `source_text` oraz `translated_text`.
2. Uruchom skrypt w terminalu lub wierszu poleceń:
   ```bash
   python <nazwa_pliku>.py
