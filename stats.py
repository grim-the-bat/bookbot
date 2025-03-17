def word_count(text):
   text_convert = list(text.split())
   total_words = len(text_convert)
   return total_words

def letter_count(text):
   letters_dict = {}
   for l in text:
      lowered = l.lower()
      if lowered in letters_dict:
         letters_dict[lowered] += 1
      else:
         letters_dict[lowered] = 1
#   sorted_dict = {k: v for k, v in sorted(letters_dict.items(), key=lambda item:item[1], reverse=True)}
   return letters_dict