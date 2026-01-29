from week4.MiniProject.anagram_checker import AnagramChecker


def main():
    checker = AnagramChecker("sowpods.txt")
    while True:
        print("\n--- MENU ANAGRAM ---")
        print("1. Enter a word")
        print("2. Exit")
        choice = input("Chose an option : ").strip()

        if choice == '2':
            exit()
        elif choice == '1':
            user_input = input("Enter a word : ").strip()

            if " " in user_input:
                print("ERROR : Only a single word is allowed.")
            elif not user_input.isalpha():
                print(
                    "ERROR : Only alphabetic characters are allowed.")
            else:
                user_word = user_input.upper()

                if checker.is_valid_word(user_word):
                    anagrams = checker.get_anagrams(user_word)

                    print(f"\nYOUR WORD : '{user_word}'")
                    print("Your input is valid.")
                    if anagrams:
                        print(
                            f"All possible anagrams to the word {user_word} are : {', '.join(anagrams)}")
                    else:
                        print("Anagrams not founded.")
                else:
                    print(
                        f"The word '{user_word}' not in the dictionary.")
        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
