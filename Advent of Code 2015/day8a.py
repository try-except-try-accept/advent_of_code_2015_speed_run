from re import search, match, findall
from collections import Counter
from helpers import PuzzleHelper

PP_ARGS = False, False #rotate, cast int

DAY = 8
TEST_DELIM = "---"
FILE_DELIM = "\n"
TESTS = r"""""
"abc"
"aaa\"aaa"
"\x27"
///12"""

DEBUG = True


def solve(data):
    
    string_code = 0
    memory = 0
    for row in data:
        print(row)
        string_code += len(row)
        memory += len(eval(row))
    

    return string_code - memory




if __name__ == "__main__":
    p = PuzzleHelper(DAY, TEST_DELIM, FILE_DELIM, DEBUG, PP_ARGS)

    if p.check(TESTS, solve):
        puzzle_input = p.load_puzzle()
        puzzle_input = p.pre_process(puzzle_input, *PP_ARGS)
        print("FINAL ANSWER: ", solve(puzzle_input))
