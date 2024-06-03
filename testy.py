import unittest
from collections import defaultdict

def znajdz_duplikaty(rows):
    widziane = set()
    duplikaty = defaultdict(list)

    for line in rows:
        source_text = line['source_text']
        translated_text = line['translated_text']
        combined_text = (source_text, translated_text)
        
        if combined_text in widziane:
            duplikaty[source_text].append(translated_text)
        else:
            widziane.add(combined_text)
    
    return duplikaty

class TestZnajdzDuplikaty(unittest.TestCase):

    def test_1_duplicate(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list, {'Hello': ['Cześć']})
        self.assertEqual(znajdz_duplikaty(rows), expected)
    
    def test_no_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Goodbye', 'translated_text': 'Do widzenia'}
        ]
        expected = defaultdict(list)
        self.assertEqual(znajdz_duplikaty(rows), expected)

    def test_multiple_duplicates(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list, {'Hello': ['Cześć'], 'Hi': ['Cześć']})
        self.assertEqual(znajdz_duplikaty(rows), expected)
    
    def test_no_duplicates_with_different_translations(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hello', 'translated_text': 'Witaj'}
        ]
        expected = defaultdict(list)
        self.assertEqual(znajdz_duplikaty(rows), expected)
    
    def test_no_duplicates_with_different_sources(self):
        rows = [
            {'source_text': 'Hello', 'translated_text': 'Cześć'},
            {'source_text': 'Hi', 'translated_text': 'Cześć'}
        ]
        expected = defaultdict(list)
        self.assertEqual(znajdz_duplikaty(rows), expected)

if __name__ == '__main__':
    unittest.main()
