from typing import Literal


def main():
    components = get_components(input("Equation: "))
    print(calculate(*components))


def get_components(text)-> []:
       
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