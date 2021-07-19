
import glob
import pandas as pd


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

def file_to_list(path):
    files = glob.glob(path)
    list_capacity = []

    for file in files:
       _file = pd.read_csv(file)
       #print(_file)

       a = _file['capacity'].tolist()

       list_capacity.append(a)

    #print(list_capacity)

    return list_capacity

       
        
          