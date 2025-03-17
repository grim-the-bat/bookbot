def word_count(text):
   text_convert = list(text.split()) #creates list from text on split
   total_words = len(text_convert) #grabs the len for the total words
   return total_words

def letter_count(text):
   letters_dict = {} #blank dictionary
   for l in text: #for each letter in the text
      lowered = l.lower() #set it to lower case
      if lowered in letters_dict: #checks to see if it's in the dicionary
         letters_dict[lowered] += 1 #if yes, ++
      else:
         letters_dict[lowered] = 1 #if not, add value
   return letters_dict

def dict_sorter(text):
   unsorted_dict = letter_count(text) #grab the letter count dict
   sorted_dict = {k: v for k, v in sorted(unsorted_dict.items(), key=lambda item:item[1], reverse=True)} #do some kind of magic
   return sorted_dict