s:str ="the quick brown fox jumps over the lazy dog"

startingIndex: int = s.find("fox")
countValue: int = s.count("the")

print(f"index of 'fox' is {startingIndex}")
print(f"'the' appears {countValue} times")