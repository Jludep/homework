"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import re
import collections

def get_longest_diverse_words(file_path: str) -> List[str]:

    with open(file_path, "r") as file:
        long_words = {'a': 1}     #{'word': *amount of unique sym* }

        for line in file:
            line = line.encode('utf-8').decode('unicode-escape')
            words = re.findall(r'\b[A-Za-zäöüÄÖÜß]+\b', line) #finds and seperates all german words

            for word in words:
                uniq_amount = len(set(word)) #value of unique sym in current word
                min_uniq_dict = min(long_words.values()) #minimal value of uniq sym in dictionary
                if len(long_words) <= 10: #just to fill first 10 values of dict
                    long_words[word]=uniq_amount
                elif uniq_amount > min_uniq_dict:
                    #so, now we need to replace a element in dict which has a minimal value of uniq sym with a new element
                    #and cuz python dictionary type cant do that, we must create a new same dict with new element instead of old

                    long_words = {key:val for key, val in long_words.items() if val != min_uniq_dict}
                    long_words[word]=uniq_amount

    return long_words



def get_rarest_char(file_path: str) -> str:
    with open(file_path, "r") as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        # counter is useful class which return a dict with all symbols in text (keys) and amount of this symbols in text (values)
        counter_dict = collections.Counter(text)
        rapest = min(counter_dict.values()) #all we need to do is just find minimal value of dictionary
        return (counter_dict.keys())[list(counter_dict.values()).index(rapest)]
        # btw it returns only a sym, not amount how much this sym appears in the text
        # this is because in our task we need return only a sym


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r") as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        punctuation_chars = re.findall(r'[^\w\s]', text)
        punctuation_chars_dict = collections.Counter(punctuation_chars) #like in previous task, we use Counter
        return punctuation_chars_dict


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r") as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        non_ascii = re.findall(r'[^\x00-\x7F]', text) #range of ascii within 0-128 in dec, or x00-x7F in hex. regex is power.
        non_ascii_dict = collections.Counter(non_ascii)
        return sum(non_ascii_dict.values())


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r") as file:
        text = file.read().encode('utf-8').decode('unicode-escape')
        non_ascii = re.findall(r'[^\x00-\x7F]', text)
        non_ascii_dict = collections.Counter(non_ascii)
        common = max(non_ascii_dict.values())
        return list(non_ascii_dict.keys())[list(non_ascii_dict.values()).index(common)]