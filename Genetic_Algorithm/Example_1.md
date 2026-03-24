def execute_crossover(parent_one, parent_two):
    split_point = len(parent_one) // 2
    offspring = parent_one[:split_point] + parent_two[split_point:]
    return offspring

p1 = [0, 0, 0, 0, 0, 0]
p2 = [1, 1, 1, 1, 1, 1]
new_child = execute_crossover(p1, p2)