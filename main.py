from stats import get_num_words, get_letters_count

def main():
  text_string = get_book_text ("books/frankenstein.txt")
  word_count = get_num_words(text_string)
  letter_count = get_letters_count(text_string)
  print (f"Found {word_count} total words")
  print (letter_count)

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text


main()
