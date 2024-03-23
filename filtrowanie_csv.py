import csv

def wyswietl_csv(Translation_csv):
    with open(Translation_csv, 'r', encoding='utf-8') as plik_csv:
        csv_reader = csv.reader(plik_csv)
        for wiersz in csv_reader:
            print(wiersz)

def wczytaj_csv(Translation_csv):
    with open(Translation_csv, 'r', encoding='utf-8') as plik_csv:
        csv_reader = csv.DictReader(plik_csv)
        rows = list(csv_reader)
        fieldnames = csv_reader.fieldnames
        for row in rows:
            print(row['source_text'], row['translated_text'])
        return rows, fieldnames

def znajdz_duplikaty(rows):
    duplikaty = {}
    for line in rows:
        source_text = line['source_text']
        translated_text = line['translated_text']
        if source_text in duplikaty:
            duplikaty[source_text].append(translated_text)
        else:
            duplikaty[source_text] = [translated_text]

    return {source_text: translations for source_text, translations in duplikaty.items() if len(translations) > 1}

def usun_duplikaty(Translation_csv, duplikaty, fieldnames):
    wiersze_do_zapisu = []
    with open(Translation_csv, 'r', encoding='utf-8') as plik_csv:
        csv_reader = csv.DictReader(plik_csv)
        for line in csv_reader:
            source_text = line['source_text']
            if source_text not in duplikaty:
                wiersze_do_zapisu.append(line)

    with open(Translation_csv, 'w', newline='', encoding='utf-8') as plik_csv:
        csv_writer = csv.DictWriter(plik_csv, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(wiersze_do_zapisu)

    with open('duplikaty.txt', 'w', encoding='utf-8') as duplikaty_file:
        duplikaty_file.write("Znalezione duplikaty:\n")
        for source_text, translations in duplikaty.items():
            duplikaty_file.write(f"Wyraz: {source_text}, Tłumaczenia: {translations}\n")

if __name__ == "__main__":
    Translation_csv = 'Translation.csv'

    rows, fieldnames = wczytaj_csv(Translation_csv)

    duplikaty = znajdz_duplikaty(rows)
    print("\nZnalezione duplikaty:")
    for source_text, translations in duplikaty.items():
        print(f"  Wyraz: {source_text}, Tłumaczenia: {translations}")

    usun_duplikaty(Translation_csv, duplikaty, fieldnames)

    print("\nZawartość pliku Translation.csv po usunięciu duplikatów:")
    wyswietl_csv(Translation_csv)
