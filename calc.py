from typing import Literal
from typing import List, Tuple


def main():
    components = get_components(input("Equation: "))
    print(calculate(*components))


def get_components(text: str)-> List[float | str]:
    '''
    Parse equation provided by user and validate it's components

    :param n: Equation that is provided by user
    :type n: str
    :raise ValueError: If equation is not valid
    :return: List of 3 components of equation:first element, operator, second element
    :rtype: list[float, str, float]
    '''
    components = text.split(" ")
       
    if len(components) != 3:
        raise ValueError
       
    first, operator, second = components
    if operator not in "+-*/" and len(operator) != 1:
        raise ValueError(f"Invalid operator {operator}")
    try: 
        first_fl = float(first)
    except: 
        raise ValueError(f"Value {first} is not a number")
    try:     
        second_fl = float(second)
    except: 
        raise ValueError(f"Value {second} is not a number")
    
    return [first_fl, operator, second_fl] 

def calculate(first:float, operator: Literal['+', '-', '*', '/'], second:float) -> float:
    '''
    Execute calculation of provided values

    :param first: First component of equation
    :type first: float
    :param operator: First component of equation
    :type operator: Allowed are 4 characters +, -, *, /
    :param second: Second component of equation
    :type second: float
    :raise ValueError: If operator is not recognized
    :raise ZeroDivisionError: If operator i division and second component is zero
    :return: Result of equation
    :rtype: float
    '''
    match operator:
      case "+":
          return first + second
      case "-":
          return first - second
      case "*":
          return first * second
      case "/":
          if second == 0: 
            raise ZeroDivisionError
          return first / second
      case _:
          raise ValueError


if __name__ == "__main__":
  main()