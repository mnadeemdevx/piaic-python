s:str ="   Python is fun!   "

stripped: str = s.strip()
leftJustify: str = stripped.ljust(20, "*")
rightJustify: str = stripped.rjust(20, "*")

print(stripped)
print(leftJustify)
print(rightJustify)