import valide, parse
from collections import deque
import sys

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

    # last_node.to_node = i
    # last_node.char_to = char_to

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

            # if c[0].id == last_open_bracket.id:
            #     bracket_dad = n


    last_open_bracket.add_child(last_node, eps) 
   
    last_dad.add_child(last_open_bracket, eps)


def state(txt):
    global i, main_list, eps, last_node, first_node
    
    '''

    '''
    rb_stack = deque()
    first_bracket = False
    last_open_bracket = first_node
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
            
        else:
            concatenate(ch)
        
        # print_main_list()

if __name__ == "__main__":
    #Globals
    main_list = []
    i = 0
    eps = 'e'
    last_node = None
    first_node = None
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    txt = "(a*b*)*"

    txt = parse.parse(txt)
    print(txt)
    init_nodes()
    
    state(txt)
    print_main_list(short=True)

    



