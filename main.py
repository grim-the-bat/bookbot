from stats import word_count, letter_count

def get_book_text(filepath):
 with open(filepath) as file:
    contents = file.read()
    return contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = word_count(book_text)
    total_letters = letter_count(book_text)
    print(f"{total_words} words found in the document")
    print(total_letters)
    

main()