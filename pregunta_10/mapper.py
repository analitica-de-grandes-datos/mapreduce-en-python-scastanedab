#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columns = line.strip().split("\t")
        num = columns[0]
        letters = columns[1].split(",")
        for letter in letters:
            sys.stdout.write(f"{num}\t{letter}\n")