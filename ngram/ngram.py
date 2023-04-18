import pickle
import random
import copy
import dask.delayed

class Ngram():
    def __init__(self, n=1):
        self.n = n
        self.chain_frequency = {}
        self.chain = {}

    def train(self, text, separator = " "):
        words = text.split(separator)
        for i in range(len(words)-self.n):
            if self.n>1:
                sequence = tuple([int(words[i+y]) for y in range(self.n)])
            else:
                sequence = int(words[i])
            get = self.chain_frequency.get(sequence,0)
            next = int(words[i+self.n])
            if get == 0:
                self.chain_frequency[sequence] = {}
                self.chain_frequency[sequence][next] = 1
            elif get.get(int(words[i+self.n]),0) == 0:
                self.chain_frequency[sequence][next] = 1
            else:
                self.chain_frequency[sequence][next] += 1

    def normalize(self):
        self.chain = copy.deepcopy(self.chain_frequency)
        for key, value in self.chain.items():
            sum_frequency = sum(value.values())
            for k, v in value.items():
                self.chain[key][k] = v / sum_frequency

    def save(self, filepath):
        with open(filepath, 'wb') as save_file:
            pickle.dump(self.__dict__, save_file)

    def load(self, filepath):
        try:
            with open(filepath, 'rb') as load_file:
                obj = pickle.load(load_file)
                self.n = obj["n"]
                self.chain_frequency = obj["chain_frequency"]
                self.chain = obj["chain"]
        except Exception as e:
            print(f"Erreur lors du chargement du fichier {filepath} : {e}")
            self.n = 1
            self.chain_frequency = {}
            self.chain = {}
