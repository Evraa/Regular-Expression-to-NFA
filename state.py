import enum
import valide, parse
from collections import deque
import sys
import copy

class Node:
    def __init__(self, start=False, end=False, left_rb=False, right_rb=False, 
                main_or=False, open_or=False, id=None) -> None:
        self.start = start
        self.end = end
        self.left_rb=left_rb
        self.right_rb = right_rb
        self.main_or = main_or
        self.open_or = open_or
        
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
    global i, main_list, eps, last_node, first_node
    first_node = Node(id=i, start=True, left_rb=True)
    i+=1
    main_list.append(first_node)
    s1 = Node(id=i)
    i+=1
    main_list.append(s1)
    first_node.add_child(s1, eps)
    last_node = s1
    

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
    global i, main_list, eps, last_node
    #fetch last node
    si = Node(id=i)
    i+=1
    main_list.append(si)
    last_node.add_child(si, char_to)
    #create new empty one with eps.
    sj = Node(id=i)
    i+=1
    main_list.append(sj)
    si.add_child(sj, eps)
    
    #pointer to last node.
    last_node = sj
    
def terminate():
    last_node.right_rb = True #doen't matter btw.
    last_node.end = True

def left_bracket():
    global i, main_list, eps, last_node
    
    if last_node.left_rb:
        si = Node (id=i, left_rb=True) 
        main_list.append(si)
        last_node = si

    last_node.left_rb = True

def right_bracket():
    last_node.right_rb = True


def asterisk(last_open_bracket):
    global main_list,first_node, last_node, eps, i
    #check that last bracket open has only one child

    #find last_node's dad
    last_dad = None

    for n in main_list:
        for c in n.children:
            if c[0].id == last_node.id:
                last_dad = n

    last_open_bracket.add_child(last_node, eps) 
   
    last_dad.add_child(last_open_bracket, eps)


def shift_update_first():
    global main_list, first_node, last_node, eps, i, spare_list
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
    i +=1
    return s0
    

def shift_update(last_open_bracket):
    global main_list, first_node, last_node, eps, i, spare_list
    
    s0 = Node(id=last_open_bracket.id, main_or=True)
    s0.add_child(last_open_bracket, eps)
    spare_list = []

    for itr,n in enumerate(main_list):

        if itr < last_open_bracket.id:
            if last_open_bracket.id - itr == 1:
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

    i +=1
    return s0


        
    

def oring(last_open_bracket) -> None:
    global main_list,first_node, last_node, eps, i

    #stuffing and shifting
    last_node.open_or = True

    if last_open_bracket == first_node: 
        new_main_or = shift_update_first()
    else:
        new_main_or = shift_update(last_open_bracket)

    new_last = Node (id=i)
    main_list[-1].add_child(new_last, eps)

    last_node = new_last

    main_list.append(new_last)
    i += 1
    return new_main_or


def state(txt):
    global i, main_list, eps, last_node, first_node

    rb_stack = deque()
    first_bracket = False
    last_open_bracket = first_node
    new_main_or = None

    for ch in txt:
        if ch == "(":
            if not first_bracket: 
                rb_stack.append(first_node)
                first_bracket = True
            else:
                last_open_bracket = last_node
                left_bracket()
                rb_stack.append(last_node)
            
        elif ch == ")":
            if len(rb_stack)==1: #last one
                #this is end (TERMINATE)
                terminate()
            else:
                right_bracket()
                rb_stack.pop()
                last_open_bracket = rb_stack[-1]

        elif ch == "*":
            asterisk(last_open_bracket)
        
        elif ch == "|":
            new_main_or = oring(last_open_bracket)
            
        else:
            concatenate(ch)

        print (ch)
        print_main_list()
        

if __name__ == "__main__":
    #Globals
    main_list = []
    i = 0
    eps = 'e'
    last_node = None
    first_node = None
    spare_list = []
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    txt = "a|b"

    txt = parse.parse(txt)
    print(txt)
    init_nodes()
    
    state(txt)
    # print_main_list(short=False)

    



