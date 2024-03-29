def find_max(list):
    for x in list:
        if x > min(list) and x >= max(list):
            print(x)