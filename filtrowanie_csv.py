import csv
from collections import defaultdict

def wczytaj_csv(plik_csv):
    with open(plik_csv, 'r', encoding='utf-8') as plik:
        csv_reader = csv.DictReader(plik)
        return list(csv_reader)

def znajdz_duplikaty(rows):
    duplikaty = defaultdict(list)
    unikalne_wiersze = []

    for line in rows:
        source_text = line['source_text']
        translated_text = line['translated_text']
        duplikaty[source_text].append(translated_text)

    return duplikaty

def zapisz_duplikaty(duplikaty):
    with open('duplikaty.csv', 'w', encoding='utf-8') as plik:
        plik.write("Znalezione duplikaty:\n")
        for source_text, translations in duplikaty.items():
            if len(translations) > 1:
                plik.write(f"Wyraz: {source_text}, Tłumaczenia: {translations}\n")

def usun_duplikaty(rows, duplikaty):
    unikalne_wiersze = []

    for source_text, translations in duplikaty.items():
        if len(translations) == 1:
            unikalne_wiersze.extend([{'source_text': source_text, 'translated_text': t} for t in translations])

    with open('Translation.csv', 'w', newline='', encoding='utf-8') as plik:
        fieldnames = ['source_text', 'translated_text']
        csv_writer = csv.DictWriter(plik, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(unikalne_wiersze)

def przetworz_csv(plik_csv):
    rows = wczytaj_csv(plik_csv)
    duplikaty = znajdz_duplikaty(rows)
    zapisz_duplikaty(duplikaty)
    usun_duplikaty(rows, duplikaty)
    print("Duplikaty zostały usunięte z pliku 'Translation.csv' i zapisane w pliku 'duplikaty.csv'.")

if __name__ == "__main__":
    przetworz_csv('Translation.csv')
