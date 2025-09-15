def get_num_words(sentence):
  full_words = sentence.split()
  count = len(full_words)
  return count

def get_num_each_character(sentence):
  count_characters = {}
  for c in sentence:
    lowered = c.lower()
    if lowered in count_characters:
      count_characters[lowered] += 1
    else:
      count_characters[lowered] = 1
  return count_characters

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
  updated_dict = []
  for key in char_dict:
    new_item = { "char": key, "num": char_dict[key] }
    updated_dict.append(new_item)
  updated_dict.sort(reverse=True, key=sort_on)
  return updated_dict