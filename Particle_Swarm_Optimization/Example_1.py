def calculate_new_position(current_position, current_velocity):
    updated_position = []
    for pos, vel in zip(current_position, current_velocity):
        updated_position.append(pos + vel)
    return updated_position

pos_vector = [15.0, 8.5]
vel_vector = [2.0, -1.0]
next_pos = calculate_new_position(pos_vector, vel_vector)