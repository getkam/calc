import pytest
from calc import get_components
from calc import calculate

def test_get_components_positive():
  assert get_components("2 + 3") == [2, '+', 3] 
  assert get_components("-2 + -3") == [-2, '+', -3]  
  assert get_components("-2.0000001 + 3") == [-2.0000001, '+', 3]  
  assert get_components("20 * 0.") == [20, '*', 0.]  
  assert get_components("2.01 + 3.01") == [2.01, '+', 3.01] 


def test_get_components_negative_val_err():
  with pytest.raises(ValueError):
      get_components("2 +3")
      get_components("2 = 3")
      get_components("2 & 3")
      get_components("2 ^ 3")
      get_components("2+ 3")
      get_components("2+3")
      get_components("2")
      get_components("+")
      get_components("blabla +")
      get_components("")

def test_calculate_positive():
   assert calculate(2, "+", 3) == 5.0
   assert calculate(2, "+", 0.0000) == 2.0
   assert calculate(2.01, "+", 3.01) == 5.02

   assert calculate(2.0, "-", 0.5) == 1.5
   assert calculate(2.0, "-", 0.0) == 2.0
   assert calculate(2.0, "-", 10.0) == -8.0

   assert calculate(2, "*", 3) == 6.0
   assert calculate(20, "*", 0.5) == 10.0
   assert calculate(2, "*", -1) == -2.0
   assert calculate(2, "*", 0) == 0.0

   assert calculate(20, "/", 2) == 10.0
   assert calculate(0, "/", 2) == 0.0
   assert calculate(20, "/", -2) == -10.0
   assert calculate(20, "/", 1.0) == 20.0
   assert calculate(20, "/", 20.000000000) == 1.0

def test_calculate_negative_value_err(): 
   with pytest.raises(ValueError):
      calculate("a", "+", "3")
      calculate("2", "+", "b")
      calculate("2", "_", "b")

def test_calculate_negative_zero_div(): 
   with pytest.raises(ZeroDivisionError):
      calculate(2, "/", 0)
      calculate(2, "/", 0.000)
      calculate(2, "/", -0)
    


