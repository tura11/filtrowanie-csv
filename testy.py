import unittest
from collections import defaultdict

def znajdz_duplikaty(rows):
    duplikaty = defaultdict(list)
    widziane_source = set()
    widzianie_translated = set()
    for line in rows:
        source_text = line['source_text']
        translated_text = line['translated_text']
        
        if source_text in widziane_source:
            duplikaty[source_text].append(translated_text)
        else:
            widziane_source.add(source_text)
        
        if translated_text in widzianie_translated:
            duplikaty[translated_text].append(source_text)
        else:
            widzianie_translated.add(translated_text)

    return duplikaty

class TestZnajdzDuplikaty(unittest.TestCase):

    def test_no_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Goodbye', 'translated_text': 'Do widzenia'}
        ]
        expected = defaultdict(list)
        self.assertEqual(znajdz_duplikaty(rows), expected)

    def test_source_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Witaj'}
        ]
        expected = defaultdict(list, {'Hello': ['Witaj']})
        self.assertEqual(znajdz_duplikaty(rows), expected)
    
    def test_translated_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list, {'Cześć': ['Hi']})
        self.assertEqual(znajdz_duplikaty(rows), expected)
    
    def test_both_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Witaj'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list, {'Hello': ['Witaj'], 'Cześć': ['Hi']})
        self.assertEqual(znajdz_duplikaty(rows), expected)

    def test_same_source_and_translated_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Hej'},
            {'source_text': 'Hello', 'translated_text': 'Hej'}
        ]
        expected = defaultdict(list, {'Hello': ['Hej']})
        self.assertEqual(znajdz_duplikaty(rows), expected)

    def test_varied_same_source_and_translated_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Hej'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Hej'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list, {'Hello': ['Hej'], 'Hi': ['Cześć']})
        self.assertEqual(znajdz_duplikaty(rows), expected)

if __name__ == '__main__':
    unittest.main()
