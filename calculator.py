import arithmetic

def check_for_valid_number(number_string):
    if number_string.isdigit() or (number_string[0] == '-' and number_string[1:].isdigit()):
        return True
    else:
        return False

def main():
  
    while True:
        calculation = raw_input(">")
        calc_parts = calculation.split(" ")
        first_input = calc_parts[0]
        valid_one_num_operators = ["square", "cube"]
        valid_two_num_operators = ["+", "-", "*", "/", "pow", "mod"]

        # determine whether they want to quit
        if len(calc_parts) == 1:
            if first_input == "q":
                break
            else:
                print "I don't understand."
                continue

        elif len(calc_parts) == 2:
            if (first_input in valid_one_num_operators) and check_for_valid_number(calc_parts[1]):
                num1 = int(calc_parts[1])
            else:
                print "I don't understand."
                continue

        elif len(calc_parts) == 3:
            if (first_input in valid_two_num_operators) and check_for_valid_number(calc_parts[1]) and check_for_valid_number(calc_parts[2]):
                num1 = int(calc_parts[1])
                num2 = int(calc_parts[2])
            else:
                print "I don't understand."
                continue
        else:
            print "I don't understand."
            continue


        # decide which math function to call
        if first_input == "+":
            print arithmetic.add(num1, num2)

        elif first_input == "-":
            print arithmetic.subtract(num1, num2)

        elif first_input == "*":
            print arithmetic.multiply(num1, num2)

        elif first_input == "/":
            print arithmetic.divide(num1, num2)

        elif first_input == "square":
            print arithmetic.square(num1)

        elif first_input == "cube":
            print arithmetic.cube(num1)

        elif first_input == "pow":
            print arithmetic.power(num1, num2)

        elif first_input == "mod":
            print arithmetic.mod(num1, num2)

        else:
            print "I don't understand."


if __name__ == "__main__":
    main()



