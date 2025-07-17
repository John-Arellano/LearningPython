#List
mylist1 = [1, 2, 3, 4, 5]
mylist1 [3:]
print(mylist1) 
print(mylist1[3:])  # Output: [4, 5]

mylist2 = list(range(50))
print(mylist2)  # Output: [0, 1, 2, ..., 49]    
mylist1.insert(2, "100")  
print(mylist1)  # Output: [1, 2, 3, 4, 5, ..., 100]

#tuple and sets
myset = {1, 2, 3, 4, 5}
print(myset)  # Output: {1, 2, 3, 4, 5}
myset.add(6)
print(myset)  # Output: {1, 2, 3, 4, 5, 6}
myset.remove(3)
print(myset)  # Output: {1, 2, 4, 5, 6}
myset.add(3)  # Adding back the removed element

myset = set([1, 2, 3, 4, 5])
print(myset)  # Output: {1, 2, 3, 4, 5}

print(1 in myset) # Output: True

#Dictionaries

mydict = {"name": "Alice", "age": 30, "city": "New York"}   
print(mydict["name"])

mydict["profession"] = "engineer"
print(mydict["profession"])  # Output: engineer
mydict["age"] = 31
print(mydict["age"])  # Output: 31
mydict["sibilings"] = 4
print(mydict["sibilings"])  # Output: 4


#List Comprehensions
miLista = [1,2,3,4,5,6]
miLista.append(7)
miListaCuadrados = [x**2 for x in miLista]
print(miListaCuadrados)  # Output: [1, 4, 9, 16, 25]
otraLista = list(range(100))
filteredList = [item for item in otraLista if item % 10 == 0] 
print(filteredList)  # Output: [0, 10, 20, ..., 90]

# Encoding ASCII art 

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

def encodeString(stringVal):

    encodedList = []
    prevChar = stringVal[0]
    count = 0

    for char in stringVal:
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count += 1
        
    encodedList.append((prevChar, count))  # Append the last character and its count
    
    return encodedList


def decodeString(encodedList):
    decoded = ""
    for char in encodedList:
        decodedStr += char[0] * char[1]  
    return decodedStr