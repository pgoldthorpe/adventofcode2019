def main():
  with open('../input/input03.txt','r') as f:
    wire1, wire2, _ = [i for i in f.read().split('\n')]
    wire1 = wire1.split(',')
    wire2 = wire2.split(',')

  def points(wire):
    x,y = 0,0
    series = [(0,0)]
    
    for item in wire:
      if item[0] == 'R':
        for i in range(int(item[1:])):
          x+=1
          series.append((x,y))
      if item[0] == 'U':
        for i in range(int(item[1:])):
          y+=1
          series.append((x,y))
      if item[0] == 'L':
        for i in range(int(item[1:])):
          x-=1
          series.append((x,y))
      if item[0] == 'D':
        for i in range(int(item[1:])):
          y-=1
          series.append((x,y))
    return series

  wire1points = points(wire1)
  wire2points = points(wire2)

  collision = set(wire1points).intersection(set(wire2points)) - {(0,0)}
  solution1 = min([abs(i[0]) + abs(i[1]) for i in collision])

  steps = {item: wire1points.index(item) + wire2points.index(item) for item in collision}
  solution2 = min(steps.values())

  if __name__ == "__main__":
    print("Solution to problem 1 is {}".format(solution1))
    print("Solution to problem 2 is {}".format(solution2))

main()