def get_book_text(filepath):
 with open(filepath) as file:
    contents = file.read()
    return contents
 
def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()