def get_book_text(filepath):
 with open(filepath) as file:
    contents = file.read()
    return contents

def word_count(text):
   text_convert = list(text.split())
   total_words = len(text_convert)
   return total_words

 
def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = word_count(book_text)
    print(f"{total_words} words found in the document")

main()