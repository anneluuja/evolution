def print_grid(grid):
    print("New Grid")
    transformed_grid = []

    for i in range((len(grid))):
        original_list = grid[i]
        transformed_list = map(lambda listitem: '_' if listitem is None else str(listitem), original_list)
        transformed_grid.append('  '.join(list(transformed_list)))

    print(*transformed_grid, sep='\n')
    print('')
