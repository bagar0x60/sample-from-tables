#!/usr/bin/env python

import csv
import random
import sys

STATS_TABLE_SIZE = 400

if __name__ == '__main__':    
    try:
        k = int(sys.argv[1])
        assert 0 <= k <= 400 
    except:
        print(  f'USAGE: get_sample <k>\n'
                f'<k> - sample size, integer from 0 to {STATS_TABLE_SIZE}')
        exit()

    stats_table = []
    with open('stats_tables.csv') as stats_tables_file:
        reader = csv.reader(stats_tables_file)
        for row in reader:
            if row[0] == '':
                continue
            stats_table.extend(zip(row[::2], row[1::2]))

    sample = random.sample(stats_table, k)
    sample.insert(0, ("v", "E"))

    with open(f'sample_{k}.csv', 'w', newline='') as sample_file:
        writer = csv.writer(sample_file)
        writer.writerows(sample)