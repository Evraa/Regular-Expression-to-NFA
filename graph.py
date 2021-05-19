from graphviz import Digraph



def graph(main_list):

    dot = Digraph(comment='NFA')
    dot  #doctest: +ELLIPSIS

    for node in main_list:
        node_name = "node_"+str(node.id)
        dot.node(node_name,node_name)

    for node in main_list:
        node_name = "node_"+str(node.id)
        for child in node.children:
            child_name = "node_"+str(child[0].id)
            dot.edge(node_name, child_name, label=child[1])
            
    print(dot.source) 
    dot.render('test-output/round-table.gv', view=True)

# if __name__ == "__main__":

#     dot = Digraph(comment='NFA')
#     dot  #doctest: +ELLIPSIS

#     dot.node('A', 'King Arthur')
#     dot.node('B', 'Sir Bedevere the Wise')
#     dot.node('L', 'Sir Lancelot the Brave')

#     dot.edges(['AB', 'AL'])
#     dot.edge('B', 'L', label="ec")

#     print(dot.source) 

#     dot.render('test-output/round-table.gv', view=True)