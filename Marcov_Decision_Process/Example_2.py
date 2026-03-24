def evaluate_best_action(current_state, available_actions, transition_matrix, reward_matrix, discount_factor=0.9):
    action_values = []
    for action in available_actions:
        action_sum = 0
        for next_state, prob in transition_matrix[current_state][action].items():
            action_sum += prob * reward_matrix[next_state] 
        action_values.append(action_sum)
    return max(action_values)