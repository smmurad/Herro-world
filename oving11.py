from sys import stdin, stderr

def test():
    #do nothn
    return 0


def best_path(nm, prob):
    if not (prob[0] and prob[-1]):
        return 0
    addprob = [0 for i in range(len(prob))]
    addprob[0] = prob[0]
    pre = [None for i in range(len(prob))]
    visited = []
    for i in range(len(prob)):
        for j in range(len(nm[i])):
            if(nm[i][j] and pre[i] != j):
                if(addprob[i]*prob[j] > addprob[j]):
                    addprob[j] = addprob[i]*prob[j]
                    pre[j] = i
    backpath = []

    backpath.append(len(prob) - 1)
    current_parent = pre[backpath[-1]]
    while(current_parent):
        backpath.append(current_parent)
        current_parent = pre[backpath[-1]]
    backpath.append(0)
    backpath.reverse()
    new_string = ''
    for i in range(len(backpath)-1):
        new_string += str(backpath[i])
        new_string += '-'
    new_string += str(backpath[-1])

    return new_string

n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities))