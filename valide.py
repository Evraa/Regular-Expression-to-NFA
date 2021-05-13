import re
from collections import deque
 
def split(word):
    return list(word)
    
def rb_dont_match(list_of_ch):
    '''
        if () dont match, return True
    '''
    rb_stack = deque()
    for ch in list_of_ch:
        if ch == "(":
            rb_stack.append("(")
            # print (rb_stack)
        elif ch == ")":
            if len(rb_stack)==0: return True
            rb_stack.popleft()
            # print (rb_stack)
    
    if len(rb_stack)>=1: return True
    return False


def doublers_found(txt):
    '''
        check for these patterns |* *| || ** ..etc.
    '''
    res = re.finditer("[|*()]", txt)
    
    prev = -1
    prev_ch = None
    for i,r in enumerate(res):
        #check for start with (
        if r.group() == '(' and i == 0:
            prev = r.start()
            prev_ch = r.group()
            continue

        ind = r.start()
        #if two concecutives are notations..check for valid cases or terminate
        if ind-prev <= 1: 
            valid = False
            #check for valid cases
            current_ch = r.group()
            if prev_ch == '*' and current_ch ==")":
                valid = True
            if prev_ch == ')' and current_ch =="*":
                valid = True
            if prev_ch == '*' and current_ch =="|":
                valid = True
            if prev_ch == '*' and current_ch =="(":
                valid = True
            if prev_ch == '|' and current_ch =="(":
                valid = True
            if prev_ch == ')' and current_ch =="|":
                valid = True
            if prev_ch == '(' and current_ch =="(":
                valid = True
            if prev_ch == ')' and current_ch ==")":
                valid = True
            if prev_ch == ')' and current_ch =="(":
                valid = True
            if not valid: return True


        prev = ind
        prev_ch = r.group()
        

    return False




def validate(txt):
    '''
    Validation function, consist of several parts:
        + No digits
        + () lengths mathces
        + () close to eachothers
    '''

    #remove spaces
    txt = txt.replace(" ","")
    #empty?
    if txt == "": return False

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

    #check for end |
    if list_of_ch[-1] == "|": return False
    
    return True








if __name__ == "__main__":
    txt = str(input("Insert RE:\n"))
    print(validate(txt))