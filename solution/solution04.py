def main():
  with open('../input/input04.txt','r') as f:
    lower, upper = [int(i) for i in f.read().replace('\n','').split('-')]
    
    counter = set()
    for i in range(10):
        for j in range(i,10):
            for k in range(j,10):
                for l in range(k,10):
                    for m in range(l,10):
                        for n in range(m,10):
                            counter.add(str(i)+str(j)+str(k)+str(l)+str(m)+str(n))
    
    def doubles(x='123455'):
        for i in range(len(x)-1):
            if x[i]==x[i+1]:
                return True
        return False

    def notriples(x='123455'):
        if (x[0]==x[1]) and (x[1]!=x[2]): return True
        if (x[5]==x[4]) and (x[4]!=x[3]): return True
        for i in range(len(x)-3):
            if (x[i] != x[i+1]) and (x[i+1] == x[i+2]) and (x[i+2] != x[i+3]):
                return True
        return False

    solution1 = len([i for i in counter if doubles(i) and lower<int(i)<upper])
    solution2 = len([i for i in counter if notriples(i) and lower<int(i)<upper])
  
    if __name__ == "__main__":
      print("Solution to problem 1 is {}".format(solution1))
      print("Solution to problem 2 is {}".format(solution2))

main()