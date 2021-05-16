import valide, parse
from collections import deque
import sys
import copy

class Node:
    def __init__(self, start=False, end=False, left_rb=False, right_rb=False, 
                main_or=False, open_or=False, id=None,opened_to=None) -> None:
        self.start = start
        self.end = end
        self.left_rb=left_rb
        self.right_rb = right_rb
        self.main_or = main_or
        self.open_or = open_or
        self.opened_to = opened_to
        self.id = id
        self.children = []

    def add_child(self, child, char):
        child_state = [child, char]
        self.children.append(child_state)
        return

    def remove_child(self, child_id):
        new_children = []
        for c in self.children:
            if c[0].id != child_id:
                new_children.append(c)

        self.children.clear()
        self.children = copy.deepcopy(new_children)

def init_nodes():
    global i, main_list, eps,first_node
    first_node = Node(id=i, start=True, left_rb=True)
    i+=1
    main_list.append(first_node)
    s1 = Node(id=i)
    i+=1
    main_list.append(s1)
    first_node.add_child(s1, eps)
    # main_list[-1] = s1
    

def print_main_list(short=True):

    global main_list

    for n in main_list:
        if short:
            for c in n.children:
                print (f'Node: {n.id}\t\tto node:{c[0].id}\tchar:{c[1]}')
            if len(n.children) == 0:
                print (f'Node: {n.id}\t\tto node:None\tchar:None')
        else:
            print (f'Node: {n.id}\t\tStart:{n.start}\tEnd:{n.end}\tLeft RB:{n.left_rb}\tRight RB:{n.right_rb}\tMain OR:{n.main_or}\tOpen OR:{n.open_or}\t')

    print ("##########EOF############\n")


def concatenate(char_to):
    global i, main_list, eps
    #fetch last node
    si = Node(id=i)
    i+=1
    main_list[-1].add_child(si, char_to)
    main_list.append(si)
    #create new empty one with eps.
    sj = Node(id=i)
    i+=1
    main_list.append(sj)
    si.add_child(sj, eps)
    
    # #pointer to last node.
    # main_list[-1] = sj
    
def terminate():
    main_list[-1].right_rb = True #doen't matter btw.
    main_list[-1].end = True

def left_bracket():
    global i, main_list, eps
    
    if main_list[-1].left_rb:
        si = Node (id=i, left_rb=True) 
        main_list[-1].add_child(si, eps)
        main_list.append(si)
        i += 1
        # main_list[-1] = si

    main_list[-1].left_rb = True

def right_bracket(new_main_or_id):
    global main_list,first_node,  eps, i
    
    if new_main_or_id is not None:
        #there's a OR that we need to close
        new_last = Node (id=i)
        i += 1
        for n in main_list:
            if n.opened_to == new_main_or_id:
                n.add_child(new_last,eps)
        main_list[-1].add_child(new_last, eps)
        main_list.append(new_last)

    else:
        main_list[-1].right_rb = True

    


def asterisk(last_open_bracket):
    global main_list,first_node, eps, i
    #check that last bracket open has only one child

    #find main_list[-1]'s dad
    last_dad = None

    for n in main_list:
        for c in n.children:
            if c[0].id == main_list[-1].id:
                last_dad = n

    last_open_bracket.add_child(main_list[-1], eps) 
   
    last_dad.add_child(last_open_bracket, eps)


def shift_update_first():
    global main_list, first_node, eps, i, spare_list
    first_node.start = False
    s0 = Node(id=0, start=True, left_rb=False, main_or=True)
    s0.add_child(first_node, eps)
    spare_list = []
    spare_list.append(s0)

    for n in main_list:
        n.id += 1
        spare_list.append(n)

    main_list.clear()
    main_list = copy.deepcopy(spare_list)
    
    return s0.id
    

def shift_update(last_open_bracket):
    global main_list, first_node,  eps, i, spare_list
    
    s0 = Node(id=last_open_bracket.id, main_or=True)
    s0.add_child(last_open_bracket, eps)
    spare_list = []

    for itr,n in enumerate(main_list):

        if itr < last_open_bracket.id:
            for c in n.children:
                if c[0].id == last_open_bracket.id:
                    n.remove_child(last_open_bracket.id)
                    n.add_child(s0, eps)

            spare_list.append(n)

        elif itr == last_open_bracket.id:
            spare_list.append(s0)
            spare_list.append(last_open_bracket)

        elif itr > last_open_bracket.id:
            n.id += 1
            spare_list.append(n)

    last_open_bracket.id += 1
    main_list.clear()
    main_list = copy.deepcopy(spare_list)

    
    return s0.id


        
    

def oring(last_open_bracket) -> None:
    global main_list,first_node, eps, i

    #stuffing and shifting
    
    if last_open_bracket == first_node: 
        new_main_or_id = shift_update_first()
        
    else:
        new_main_or_id = shift_update(last_open_bracket)
    i += 1
    main_list[-1].open_or = True
    main_list[-1].opened_to = new_main_or_id


    new_last = Node (id=i)
    for n in main_list:
        if n.id == new_main_or_id:
            n.add_child(new_last, eps)

    main_list.append(new_last)
    i += 1
    return new_main_or_id


def pair_me(txt):
    rb_stack = deque()
    pairs = []
    for i,ch in enumerate(txt):
        if ch == "(":
            rb_stack.append([0,i])
        elif ch == ")":
            my_bracket = rb_stack.pop()
            pairs.append([my_bracket[1], i])
    return pairs

def find_my_partner(x,pairs):
    for p in pairs:
        if p[1] == x: return p[0]
    print ("Error: bracket doesnt exist ya ngm")

def or_within(txt, y, x):
    for i in range (y,x):
        if txt[i] == "|": return True
    return False
def state(txt):
    global i, main_list, eps, first_node

    rb_stack = deque()
    first_bracket = False
    last_open_bracket = first_node
    new_main_or_id_list = []
    pairs = pair_me(txt)

    for itr,ch in enumerate(txt):
        print(ch)
        if ch == "(":
            if not first_bracket: 
                rb_stack.append(first_node)
                first_bracket = True
            else:
                last_open_bracket = main_list[-1]
                left_bracket()
                rb_stack.append(main_list[-1])
            
        elif ch == ")":
            if len(rb_stack)==1 and len(new_main_or_id_list)==0: #last one
                #this is end (TERMINATE)
                terminate()
            else:
                #check that ) closes an OR
                y = find_my_partner(itr,pairs)
                if or_within(txt, y, itr):
                    if len(new_main_or_id_list) >= 1:
                        last_opened_or_id = new_main_or_id_list[-1]
                        new_main_or_id_list = new_main_or_id_list[:-1]
                    else:
                        last_opened_or_id = None

                    right_bracket(last_opened_or_id)
                else:
                    right_bracket(None)
                
                last_open_bracket.left_rb = False
                rb_stack.pop()
                if len(rb_stack) != 0:
                    last_open_bracket = rb_stack[-1]

                if len(rb_stack) <= 1:
                    terminate()
                else:
                    last_open_bracket = rb_stack[-1]

        elif ch == "*":
            asterisk(last_open_bracket)
        
        elif ch == "|":
            new_main_or_id = oring(last_open_bracket)
            new_main_or_id_list.append(new_main_or_id)
            
        else:
            concatenate(ch)
            
        print_main_list()
        
        

if __name__ == "__main__":
    #Globals
    main_list = []
    i = 0
    eps = 'e'
    # main_list[-1] = None
    first_node = None
    spare_list = []
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    txt = "(ax|b)|(c|re)"

    txt = parse.parse(txt)
    print(txt)
    init_nodes()
    
    state(txt)
    print_main_list(short=False)
    print_main_list(short=True)
    

    



'''
    Correct Test cases:
        a|b
        a*|b
        a*|b*
        a|b|c
        a*|b|c
        a*|b*|c
        a*|b*|c*
        (ax|b)|c
        
'''