from graphviz import Digraph



def graph(main_list):
    if len(main_list) == 0: return

    dot = Digraph(comment='NFA')
    dot  #doctest: +ELLIPSIS
    dot.attr(rankdir="LR")
    for node in main_list:

        node_name = "S"+str(node.id)


        if node.end:
            dot.attr('node', shape="doublecircle")
        else:
            dot.attr('node', shape="circle")

        dot.node(node_name,node_name)

    dot.attr('node', shape="plaintext")
    dot.node("start","start")

    dot.edge(head_name="S0", tail_name="start")

    for node in main_list:
        node_name = "S"+str(node.id)
        for child in node.children:
            child_name = "S"+str(child[0].id)
            dot.edge(node_name, child_name, label=child[1])

    # print(dot.source) 
    dot.render('test-output/round-table.gv', view=True)
