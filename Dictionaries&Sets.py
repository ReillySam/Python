# =============================== Exercise 1 ===============================
D = {"a" : 3, "x" : 7, "r": 5}

def specifically_key_values(D):
    ''' return key, values specifically using single methods'''
    print(D["x"]) # returns value
    print(list(D.keys())[list(D.values()).index(7)]) # returns key

specifically_key_values(D)


# =============================== Exercise 2 ===============================
my_dict = {'a' : 15, 'b' : 35, 'c' : 20}

def print_key_values(my_dict):
    ''' print all keys'''
    for key in my_dict:
        print(key)
    print(my_dict.keys(),'\n')

    '''print all values'''
    for key in my_dict:
        print(my_dict[key])
    print(my_dict.values(),'\n')

    '''print all key, values of dict'''
    for key, values in my_dict.items():
        print(key, ':', values,)
    print()
    #print((k, v) for (k, v) in my_dict.items()) # doesn't work

    '''print keys in order'''
    key_list = []
    for key in my_dict.keys():  # print keys in order
        key_list.append(key)
        key_list.sort()
    print(key_list, '\n')

    '''print values in order'''
    value_list = []
    for v in my_dict.values():  # print values in order
        value_list.append(v)
        value_list.sort()
    print(value_list, '\n')

    key_value_list = []
    y = ''
    for i in my_dict.items():
        key_value_list.append(i)
        y = sorted(key_value_list, key= lambda key_value_list: key_value_list[1])
    print(y)

print_key_values(my_dict)

# =============================== Exercise 3 ===============================
# Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x)

def my_dict(n):
    my_dict = {}
    for i in range(1, n+1):
        my_dict[i] = i*i
    for k,v in my_dict.items():
        print(k,v)

my_dict(5)

# =============================== Exercise 4 ===============================
#  Write a Python program to combine these two dictionaries adding values for
# common keys.

def combine_dict(d1,d2):
    d3 = {}
    for key, value in d1.items():
        for keys, values in d2.items():
            if keys == key:
                d3[keys] = values + value
    d3[key] = value
    d3[keys] = values
    print(d3)


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 800, 'b': 250, 'd':400}

combine_dict(d1,d2)

# =============================== Exercise 5 ===============================
# Use a dictionary to create a program that prompts for an integer and prints out
# the integer using words. For example: 138 will print “one three eight”

def int_word_change(num):
    my_dict = {'0':'Zero', '1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six',
               '7':'Seven', '8':'Eight', '9':'Nine'}
    num_str = str(num)
    int_to_word = ''
    for i in num_str:
        for key in my_dict.keys():
            if i == key:
                int_to_word += my_dict[key]
                int_to_word += ' '

    print(int_to_word)

def int_input():
    num = int(input("Enter an integer: "))
    int_word_change(num)

int_input()

# =============================== Exercise 6 ===============================
# Create a dictionary that maps countries to their capitals. You may start with an
# empty dictionary. Ask the user to input the name of the country and its capital and
# add them to the dictionary. E.g., capitals = {'Argentina':'Buenos
# Aires','France':'Paris', 'US': 'Washington D.C.'} Once the
# dictionary is created, print the capitals in alphabetical order.

def country_cap():
    my_dict = {}
    while True:
        cntry_cap = input("Enter a country and its capital, separated by a ','. "
                          "Press 'q' to exit.")
        if ',' not in cntry_cap:
            print("Please use a ','.")
        if cntry_cap != 'q':
            input_list = list(cntry_cap.split(','))
            my_dict[input_list[0]] = input_list[1]
        else:
            cap_list =[]
            for values in my_dict.values():
                cap_list.append(values)
                cap_list.sort()
            print(cap_list)
            break

country_cap()

# =============================== Exercise 7 ===============================
# Given a string S of lower case characters check whether this string is Heterogram
# or not. A heterogram is a word, phrase, or sentence in which no letter of the alphabet
# occurs more than once. Hint: remember that sets by definition do not have repeated
# elements. So try to somehow use sets to solve the problem. Check whether the
# strings below are Heterograms or not

def heterogram():
    while True:
        s = input("Enter a string to check if it's a Heterogram (type 'q' to quit): ")
        s_lower = s.lower()
        join_s = s_lower.replace(' ', '')
        set_s = set(join_s)
        if s == 'q':
            break
        elif len(join_s) == len(set_s):
            print("This string is a Heterogram")
        else:
            print("This string is not a Heterogram")

heterogram()

# =============================== Exercise 8 ===============================
# Given a string S of lower case characters check whether this string is a Pangram
# or not. Pangram is a sentence using every letter of a given alphabet at least once.
# Check whether the string below is a Pangram or not:

def pangram():
    while True:
            s = input("Enter a string to check if it's a Pangram (type 'q' to quit): ")
            s_lower = s.lower()
            join_s = s_lower.replace(' ','')
            set_s = set(join_s)
            alpha_set = set('abcdefghijklmnopqrstuvwxyz')
            if s == 'q':
                break
            elif list(set_s) == list(alpha_set):
                print("This string is a Pangram.")
            else:
                print("This string is not a Pangram.")

pangram()

# =============================== Exercise 9 ===============================
#  Make a word cloud. A word cloud is a visual representation for text data typically
# used to depict keyword metadata on websites, or to visualize free form text. An
# example is given below:

# don't have text files. Going to try with webscrape soon

import string

def create_dict():

    fo = open("hare_and_tortoise.txt", "r")
    fstop = open("stopwords.txt")
    stopwords = fstop.read().splitlines()

    dict={}
    for line in fo:
        line = line.lower()
        line = line.split()
        ##print(line)
        for w in line:
            if (w in stopwords):
                continue
            w = w.strip(string.punctuation)
            w = w.strip(string.whitespace)
            add_to_dict(w, dict)
    fo.close()
    return dict

def add_to_dict(word, dict):
    for key in dict.keys():
        if key == word:
            dict[key] = dict[key]+1
            return dict
    else:
        dict[word] =1
        return dict

def create_html(dict):
    html = '<!DOCTYPE html>\ <html> <head lang="en"> <meta charset="UTF-8"> <title>Tag Cloud Generator</title>'
    '</head> <body> <div style="text-align: center; width: 15%; vertical-align: middle; font-family: arial;'
    'color: white; background-color:black; border:1px solid black">'
    count = 0
    for key in dict.keys():
        html += '<span style="font-size: '
        html += str(dict[key]*10)
        html += 'px"> '
        html += key
        html += '</span>'
        count += 1
        if count % 4 == 0:
            html += '<br>'

    html += '</div> </body> </html>'
    fo = open("output.html", "w")
    fo.write(html)

## Main
dict = create_dict()
create_html(dict)
