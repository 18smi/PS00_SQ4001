def main():
    input_string = input("input please\n")
    print(convert(input_string))

def convert(input_string):
    output_string = ""
    face_started = False

    for i in input_string:
        if face_started:
            face_started = False
            if  i == ')':
                output_string += '🙂'
                continue
            elif  i == '(':
                output_string += '🙁'
                continue
            else:
                output_string += ':'
            

        if face_started == False and i == ':':
            face_started = True
        else:
            output_string += i

    return output_string

main()
    