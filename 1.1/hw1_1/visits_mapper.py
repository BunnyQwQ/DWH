import sys
import logging

logging.basicConfig(level=logging.INFO)

for line in sys.stdin:
    try:
        site, dt = line.strip().split(';')
        date = dt.split()[0]
        print(f"{date}\t{site}\t1")
    except Exception as e:
        logging.error(f"bad line {line!r}: {e}")
