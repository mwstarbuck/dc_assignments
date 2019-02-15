# create list/array
names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
# sort list


def rmv_dups(names):
    # make new list
    mod_list = names
    # sort the list
    mod_list.sort()
    # make a new list for no duplicates
    no_dups = []
    no_dups.append(mod_list[0])
    value = mod_list[0]
    for name in mod_list:
        if name != value:
            no_dups.append(name)
        value = name
    print(no_dups)


rmv_dups(names)
# remove any duplicates
