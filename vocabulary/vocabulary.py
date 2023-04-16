import pickle

class Vocabulary:
    def __init__(self):
        """
        Initialiser le vocabulaire
        """
        self.vocab = {}
        self.id2word = {}
        self.counter = 1
        self.counter_total = [0]
        self.nb_documents = 0

    def update(self, text):
        """
        Mettre à jour le vocabulaire à partir d'une chaîne de caractères.
        """
        text = str(text)
        for word in text.split():
            get = self.vocab.get(word, 0)
            if get == 0:
                self.vocab[word] = self.counter
                self.id2word[self.counter] = word
                self.counter += 1
        self.counter_total.append(self.counter)
        self.nb_documents += 1

    def word_to_id(self, word):
        """
        Retourner l'identifiant unique d'un mot.
        """
        word_id = self.vocab.get(word)
        if word_id is None:
            raise KeyError(f"Le mot '{word}' n'existe pas dans le vocabulaire")
        return word_id

    def id_to_word(self, id):
        """
        Retourner le mot correspondant à un identifiant unique.
        """
        word = self.id2word.get(id)
        if word is None:
            raise KeyError(f"L'identifiant '{id}' n'existe pas dans le vocabulaire")
        return word

    def save(self, filepath):
        """
        Sauvegarder l'objet Vocabulary dans un fichier pickle.
        """
        with open(filepath, 'wb') as f:
            pickle.dump(self.__dict__, f)

    def load(self, filepath):
        """
        Charger l'objet Vocabulary depuis un fichier pickle.
        """
        with open(filepath, 'rb') as f:
            obj = pickle.load(f)
            self.vocab = obj['vocab']
            self.id2word = obj['id2word']
            self.counter = obj['counter']
            self.counter_total = obj['counter_total']
            self.nb_documents = obj['nb_documents']
