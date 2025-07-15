import math
# Basic Data Types in Python

# Ints and floats # are numeric data types in Python.   

print(20 / 4)
print(20 / 4.0)
print(4 ** 4.0)
print(int(8.99999909090))   
print(round(14/3, 5))    

# Other types of numbers 

print(int('100', base=2))  # Convert binary string to int   
print(int('100', base=16))  # Convert hexadecimal string to int
print(int('100', base=8))   # Convert octal string to int  
print(float('3.14'))  # Convert string to float  
print(1.2-1.0)  # Subtract two floats
print(1.0 - 1)  # Subtract float and int
print(1 - 1.0)  # Subtract int and float

# Boolean values


print(bool(0))  # False
print(bool(1))  # True  
print(bool(-1))  # True
print(bool(0.0))  # False
print(bool(0.1))  # True
print(bool(''))  # False
print(bool(' '))  # True
print(bool([]))  # False
print(bool(1j))  # True  

myList = [1, 2, 3, 4]
if bool(myList):
    print("My List has some values!") 



weatherIsNice = False
haveUmbrella = True
if not (weatherIsNice or haveUmbrella):
    print("Stay inside!")
else:
    print("Go for a walk!")   

# Strings 

name = "My Name is John Arellano"
print(name[0])  # First character
print(name[11:])   # From index 11 to the end
print(name[11:16])  # From index 11 to 16
print(len(name))  # Length of the string
print(name.lower())  # Convert to lowercase
print(name.upper())  # Convert to uppercase
print(name.replace("John", "Jane"))  # Replace substring

print('My number is: '+str(5))  # Concatenate string with number
print('My number is: {}'.format(5))  # Format string with number
print(f'My number is: {5}')  # f-string formatting
print(f'Pi is: {math.pi:.2f}')  # Formatted string with math constant

#Bytes
print(bytes(4))  # Create bytes object of length 4      
print(bytes([65, 66, 67]))  # Create bytes object from list of integers
print(bytes(':)', 'utf-8'))  # Create bytes object from string with encoding

#convert hexadecimal to decimal

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Function to convert hexadecimal string to decimal integer
def hexToDec(hexNum): 

   # NumHex = hexNum.upper()  # Convert to uppercase for consistency
    decimalValue = 0
    for i, digit in enumerate(reversed(hexNum)):
        decimalValue += hexNumbers[digit] * (16 ** i)
    return decimalValue

def main():
    print(hexToDec('AAAAB'))  # Example usage
    print(hexToDec('FF'))  # Example usage
    print(hexToDec('10'))  # Example usage
    print(hexToDec('0'))  # Example usage


if __name__ == "__main__":
    main()       

