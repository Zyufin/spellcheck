#!/usr/bin/env python
from itertools import product, compress, combinations, chain
import sys

class TwitchDictionary(object):
    def __init__(self):
        self.dictionary = set()
        self.max_length = 0
        self.fill_dictionary()

    def is_correct(self, word):
        if word in self.dictionary:
            return True
        else:
            return False

    def check_variations(self, word):
        for variation in word_variations(word):
            if self.is_correct(variation):
                return variation
        return 'NO SUGGESTION'

    def spellcheck(self, word):
        word = word.lower()
        if self.is_correct(word):
            return word
        else:
            return self.check_variations(word)

    def fill_dictionary(self):
        dictionary_file = open('/usr/share/dict/words', 'rU')
        add_entry = self.dictionary.add
        for line in dictionary_file:
            entry = line.strip().lower()
            add_entry(entry)
            entry_length = len(entry)
            if entry_length > self.max_length:
                self.max_length = entry_length
        dictionary_file.close()

def build_selectors(char_list, unselections):
    selectors = {}
    for i in range(len(char_list)):
        if i in unselections:
            selectors[i] = 0
        else:
            selectors[i] = 1
    return selectors

def catalog_repeats(char_list):
    repeats = set()
    for i in range(len(char_list) - 1):
        if char_list[i + 1] == char_list[i]:
            repeats.add(i + 1)
    return repeats

def power_set(s):
    cardinality = len(s)
    for m in range(cardinality + 1):
        for combo in chain(combinations(s, m)):
            yield combo

def repitition_variants(word):
    char_list = list(word)
    repeats = catalog_repeats(char_list)
    for subset in power_set(repeats):
        selectors = build_selectors(char_list, subset)
        variant_char_list = []
        for i in range(len(char_list)):
            if selectors[i] == 1:
                variant_char_list.append(char_list[i])
        variant = ''.join([char for char in variant_char_list])
        yield variant

def vowel_variants(word):
    char_list = list(word)
    yield ''.join(char_list)
    vowels = set(['a','e','i','o','u','y'])
    vowel_map = []
    variant_word = ''
    for i in range(len(char_list)):
        char = char_list[i]
        if char in vowels:
            vowel_map.append(i)
    vowel_combinations = product(vowels, repeat=len(vowel_map))
    variant_char_list = char_list
    for vowel_combo in vowel_combinations:
        for i in range(len(vowel_map)):
            vowel_index = vowel_map[i]
            variant_char_list[vowel_index] = vowel_combo[i]
            variant_word = ''.join(variant_char_list)
        yield variant_word

def word_variations(word):
    for v_variant in vowel_variants(word):
        yield v_variant
    for rep_variant in repitition_variants(word):
        for v_variant in vowel_variants(rep_variant):
            yield v_variant

def main():
    dictionary = TwitchDictionary()
    while(True):
        print(dictionary.spellcheck(input('>')))

if __name__ == '__main__':
    main()
