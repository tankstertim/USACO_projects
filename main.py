from math import sqrt
def getGrid():
  f = open("buckets.in", 'r')
  text = f.readlines()
  f.close()
  grid = []
  obstacles = []
  for i in range(len(text)):
    grid_line = []
    for j in range(len(text[i].strip('\n'))):
      if text[i][j] == 'B':
        start_point = [j,i]
      elif text[i][j] == 'L':
        end_point = [j,i]
      elif text[i][j] == "R":
        obstacles.append([j,i])
        
      grid_line.append([i,j])
    grid.append(grid_line)
  return grid, start_point, end_point, obstacles
grid, start_point, end_point, obstacles  = getGrid()
print(grid)
print(start_point)
print(end_point)
print(obstacles)

def check_if_move_is_valid(cordinate, grid, obstacles):
  #print(f'cordinate: {cordinate}')
  for line in grid:
      if cordinate in line:
          #print(True)
          return True
  #print(False)
  return False
check_if_move_is_valid([2,2], grid, [[2,2]])

def find_distance(start,end):
  distance_of_x = start[0] - end[0]
  distance_of_y = start[1] - end[1]
  sum = (distance_of_x*distance_of_x) + (distance_of_y*distance_of_y)
  print(sum)
  sum = sqrt(sum)
  return sum

def check_if_goal_reached(cord1, cord2, curr_move, moves):
  moves_checked = []
  for move in curr_move:
    #print(f'move of x: {moves[move][0]}\nmove of y: {moves[move][1]}\ntotal of moves: [{cord1[0] + moves[move][0] }, {cord1[1] + moves[move][1]}]')
    cord1[0] += moves[move][0]
    cord1[1] += moves[move][1]
    
    if not check_if_move_is_valid(cord1, grid, obstacles) or cord1 in moves_checked:
      cord1[0] -= moves[move][0]
      cord1[1] -= moves[move][1]
    moves_checked.append([cord1[0] + moves[move][0],cord1[1] + moves[move][1] ])
    #print(f'moves checked: {moves_checked}')
  #print(curr_move)
  #print(cord1)
  #print(cord2)
  return (True if cord1 == cord2 else False)
  pass
def find_path(grid, start, end):
    moves = {'r': [1,0], 'l': [-1,0], 'd': [0,-1], 'u': [0,1]}
    all_moves = []
    solved = False
    while not solved:
      if all_moves == []:
        for move in moves:
          all_moves.append(move)
      else:
        curr_move = all_moves.pop(0)
        for move in moves:
          curr_move += move
          all_moves.append(curr_move)
          if check_if_goal_reached(start, end, curr_move, moves):
            solved_move = curr_move
            solved = True
            break
          
      
      
    return len(solved_move)
print(find_path(grid,start_point,end_point))
    
  
  
