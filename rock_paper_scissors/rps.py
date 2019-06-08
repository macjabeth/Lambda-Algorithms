#!/usr/bin/python

import sys


def rock_paper_scissors(rounds):
    plays = ['rock', 'paper', 'scissors']
    result = []
    def rps(r=[], rn=1):
        for play in plays:
            r.append(play)
            if rn == rounds:
                result.append(r[:])
            else:
                rps(r, rn + 1)
            r.pop()
    rps()
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
