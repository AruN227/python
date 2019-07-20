def calculate_total(books):
    d = {0:0,1:800,2:1500,3:1700,4:2000,5:2100}
    total_cost = 0
    total_cost_lst = 0

    counts = [books.count(i) for i in range(1,6)]
    counts.sort(reverse=True)

    lst = counts.copy()

    while counts:
        counts = [x for x in counts if x != 0]
        uniques = len(counts)
        counts = [x-1 if x > 0 else 0 for x in counts]
        total_cost += d[uniques]

    while lst:
        lst = [x for x in lst if x !=0]

        if len(lst) >= 4:
            total_cost_lst += d[4]
            for i in range(4):
                lst[i] -= 1

        else:
            total_cost_lst += d[len(lst)]
            lst = [x-1 if x > 0 else 0 for x in lst]

    return min(total_cost_lst,total_cost)

