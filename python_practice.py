"""
Python Practice
Beginner Python exercises and algorithms.
"""

import math
import secrets
import string


# 1. Numbers from 1 to 100
print("1 TASK")
for number in range(1, 101):
    print(number)


# 2. Even numbers from 1 to 50
print("\n2 TASK")
for number in range(1, 51):
    if number % 2 == 0:
        print(number)


# 3. Sum from 1 to n using while
print("\n3 TASK")
n = 5
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print(total)


# 4. FizzBuzz
print("\n4 TASK")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 5. Check if number is even
print("\n5 TASK")

def is_even(number):
    return number % 2 == 0


print(is_even(5))
print(is_even(10))


# 6. Factorial
print("\n6 TASK")

def factorial(number):
    return math.factorial(number)


print(factorial(5))


# 7. Fibonacci number
print("\n7 TASK")

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))


# 8. Max, min, average
print("\n8 TASK")

numbers = [5, 2, 9, 1, 7]

print("Max:", max(numbers))
print("Min:", min(numbers))
print("Average:", sum(numbers) / len(numbers))


# 9. Reverse list without reverse()
print("\n9 TASK")

numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]

print(reversed_list)


# 10. Remove duplicates
print("\n10 TASK")

my_list = ["a", "b", "c", "c", "b"]
unique_list = list(dict.fromkeys(my_list))

print(unique_list)


# 11. Second largest element
print("\n11 TASK")

numbers = [5, 2, 9, 1, 7]
largest = max(numbers)

numbers.remove(largest)

print(max(numbers))


# 12. Merge two lists into dictionary
print("\n12 TASK")

keys = ["a", "b", "c"]
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)


# 13. Count letters in string
print("\n13 TASK")

text = "hello"
count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

print(count)


# 14. Most frequent word
print("\n14 TASK")

text = "I love sport sport"
words = text.split()

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

most_common = max(count, key=count.get)

print(most_common)


# 15. Anagram check
print("\n15 TASK")

a = "listen"
b = "silent"

print(sorted(a) == sorted(b))


# 16. Count vowels
print("\n16 TASK")

text = "I love spaghetti".lower()
vowels = "aeiouy"

count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)


# 17. Palindrome check
print("\n17 TASK")

text = "radar"

print(text == text[::-1])


# 18. Find duplicates
print("\n18 TASK")

words = ["apple", "apple", "banana", "onion"]

count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

duplicates = [word for word, freq in count.items() if freq > 1]

print(duplicates)


# 19. Count unique characters
print("\n19 TASK")

text = "I love spaghetti"

unique = set(text.lower().replace(" ", ""))

print(len(unique))


# 20. Set operations
print("\n20 TASK")

a = {"apple", "banana", "orange"}
b = {"banana", "kiwi", "apple"}

print("banana" in a)
print(a & b)
print(a - b)


# 21. Histogram
print("\n21 TASK")

values = [3, 1, 5]

for value in values:
    print("*" * value)


# 22. Password generator
print("\n22 TASK")

length = 12

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(
    secrets.choice(characters) for _ in range(length)
)

print(password)