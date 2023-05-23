while True:
    Binary_number = input("Enter Binary Number or Enter 'e' to end: ")
    if Binary_number == 'e':
        break
    Decimal_number = 0
    for i in Binary_number:
        if i not in ['0','1']:
            print('ادخال خاطئ, أدخل رقم ثنائي')
            break
    else:
        for x in range(len(Binary_number)):
            Decimal_number += int(Binary_number[x])*2**(len(Binary_number)-1-x)
        print(Binary_number,"=",Decimal_number)
        
                