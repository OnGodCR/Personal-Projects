import random



def generate_letter_capital():
    r=(random.randrange(1,27))
    letter=0
    if r==1:
        letter="A"
    if r==2:
        letter="B"
    if r==3:
        letter="C"
    if r==4:
        letter="D"
    if r==5:
        letter="E"
    if r==6:
        letter="F"
    if r==7:
        letter="G"
    if r==8:
        letter="H"
    if r==9:
        letter="I"
    if r==10:
        letter="J"
    if r==11:
        letter="K"
    if r==12:
        letter="L"
    if r==13:
        letter="M"
    if r==14:
        letter="N"
    if r==15:
        letter="O"
    if r==16:
        letter="P"
    if r==17:
        letter="Q"
    if r==18:
        letter="R"
    if r==19:
        letter="S"
    if r==20:
        letter="T"
    if r==21:
        letter="U"
    if r==22:
        letter="V"
    if r==23:
        letter="W"
    if r==24:
        letter="X"
    if r==25:
        letter="Y"
    if r==26:
        letter="Z"
    return letter

def generate_letter_lowercase():
    r=random.randrange(1,27)
    letter=0
    if r==1:
        letter="a"
    if r==2:
        letter="b"
    if r==3:
        letter="c"
    if r==4:
        letter="d"
    if r==5:
        letter="e"
    if r==6:
        letter="f"
    if r==7:
        letter="g"
    if r==8:
        letter="h"
    if r==9:
        letter="i"
    if r==10:
        letter="j"
    if r==11:
        letter="k"
    if r==12:
        letter="l"
    if r==13:
        letter="m"
    if r==14:
        letter="n"
    if r==15:
        letter="o"
    if r==16:
        letter="p"
    if r==17:
        letter="q"
    if r==18:
        letter="r"
    if r==19:
        letter="s"
    if r==20:
        letter="t"
    if r==21:
        letter="u"
    if r==22:
        letter="v"
    if r==23:
        letter="w"
    if r==24:
        letter="x"
    if r==25:
        letter="y"
    if r==26:
        letter="z"
    return letter
    

def generate_number():
    number=random.randint(1,9)
    return number

def generate_special():
    r=random.randrange(1,6)
    letter=0
    if r==1:
        letter="!"
    elif r==2:
        letter="@"
    elif r==3:
        letter="#"
    elif r==4:
        letter="$"
    elif r==5:
        letter="%"
    elif r==6:
        letter="&"
    return letter
    

def generate_default_pass():
        c1= generate_letter_capital()
        c2= generate_letter_lowercase()
        c3= generate_letter_capital()
        c4= generate_letter_lowercase()
        c5= generate_letter_capital()
        c6= generate_letter_lowercase()
        c7= generate_letter_capital()
        c8= generate_letter_lowercase()
        c9= generate_letter_capital()
        c10= generate_letter_lowercase()
        c11= generate_special()
        c12= generate_number()
        c13= generate_number()
        c14= generate_number()
        c15= generate_number()
        c16= generate_special()
        print("Your default password is")
        print(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16, sep='')


   
        


print("Hello! Lets help you make a randomized password, but first, answer a few simple questions!")
type=input('Would you like to generate a "Default" or "Custom" password? (Default includes 16 characters, including 5 uppercase letters, 5 lowercase letters, 4 numbers and 2 special characters) ')
type = type.title()
if type=="Custom":
    characters=int(input("How many characters would you like this password to be? (4-20 character limit) "))
    if characters>20 or characters<4:
        print("Invalid input, 4-20 character limit")
    else:
        letters=int(input("How many letters would you like? (Enter 0 if none) "))
        if letters>0:
            capital=int(input("How many capital letters would you like? (Enter 0 if none) "))
        numbers=int(input("How many numbers would you like? (Enter 0 if none) "))
        special=int(input("How many special characters would you like? (Enter 0 if none) "))
        if letters+numbers+special!=characters:
            print("Invalid input, characters don't add up. Please try again.")
        else:
            while characters!=0:
                if letters>0:
                    if capital>0:
                        p= generate_letter_capital
                        capital = capital-1
                        letters = letters-1
                    else:
                        p=generate_letter_lowercase
                        letters-1
                elif numbers>0:
                    p=generate_number
                    numbers-1
                elif special>0:
                    p=generate_special
                    special-1
            final_password="none"
            final_password= p +final_password
            characters-1
    print("Your custom password is")
    print(final_password)
elif type=="Default":
    generate_default_pass()
else:
    print('Invalid input, please enter "Default" or "Custom"')