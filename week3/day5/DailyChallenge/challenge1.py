

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        word_lst = self.text.split()
        word_count = 0
        for w in word_lst:
            if w == word:
                word_count += 1
        if word_count >0:
            return f"The word {word} is found {word_count} times is the text"
        else:
            return f"The word {word} is not found in the text"

    def most_common_word(self):
        word_lst = self.text.split()
        words_dict = {}
        for w in word_lst:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1
        common_word = max(words_dict, key = words_dict.get)
        return f"The word {common_word} is the " \
               f"most common word and it apperes {words_dict[common_word]}"

    def unique_words(self):
        word_lst = self.text.split()
        unique_set = set(word_lst)
        return list(unique_set)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return cls(content)




