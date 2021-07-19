list_temp = [

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
]

def cut_by_min(graph):
    min_len = 9999999
    cut_by_min_graph = []
    
    for i in graph:
        if min_len > len(i):
            min_len = len(i)

    
    for x in graph:
        _x = x[:min_len]
        cut_by_min_graph.append(_x)
    #print(cut_by_min_graph)

    return cut_by_min_graph

cut_by_min(list_temp)
print(cut_by_min(list_temp)) 