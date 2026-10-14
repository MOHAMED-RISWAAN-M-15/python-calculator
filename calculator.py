import math
class Calculator:
    def __init__(self, number1: float=0, operator: str|None=None, number2: float=0):
        self.number1 = number1
        self.number2 = number2
        self.operator = operator

    def match_checker(self) -> int | float:
        match self.operator:
            case "+":
                return (self.number1) + (self.number2)
            case "-":
                return (self.number1) - (self.number2)

            case "*":
                return (self.number1) * (self.number2)

            case "/":
                return (self.number1) / (self.number2)
            case "%":
                 return (self.number1) % (self.number2)

            case "power":
                return (self.number1)**(self.number2)
            case "sqrt":
                return math.sqrt(self.number1)
            case _:
                raise ValueError("Invalid Operator")
            
                

    @classmethod
    def get_number(cls):
        while True:
            try:
                number1: float = float(input("\033[34mEnter First Number:\033[0m"))
                operator: str = input("\033[34mEnter operator (+,-,*,/,%,power,sqrt):\033[0m").lower()
                if operator not in ("+", "-", "*", "/","%","power","sqrt"):
                    raise ValueError
                elif operator == "sqrt":
                    if number1<0:
                        raise ValueError
                    return cls(number1=number1, operator=operator)
                number2: float = float(input("\033[34mEnter Second Number:\033[0m"))

                if number2 == 0 and operator in ("/","%"):
                    raise ZeroDivisionError
                
                return cls(number1=number1, operator=operator, number2=number2)
            except ValueError:
                print(
                    "\033[31mPlease enter a valid input( non-Negative Number for SquareRoot)  and Operator(+,-,*,/,%,power,sqrt)\033[0m"
                )
                
            except ZeroDivisionError:
                print("\033[31mCannot Divide By Zero\033[0m")
               


def main():
    calculator = Calculator.get_number()  
    print(f"\033[32m{calculator.match_checker()}\033[0m")


if __name__ == "__main__":
    main()
