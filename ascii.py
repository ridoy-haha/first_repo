def ascii (char):
    if len(char) !=1 :
        return "Error! Input single character."
    else:
        return ord(char)
    
char=input("Enter the character: ")
ascii_code=ascii(char)
print(f"{char} ascii code is {ascii_code}")
binary = bin(ascii_code)[2:]
print(f"Binary no of the {char} is {binary}")