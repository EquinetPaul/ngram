import vocabulary
import ngram
import logging

from tqdm import tqdm
from glob import glob

import pandas as pd

name  = "books"

vocab = vocabulary.Vocabulary()
vocab.load("data/"+name+".vocab")

gram = ngram.Ngram(n=3)

# df = pd.read_csv("../data/speeches/discours_emmanuel_macron.csv", encoding="utf-8", sep=";")
files = glob("../data/clean_books/*.txt")

# Train Ngram
for file in tqdm(files):
    with open(file, mode="r", encoding="utf-8") as fp:
        content = fp.read()
        text = " ".join([str(vocab.word_to_id(t)) for t in content.split()])
    gram.train(text)

logging.warning("Normalization")
gram.normalize()

logging.warning("Saving")
gram.save("data/"+name+"_"+str(gram.n)+".ngram")
