import valide, parse

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




main_list = []
eps = 'e'


def init_nodes():
    s0 = Node(id=0, start=True, left_rb=True, to_node=1, char_to=eps)
    main_list.append(s0)
    s1 = Node(id=1)
    main_list.append(s1)
    

def print_main_list(short=True):
    for n in main_list:
        if short:
            print (f'Node: {n.id}\t\tto node:{n.to_node}\tchar:{n.char_to}')
        else:
            print (f'Node: {n.id}\t\tto node:{n.to_node}\tchar:{n.char_to}\t\tStart:{n.start}\tEnd:{n.end}\tLeft RB:{n.left_rb}\tRight RB:{n.right_rb}\tMain OR:{n.main_or}\tOpen OR:{n.open_or}\t')

def state(txt):
    '''

    '''

    init_nodes()
    print_main_list()


if __name__ == "__main__":
    # txt = str(input("Insert RE:\n"))
    # valide.validate(txt)
    # txt = parse.parse(txt)
    txt = "(ab)"
    state(txt)
    



