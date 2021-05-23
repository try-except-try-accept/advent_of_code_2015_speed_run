from re import match

with open("day6.txt") as f:
     input_data = [line.strip() for line in f.readlines()]

def solve(data, log=False):
     lights = [[0 for x in range(1000)] for y in range(1000)]
     for line in data:
          i = 2
          j = 4

          tokens = line.split(" ")
          if "," in tokens[1]:
               action = "toggle"
               i -= 1
               j -= 1               
          else:
               action = " ".join(tokens[:2])

          start = list(map(int, tokens[i].split(",")))
          stop = list(map(int, tokens[j].split(",")))

          for y in range(start[1], stop[1]+1):
               for x in range(start[0], stop[0]+1):
                    if log:
                         print(x, y)
                   
                    if action == "toggle":
                         lights[y][x] += 2
                    elif "on" in action:
                         lights[y][x] += 1
                    else:
                         lights[y][x] -= 1
                         if lights[y][x] < 0:
                              lights[y][x] = 0


               
     return sum([sum(row) for row in lights])



tests = [["turn on 0,0 through 999,999"],
         ["toggle 0,0 through 999,0"],
         ["turn off 499,499 through 500,500"],
         input_data]

results = [1000000,
           1000,
           1000000-4,
           None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test, log=result_needed==4)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     elif result_needed == None:
          print(f"Is {result_given} your final answer?")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
