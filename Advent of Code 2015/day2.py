from re import match

with open("day2.txt") as f:
     input_data = [line.strip() for line in f.readlines()]

l, w, h = 0, 0 , 0

def solve(data):
     total = 0
     for line in data:
          l, w, h = map(int, line.split("x"))

          sides = [2*l*w, 2*w*h, 2*h*l]

          total += sum(sides)
          total += min(sides) / 2
     
     return total



tests = [["2x3x4"], ["1x1x10"], input_data]
results = [58, 43, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
