import re
import sys
fo=open(sys.argv[1],'r')
fo1=open(sys.argv[2],'w')
strlist=['cuteSV','svim']
for line in fo:
    if line.startswith("#"):
        fo1.write(line)
    else:
        line = line.strip().split()
        if line[3] != 'N':  ###不是N的先输出
            if line[4] == '<DUP>' or line[4] == '<INV>':  ##不是N的里面去掉这两类
                pass
            else:
                fo1.write('\t'.join(line) + '\n')
        else:
            if line[4] == '<INS>' or line[4] == '<DEL>':  ##是N的里面把这两类补齐
                for j in line[9:]:
                    if 'cuteSV' in j or 'svim' in j:
                        line[3] = j.split(":")[8]
                        line[4] = j.split(":")[9]
                        fo1.write('\t'.join(line) + '\n')
                        break
                    else:
                        pass
            else:
                pass
