class CharsetEditor:
    def __init__(self, text=""):
        self.text = text
        self.letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz'


    def set_text(self, text):
        self.text = text
        return self


    def count_words(self):
        counts = dict()
        words = self.text.lower().split()
        for word in words:
            clean = ''.join(cs for cs in word if cs in self.letters)
            if clean:
                counts[clean] = counts.get(clean, 0) + 1
        return counts


    def unique(self):
        counts = self.count_words()
        return {w: c for w, c in counts.items() if c == 1}


    def remove_duplicates(self):
        seen = set()
        result = []
        words = self.text.lower().split()
        for word in words:
            clean = ''.join(cs for cs in word if cs in self.letters)
            if clean and clean not in seen:
                seen.add(clean)
                result.append(clean)
        return ' '.join(result)


    def palindromes(self):
        result = set()
        words = self.text.lower().split()
        for word in words:
            clean = ''.join(cs for cs in word if cs in self.letters)
            if clean and clean == clean[::-1] and len(clean) > 1:
                result.add(clean)
        return list(result)
