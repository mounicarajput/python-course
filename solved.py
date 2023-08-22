#Write a Python function that takes a list of numbers as input
# and returns the sum of all the numbers in the list.

def list(num_list):
    sum=0
    for i in num_list:
        sum=sum+i
    return sum
num_list=[1,3,2]
result=list(num_list)
print(result)


def sum_list(list):
    total=0
    for i in list:
        total=total+i
    return total
print(sum_list([2,4,5]))


#Write a Python function that takes a string as input and returns
# the reverse of that string. For example, if the input is "Hello, World!",
# the function should return "!dlroW ,olleH".

def reverse(string):
    a=""
    for i in string:
        a=i+a
    return a
print(reverse("mona"))

#Write a Python function that takes a list of integers as input and returns a
# new list containing only the even numbers from the input list. For example,
# if the input list is [1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].

def fun(int_list):
    new_list=[]
    for i in int_list:
        if i%2==0:
            new_list.append(i)
    return new_list

print(fun([1,2,4,8,7]))


#Write a Python function that takes a string as input and
# returns the count of each unique character in the string as a dictionary.
# For example, if the input is "hello", the function should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

def count_unique_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] = char_count[char] +1
        else:
            char_count[char] = 1
    return char_count

print(count_unique_characters("hello"))


#Write a Python function that takes a list of strings as input and
# returns a new list containing only the strings that start with the
# letter 'A' (case-insensitive). For example, if the input list is
# ['apple', 'banana', 'Avocado', 'orange'], the function should return ['apple', 'Avocado'].

def fun(string):
    new_list=[]
    for i in string:
        if i[0].lower() =="a":
            new_list.append(i)
    return new_list

print(fun(["apple","bb","Apple"]))

#Write a Python function that takes a string as input and returns
# the reverse of the string. For example,
# if the input is "hello", the function should return "olleh".

def fun(string):
    reverse=''
    for i in string:
        reverse=i[-1]+reverse
    return reverse

print(fun("hello"))


#Write a Python function that takes a list of
# integers as input and returns a new list containing
# only the even numbers from the original list.
# For example, if the input list is [1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].


def fun(int_list):
    new_list=[]
    for i in int_list:
        if i%2==0:
            new_list.append(i)
    return new_list

print(fun([2,6,7]))


#Write a Python function that takes a string as input and
# checks if it is a palindrome. A palindrome is a word, phrase,
# number, or other sequence of characters that reads the same forward
# and backward. The function should return True if the string is a
# palindrome and False otherwise. For example, if the input
# string is "madam", the function should return True,
# but if the input string is "hello", the function should return False.



def palindrome(string):
    string=string.lower().replace(" ","")

    if string == string[::-1]:
        return True
    else:
        return False
string="ma     dam"
print(palindrome(string))


#Write a Python function that takes a list of integers
# as input and returns the product of all the numbers in the
# list. For example, if the input list is [2, 3, 4],
# the function should return 24 (2 * 3 * 4).


def multiple(list):
    a=1
    for i in list:
        a =a*i
    return a

list=[2,3,4]
print(multiple(list))

#Write a Python function that takes a list of integers as
# input and returns a new list that contains only the unique
# elements from the original list. The order of the elements in
# the new list should be the same as in the original list.
# For example, if the input list is [1, 2, 2, 3, 3, 4, 5, 5], the function should return [1, 2, 3, 4, 5].


def num(list):
    new_list=[]
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

list=[1, 2, 2,2, 3, 3, 4, 5, 5,6,6,6]
print(num(list))


#Write a Python function that takes a list of integers as
# input and returns a new list where each element is multiplied by 2.
# For example, if the input list is [1, 2, 3, 4], the function should return [2, 4, 6, 8].

def num(list):
    a=[]
    for i in list:
        b=i*2
        a.append(b)
    return a

list=[1, 2, 3, 4]
print(num(list))


#Write a Python function that takes a list of strings as input and
# returns a new list where each string is reversed. For example, if
# the input list is ["hello", "world", "python"],
# the function should return ["olleh", "dlrow", "nohtyp"].


def reverse_list(list):
    a=[]
    for i in list:
        b=i[::-1]
        a.append(b)
    return a

list=["hello", "world", "python"]

print(reverse_list(list))


#Write a Python function that takes a string as input
# and returns the number of vowels (a, e, i, o, u) in the string.
# For example, if the input string is "hello world", the function should return 3.


def vowels(string):
    a=0
    char='aeiouAEIOU'
    for i in string:
        if i in char:
            a=a+1
    return a

string="hello world"
print(vowels(string))




