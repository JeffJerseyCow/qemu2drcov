#!/usr/bin/python3
import sys
import argparse
from qemu2drcov.core import parsePages, parseTraces, buildDrcov

def main():
    parser = argparse.ArgumentParser('qemu2drcov')
    parser.add_argument('-n', '--name', required=True, type=str,
                        help='Name of binary to trace')
    name = parser.parse_args().name

    inLines = []

    try:
        for line in sys.stdin:
            inLines.append(line.strip())
    except KeyboardInterrupt:
        pass

    pages = parsePages(inLines)
    if not pages or len(pages) <= 0:
        print('Error: Cannot parse memory pages')
        return False

    traces = parseTraces(inLines)
    if not traces or len(traces) <= 0:
        print('Error: Cannot parse code traces')
        return False
    data = buildDrcov(name, pages, traces)
    sys.stdout.buffer.write(data)

    return True

if __name__ == '__main__':
    sys.exit(main())
