def get_num_words (book_text):
  num_words = len(book_text.split())
  return num_words

def get_letter_count (book_text):
  lowercase = book_text.lower()
  letters_dict = {}
  for x in lowercase:
    if x in letters_dict:
      letters_dict[x] = letters_dict[x] + 1
    else:
      letters_dict[x] = 1
  return letters_dict

def sort_on(char):
  return char["num"]

def sort_letters(letters_dict):
  chars = []
  for char, count in letters_dict.items():
    s = {"char": char, "num": count}
    chars.append(s)

chars.sort(reverse=True, key=sort_on)
  return chars

  
