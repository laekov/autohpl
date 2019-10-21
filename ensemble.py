#!/usr/bin/python3 -u

def main():
    with open('run_hpl.log', 'r') as f:
        lines = f.readlines()
        clogs = [tuple(map(float, li.split(' '))) for li in lines if len(li) > 2]
    with open('power.log', 'r') as f:
        lines = f.readlines()
        plogs = [tuple(map(float, li.split(' '))) for li in lines if len(li) > 2]
    with open('power_ctl.in', 'w') as f:
        for pc in clogs:
            mxp = 0
            while plogs[0][0] < pc[0]:
                mxp = max(mxp, plogs[0][1])
                plogs.pop(0)
            f.write('{} {}\n'.format(mxp, int(pc[1])))


if __name__ == '__main__':
    main()

