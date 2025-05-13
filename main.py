from stats import get_book_text_count

def main():
    book_path = 'books/frankenstein.txt'
    #text = get_book_text(book_path)
    text_count = get_book_text_count(book_path)
    print(f"{text_count} words found in the document")

def get_book_text(file_path):
    # This function reads the content of a book file and returns it as a string.
    with open(file_path) as f:
        book_text = f.read()
    print(book_text) 



main()