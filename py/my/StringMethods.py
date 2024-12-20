name = ("Enter your name: ")
myList = ['a',1, True]

# append.() adds new variable to the end of the string
newlist1 = myList.append("new string element")

# extend() adds ANOTHER list to a list
list1 = ['a', 'b', 'c', 2, 3, 4, 6]
newlist2 = myList.extend(list1)

# len() returns the number of characters in a string.
length = len(name)

# capitalize() converts the 1st char of a string to uppercase and makes all other characters lowercase.
size = name.capitalize()

#returns True if all characters in the string are alphanumeric (either alphabets or numbers).
alphanumeric = name.isalnum()

#True if all characters in the string are alphabets.
alphabetic = name.isalpha()

# True if all characters in the string are digits.
digit = name.isdigit()

# returns True if all characters in the string are uppercase.
result = name.isupper()

#returns True if all characters in the string are lowercase.
result = name.islower()

# converts all characters in a string to uppercase.
result = name.upper()

# The lower() function converts all characters in a string to lowercase.
result = name.lower()

#   pop() removes last element from list
list1.pop()

#   insert () replaces position of list with a new element
list1.insert(4, "four")

#   remove() removes the 1st occurence of a condition
list1.remove("four")

#   sort() sorts the list in ascending order. Can specify order using conditions
list1.sort()

# reverse() reverses the list
list1.reverse()


#* the strip() function removes all leading and ending instances of parameter. 
# defaults to whitespaces
# my_name = "Antonio and Anna"
# my_name = my_name.strip("Aa") #? <--  can replace many chars at once
# print (my_name)

#* the count() myfunction returns the number of characters that meet the condition
#phone_number = input("enter ur phone number: ")
# check to see how much dashes in phone num:
#dashes = phone_number.count("-")

#* removes all dashes in phone number by replacing with empty string
#clean_num = phone_number.replace("-"," ● ")
#print(clean_num)


#* You can also assign replaced values to the str directly
#phone_number = phone_number.replace(" ● ", "--")
#print(phone_number)


#* Randomizing strings using shuffle 
# import random
# numbers = ["a","b","c"]
# random.shuffle(numbers)
# print (numbers)


#*  join() inputs a parameter between each index of a list
str1 = "abcdefg"
str1 = "-".join(str1) #OR 
str2 = "-".join(str1)
print(str1)
print(str2)


#* map() takes in a func and a list 
#* and produces a list containing the result of applying 
#* said function to each element of the list

# map.(lambda x: n**2, [1,2,3,4])

def my_map(f, lst):
    if list == []:  return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])
    
#? using 


