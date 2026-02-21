def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return int(d.replace('$', '').replace('.', '')) * 0.01
    # uses the asumption of the format $xx.xx to convert the str to a float


def percent_to_float(p):
    return int(p.replace('%', ''))*0.01
    # returns the string withou the '%' * 0.01 as a float


main()