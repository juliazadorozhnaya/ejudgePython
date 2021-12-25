def check(s, p):
    counter = 0
    start = 0
    good_index = -1
    while start < len(s):
        if s[start] == p[counter] or p[counter] == '@':
            if counter == 0:
                good_index = start
            counter += 1
        else:
            if counter != 0:
                if good_index != -1:
                    start = good_index
                else:
                    start -= 1
            counter = 0
        start += 1
        if counter == len(p):
            return good_index
    return good_index if counter == len(p) else -1