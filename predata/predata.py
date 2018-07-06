import random

if __name__ == '__main__':

    rf = open('seed_nodes.tsv', 'r')
    result = []
    for line in open('seed_nodes.tsv'):
        num = random.randint(0, 100)
        if num < 1:
            line = rf.readline()
            result.append(line)
    rf.close()

    wf = open('seed_nodes2.tsv', 'w')
    wf.write('%s' % ''.join(result))
