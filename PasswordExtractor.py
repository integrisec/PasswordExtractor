import sys
import argparse
import os

def extract(input, output, length, lower, upper, number, special):
    lc = set('abcdefghijklmnopqrstuvwxyz')
    uc = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    nc = set('1234567890')
    sc = set('`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?")
    ow = None

    try:
        with open(input, 'r') as i:
            if output:
                if os.path.exists(output):
                    ow = True if raw_input('"' + output + '" already exists. Overwrite? [N/y]: ').lower() == 'y' else False
                else:
                    ow = True

                if ow:
                    o = open(output, 'w+')

            for line in i:
                l = str(line.strip('\n'))

                if len(l) < length:
                    continue

                if lower:
                    if not any((c in lc) for c in l):
                        continue

                if upper:
                    if not any((c in uc) for c in l):
                        continue

                if number:
                    if not any((c in nc) for c in l):
                        continue

                if special:
                    if not any((c in sc) for c in l):
                        continue

                print(l)

                if ow:
                    o.write(l + '\n')

        if o:
            o.close()
    except KeyboardInterrupt:
        exit()

def main(argv):
    parser = argparse.ArgumentParser(description='Password extractor matching a particular policy.')
    parser.add_argument('-i', '--input', default='passwords.txt', help='Password input file (newline separated)', required='False')
    parser.add_argument('-o', '--output', help='Output file containing matching passwords')
    parser.add_argument('-l', '--length', default=1, type=int, help='Minimum password length')
    parser.add_argument('-a', action='store_true', default=False, help='Password contains lowercase character')
    parser.add_argument('-A', action='store_true', default=False, help='Password contains uppercase character')
    parser.add_argument('-n', action='store_true', default=False, help='Password contains number')
    parser.add_argument('-s', action='store_true', default=False, help='Password contains special character')
    args = parser.parse_args()

    extract(args.input, args.output, args.length, args.a, args.A, args.n, args.s)

if __name__ == "__main__":
    main(sys.argv)
