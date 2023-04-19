# Tyler Boudreau
# 01/28/2023
# COT 4500, Assigment 1, UCF

import numpy as np
from decimal import Decimal

def func(x):
    return x*x*x + 4*x*x - 10

def bisection_method(left: float, right: float, given_function: str):
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = .0001
    diff: float = right - left
    max_iterations = 40
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        x = left
        evaluated_left_point = eval(given_function)
        
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint >0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint <0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
    print(iteration_counter, "\n")

def function(value):
    return (value ** 3) + (4*value**2) - 10
def custom_derivative(value):
    return (3 * value* value) + (8 * value)
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f' 
        f_prime = custom_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1

    print(iteration_counter)      

def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check

def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

if __name__ == "__main__":
    f = ((.5)+(.5**2)+(.5**3)+(.5**5)+(.5**7)+(.5**8)+(.5**9)+(.5**12))
    c = ((2**10)+(2**2)+(2)+(1))
    # c = 1031
    bfpa = ((2**(c-1023))*(1+f))
    print(bfpa,"\n")

    normalized = bfpa*.001
    normalizedr = f'{normalized:.4f}'[:-1]
    chopping3 = normalizedr
    print(chopping3,"\n")

    rounding3 = normalized+0.0005
    choppingr = f'{rounding3:.4f}'[:-1]
    unnormchoppingr = round(bfpa,0)
    print(choppingr, "\n")

    AbsError = (abs(Decimal(normalized) - Decimal(choppingr)))
    AbsErrorR = f'{AbsError:.8f}'[:-1]
    print(AbsErrorR)

    RelativeError = (abs(Decimal(bfpa)-Decimal(unnormchoppingr))/(abs(Decimal(bfpa))))
    print(RelativeError, "\n")

    infinite_series_atf1: str = "((-1**k)*((x**k)/(k**3)))"
    x:  int = 1
    check1: bool = check_for_alternating(infinite_series_atf1, )
    #Function is alternating series as check returns TRUE

    # Solve for: 1/(n+1)^3 < 10**-4,
    # = (n+1)**3 > 10^4,
    # = (n+1) > 10**(4/3),
    # = n > 10**4/3 -1, = n > 21.5443 - 1
    # = n > 20.5443, rounded up to next hole int number, n = 21.
    # 21 terms needed to calculate f(1) of the infinite series with error < 10**-4
    print("21\n")

    # Bisection method
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_string)

    # Newton Raphson method
    initial_approximation: float = 7
    tolerance: float = .0001
    sequence: str = "x**3 + 4*(x**2) - 10"
    newton_raphson(initial_approximation, tolerance, sequence)

