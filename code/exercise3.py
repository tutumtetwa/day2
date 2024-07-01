def swap(dictionary):
  if not all(isinstance(value, (int, float, str, tuple)) for value in dictionary.values()):
    return "Cannot swap the keys and values for this dictionary"

  swapped_dict = {v: k for k, v in dictionary.items()}

  return swapped_dict


# test code below

