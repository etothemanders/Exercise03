import arithmetic

def main():
    
    while True:
        calculation = raw_input(">")
        calc_parts = calculation.split(" ")
        math_fcn = calc_parts[0]

        # determine whether they want to quit
        if math_fcn == "q":
            break

        else:
            try:
                num1 = int(calc_parts[1])
                num2 = int(calc_parts[2])
            except IndexError:
                print "I don't understand"
                continue
            except ValueError:
                print "I don't understand"
                continue

        # decide which math function to call
        if math_fcn == "+":
            print arithmetic.add(num1, num2)
        elif math_fcn == "-":
            print arithmetic.subtract(num1, num2)

        elif math_fcn == "*":
            print arithmetic.multiply(num1, num2)

        elif math_fcn == "/":
            print arithmetic.divide(num1, num2)

        elif math_fcn == "square":
            print arithmetic.square(num1)

        elif math_fcn == "cube":
            print arithmetic.cube(num1)

        elif math_fcn == "pow":
            print arithmetic.power(num1, num2)

        elif math_fcn == "mod":
            print arithmetic.mod(num1, num2)

        else:
            print "I don't understand."


if __name__ == "__main__":
    main()



