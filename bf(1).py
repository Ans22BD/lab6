#1
import math
import time

def multiply_list(numbers):
    return math.prod(numbers)


nums = [1, 2, 3, 4]
result = multiply_list(nums)
print("Product of list elements:", result)


#2
def count_upper_lower(s):
    
    upper_count = sum(map(str.isupper, s)) 
    lower_count = sum(map(str.islower, s))  
    return upper_count, lower_count


input_string = input()

upper_count, lower_count = count_upper_lower(input_string)

print(f"Прописные буквы: {upper_count}")
print(f"Строчные буквы: {lower_count}")

#3
def palindrome(s):
    string = ''.join(reversed(s))
    return string


s = input("Напиши слово для проверки палиндрома: ")

string = palindrome(s)
if string == s:
    print("Является палиндромом")
else:
    print("Не является палиндромом")


#4

s = int(input("Square root of: "))
time_s = int(input("After miliseconds: "))

r = s**(1/2)

time.sleep(time_s/1000)

print(f"Square root of {s} after {time_s} miliseconds is {r}")

#5
def all_elements_true(t):
    return all(t)


the_list = [1, 0, 3, 4]

if all_elements_true(the_list):
    print("All elements true")
else:
    print("All elements not true")



