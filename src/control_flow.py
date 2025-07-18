from datetime import datetime

#if else

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    else:
        if n % 3 == 0:
            print("Fizz")
        else:
            if n % 5 == 0:
                print("Buzz")
            else:
                print(n)

for n in range(1, 101):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n  % 5 == 0:
        print("Buzz")
    else:
        print(n)


# while Loops

print(datetime.now().second)

wait_until = (datetime.now().second + 2) % 60
while datetime.now().second != wait_until:
    pass
print("Waited until second:", wait_until)

while True:
   if datetime.now().second == wait_until:
       print
       break
   
# for

myList = [1, 2, 3, 4, 5, 6]
for item in myList:
    print(item)
   

animalLookup = {
    "a": ['aardvark', 'antelope'],
    "b": ["bear"],
    "c": ['cat'],
    "d": ['dog'],
    }
for letter, animals in animalLookup.items():
    pass

for letter, animals in animalLookup.items():
    if len(animals) > 1:
        continue
    print(f'Only one animal')

    def allPrimesUpTo(num):
        """Returns a list of all prime numbers up to num."""
        primes = []
        for n in range(2, num + 1):
            is_prime = True
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
        return primes

print(allPrimesUpTo(10))