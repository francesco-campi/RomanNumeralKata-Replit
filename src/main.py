

def from_roman(roman: str) -> int:
  symbol_dic = {'N':0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
  number = 0
  previous_char = None
  for character in roman[::-1]:
    if previous_char is not None and previous_char > symbol_dic[character]:
      number -= symbol_dic[character]
    else:
      number += symbol_dic[character]
    previous_char = symbol_dic[character]
  return number


