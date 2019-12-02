def main():
  with open('../input/day01.txt') as f:
    mass = [int(i) for i in f.read().splitlines()]

    def fuel(value):
      return int(value/3//1-2)

    def fuelsum(value):
      ans = int(value/3//1-2)
      if ans <= 0:
          return 0
      return ans + fuelsum(ans)

  if __name__ == "__main__":
    print("Solution to problem 1 is {}".format(sum([fuel(i) for i in mass])))
    print("Solution to problem 2 is {}".format(sum([fuelsum(i) for i in mass])))

main()