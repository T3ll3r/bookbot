
def get_book_text(file_path):
    # This function reads the content of a book file and returns it as a string.
    with open(file_path) as f:
        book_text = f.read()
    print(book_text) 


def get_book_text_count(file_path):
    with open(file_path) as f:
        book_text = f.read()
    word_count = len(book_text.split())
    return word_count


def get_book_character_count_by_letter(file_path):
    with open(file_path) as f:
        book_text = f.read()
        lowered_book_text = book_text.lower()
    # Count the number of characters in the book text
    char_count = len(lowered_book_text)
    # Count the number of characters by letter
    char_count_by_letter = {}
    for char in lowered_book_text:
       # if char.isalpha():
            char_count_by_letter[char] = char_count_by_letter.get(char, 0) + 1
    return char_count_by_letter