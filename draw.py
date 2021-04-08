import os
import argparse
import numpy as np
import matplotlib.pyplot as plt


def draw(path: str, average: int, label: str) -> None:
    scores = []

    with open(path) as txt_file:
        for line in txt_file:
            scores = list(map(lambda x: int(x), line.split()))

    scores = np.mean(np.array(scores).reshape(-1, average), axis=1)

    plt.plot(scores, label=label)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--average', type=int, default=100)
    args = parser.parse_args()

    if os.path.exists('score_before.txt'):
        draw('score_before.txt', args.average, 'before state')

    if os.path.exists('score_after.txt'):
        draw('score_after.txt', args.average, 'after state')

    plt.legend()

    plt.show()
