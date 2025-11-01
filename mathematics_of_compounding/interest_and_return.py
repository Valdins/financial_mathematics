from decimal import Decimal


def total_return(principal: Decimal, accumulated_value: Decimal):
    return accumulated_value / principal

def rate_of_return(principal: Decimal, accumulated_value: Decimal):
    return accumulated_value / principal - 1




def calculate_annual_returns_for_each_year(initial_amount: Decimal, years: int, rate: Decimal):
    result = {}
    V0 = initial_amount
    for year in range(years):
        year += 1
        Vn = initial_amount * (rate*(year**2) + 1)

        r = (Vn - V0) / V0

        result[year] = {"Ammount" : Vn, "Rate" : r}
        V0 = Vn

    return result

def calculate_accumulated_value(amount: Decimal, start_year: int, end_year: int):
    result = {}
    V0 = amount
    for year in range(start_year, end_year + 1):
        r = ((3 * year) + 2) / ((2 * year) + 2)

        Vn = V0 * Decimal(r)
        V0 = Vn

        result[year] = {"Ammount": Vn, "Rate": r}

    return result





if __name__ == '__main__':
    # P = Decimal('1000')
    # Vt = Decimal('1200')
    #
    # print(f"Principal: {P}, Accumulated Value: {Vt}")
    #
    # total_return = total_return(principal=P, accumulated_value=Vt)
    # print(f"Total Return: {total_return}")
    #
    # interest_earned = Vt - P
    # rate_of_return = rate_of_return(principal=P, accumulated_value=Vt)
    # print(f"Rate of return: {rate_of_return}")
    #
    #
    # print("Exercise 1.2")
    # initial_amount = Decimal('200')
    # years = 3
    # rate = Decimal('0.1')
    # result = calculate_annual_returns_for_each_year(initial_amount=initial_amount, years=3, rate=rate)

    print("Exercise 1.3")
    amount = Decimal('1000')
    year = 3
    result = calculate_accumulated_value(amount=amount, start_year=4, end_year=6)

    print(f"Accumulated Amount: {result}")



