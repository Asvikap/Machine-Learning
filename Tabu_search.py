import random

# define the objective function
def objective_function(x):
    return x**2

# define the initial solution
def initial_solution(bounds):
    return [random.uniform(bounds[i][0], bounds[i][1]) for i in range(len(bounds))]

# define the tabu search algorithm
def tabu_search(objective_function, bounds, max_iter, tabu_list_size):
    # initialize the best solution
    best_sol = None
    best_val = None
    # initialize the tabu list
    tabu_list = []
    # initialize the current solution
    curr_sol = initial_solution(bounds)
    curr_val = objective_function(curr_sol)
    # iterate for a given number of iterations
    for i in range(max_iter):
        # find the best neighbor solution
        best_neighbor_sol = None
        best_neighbor_val = None
        for j in range(len(bounds)):
            for k in range(-1, 2):
                if k == 0:
                    continue
                neighbor_sol = list(curr_sol)
                neighbor_sol[j] += k
                if neighbor_sol[j] < bounds[j][0]:
                    neighbor_sol[j] = bounds[j][0]
                elif neighbor_sol[j] > bounds[j][1]:
                    neighbor_sol[j] = bounds[j][1]
                if neighbor_sol not in tabu_list:
                    neighbor_val = objective_function(neighbor_sol)
                    if best_neighbor_val is None or neighbor_val < best_neighbor_val:
                        best_neighbor_sol = neighbor_sol
                        best_neighbor_val = neighbor_val
        # update the tabu list
        tabu_list.append(best_neighbor_sol)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)
        # update the current solution
        curr_sol = best_neighbor_sol
        curr_val = best_neighbor_val
        # update the best solution
        if best_val is None or curr_val < best_val:
            best_sol = curr_sol
            best_val = curr_val
    return (best_sol, best_val)