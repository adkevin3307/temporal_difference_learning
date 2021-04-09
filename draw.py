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
    parser.add_argument('-f', '--files', nargs='+', required=True)
    args = parser.parse_args()

    colors = [('cornflowerblue', 'maroon'), ('navy', 'tomato')]

    plt.figure(figsize=(8, 6))

    plt.xlabel(f'epoch ({args.section} elements / section)')
    plt.ylabel('score')

    for i, score_file in enumerate(args.files):
        if os.path.exists(score_file):
            draw(score_file, args.section, colors[i], score_file.split('.')[0])

    plt.legend()

    plt.show()
