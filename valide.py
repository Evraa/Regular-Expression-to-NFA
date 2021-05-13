import re
from collections import deque
 
def split(word):
    word = word.replace(" ","")
    return list(word)
    
def rb_dont_match(list_of_ch):
    '''
        if () dont match, return True
    '''
    rb_stack = deque()
    for ch in list_of_ch:
        if ch == "(":
            rb_stack.append("(")
            print (rb_stack)
        if ch == ")":
            if len(rb_stack)==0: return True
            rb_stack.popleft()
            print (rb_stack)
    
    if len(rb_stack)>=1: return True
    return False

def validate(txt):
    '''
    Validation function, consist of several parts:
        + No digits
        + () lengths mathces
        + () close to eachothers
    '''

    #check for digits
    if re.search(r"\d",txt): return False

    #find all (
    left_rb = re.findall(r"\(",txt)
    #find all )
    right_rb = re.findall(r"\)",txt)
    #check for length
    if len(left_rb) != len(right_rb): return False
    
    #check for ()
    if rb_dont_match(split(txt)): return False
    

    return True








if __name__ == "__main__":
    txt = str(input("Insert RE:\n"))
    print(validate(txt))