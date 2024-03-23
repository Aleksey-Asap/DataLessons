def work_list(lst):
    for i in range(len(lst)):
        if lst[i].isdigit():
            lst[i] = int(lst[i])