def word_count(text):
   text_convert = list(text.split())
   total_words = len(text_convert)
   return total_words

def letter_count(text):
   letter_dict = {}
   all_letters = set(text.lower())
   for a in all_letters:
     letter_dict[a] = text.lower().count(a)
   return letter_dict