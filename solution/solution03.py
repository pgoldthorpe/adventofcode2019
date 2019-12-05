def main():
  with open('../input/input03.txt','r') as f:
    wire1_instructions, wire2_instructions, _ = [i for i in f.read().split('\n')]
    wire1_instructions = wire1_instructions.split(',')
    wire2_instructions = wire2_instructions.split(',')

  def points(wire):
    x,y = 0,0
    series = {(0,0): 0}
    length = 0
    
    for item in wire:
      direction, steps = item[0], int(item[1:])
      if direction == 'R':
        for i in range(steps):
          length+=1
          x+=1
          series.setdefault((x,y), length)
      if direction == 'U':
        for i in range(steps):
          length+=1
          y+=1
          series.setdefault((x,y), length)
      if direction == 'L':
        for i in range(steps):
          length+=1
          x-=1
          series.setdefault((x,y), length)
      if direction == 'D':
        for i in range(steps):
          length+=1
          y-=1
          series.setdefault((x,y), length)
    return series

  wire1_points = points(wire1_instructions)
  wire2_points = points(wire2_instructions)

  collision_points = set(wire1_points).intersection(set(wire2_points)) - {(0,0)}
  solution1 = min({abs(i[0]) + abs(i[1]) for i in collision_points})
  solution2 = min({wire1_points[i] + wire2_points[i] for i in collision_points})

  if __name__ == "__main__":
    print("Solution to problem 1 is {}".format(solution1))
    print("Solution to problem 2 is {}".format(solution2))

main()