import sys

current_date = None
n = 0

for line in sys.stdin:
    date, site, count = line.strip().split('\t')
    if date != current_date:
        current_date = date
        n = 0
    if n < 5:
        print(f"{date}\t{site}\t{count}")
        n += 1
