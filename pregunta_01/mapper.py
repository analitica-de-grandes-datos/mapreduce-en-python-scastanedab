#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "**main**":
    for line in sys.stdin:
        sys.stdout.write("{}\t1\n".format(line.split(",")[2]))