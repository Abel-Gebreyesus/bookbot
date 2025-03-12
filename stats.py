def get_num_words(f):
  with open(f, 'r') as file:
    contents = file.read()
  return len(contents.split())

def get_char_instances(f):
  with open(f, 'r') as file:
    contents = file.read()
  dict = {}
  for char in contents:
    char = char.lower()
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1
  return dict

def sort_dict(dict):
  return sorted(dict.items(), key=lambda item: item[1], reverse=True)