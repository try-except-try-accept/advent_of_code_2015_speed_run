from re import match

with open("day7.txt") as f:
     input_data = [line.strip() for line in f.readlines()]



def eval_not(exp, wires):

     result = [0] * 16

     term = exp.replace("NOT ", " ").strip()
     term_as_bin = bin(wires[term])[2:].zfill(16)
     for i, bit in enumerate(term_as_bin):
          result[i] = str(int(not int(bit)))
            

     return int("".join(result), 2)

                    
             



def solve(data):

    

     wires = {}
     line_count = 0
     while len(data):
          line = data[line_count]
          orig = line
          
##   
##          print("Expression")
##          print(line)
          #pseudonymise Python reserved keywords that have been used as gate names
          line = line.replace("is", "xxxx").replace("as", "yyyy").replace("in", "zzzzz").replace("if", "aaaaa")
          
          exp = line.split(" -> ")[0]
          target = line.split(" -> ")[-1]
##          print("Targetr is", target)
##          input()
##       

          try:
               if exp.startswith("NOT"):

                    result = eval_not(exp, wires)

               else:
                    
                    for operator, rep in zip(["AND", "LSHIFT", "RSHIFT", "OR"],
                                       ["&", "<<", ">>", "|"]):

                         if operator in exp:

                              
                              exp = exp.replace(" "+operator+" ", rep)

                              result = eval(exp, {}, wires)
                              print(exp, "result is", result)
               

                       
                    else:
                         result = eval(exp, {}, wires)
               wires[target] = int(result)

               data.remove(orig)
          except Exception as e:
##               print(e)
##               print("Will come back to this line.")
               line_count += 1
          if line_count > len(data) - 1:
               line_count = 0
               
               
          
  
         
 
     for wire, val in wires.items():
          print(f"{wire}: {val}")
     return wires

test1 = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i'''.split("\n")

tests = [test1, input_data]
results = ['''d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456''',
None]

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
