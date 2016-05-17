import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\t')
    spamwriter.writerows([['apple','banana', 'ccc']])