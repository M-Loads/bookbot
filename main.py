import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words, get_letter_count, sort_letters

def main():
  path = sys.argv[1]
  text_string = get_book_text (path)
  word_count = get_num_words(text_string)
  letter_count = get_letter_count(text_string)
  letter_sorting = sort_letters(letter_count)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print (f"Found {word_count} total words")
  print("--------- Character Count -------")
  print_report(letter_sorting)
  print("============= END ===============")

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()
  return book_text

def print_report(sorted_letters):
  for entry in sorted_letters:
    char = entry ["char"]
    num = entry ["num"]
    if char.isalpha():
      print (f"{char}: {num}")

main()
