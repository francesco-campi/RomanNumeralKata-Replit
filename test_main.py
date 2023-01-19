import pytest
from main import from_roman
from roman import toRoman, fromRoman
import numpy as np

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('IV', 4),
  ('V', 5),
  ('VI', 6),
  ('VII', 7),
  ('VIII', 8),
  ('IX', 9),
  ('X', 10),
  ('XI', 11),
  ('XII', 12),
  ('XIII', 13),
  ('XIV', 14),
  ('XV', 15),
  ('XVI', 16),
  ('XVII', 17),
  ('XVIII', 18),
  ('XIX', 19),
  ('XX', 20),
  ('XXI', 21),
  ('XXII', 22),
  ('XXIII', 23),
  ('XXIV', 24),
  ('XXV', 25),
  ('XL', 40),
  ('XC', 90),
  ('LXXXVIII', 88)
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman

@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_2(num: int, roman: str):
  assert from_roman(num) == fromRoman(num)


def test_random_roman():
  for rand_int in np.random.randint(0,100,50):
    rand_int = int(rand_int)
    roman = toRoman(rand_int)
    assert from_roman(roman) == rand_int, f"Wrong for number {rand_int}"
