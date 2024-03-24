import csv
from collections import defaultdict

def wczytaj_csv(Translation_csv):
    with open(Translation_csv, 'r', encoding='utf-8') as plik_csv:
        csv_reader = csv.DictReader(plik_csv)
        rows = list(csv_reader)
    return rows

def znajdz_duplikaty_i_usun(rows):
    duplikaty = defaultdict(list)
    unikalne_wiersze = []

    for line in rows:
        source_text = line['source_text']
        translated_text = line['translated_text']
        duplikaty[source_text].append(translated_text)

    with open('duplikaty.txt', 'w', encoding='utf-8') as duplikaty_file:
        duplikaty_file.write("Znalezione duplikaty:\n")
        for source_text, translations in duplikaty.items():
            if len(translations) > 1:
                duplikaty_file.write(f"Wyraz: {source_text}, Tłumaczenia: {translations}\n")
            else:
                unikalne_wiersze.extend([{'source_text': source_text, 'translated_text': t} for t in translations])

    with open('Translation.csv', 'w', newline='', encoding='utf-8') as translation_file:
        fieldnames = ['source_text', 'translated_text']
        csv_writer = csv.DictWriter(translation_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(unikalne_wiersze)

if __name__ == "__main__":
    rows = wczytaj_csv(Translation_csv='Translation.csv')
    znajdz_duplikaty_i_usun(rows)
    print("Duplikaty zostały usunięte z pliku 'Translation.csv' i zapisane w pliku 'duplikaty.txt'.")
