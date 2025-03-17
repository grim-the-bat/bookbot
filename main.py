import sys
from stats import word_count,dict_sorter 

def get_book_text(filepath):
 with open(filepath) as file:
    contents = file.read()
    return contents

def main():
    if len(sys.argv) < 2:
       print(f"Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    total_words = word_count(book_text)
    total_letters = dict_sorter(book_text)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------""")
    for k,v in total_letters.items():
       if k.isalpha() == True:
         print(f"{k}: {v}")  
    print(f"""============= END ===============""")

main()