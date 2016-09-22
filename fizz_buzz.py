# 1) Write a function "def fizzbuzz(fizz_number, buzz_number):" that prints the numbers from 1 to 100. 
# But for multiples of "fizz_number" print "Fizz" instead of the number and for the multiples of "buzz_number" print "Buzz". 
# For numbers which are multiples of both fizz_number and buzz_number print "FizzBuzz".
#
# - The output should be one line only, without a new line at the end
# - Each number or word should be separated by a space
#
# Example: fizzbuzz(3, 7)
# 1 2 Fizz 4 5 Fizz Buzz 8 Fizz 10 11 Fizz 13 Buzz Fizz 16 17 Fizz 19 20 FizzBuzz 22 23 Fizz 25 26 Fizz Buzz 29 Fizz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz 40 41 FizzBuzz 43 44 Fizz 46 47 Fizz Buzz 50 Fizz 52 53 Fizz 55 Buzz Fizz 58 59 Fizz 61 62 FizzBuzz 64 65 Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizz 76 Buzz Fizz 79 80 Fizz 82 83 FizzBuzz 85 86 Fizz 88 89 Fizz Buzz 92 Fizz 94 95 Fizz 97 Buzz Fizz 100

def fizzbuzz(fizz_number, buzz_number):
    for i in range(1, 101):
        if i % fizz_number == 0 and i % buzz_number == 0:
            print "FizzBuzz",
        elif i % fizz_number == 0:
            print "Fizz",
        elif i % buzz_number == 0:
            print "Buzz",
        else:
            print i,

if __name__ == "__main__":
    fizzbuzz(3, 7)