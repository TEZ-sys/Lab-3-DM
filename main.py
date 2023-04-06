import numpy as np


def load_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        matrix = np.zeros((n, n), dtype=int)

        for i in range(n):
            row = lines[i + 1].split()
            for j in range(n):
                matrix[i][j] = int(row[j])

        return matrix, n



def calculate_route_cost(route, matrix):
    cost = 0
    for i in range(len(route) - 1):
        if matrix[route[i]][route[i + 1]] == 0:
            return None
        cost += matrix[route[i]][route[i + 1]]
    return cost



def tsp(matrix):
    n = len(matrix)
    best_route = None
    best_cost = float('inf')

    def backtrack(curr_route, curr_cost):
        nonlocal best_route, best_cost
        if len(curr_route) == n:
            cost = calculate_route_cost(curr_route, matrix)
            if cost is not None and cost < best_cost:
                best_route = curr_route
                best_cost = cost
        else:
            for i in range(n):
                if i not in curr_route:
                    backtrack(curr_route + [i], curr_cost + matrix[curr_route[-1]][i])

    backtrack([0], 0)
    return best_route, best_cost


matrix, n = load_matrix('input.txt')

best_route, best_cost = tsp(matrix)

if best_route is None:
    print("Неможливо знайти маршрут, що відвідає всі вершини")
else:
    print("Оптимальний маршрут:", best_route)
    print("Вага оптимального маршруту:", best_cost)
