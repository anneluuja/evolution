def get_animal_direction(animal, genome_buckets_of_animal, random_no):

    i = 0
    bucket_not_found = True
    while bucket_not_found is True:
        if random_no in genome_buckets_of_animal[i]:
            direction = list(animal.genome.keys())[i]
            bucket_not_found = False
        else:
            i += 1
    return direction


def handle_move(animal, direction, gridsize, unavailable_spots):
    animal_current_pos = (animal.current_x_pos, animal.current_y_pos)
    if direction == 'up':
        new_x_pos = animal.current_x_pos - 1
        if new_x_pos >= 0:
            animal.current_x_pos -= 1
    if direction == 'down':
        new_x_pos = animal.current_x_pos + 1
        if new_x_pos < gridsize:
            animal.current_x_pos += 1
    if direction == 'left':
        new_y_pos = animal.current_y_pos - 1
        if new_y_pos >= 0:
            animal.current_y_pos -= 1
    if direction == 'right':
        new_y_pos = animal.current_y_pos + 1
        if new_y_pos < gridsize:
            animal.current_y_pos += 1
    animal_proposed_new_pos = (animal.current_x_pos, animal.current_y_pos)

    if animal_proposed_new_pos in unavailable_spots:
        animal.current_x_pos, animal.current_y_pos = animal_current_pos

    animal_actual_new_pos = (animal.current_x_pos, animal.current_y_pos)

    if animal_actual_new_pos != animal_current_pos:
        unavailable_spots.remove(animal_current_pos)
        unavailable_spots.append(animal_actual_new_pos)