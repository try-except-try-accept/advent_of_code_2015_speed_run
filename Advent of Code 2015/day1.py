with open("day1.txt") as f:
     input_data = f.read()

def solve_a(data):
     floor = 0
     for char in data:
 
          if char == "(":
               floor += 1
          elif char == ")":
               floor -= 1

     return floor

def solve(data):
     floor = 0

     for pos, char in enumerate(data):
 
          if char == "(":
               floor += 1
          elif char == ")":
               floor -= 1

          if floor == -1:
               return pos+1

     return floor


t = '''(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.'''


from re import match


tests = [input_data]


results = [None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
