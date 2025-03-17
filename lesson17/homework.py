import re

# Task1
print("Task1")
lines = ["cat", "dog", "category", "scatter", "wildcat", "empty", "words"]
pattern = r"cat"

for line in lines:
    if re.search(pattern, line):
        print(line)

# Task2
print("\nTask2")
lines = ["zabz", "z123z", "zzz", "zabcde", "z1z2z"]
pattern = r"z.{3}z"

for line in lines:
    if re.search(pattern, line):
        print(line)

# Task3
print("\nTask3")
lines = ["89001234567", "8900123456", "3900123456", "9001234567", "z1z2z"]
pattern = r"[89]\d{9}"

for line in lines:
    if re.search(pattern, line):
        print(line)

# Task4
print("\nTask4")

text = "The quick brown fox jumps over the lazy dog. Apple."
pattern = r"\b[AEIOUaeiou]\w*"

matches = re.findall(pattern, text)
print(*matches)

# Task5
print("\nTask5")

text = "The temperature is -15 degrees and speed 15 m-s"
pattern = r"-?\d+"

matches = re.findall(pattern, text)
print(*matches)

# Task6
print("\nTask6")

lines = ["I am a human.", "Humans are humans.", "I'm human, not robot."]
pattern = r"human"
replacement = "computer"

for line in lines:
    new_line = re.sub(pattern, replacement, line, flags=re.IGNORECASE)
    print(new_line)

# Task7
print("\nTask7")

text = "The date today is 17-03-2025, next day is 18-03-2025."
pattern = r"\d{2}-\d{2}-\d{4}"

matches = re.findall(pattern, text)
print(*matches)

# Task8
print("\nTask8")

text = "The big brown bear like the wildberries. igb"
pattern = r"(\w+?b\w+|b\w+|\w+b)"

matches = re.findall(pattern, text)
print(*matches)

# Task9
print("\nTask9")

lines = ["Hello", "keeper", "committee", "mississippi", "book", "wildberries"]
pattern = r"(\w)\1+"

for line in lines:
    new_line = re.sub(pattern, r"\1", line)
    print(new_line)