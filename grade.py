n = int(raw_input())
record = sorted([[raw_input(),float(raw_input())] for i in range(n)])
grade=sorted(set([record[i][1] for i in range(n)]))
second_highest = grade[1]

for x in range(n):
    
    if record[x][1] == second_highest:
        print record[x][0]
