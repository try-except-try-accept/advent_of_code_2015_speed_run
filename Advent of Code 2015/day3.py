from re import match

with open("day3.txt") as f:
     input_data = f.read()

def solve(data):
     x, y = 0, 0
     visited = [[x,y]]
     for move in data:
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
     
     return len(visited)



tests = [">", "^>v<", "^v^v^v^v^v", input_data]
results = [2, 4, 2, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
