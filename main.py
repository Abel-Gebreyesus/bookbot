from stats import *
import sys

# Main - calls from stats.py and formats data
def main():
  # Informs user to include path to book
  if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
  # Gets path and calculates relevent information
  path = sys.argv[1]
  num = get_num_words(path)
  dict = sort_dict(get_char_instances(path))
  # Formats information
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