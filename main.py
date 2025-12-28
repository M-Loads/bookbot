def main():
  text_string = get_book_text ("books/frankenstein.txt")
  word_count = number_of_words(text_string)
  print (f"Found {word_count} total words")

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text

def number_of_words (book_text):
  num_words = len(book_text.split())

  return num_words

main()
