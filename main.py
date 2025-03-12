from stats import *
import sys

def main():
  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
  path = sys.argv[1]
  num = get_num_words(path)
  dict = sort_dict(get_char_instances(path))
  print('============ BOOKBOT ============')
  print('Analyzing book found at ' + path)
  print('----------- Word Count ----------')
  print('Found ' + str(num) + ' total words')
  print('--------- Character Count -------')
  for char, value in dict:
    if char.isalpha():
      print(char + ': ' + str(value))
  print('============= END ===============')

main()