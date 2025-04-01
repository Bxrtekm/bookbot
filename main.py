from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def menu(path_to_file, num_words, sorted_chars_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_chars_dict:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[2]
    text = get_book_text(path_to_file)
    num_words = number_of_words(text)
    chars_dict = number_of_each_character(text)
    sorted_chars_dict = func(chars_dict)

    menu(path_to_file, num_words, sorted_chars_dict)
main()