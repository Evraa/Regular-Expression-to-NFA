import enum
import re
from typing import NewType
import valide
from collections import deque


def split(word):
    return list(word)

def join_str(list_of_ch):
    res =""
    for ch in list_of_ch: res+= ch
    return res

def parse_asterisk(list_of_ch):
    prev_ch = None
    new_list = []
    close_it = False
    for i,ch in enumerate(list_of_ch):

        if ch =="*" and prev_ch != ")" :
            #for sure it's a character
            new_list.insert(-1,"(")
            close_it = True

        #append the char
        if close_it:
            close_it = False
            new_list.append('*')
            new_list.append(")")
            
        else:
            new_list.append(ch)

        prev_ch = ch

    return new_list
        
def parse_consecutive(txt, list_of_ch):
    res = re.finditer("[|*()]", txt)
    notations_index = [r.start() for r in res]
    
    #no notations at all
    # if len(notations_index) == 0:
    #     list_of_ch.insert(0,'(')
    #     list_of_ch.append(')')

    # max_range = max(notations_index)+1
    prev_index = -1
    prev_ch = None
    additions = 0
    for i in notations_index:
        index = i + (2*additions)

        if index - prev_index > 2 and not (prev_ch=="(" and list_of_ch[index]==")"):
            if prev_index == -1:
                list_of_ch.insert(0,'(')
            else:
                list_of_ch.insert(prev_index+1,'(')
            list_of_ch.insert(index+1,')')
            additions += 1
        
        index = i + (2*additions)
        prev_index = index
        prev_ch = list_of_ch[prev_index]

        
    return list_of_ch



def remove_repeated_brackets(txt):
    rb_stack = deque()
    pairs = []
    for i,ch in enumerate(txt):
        if ch == "(":
            rb_stack.append([0,i])
        elif ch == ")":
            my_bracket = rb_stack.pop()
            pairs.append([my_bracket[1], i])
    
    
    last = pairs[-1]
    truncation_level = 0
    for i,p in enumerate(reversed(pairs)):
        if i == 0: continue

        if abs(p[0] - last[0]) == 1 and abs(p[1] - last[1]) == 1:
            truncation_level += 1
        else:
            break
        
        last = p
    
    new_txt = ""
    L = len(txt)
        
    for i, ch in enumerate(txt):
        if i < truncation_level or i>=L-truncation_level: continue
        new_txt += ch

    return new_txt

def parse(txt):
    #remove spaces
    txt = txt.replace(" ","")
    txt = "("+txt+")"
    list_of_ch = split(txt)
    list_of_ch = parse_asterisk(list_of_ch)
    txt = join_str(list_of_ch)
    list_of_ch = parse_consecutive(txt, list_of_ch)
    txt = join_str(list_of_ch)
    txt = remove_repeated_brackets(txt)

    return (txt)


# if __name__ == "__main__":
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    # txt = "((((a)|(B))))"
    # parse(txt)
    