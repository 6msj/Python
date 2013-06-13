from Node import Node


def open_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return content


# assumes a goes before b
# modifies all of the nodes in B's after list
# to also include a in the before list
def batch_modify_before_lists(a_name, b_name, nodes_dict):
    nodeB = nodes_dict[b_name]
    for node_name in nodeB.after:
        node = nodes_dict[node_name]
        if not a_name in node.before:
            node.before.add(a_name)

    nodeA = nodes_dict[a_name]
    for node_name in nodeA.before:
        node = nodes_dict[node_name]
        if not b_name in node.after:
            node.after.add(b_name)


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
        return False
    if b_name in nodeA.before and b_name in nodeA.after:
        return False
    return True


# returns the node required highest up before B
# assumes b is currently before a
def find_top_most_required(nodeA, nodeB):
    curr = nodeA.prev
    current_node_to_consider_priority = nodeA
    required = nodeA
    while not curr.name == nodeB.name:
        if curr.name in current_node_to_consider_priority.before:
            required = curr
            current_node_to_consider_priority = curr
        curr = curr.prev
    return required


# assumes a before b
# returns the head of the current linked list
def modify_linked_list(node_a_name, node_b_name,
                       nodes_dict, nodes_as_linked_list):
    nodeA = None
    nodeB = None
    foundBefore = False
    tail = None

    curr = nodes_as_linked_list

    while curr:
        if curr.name == node_a_name:
            nodeA = curr
            if not nodeB:
                foundBefore = True

        if curr.name == node_b_name:
            nodeB = curr

        if not curr.next:
            tail = curr

        curr = curr.next

    if nodeA and nodeB:
        # both node A and node B exist
        if foundBefore:
            return nodes_as_linked_list
        else:
            # first case B -> A
            aNext = nodeA.next
            bPrev = nodeB.prev
            bNext = nodeB.next

            if bNext and bNext.name == node_a_name:
                # swap a and b
                if aNext:
                    aNext.prev = nodeB
                if tail.name == nodeA.name:
                    tail = nodeB

                if bPrev:
                    bPrev.next = nodeA
                elif nodes_as_linked_list.name == nodeB.name:
                    nodes_as_linked_list = nodeA
                nodeA.prev = bPrev
                nodeB.next = aNext

            else:
                topMostRequired = find_top_most_required(nodeA, nodeB)
                tMRPrev = topMostRequired.prev
                topMostRequired.prev = bPrev

                if bPrev:
                    bPrev.next = topMostRequired
                else:
                    nodes_as_linked_list = topMostRequired
                if aNext:
                    aNext.prev = tMRPrev
                tMRPrev.next = aNext
            nodeB.prev = nodeA
            nodeA.next = nodeB
    elif nodeA:
        # only node A exists
        nodeB = nodes_dict[node_b_name]
        nodeANext = nodeA.next
        nodeA.next = nodeB
        nodeB.prev = nodeA
        nodeB.next = nodeANext

        if nodeANext:
            nodeANext.prev = nodeB

    elif nodeB:
        # only node B exists
        prevNodeB = nodeB.prev
        nodeA = nodes_dict[node_a_name]
        nodeA.next = nodeB
        nodeA.prev = prevNodeB

        nodeB.prev = nodeA
        if prevNodeB:
            prevNodeB.next = nodeA

        if nodes_as_linked_list.name == nodeB.name:
            nodes_as_linked_list = nodeA

    else:
        # neither A nor B exist yet, append to tail (could prepend to head)
        nodeA = nodes_dict[node_a_name]
        nodeB = nodes_dict[node_b_name]

        nodeA.prev = tail
        tail.next = nodeA
        nodeA.next = nodeB
        nodeB.prev = nodeA
        nodeB.next = None
        tail = nodeB
    return nodes_as_linked_list


def build_list(nodes_dict, file_content):
    # should be pointing to the start of the list
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

        # after the for loop, node_a_name is the name of the first city
        # node_b_name is the name of hte second city
        # if before is True, then node_a_name comes before node_b_name
        # else, node_a_name comes after node_b_name

        if not node_a_name in nodes_dict:
            nodes_dict[node_a_name] = Node(node_a_name)
        if not node_b_name in nodes_dict:
            nodes_dict[node_b_name] = Node(node_b_name)

        if not modify_nodes(nodes_dict, node_a_name, node_b_name, before):
            return None

        if nodes_as_linked_list is None:
            nodes_as_linked_list = nodes_dict[node_a_name]
            if before:
                # set head to node A and set node A's next to point to B
                nodes_as_linked_list.prev = None
                nodes_as_linked_list.next = nodes_dict[node_b_name]
                nodes_dict[node_b_name].prev = nodes_as_linked_list
                nodes_dict[node_b_name].next = None
            else:
                # set head to node B and set node B's next to point to A
                nodes_as_linked_list.prev = nodes_dict[node_b_name]
                nodes_as_linked_list.next = None
                nodes_as_linked_list = nodes_as_linked_list.prev
                nodes_as_linked_list.next = nodes_dict[node_a_name]
                nodes_as_linked_list.prev = None
        else:
            if before:
                nodes_as_linked_list = modify_linked_list(node_a_name,
                                                          node_b_name,
                                                          nodes_dict,
                                                          nodes_as_linked_list)
            else:
                nodes_as_linked_list = modify_linked_list(node_b_name,
                                                          node_a_name,
                                                          nodes_dict,
                                                          nodes_as_linked_list)

    return nodes_as_linked_list


def main():
    content = open_file('text')
    nodes_dict = dict()  # list of nodes
    ordered_list = build_list(nodes_dict, content)
    if ordered_list is None:
        print "Error with file format"
    else:
        count = 1
        while ordered_list:
            print str(count) + ". " + ordered_list.name
            ordered_list = ordered_list.next
            count += 1

main()
