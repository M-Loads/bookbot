from stats import get_num_words

def main():
  text_string = get_book_text ("books/frankenstein.txt")
  word_count = get_num_words(text_string)
  print (f"Found {word_count} total words")

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text


main()
