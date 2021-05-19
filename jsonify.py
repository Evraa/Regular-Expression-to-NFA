import json
import pprint





def jsonify(main_list):

    main_str = '{ "startingState": "S0"'
    for node in main_list:
        main_str += f', "node_{str(node.id)}":'

        node_i = f'"isTerminatingState":"{node.end}"'
        for child in node.children:
            node_i += f',"{child[1]}": "node_{str(child[0].id)}" '
        node_i = "{"+node_i+"}"
        main_str += node_i

    main_str += "}"

    y = json.loads(main_str)
    pprint.pprint (y)
    