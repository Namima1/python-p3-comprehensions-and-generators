#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 ==0]

#num for num in num_list: Loops through each element (num) in the list num_list.
#if num % 2 == 0: Filters the numbers that are divisible by 2 (even numbers).

print(return_evens([0, 1, 3, 5, 7, 8, 9]))



def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
