#!/usr/bin/python3
"""_summary_
    """
from sys import stdin
import sys


def main():
    """_summary_
    """
    file_size = 0
    counter = 0

    sts_codes = {200: 0, 301: 0, 400: 0,
                 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            counter += 1
            strlen = len(line.split())
            if strlen < 9:
                continue

            if strlen == 9:
                code = line.split()[7]
                sts_codes[int(code)] += 1
                file_size += int(line.split()[8])
            if counter == 10:
                counter = 0

                print("File size: {}".format(file_size))
                for key, value in sorted(sts_codes.items()):
                    if value:
                        print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        counter = 0

        print("File size: {}".format(file_size))
        for key, value in sorted(sts_codes.items()):
            if value:
                print("{}: {}".format(key, value))

    print("File size: {}".format(file_size))
    for key, value in sorted(sts_codes.items()):
        if value:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    main()
