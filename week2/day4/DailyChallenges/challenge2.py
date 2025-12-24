# Challenge 2: Longest Word

sentence = input("Enter a sentence: ")


# Step 1: Define the Function
def longest_word(sentence):
    # Step 2: Split the Sentence into Words
    lst_words = sentence.split(' ')
    # Step 3: Initialize Variables
    long_word = lst_words[0]
    max_len = 0
    # Step 4: Iterate Through the Words
    for word in lst_words:
        # Step 5: Compare Word Lengths
        if len(word) > max_len:
            max_len = len(word)
            long_word = word
    # Step 6: Return the Longest Word
    return long_word


print(longest_word(sentence))
