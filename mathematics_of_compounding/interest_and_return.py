from decimal import Decimal


def total_return(principal: Decimal, accumulated_value: Decimal):
    return accumulated_value / principal

def rate_of_return(principal: Decimal, accumulated_value: Decimal):
    return accumulated_value / principal - 1








if __name__ == '__main__':
    P = Decimal(1000)
    Vt = Decimal(1200)

    print(f"Principal: {P}, Accumulated Value: {Vt}")

    total_return = total_return(principal=P, accumulated_value=Vt)
    print(f"Total Return: {total_return}")

    interest_earned = Vt - P
    rate_of_return = rate_of_return(principal=P, accumulated_value=Vt)
    print(f"Rate of return: {rate_of_return}")



