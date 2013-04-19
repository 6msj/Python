from Node import Node
from sys import exit
def open_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

# The purpose of this function is to take the list of requirements and
# turn them into lists, with words concatenated properly for proper
# parsing later. The function could probably be refactored for better
# readability, but for the purpose of this problem, it is better to leave it.
def build_a_list(content):
    built_list = []
    for line in content:
        split_line = line.split()
        indexCome = split_line.index("comes")
        concat_before_come = []
        word_before_come = ""

        # Merge words before "comes" together.
        for i in range (0, indexCome):
            word_before_come += split_line[i]
            if i != indexCome-1:
                word_before_come += " "
        concat_before_come.append(word_before_come)
        for index in range (indexCome, len(split_line)):
            concat_before_come.append(split_line[index])

        # Merge words after "before/after" together.
        if "before" in concat_before_come:
            indexReq = concat_before_come.index("before")
        else: # "after"
            indexReq = concat_before_come.index("after")

        newWord = ""
        for i in range (indexReq, len(concat_before_come)-1):
            newWord += concat_before_come[i+1]
            if i < len(concat_before_come)-2:
                newWord += " "

        anotherList = []
        for i in range (0, indexReq+1):
            anotherList.append(concat_before_come[i])
        anotherList.append(newWord)
        built_list.append(anotherList)
    return built_list

# Swap every list that has after in it so, every requirement becomes a 
# before requirement. Unneeded, but swap the "after" word to "before" to
# avoid confusion.
def change_after_to_before(list_of_lists):
    for list in list_of_lists:
        if "after" in list:
            indexAfter = list.index("after")
            list[indexAfter] = "before"
            temp = list[0]
            list[0] = list[len(list)-1]
            list[len(list)-1] = temp

# There might be a possibility of duplicate requirements through different
# wording. Remove any duplicate requirements to form a new list.
def trim_requirements_from_lists(list_of_lists):
    new_list_of_lists = []
    for list in list_of_lists:
        if list not in new_list_of_lists:
            new_list_of_lists.append(list)
    return new_list_of_lists

def print_contents_of_lists(list_of_lists):
    for list in list_of_lists:
        print list

def detect_errors(listRequirements, holdNodes):
    first = 0
    last = len(listRequirements[0])-1
    # Set up the first requirement with nodes.
    firstNode = Node(listRequirements[first][first])
    secondNode = Node(listRequirements[first][last])
    holdNodes.append(firstNode)
    holdNodes.append(secondNode)
    add_names_to_set(firstNode, secondNode, holdNodes)

    for requirement in listRequirements[1:len(listRequirements)]:
        firstNode = find_node(requirement[first], holdNodes)
        if firstNode:
            # If the first name was found, try and find the second name too.
            secondNode = create_secondNode(firstNode, secondNode, holdNodes, requirement)
        else:
            # The first node wasn't found, create it and proceed.
            firstNode = Node(requirement[first])
            holdNodes.append(firstNode)
            secondNode = create_secondNode(firstNode, secondNode, holdNodes, requirement)

def create_secondNode(firstNode, secondNode, holdNodes, requirement):
    last = len(requirement)-1
    secondNode = find_node(requirement[last], holdNodes)
    if secondNode:
        # The first node was created and added to the list of nodes, and the second name was found.
        check_illegal_request(firstNode, secondNode, holdNodes)
        move_nodes_around(firstNode, secondNode, holdNodes)
    else:
        # Second name wasn't found either. Create it and insert after first name.
        secondNode = Node(requirement[last])
        index_to_insert_after = holdNodes.index(firstNode)
        holdNodes.insert(index_to_insert_after+1, secondNode)
        check_illegal_request(firstNode, secondNode, holdNodes)
    return secondNode

def move_nodes_around(firstNode, secondNode, holdNodes):
    indexFirst = holdNodes.index(firstNode)
    indexSecond = holdNodes.index(secondNode)
    if indexSecond > indexFirst:
        print "first " + firstNode.name
        print "second " +secondNode.name
        node = holdNodes.pop(indexSecond)
        print "node "  + node.name
        holdNodes.insert(indexFirst, secondNode)

def check_illegal_request(firstNode, secondNode, holdNodes):
    if not add_names_to_set(firstNode, secondNode, holdNodes):
        print "Illegal Request File!"
        exit()

# Suppose Node A precedes Node B, check every Node that is after Node B to see if there exists a Node A requirement.
# If there is somehow a match, the requirements can't be completed due to conflicts.
# This function takes care of the A Before B, B Before C, C Before A type of conflict.
def any_node_brings_an_error(firstNode, secondNode):
    for before_node in firstNode.before:
        for after_node in secondNode.after:
            if before_node.name == after_node.name:
                return True
    return False

# Checks for A Before B, B Before A conflicts.
def check_for_direct_conflict(req_lists):
    first = 0
    last = len(req_lists[0])-1
    for req in req_lists:
        for next_req in req_lists[1:len(req_lists)]:
            if req[first] == next_req[last] and req[last] == next_req[first]:
                print "Illegal Request File!"
                return True
    return False

# After adding nodes respectively to each other's before and after list, check to see if there are any errors.
# If there are errors, return False, otherwise the program will proceed with True.
def add_names_to_set(firstNode, secondNode, holdNodes):
    firstNode.after.add(secondNode)
    secondNode.before.add(firstNode)
    if any_node_brings_an_error(firstNode, secondNode):
        return False
    else:
        return True

def print_values_in_node(node):
    for value in node:
        print value.name

def find_node(name, holdNodes):
    for node in holdNodes:
        if name == node.name:
            return node
    return False

# The node that has an empty Before set should be the first in the list.
def find_firstNode(holdNodes):
    for node in holdNodes:
        if not node.before:
            holdNodes.remove(node)
            return node

def main():
    content = open_file('text')
    holdNodes = []
    output = []
    req_lists = build_a_list(content)
    change_after_to_before(req_lists)
    req_lists = trim_requirements_from_lists(req_lists)
    check_for_direct_conflict(req_lists)
    detect_errors(req_lists, holdNodes)
    for node in holdNodes:
        print node.name


main()
