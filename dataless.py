import math
import random
from sequence_modalities import SEQUENCES

RAND_OFFSET = 0.42

class DataLess:
    def __init__(self):
        print("Initializing DataLess")

    def rand_price_between(self, low, high):
        if low is None or high is None:
            raise ValueError("Please ensure you have supplied a high and low")
        return round(random.uniform(low, high), 2)

    def low_and_high_seq_offset(self, price):
        offset = (price * RAND_OFFSET / 100)
        return self.rand_price_between(price - offset, price + offset)

    def new_seq_num(self, start_price, percent):
        num = start_price + (start_price * percent / 100)
        return self.low_and_high_seq_offset(num)

    def build_sequences(self, start_price, count):
        if start_price is None or count is None:
            raise ValueError("Please ensure you have supplied a target start price and sequence count")
        if count < 8:
            raise ValueError("Please ensure that count is >= 8")
        sequences = []
        for sequence_name in SEQUENCES.keys():
            new_sequence = self.create_sequence(start_price, count, SEQUENCES[sequence_name])
            sequences.append(new_sequence)
        return sequences

    def create_sequence(self, start_price, count, modality_markers):
        sequence = []
        prices_per_marker = math.floor(count / len(modality_markers))
        for percentage_mark in modality_markers:
            pm_index = modality_markers.index(percentage_mark)
            if pm_index < (len(modality_markers) - 1):
                seq_pct_diff = modality_markers[pm_index + 1] - percentage_mark
                percentage_step = seq_pct_diff / prices_per_marker
                for i in range(prices_per_marker):
                    sequence.append(self.new_seq_num(start_price, percentage_mark + i * percentage_step))
            elif pm_index == (len(modality_markers) - 1):
                    sequence.append(self.new_seq_num(start_price, percentage_mark))
        return sequence
