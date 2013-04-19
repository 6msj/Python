from Node import Node

def open_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

# assumes a goes before b
# modifies all of the nodes in B's after list to also include a in the before list
def batch_modify_before_lists(a_name, b_name, nodes_dict):
    nodeB = nodes_dict[b_name]
    for node_name in nodeB.after:
        node = nodes_dict[node_name]
        if not a_name in node.before:
            node.before.add(a_name)

def modify_node(a_name, b_name, nodes_dict):
    nodeA = nodes_dict[a_name]
    nodeB = nodes_dict[b_name]

    if a_name not in nodeB.before:
        nodeB.before.add(a_name)

    # add b to a's after list
    if b_name not in nodeA.after:
        nodeA.after.add(b_name)

    # everything that goes before b should also go after a
    batch_modify_before_lists(a_name, b_name, nodes_dict)


def modify_nodes(nodes_dict, a_name, b_name, before):
    nodeA = nodes_dict[a_name]
    nodeB = nodes_dict[b_name]

    if before:
        modify_node(a_name, b_name, nodes_dict)
    else:
        modify_node(b_name, a_name, nodes_dict)
            
        # sanity check
        if a_name in nodeB.before and a_name in nodeB.after:
            print " C:test"
            return False
        if b_name in nodeA.before and b_name in nodeA.after:
            print " D:test"
            return False


def build_list(nodes_dict, file_content):
    nodes_as_linked_list = None

    for line in file_content:
        tokens = line.split()
        node_a_name = ""
        node_b_name = ""
        switch = 0
        before = True
        for string in tokens:
            if string == "after":
                before = False
            elif string == "comes":
                switch = 1
            elif not string == "before":
                if switch == 0:
                    node_a_name += string
                else:
                    node_b_name += string

        # after the for loop, node_a_name is the name of the firt city
        # node_b_name is the name of the second city
        # if before is true, then node_a_name comes before node_b_name
        # else, node_a_name comes after node_b_name

        if not node_a_name in nodes_dict:
            nodes_dict[node_a_name] = Node(node_a_name)
        if not node_b_name in nodes_dict:
            nodes_dict[node_b_name] = Node(node_b_name)


        if not modify_nodes(nodes_dict, node_a_name, node_b_name, before):
            return None

        if nodes_as_linked_list is None:
            nodes_as_linked_list = nodes_dict[node_a_name]
            nodes_as_linked_list.prev = None
            if before:
                nodes_as_linked_list.prev = None
                nodes_as_linked_list.next = nodes_dict[node_b_name]
            else:
                nodes_as_linked_list.prev = nodes_dict[node_b_name]
                nodes_as_linked_list.next = None
                nodes_as_linked_list = nodes_as_linked_list.prev
        else:

            print "etst"

    print "Finished building list"

            
def main():
    content = open_file('text')
    nodes_dict = dict() # list of nodes
    ordered_list = build_list(nodes_dict, content)
    if ordered_list is None:
        print "Error with file format"
    else:
        while ordered_list:
            print ordered_list.name 
            ordered_list = ordered_list.next
    print nodes_dict


main()

                

