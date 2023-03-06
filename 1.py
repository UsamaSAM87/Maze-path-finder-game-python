def Find_Path():
    maze[Starting_positionXY[0]][Starting_positionXY[1]] = '*'
    current_cell = Path_positions[len(Path_positions) - 1]
    if current_cell == Goal:
        return '\0'

    if maze[current_cell[0]][current_cell[1] + 1] == 'p':
        maze[current_cell[0]][current_cell[1] + 1] = '*'
        Path_positions.append([current_cell[0], current_cell[1] + 1])
        Find_Path()
    if maze[current_cell[0]][current_cell[1] - 1] == 'p':
        maze[current_cell[0]][current_cell[1] - 1] = '*'
        Path_positions.append([current_cell[0], current_cell[1] - 1])
        Find_Path()

    if maze[current_cell[0] + 1][current_cell[1]] == 'p':
        maze[current_cell[0] + 1][current_cell[1]] = '*'
        Path_positions.append([current_cell[0] + 1, current_cell[1]])
        Find_Path()
    if maze[current_cell[0] - 1][current_cell[1]] == 'p':
        maze[current_cell[0] - 1][current_cell[1]] = '*'
        Path_positions.append([current_cell[0] - 1, current_cell[1]])
        Find_Path()

    current_cell = Path_positions[len(Path_positions) - 1]
    if current_cell != Goal:
        cell_to_remove = Path_positions[len(Path_positions) - 1]
        Path_positions.remove(cell_to_remove)
        maze[cell_to_remove[0]][cell_to_remove[1]] = 'p'

def Print_maze():
    for i in range(0, len(maze)):
        for j in range(0, len(maze[0])):
            print(maze[i][j], end=" ")
        print('\n')

maze = [
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
['#','p','p','p','p','p','#','p','p','s','#','#','p','p','#','#'],
['p','p','#','#','#','p','p','p','p','#','#','#','p','p','#','#'],
['#','p','#','#','#','p','p','#','p','#','#','p','p','p','#','#'],
['#','p','p','p','p','#','#','p','p','#','#','p','p','p','#','#'],
['#','#','#','#','p','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','p','p','#','#','#','#','#','#','#','#','#','#','#'],
['#','#','#','#','p','p','p','p','p','#','#','#','#','#','#','#'],
['#','#','#','#','#','#','#','#','p','p','#','#','#','#','p','p'],
['#','#','#','#','#','#','#','#','p','p','p','p','p','p','p','#'],
['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]

Starting_positionXY= [2, 0]
Goal=[8, 15]
print("Maze")
Print_maze()
Path_positions = [Starting_positionXY]
print("Path")
Find_Path()
Print_maze()