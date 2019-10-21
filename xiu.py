#!/usr/bin/python3
import math

learning_rate = 0.1

def main():
    powers = []
    cpus = []
    with open('power_ctl.in', 'r') as f:
        for l in f:
            ls = l.split()
            p, c = int(float(ls[0])), int(ls[1])
            powers.append(p)
            cpus.append(c)
    for i in range(len(cpus) - 1):
        if powers[i + 1] == 0:
            continue
        delta = (300 - powers[i + 1]) * learning_rate
        cpus[i] = int(cpus[i] + delta)
    with open ('power_ctl.in', 'w') as f:
        for i, p in zip(powers, cpus):
            f.write('{} {}\n'.format(i, p))

if __name__ == '__main__':
    main()

