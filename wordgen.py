#!/usr/bin/env python
import sys

sys.path.append('~/Downloads')

import spellcheck as spellchecker
import random

def gen_word(word):
    vowels = set(['a','e','i','o','u','y'])
    char_list = list(word)
    length = len(char_list)
    p = 1.0 / length
    for i in range(length):
        if random.random() <= p:
            if char_list[i] in vowels:
                char_list[i] = random.sample(vowels, 1)[0]
            else:
                char_list.insert(i, char_list[i])
    return ''.join(char_list)

def main():
    dictionary_file = open('C:\Documents and Settings\Owner\Desktop\impstuff\words', 'rU')
    dictionary = spellchecker.TwitchDictionary()
    for line in dictionary_file:
        correct_word = line.strip()
        mangled_word = gen_word(correct_word)
        suggestion = dictionary.spellcheck(mangled_word)
        if suggestion == 'NO SUGGESTION':
            print("You read: ", mangled_word)
            print("You should have suggested:  ",correct_word", but didn't.")
            print("Ya dun goofed!!!  Yo program don' work.  Shuttin down, Cap'n.")
            quit()
    print("Mission accomplished")


if __name__ == '__main__':
    main()
