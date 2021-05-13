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


def doublers_found(txt):
    '''
        check for these patterns |* *| || ** ..etc.
    '''
    txt = txt.replace(" ","")
    res = re.finditer("[|*]", txt)
    
    prev = -1
    for i,r in enumerate(res):
        ind = r.start()
        if ind-prev <= 1: return True
        prev = ind
    
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
    
    list_of_ch = split(txt)
    #check for ()
    if rb_dont_match(list_of_ch): return False
    
    #check for double notations | *
    if doublers_found(txt): return False
    

    return True








if __name__ == "__main__":
    txt = str(input("Insert RE:\n"))
    print(validate(txt))