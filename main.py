def get_book_text(path):
  with open(path) as f:
      book_text = f.read()

  return book_text
