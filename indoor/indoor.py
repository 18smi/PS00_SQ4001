input_string = input("input please\n")
output_string = ""
for i in input_string:
    if i.isupper():
        output_string += i.lower()
    else:
        output_string += i

print(output_string)