from re import match

with open("day5.txt") as f:
     input_data = [line.strip() for line in f.readlines()]

def solve(data):
     count = 0
     for line in data:

          vowel = sum([line.count(v) for v in "eioua"]) >= 3
          twice = any([chr(i)+chr(i) in line for i in range(97, 97+26)])
          banned = any([ban in line for ban in ["ab", "cd", "pq", "xy"]])

          if vowel and twice and not banned:
               count += 1
     return count



tests = [["ugknbfddgicrmopn"],
         ["aaa"],
         ["jchzalrnumimnmhp"],         
         ["haegwjzuvuyypxyu"],
         ["dvszwmarrgswjxmb"],
         input_data]
results = [1, 1, 0, 0, 0, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     elif result_needed == None:
          print(f"Is {result_given} your final answer?")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
