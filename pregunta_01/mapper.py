#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "main":
    for line in sys.stdin:
    line = line.strip()
    splits = line.split(',')
    print(splits[2] + '\t' + '1')