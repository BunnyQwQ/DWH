import sys

current_key = None
current_count = 0

for line in sys.stdin:
    date, site, count = line.strip().split('\t')
    if (date, site) == current_key:
        current_count += int(count)
    else:
        if current_key is not None:
            print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")
        current_key = (date, site)
        current_count = int(count)

if current_key is not None:
    print(f"{current_key[0]}\t{current_key[1]}\t{current_count}")
