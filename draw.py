import os
import argparse
import numpy as np
import matplotlib.pyplot as plt


def draw(path: str, section: int, colors: tuple[str, str], label: str) -> None:
    scores = []

    with open(path) as txt_file:
        for line in txt_file:
            scores = list(map(lambda x: int(x), line.split()))

    max_scores = np.max(np.array(scores).reshape(-1, section), axis=1)
    mean_scores = np.mean(np.array(scores).reshape(-1, section), axis=1)

    plt.plot(max_scores, color=colors[0], label=f'{label} (max)')
    plt.plot(mean_scores, color=colors[1], label=f'{label} (mean)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--section', type=int, default=100)
    args = parser.parse_args()

    plt.figure(figsize=(8, 6))

    plt.xlabel(f'epoch ({args.section} elements / section)')
    plt.ylabel('score')

    if os.path.exists('score_before.txt'):
        draw('score_before.txt', args.section, ('cornflowerblue', 'maroon'), 'before state')

    if os.path.exists('score_after.txt'):
        draw('score_after.txt', args.section, ('navy', 'tomato'), 'after state')

    plt.legend()

    plt.show()
