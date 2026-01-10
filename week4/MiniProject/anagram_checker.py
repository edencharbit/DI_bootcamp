class AnagramChecker:

    def __init__(self, word_file):
        self.word_lst = []
        with open(word_file, 'r', encoding='utf-8') as file:
            for line in file:
                self.word_lst.append(line.strip().upper())

    def is_valid_word(self, word):
        return word.upper() in self.word_lst

    def get_anagrams(self, word):
        word=word.upper()
        anagram_lst = []
        for w in self.word_lst: #check all the p
            if self.is_anagram(word, w):
                anagram_lst.append(w)
        return anagram_lst

    @staticmethod
    def is_anagram(word1, word2):
        word1 = word1.upper()
        word2 = word2.upper()
        if sorted(word1) == sorted(word2) and word1 != word2:
            return True

