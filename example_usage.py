from dataless import DataLess

#STARTING_PRICE is the price where you want your sequence of output to base from
STARTING_PRICE = 478.34
#DATA_POINT_COUNT is the number of desired output values per sequence
DATA_POINT_COUNT = 42

dl = DataLess()
data = dl.build_sequences(STARTING_PRICE, DATA_POINT_COUNT)

for seq_output_data in data:
    print(seq_output_data)
