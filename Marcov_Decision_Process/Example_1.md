def compute_expected_value(transition_probs, state_rewards):
    total_expected_reward = 0.0
    for next_state, probability in transition_probs.items():
        total_expected_reward += probability * state_rewards[next_state]
    return total_expected_reward

transitions = {'State_X': 0.8, 'State_Y': 0.2}
rewards = {'State_X': 50, 'State_Y': -10}
expected_val = compute_expected_value(transitions, rewards)