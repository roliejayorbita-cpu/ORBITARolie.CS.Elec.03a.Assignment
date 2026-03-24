import random

def adjust_velocity(vel, pos, personal_best, global_best, inertia=0.6, c1=1.5, c2=1.5):
    r1, r2 = random.random(), random.random()
    updated_vel = []
    for i in range(len(vel)):
        momentum = inertia * vel[i]
        cognitive = c1 * r1 * (personal_best[i] - pos[i])
        social = c2 * r2 * (global_best[i] - pos[i])
        updated_vel.append(momentum + cognitive + social)
    return updated_vel