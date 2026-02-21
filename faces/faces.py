def main():
    print(convert(input("input please\n")))# prints the converted input

def convert(input_string):
    return input_string.replace(":)", '🙂').replace(":(", '🙁')
    # replaces all instances of :) and :( with 🙂 and 🙁 respectively

main()
    