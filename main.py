class CharsetEditor:
    def __init__(self, text=""):
        self.text = text
        self.letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'

    def set_text(self, text):
        self.text = text
        return self
    
#подсчет одинаковых слов
#http://127.0.0.1:5000/charset_count?query=тест+тест+тест+пример

    def count_words(self):
        counts = dict()
        words = self.text.lower().split()
        for word in words:
            clean = ''
            for cs in word:
                if cs in self.letters:
                    clean += cs
            if clean:
                if clean in counts:
                    counts[clean] += 1
                else:
                    counts[clean] = 1
        return counts
    
#подсчет уникальных слов, то есть тех, которые повторяются 1 раз
#http://127.0.0.1:5000/charset_unique?query=тест+уникальный+уникальный+пример

    def unique(self):
        counts = self.count_words()
        unique_words = {}
        for w, c in counts.items():
            if c == 1:
                unique_words[w] = c
        return unique_words
    
#удаление слов, которые повторяются впринципе. выведет все слова, которые имеются, но без повторений
#http://127.0.0.1:5000/charset_remove_duplicates?query=тест+тест+повтор+повтор+пример

    def remove_duplicates(self):
        seen = set()
        result = []
        words = self.text.lower().split()
        for w in words:
            clean = ''
            for cs in w:
                if cs in self.letters:
                    clean += cs
            if clean and clean not in seen:
                seen.add(clean)
                result.append(clean)
        return ' '.join(result)
    
#поиск палиндромов
#http://127.0.0.1:5000/charset_palindromes?query=заказ+шалаш+довод+тест

    def palindromes(self):
        result = set()
        words = self.text.lower().split()
        for w in words:
            clean = ''
            for cs in w:
                if cs in self.letters:
                    clean += cs
            if clean and clean == clean[::-1] and len(clean) > 1:
                result.add(clean)
        return list(result)
