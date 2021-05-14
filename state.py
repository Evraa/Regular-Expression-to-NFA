import valide, parse
from collections import deque
import sys

class Node:
    def __init__(self, start=False, end=False, left_rb=False, right_rb=False, 
                main_or=False, open_or=False, to_node=None, id=None, char_to=None) -> None:
        self.start = start
        self.end = end
        self.left_rb=left_rb
        self.right_rb = right_rb
        self.main_or = main_or
        self.open_or = open_or
        self.to_node = to_node
        self.id = id
        self.char_to = char_to





def init_nodes():
    global i, main_list, eps, last_node
    s0 = Node(id=i, start=True, left_rb=True, to_node=1, char_to=eps)
    i+=1
    main_list.append(s0)
    s1 = Node(id=i)
    i+=1
    main_list.append(s1)
    last_node = s1
    

def print_main_list(short=True):

    global main_list

    for n in main_list:
        if short:
            print (f'Node: {n.id}\t\tto node:{n.to_node}\tchar:{n.char_to}')
        else:
            print (f'Node: {n.id}\t\tto node:{n.to_node}\tchar:{n.char_to}\t\tStart:{n.start}\tEnd:{n.end}\tLeft RB:{n.left_rb}\tRight RB:{n.right_rb}\tMain OR:{n.main_or}\tOpen OR:{n.open_or}\t')

    print ("##########EOF############\n")


def concatenate(char_to):
    global i, main_list, eps, last_node
    #fetch last node
    last_node.to_node = i
    last_node.char_to = char_to
    si = Node(id=i, to_node=i+1, char_to=eps)
    i+=1
    main_list.append(si)
    #create new empty one with eps.
    si = Node(id=i)
    i+=1
    main_list.append(si)
    #pointer to last node.
    last_node = si
    
def terminate():
    last_node.right_rb = True #doen't matter btw.
    last_node.end = True


def state(txt):
    global i, main_list, eps, last_node
    
    '''

    '''
    print(txt)
    init_nodes()
    print_main_list()
    rb_stack = deque()
    
    for ch in txt:
        if ch == "(":
            rb_stack.append("(")
            
        elif ch == ")":
            #just check.
            if len(rb_stack)==0: sys.exit(0)
            if len(rb_stack)==1: #last one
                #this is end (TERMINATE)
                terminate()
            else:
                #7war
                pass
        else:
            concatenate(ch)
        print_main_list()



if __name__ == "__main__":
    #Globals
    main_list = []
    i = 0
    eps = 'e'
    last_node = None
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    # txt = parse.parse(txt)
    txt = "(ab)"
    state(txt)
    



