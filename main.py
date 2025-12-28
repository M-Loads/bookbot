def main():
  text_string = get_book_text ("books/frankenstein.txt")
  word_count = number_of_words(text_string)
  print (f"Found {word_count} total words")

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text

from stats import num_words

return num_words

main()
