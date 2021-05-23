from re import match
from collections import defaultdict

with open("day5.txt") as f:
     input_data = [line.strip() for line in f.readlines()]

def solve(data):
     count = 0
     print(data)
     for line in data:
          rep_check = False
          overlap_check = defaultdict(set)
          rep = []
          prev = None
          for i, char in enumerate(line):
               if prev is not None:
                    overlap_check[prev+char].add(i)
                    overlap_check[prev+char].add(i-1)
               if len(rep) == 2:
                    if char == rep[0]:

                         rep_check = True
               
                    rep.pop(0)
               rep.append(char)
               

               prev = char

               
          if rep_check and any([len(i) >= 4 for i in overlap_check.values()]):
               count += 1


     return count



tests = [["aaa"],
     ["qjhvhtzxzqqjkmpb"],
         ["xxyxx"],
         ["uurcxstgmygtbstg"],         
         ["ieodomkazucvgmuy"],
         input_data]
results = [0, 1, 1, 0, 0, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     elif result_needed == None:
          print(f"Is {result_given} your final answer?")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
     input()

