#!/usr/bin/env python3

def happy_new_year():
   
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")    

def square_integers(int_list):
    return [integer * integer for integer in int_list ]

def fizzbuzz():
     for j in range(1, 101):
        if j % 3 == 0 and j % 5 == 0:
            print("FizzBuzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(j)
        
           
             
              