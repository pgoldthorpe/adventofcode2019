def main():
  with open('../input/day02.txt') as f:
    input_file = [int(i) for i in f.read().split(',')]

  def intcode(noun=12, verb=1):
    arr = input_file.copy()
    arr[1], arr[2] = noun, verb
    index = 0
    while True:
      if arr[index] == 1: arr[arr[index+3]] = arr[arr[index+1]] + arr[arr[index+2]]
      if arr[index] == 2: arr[arr[index+3]] = arr[arr[index+1]] * arr[arr[index+2]]
      if arr[index] == 99: break
      index+=4
    return arr[0]

  for noun in range(100, 0, -1):
    for verb in range(100, 0, -1):
      if intcode(noun, verb) == 19690720:
        result = 100*noun+verb
        break

  if __name__ == "__main__":
    print("Solution to problem 1 is {}".format(intcode()))
    print("Solution to problem 2 is {}".format(result))

main()