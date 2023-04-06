from sys import maxsize
from itertools import permutations


def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        path = [s]
        for j in i:
            current_pathweight += graph[k][j]
            k = j
            path.append(j)
        current_pathweight += graph[k][s]
        path.append(s)
        if current_pathweight < min_path:
            min_path = current_pathweight
            min_path_vertex = path
    
    return min_path_vertex

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        contents = file.read()
        string_values = contents.split()
        int_values = [int(x) for x in string_values]
        V = int_values[0]
        int_values.remove(V)
        sublist_len = len(int_values) // V
        graph = [int_values[i:i + sublist_len] for i in range(0, len(int_values), sublist_len)]

        s = 1
        print(travellingSalesmanProblem(graph, s))
