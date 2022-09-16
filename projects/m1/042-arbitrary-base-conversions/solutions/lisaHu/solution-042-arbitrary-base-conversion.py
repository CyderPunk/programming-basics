#the calculation for the conversion of numbers between bases was taken from here:
#ITALIAN: http://www.economia.unical.it/ProvaInformatica/argomenti/conversione_dei_numeri_tra_basi_.htm


def convert_base_10(num, base_arb):
    #reverse num (which is currently a string) so that it's easier to calculate with base ten
    #as the base ten gets smaller the further the position of the digit is starting from left
    num = num[::-1]
    base_10 = 0
    convert_num = 0
    #for every digit in the reversed number
    for digit in num:
        digit = int(digit) * (base_arb ** base_10)
        #add the new digit to the variable that will store the result
        convert_num = convert_num + digit
        #raise the power of the calculation as the new digit the program will calculate has a different position
        base_10 += 1
    return convert_num


def convert_base_arb(num, base_arb):
    converted_num = ''
    #use result from conversion to base 10 as number of this conversion
    num = convert_base_10(num, base_arb)
    while True:
        if int(num) < base_arb:
            break
        #the remainder will be part of the result and the new num will be used in the next calculations
        remainder = int(num) % base_arb
        num = int(num) // base_arb
        #store the remainder as string and later convert it in an integer in the return statement
        converted_num += str(remainder)
    return int(converted_num[::-1])


#get inputs from user, call functions, display results and error message if needed
if __name__=='__main__':
    num = input('Enter number to convert: ')
    base_arb = int(input('Enter arbitrary base between 2 and 16: '))
    if 2 <= base_arb <= 16:
        print()
        convert_base_10(num, base_arb)
        convert_base_arb(num, base_arb)
        print('The converted number from base ' + str(base_arb) + ' to base 10 is: ' + str(convert_base_10(num, base_arb)))
        print('The converted number from base 10 to base ' + str(base_arb) + ' is: ' + str(convert_base_arb(num, base_arb)))
    else:
        print('Error: Number entered is outside of specified range')