""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
def lines_from_file(path):
    file=open(path)
    assert readable(file)==True
    str_lst=readlines(file)
    for i in range(len(str_lst)):
        str_lst[i]=strip(str_lst[i])
    close(file)
    return str_lst
def new_sample(path,i):
    str_lst=lines_from_file(path)
    return str_lst[i]
def analyze(sample_paragraph,typed_string,start_time,end_time):
    seconds=end_time-start_time
    minutes=seconds/60
    words=split(sample_paragraph)
    typed_words=split(typed_string)
    total_typed=len(typed_words)
    total_words=len(words)
    words_per_minutes=(len(typed_string)/5)/minutes
    correct_words=0
    accuracy_percentage = 0
    if total_typed<=1:
        if typed_words[0]!=words[0]:
            accuracy_percentage=0
    elif total_typed<=total_words:
        for i in range(total_typed):
            if typed_words[i]==words[i]:
                correct_words+=1
        accuracy_percentage=correct_words/typed_words
    elif total_typed>total_words:
        for i in range(total_typed):
            if typed_words[i]==words[i]:
                correct_words+=1
        accuracy_percentage = correct_words / total_words
    lst=[words_per_minutes,accuracy_percentage]
    return lst
def pig_latin(words):
    if words[0] in 'aeiou':
        return words+'way'
    else:
        for i in range(len(words)):
            if words[i] in 'aeiou':
                return words[i:]+words[:i]+'ay'
        return words+'ay'
def autocorrect(user_input,words_list,score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list,key=lambda x:score_function(user_input,x))
def swap_function(str1,str2):
    ans=0
    if str1=='' or str2=='':
        return ans
    else:
        if str1[0]==str2[0]:
            ans+=1
        return (str1-str1[0],str2-str2[0])

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1=='' or word2=='' or word1 in word2 or word2 in word1: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return abs(len(word1)-len(word2))
        # END Q6

    elif word1[0]==word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return score_function(word1[1:],word2[1:])
        # END Q6
    
    else:
        add_char = 1+score_function(word1,word2[1:])  # Fill in these lines
        remove_char = 1+score_function(word1[1:],word2)
        substitute_char = 1+score_function(word1[1:],word2[1:])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return min(add_char,remove_char.substitute_char)
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1,word2):
    if word1=='' or word2=='' or word2 in word1 or word1 in word2:
        return abs(len(word1)-len(word2))
    elif word1[0]==word2[0]:
        return score_function(word1[1:],word2[1:])
    else:
        add_char = 1+score_function(word1,word2[1:])
        remove_char = 1+score_function(word1[1:],word2)
        substitute_char = KEY_DISTANCES[word1[0],word2[0]]+score_function(word1[1:],word2[1:])
        return min(add_char, remove_char.substitute_char)
def memoize(fn):
    d=dict()
    def memoize_fn(*args):
        if args in d:
            return d[args]
        result=fn(*args)
        d[args]=result
        return result
    return memoize_fn
def score_function_final(word1,word2):
    if word1=='' or word2=='' or word2 in word1 or word1 in word2:
        return abs(len(word1)-len(word2))
    elif word1[0]==word2[0]:
        return score_function(word1[1:],word2[1:])
    else:
        add_char = 1+score_function(word1,word2[1:])
        remove_char = 1+score_function(word1[1:],word2)
        substitute_char = KEY_DISTANCES[word1[0],word2[0]]+score_function(word1[1:],word2[1:])
        return min(add_char, remove_char.substitute_char)

score_function_final=memoize(score_funciton_final)
# END Q7-8
