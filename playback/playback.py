input_string = input("input please\n")
output_string = ""
for i in input_string:
    if i == ' ':
        output_string += "..."
    else:
        output_string += i
print(output_string)