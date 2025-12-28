def main():
  result = get_book_text ("books/frankenstein.txt"):
  print (result)

def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text

main()
