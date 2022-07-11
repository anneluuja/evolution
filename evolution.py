import config
import random
from movement import get_animal_direction
from movement import handle_move
from createpairs import create_pairs

class Loom:

    def __init__(self, init_x_pos, init_y_pos, id, genome):
        #print("New Loom created")
        self.init_x_pos = init_x_pos
        self.init_y_pos = init_y_pos
        self.current_x_pos = init_x_pos
        self.current_y_pos = init_y_pos
        self.id = id
        self.genome = genome

    def genome_buckets(self):
        buckets = []
        values = list(self.genome.values())
        last_value = 0
        current_value = 0
        for i in range(0, len(values)):
            current_value += values[i]
            bucket = list(range(last_value, current_value))
            last_value = current_value
            buckets.append(bucket)
        return buckets

    def __str__(self):
        return str(self.id)


def new_grid(gridsize):
    grid = [[None for i in range(gridsize)] for j in range(gridsize)]
    return grid


def create_first_generation(gensize, gridsize, genome):
    unavailable_spots = []
    animals = []

    for i in range(gensize):
        spot_not_found = True
        while spot_not_found is True:
            x, y = random.randint(0, gridsize - 1), random.randint(0, gridsize - 1)
            spot = (x, y)
            if spot in unavailable_spots:
                continue
            else:
                spot_not_found = False
                unavailable_spots.append(spot)

        init_x, init_y = spot
        grid[init_x][init_y] = i
        loom = Loom(init_x, init_y, i, genome)
        animals.append(loom)
    max_id = i
    return max_id, animals, gridsize, unavailable_spots


grid = new_grid(config.gridsize)
max_id, animals, gridsize, unavailable_spots = create_first_generation(config.generationsize, config.gridsize, config.genome)


genome_dict = {}
for animal in animals:
    bucket = animal.genome_buckets()
    genome_dict[animal.id] = bucket


def calculate_simsteps(animals, gridsize, simsteps, unavailable_spots):
    grids = []
    for simstep in range(simsteps):
        for animal in animals:
            random_no = random.randint(0, 99)
            genome_buckets_of_animal = genome_dict[animal.id]

            direction = get_animal_direction(animal, genome_buckets_of_animal, random_no)

            handle_move(animal, direction, gridsize, unavailable_spots)

        updated_grid = new_grid(gridsize)

        for animal in animals:
            updated_grid[animal.current_x_pos][animal.current_y_pos] = animal.id
        grids.append(updated_grid)

    return grids

grids = calculate_simsteps(animals, config.gridsize, config.simsteps, unavailable_spots)
#print('print all grids')
#for grid in grids:
#    print_grid(grid)

# Print animals sorted by x and y positions
animals2 = sorted(animals, key=lambda x: (x.current_x_pos, x.current_y_pos), reverse=False)
#for animal in animals2:
#    print(animal.id, animal.current_x_pos, animal.current_y_pos


# Create a new generation based on some animals of the previous generation
pairs = create_pairs(animals)


# Create a new generation from survived animals
# Each pair to first have one child, then a second one if gensize has not hit the max limit
def reproduce(gensize, pairs, mutation_intensity, max_id):

    #for i in range (0, len(gensize)):
        #loom = Loom(init_x, init_y, i, genome)

    no_of_animals = 0
    i = 0
    while no_of_animals < gensize:
        child_genome = []
        parent_1, parent_2 = pairs[i]
        print('Next pair')
        print(f'i: {i}, no of pairs: {len(pairs)}')
        print(parent_1, parent_2)

        parent_1_genome_list = list(parent_1.genome.items())
        first_gene = random.choice(parent_1_genome_list)
        parent_1_genome_list.remove(first_gene)
        second_gene = random.choice(parent_1_genome_list)
        parent_1_genome_list.remove(second_gene)
        child_genome.append(first_gene)
        child_genome.append(second_gene)

        parent_2_genome_list = list(parent_2.genome.items())
        key1, value1 = first_gene
        key2, value2 = second_gene
        for gene in parent_2_genome_list:
            key, value = gene
            if key != key1 and key != key2:
                child_genome.append(gene)
        print(f'initial genome: {child_genome}')

        # Apply mutations
        mut_gene_index = random.randint(0, len(child_genome)-1)
        child_genome_mutated = []

        unmutated_gene_1 = child_genome.pop(mut_gene_index)
        gene_1, value_1_init = unmutated_gene_1
        if value_1_init < 100:
            value_1 = value_1_init + mutation_intensity
        else:
            value_1 = value_1_init

        mutated_gene_1 = gene_1, value_1

        unmutated_gene_2 = child_genome.pop(0)
        gene_2, value_2_init = unmutated_gene_2
        if value_1_init < 100 and value_2_init > 0:
            value_2 = value_2_init - mutation_intensity
        else:
            value_2 = value_2_init
        mutated_gene_2 = gene_2, value_2

        child_genome_mutated.append(mutated_gene_1)
        child_genome_mutated.append(mutated_gene_2)
        child_genome_mutated.extend(child_genome)
        print(f'mutated genome: {child_genome_mutated}')
        print("")

        if i < len(pairs) - 1:
            i +=1
        else:
            i = 0

        no_of_animals += 1
        print(no_of_animals)

        # Now need to create new animals; also add id which should always incrementally increase for the max_id of the last generation

reproduce(config.generationsize, pairs, config.mutationintensity, max_id)