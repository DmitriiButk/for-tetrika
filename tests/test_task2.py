import unittest
from collections import Counter
from task2.solution import save_to_csv


class TestSaveToCSV(unittest.TestCase):
    def test_save_to_csv_creates_file(self):
        import os
        filename = 'test_beasts.csv'
        counter = Counter({'А': 2, 'Б': 1})
        save_to_csv(counter, filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
        self.assertIn('А,2\n', lines)
        self.assertIn('Б,1\n', lines)
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
