# Librairies
import vocabulary
from tqdm import tqdm
import matplotlib.pyplot as plt

# Load Data
    ## Speeches
    # import pandas as pd
    # df = pd.read_csv("../data/speeches/discours_emmanuel_macron.csv", encoding="utf-8", sep=";")

from glob import glob
files = glob("../data/clean_books/*.txt")

# Create Vocabulary
vocab = vocabulary.Vocabulary()

# Train Vocabulary
for file in tqdm(df["speech"]):
    with open(file, mode="r", encoding="utf-8") as fp:
        text = fp.read()
        vocab.update(file)

# Save Vocabulary
vocab.save("data/chirac.vocab")
