import os
from math import sqrt

INPUT_DATA_FILE = 'input.txt'

cached_lengths = {}


def calculate_length(peak1: tuple, peak2: tuple):
    x1, y1 = peak1
    x2, y2 = peak2

    edge1, edge2 = sorted((x2 - x1, abs(y2 - y1)))
    length = cached_lengths.get((edge1, edge2))

    if not length:
        length = sqrt(edge1 ** 2 + edge2 ** 2)
        cached_lengths[(edge1, edge2)] = length

    return length


def main():
    assert os.path.exists(INPUT_DATA_FILE), f'Create a file "{INPUT_DATA_FILE}" with input data to run the script.'

    funicular_length = 0
    last_peak = (0, 0)
    last_highest_peak_id, last_highest_peak = 0, (0, 0)

    with open(INPUT_DATA_FILE) as input_data_file:
        input_data_file.readline()  # Skip count of peaks in data file

        for peak_id, peak in enumerate(input_data_file):
            peak = tuple(map(int, peak.split()))

            funicular_length += calculate_length(last_peak, peak)
            last_peak = peak

            if peak[1] >= last_highest_peak[1]:
                if peak_id > last_highest_peak_id + 1:
                    funicular_length += calculate_length(last_highest_peak, peak)
                last_highest_peak_id, last_highest_peak = peak_id, peak

    return funicular_length


if __name__ == '__main__':
    print(main())
