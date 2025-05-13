def get_book_text_count(file_path):
    with open(file_path) as f:
        book_text = f.read()
    word_count = len(book_text.split())
    return word_count
    