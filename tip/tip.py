def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return int(d[1])*10 + int(d[2]) + int(d[4])*0.1 + int(d[5])*0.01


def percent_to_float(p):
    return int(p[0])*0.1 + int(p[1])*0.01


main()