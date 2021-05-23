from re import match
from hashlib import md5

input_data = "bgvyzdsv"

def solve(data):
     solved = False
     num = 1
     while not solved:

          this_hash = md5((data+str(num)).encode()).hexdigest()

          if this_hash.startswith("000000"):
               return num
          num += 1
     
     



tests = ["abcdef", "pqrstuv", input_data]
results = [609043, 1048970, None]

for i, (test, result_needed) in enumerate(zip(tests, results)):

     result_given = solve(test)
     if  result_given == result_needed:
          print(f"Test {i+1} successful.")
     elif result_needed == None:
          print(f"Is {result_given} your final answer?")
     else:
          print(f"Test {i+1} unsuccessful.")
          print(f"Received {result_given} but wanted {result_needed}")
