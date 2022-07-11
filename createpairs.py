def create_pairs(animals):

    ids_of_current_animals = [animal.id for animal in animals]
    max_current_id = max(ids_of_current_animals)
    print(max_current_id)

    # Create random pairs from the animals which survived
    # If the number of survived animals is not even, then one  animal will not reproduce
    survived_animals = [animal for animal in animals if animal.current_y_pos <= 14]
    print(f'No of survived animals: {len(survived_animals)}')
    # for animal in survived_animals:
    #     print(animal.current_x_pos, animal.current_y_pos)

    pairs = []
    while len(survived_animals) > 1:
        random_animal_1_id = random.randrange(0, len(survived_animals))
        random_animal_1 = survived_animals.pop(random_animal_1_id)
        random_animal_2_id = random.randrange(0, len(survived_animals))
        random_animal_2 = survived_animals.pop(random_animal_2_id)
        pair = random_animal_1, random_animal_2
        pairs.append(pair)

    return pairs