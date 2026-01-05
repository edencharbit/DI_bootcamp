# Exercise 1: Random Sentence Generator
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_words_from_file(file_path):
    with open(f"{dir_path}/{file_path}", 'r', encoding='utf-8') as file:
        content = file.read()
        words_lst = content.split()
        return words_lst


def get_random_sentence(length):
    words_lst = get_words_from_file("words.txt")
    sentence = ""
    for i in range(length):
        word_choice = random.choice(words_lst)
        sentence += word_choice + ' '
    return sentence.lower()


def main():
    print('The programme generates a random sentence of a specified length '
          'from a word list.\n')
    length_sentence = input("Enter a desired sentence length : ")
    try:
        length = int(length_sentence)
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print(f"\nThe the generated sentence :\n{sentence}")
        else:
            print("Error: the number is not between 2 and 20")
            exit()

    except ValueError:
        print("Error : your input is not an integer")
        exit()


if __name__ == '__main__':
    main()
