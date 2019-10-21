#!/usr/bin/python3
import os
import sys
import time


workers = 'e[5,8]'
exec_pref = 'sudo clush -b -w {} '.format(workers)
def set_cpu_freq(lvl=None, cpuid=None):
    scr = '/home/laekov/scripts/inspurbaobao{}.sh'.format(cpuid) if cpuid is not None else '/home/sc/baobao/baobaoctl.sh'
    if lvl is None:
        os.system(exec_pref + 'bash {} 255 255'.format(scr))
    elif isinstance(lvl, tuple):
        os.system(exec_pref + 'bash {} {} {}'.format(scr, lvl[0], lvl[1]))
    else:
        os.system(exec_pref + 'bash {} {} {}'.format(scr, lvl, lvl))

def set_gpu_freq(lvl=None):
    gpu_freqs = [135, 142, 150, 157, 165, 172, 180, 187, 195, 202, 210, 217, 225, 232, 240, 247, 255, 262, 270, 277, 285, 292, 300, 307, 315, 322, 330, 337, 345, 352, 360, 367, 375, 382, 390, 397, 405, 412, 420, 427, 435, 442, 450, 457, 465, 472, 480, 487, 495, 502, 510, 517, 525, 532, 540, 547, 555, 562, 570, 577, 585, 592, 600, 607, 615, 622, 630, 637, 645, 652, 660, 667, 675, 682, 690, 697, 705, 712, 720, 727, 735, 742, 750, 757, 765, 772, 780, 787, 795, 802, 810, 817, 825, 832, 840, 847, 855, 862, 870, 877, 885, 892, 900, 907, 915, 922, 930, 937, 945, 952, 960, 967, 975, 982, 990, 997, 1005, 1012, 1020, 1027, 1035, 1042, 1050, 1057, 1065, 1072, 1080, 1087, 1095, 1102, 1110, 1117, 1125, 1132, 1140, 1147, 1155, 1162, 1170, 1177, 1185, 1192, 1200, 1207, 1215, 1222, 1230, 1237, 1245, 1252, 1260, 1267, 1275, 1282, 1290, 1297, 1305, 1312, 1320, 1327, 1335, 1342, 1350, 1357, 1365, 1372, 1380]
    scr = 'nvidia-smi -ac 877,{}'.format(gpu_freqs[lvl])


def set_fan(lvl=None):
    if lvl is None:
        os.system(exec_pref + 'bash /home/laekov/scripts/localfan_supermicro')
    else:
        os.system(exec_pref + 'bash /home/laekov/scripts/localfan_supermicro {}'.format(lvl))



def main():
    with open('power_ctl.in', 'r') as f:
        powers = [int(li.split()[1]) for li in f.readlines() if len(li) > 2]
    ouf = open('run_hpl.log', 'w')
    idx = 0
    set_gpu_freq(166)
    set_fan(80)
    time.sleep(1)
    with os.popen('tail -f process.log', 'r') as f:
        last_p = 55
        set_gpu_freq(last_p)
        for line in f:
            if line.find('PCOL') > -1:
                set_fan(8)
            if line.find('Prog= ') > -1:
                print('{} -> {}'.format(line.rstrip(), powers[idx]))
                ouf.write('{} {}\n'.format(time.time(), powers[idx]))
                if last_p != powers[idx]:
                    set_gpu_freq(powers[idx])
                    last_p = powers[idx]
                if idx + 1 < len(powers):
                    idx += 1
                print('{}: {}'.format(idx, line))
            elif line.find('DONE') > -1:
                print('HPL DONE')
                ouf.close()
                set_gpu_freq(166)
                return
            else:
                print('HPL LOG: ', line.rstrip())


if __name__ == '__main__':
    main()
    set_fan(60)
