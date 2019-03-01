import pandas as pd
import os

def main():
    data_dir = "../data/"

    for fname in os.listdir(data_dir):
        df = pd.read_csv(f"{data_dir}{fname}", header=9)
        mark_col = df["CH20"].tolist()
        marks = [i for i, mark in enumerate(mark_col) if mark == 5]
        cleaned = [mark for i, mark in enumerate(marks) if mark-1 != marks[i-1]]
        print(fname[0:4])
        print(len(cleaned))

if __name__ == "__main__":
    main()
