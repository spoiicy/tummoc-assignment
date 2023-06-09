def isValidCredit(number):
    number = str(number)
    size = len(number)
    if((number[0]=="4" and size==13) or (number[0]=="5" and size == 13) or (number[0] == "6" and size == 16) or (number[0]=='3' and number[1]=='7' and size == 16)):
        print("credit card format is valid")
        return isValidNumber(number)
    else:
        print("credit card format not valid")
        return False



def isValidNumber(number):
    
    total = 0 
    isEven = False
    slider = len(number) - 1
    while(slider >= 0):
        if isEven:
            num = int(number[slider])*2
            total += num if num < 10 else (num//10) + (num%10)
        else:
            total += int(number[slider])
        isEven = not isEven
        slider -= 1
        
    return True if (total%10==0) else False
    

credit_card_number = input("enter credit card number")


if isValidCredit(credit_card_number):
    print("Credit Card Number is valid")
else:
    print("Credit Card Number is not valid")


