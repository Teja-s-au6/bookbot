from stats import (get_num_words, get_num_each_character, sort_dict)
import sys

def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  path = sys.argv[1]
  file_contents = get_book_text(path)
  num_words = get_num_words(file_contents)
  character_count = get_num_each_character(file_contents)
  print_report(path, character_count, num_words)

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def print_report(book_path, character_count, num_words):
  sorted_dict = sort_dict(character_count)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at ${book_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for item in sorted_dict:
    if not item["char"].isalpha():
      continue
    print(f"{item["char"]}: {item["num"]}")


  print("============= END ===============")

main()