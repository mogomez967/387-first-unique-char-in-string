def firstUniqChar(s):
    # Given a string s, find the first non-repeating character in it and return
    # its index. If it does not exist, return -1

    # brute force approach:
    # iterate through string, store current char in list,
    # then if next iterable char is in list, remove the chars from list,
    # and then store the next one.
    # if next char is unique, keep previous char in list until a repetition
    # is come across
    # if there are multiple unique chars, the first occurence should be the
    # first element in the list
    lib = []
    skip = []
    if len(s) > 1:
        lib.append(s[0])            # if s len > 1, put first char in lib
    else:
        return 0                    # the string s is a single char
    
    for letter in s[1:]:
        if letter not in lib and letter not in skip:
            lib.append(letter)      # we have hit a unique (for now) char
            skip.append(letter)     # add this letter to a list of hits
        else:
            if letter in lib:
                lib.remove(letter)  # this is a duplicate; so delete it
            skip.append(letter)     # skips will tell if a letter was deleted
            
    if len(lib) > 0:
        return s.index(lib[0])      # lib[0] holds first unique char
    else:
        return -1

s = "aadadaad"
print(firstUniqChar(s))
