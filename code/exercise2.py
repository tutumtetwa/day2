def move_to_bottom(dictionary, key):
  if key not in dictionary:
    return f"The key '{key}' is not in the dictionary."

  value = dictionary.pop(key)

  dictionary[key] = value

  return dictionary

  



# test code below

