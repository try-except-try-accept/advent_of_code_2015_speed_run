from re import match

with open("day3.txt") as f:
     input_data = f.read()

def solve(data):
     sx, sy = 0, 0
     rx, ry = 0, 0
     who = [[sx, sy], [rx, ry]]
     visited = [[sx,sy]]
     for i, move in enumerate(data):
          x, y = who[i % 2]
          
          if move == "^":
               y -= 1
          elif move == "v":
               y += 1
          elif move == "<":
               x -= 1
          elif move == ">":
               x += 1

          if [x, y] not in visited:
               visited.append([x, y])

          who[i % 2] = [x, y]
     
     return len(visited)



tests = ["^v", "^>v<", "^v^v^v^v^v", input_data]
results = [3, 3, 11, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     elif result_needed == None:
          print(f"Is {result_given} your final answer?")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
