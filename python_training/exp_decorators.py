
import math

# add a decorator for correcting for inflation
def correct_inflation(func):
    '''
    Correct for the inflation
    '''
    
    def wrapper(amount, rate, years):
        result = func(amount, rate / 2, years)
        return result

    return wrapper


# add a decorator that prints the interest of each year
def print_interest(func):
    def wrapper(amount, rate, years):
        for year in range(years):
            amount = func(amount, rate, 1)
            print(f"{year + 1}: {amount}")
        return amount
    return wrapper

# define function to calculate the interest
@print_interest
@correct_inflation
def calc_interest_inflated(amount: float, rate: float, years:int):
    '''
    Calculates the amount after interest for a number of years
    
    '''
    rate_pct = rate / 100
    final_amount = amount * (1 + rate_pct) ** years
    return final_amount 


def calc_interest(amount: float, rate: float, years:int):
    '''
    Calculates the amount after interest for a number of years
    
    '''
    rate_pct = rate / 100
    final_amount = amount * (1 + rate_pct) ** years
    return final_amount 


def calc_circle(diameter):
    result = (diameter / 2) **2 * math.pi
    return result

# create a function that both uses the 'print_interest' and 'correct_inflation' wrappers



if __name__ == '__main__':
    result = calc_interest(1000, 5, 10)
    result_inflated = calc_interest_inflated(1000, 5, 10)
    print(result)
    pass