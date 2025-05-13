from stats import *

def main():
    book_path = 'books/frankenstein.txt'
    #text = get_book_text(book_path)
    #text_count = get_book_text_count(book_path)
    #print(f"{text_count} words found in the document")
    char_count = get_book_character_count_by_letter(book_path)
    print(char_count)
main()