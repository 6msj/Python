def open_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return content

def opposing_list(compared_to, recent):
    # if the two lists are opposites, that means that there are two
    # opposing requirements
    if compared_to[0] == recent[1] and compared_to[1] == recent[0]:
        return True
    return False

def check_for_invalids(compare, recent):
    for single_list in compare:
        if(opposing_list(single_list, recent)):
            return False
    compare.append(recent)
    return True

def add_to_output(output, values, before_after):
    recentList = []

    # if not in list
    if before_after == "before":
        if values[0] not in output:
            output.insert(0, values[0])

            # FIGURE OUT WHAT TO DO WHEN THE VALUE IS ALREADY IN THE LIST

        if values[3] not in output:
            output.append(values[3])
        recentList.append(values[0])
        recentList.append(values[3])
    else:
        if values[0] not in output:
            output.append(values[0])
        if values[3] not in output:
            output.insert(0, values[3])
        recentList.append(values[3])
        recentList.append(values[0])

    return recentList

content = open_file('text')

output = [] # get the list in order, then print the list
compare = []

for value in content:
    recent = [] # create a recent list to check for errors
    tokenized_vals = value.split()
    if tokenized_vals[2] == "before":
        # insert
        recent = add_to_output(output, tokenized_vals, "before")
    else:
        # append
        recent = add_to_output(output, tokenized_vals, "after")
    if not check_for_invalids(compare, recent):
        print "Illegal request file!"
        break


print output


