import sys

for line in sys.stdin:
    for word in line.split():
        if len(word) > 4:
            print(f"{word}\t1")
