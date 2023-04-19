import logging

import vocabulary
import ngram

import json
from glob import glob
from tqdm import tqdm
import time
import random

logging.basicConfig(format='%(levelname)s %(asctime)s - %(message)s', level=logging.INFO)

def load_config():
    """
    Fonction permettant de charger le fichier de configuration config.json et de le charger en tant que dictionnaire Python.
    """
    try:
        logging.info("Loading configuration...")
        with open('config.json') as json_config_file:
            config = json.load(json_config_file)
        logging.info("Loaded.")
        return config
    except Exception as e:
        logging.error("Error while loading configuration file 'config.json'.")
        logging.error(e)
        logging.error("Exiting.")
        sys.exit(1)
        raise

def load_models(generate_name, max_ngram_to_use):
    logging.info("Loading models...")
    sub_folders = glob(f"data/ngram/{generate_name}/*")
    models = {}
    for folder in sub_folders:
        n = int(folder.split("\\")[-1])

        if n > max_ngram_to_use:
            break

        logging.info(f"\tLoading Ngram model, n={n}...")

        temp_ngram = ngram.Ngram()
        path_model = glob(f"{folder}/*.ngram")
        temp_ngram.load(path_model[0])

        models[n] = temp_ngram

    return models

class Sentence:
    def __init__(self, start=""):
        self.s = start
        self.models_used = []

def generate_sentence(models, vocab, starts_with, min_words, end_char, display_model_used):
    model_keys = list(models.keys())
    max_models = max(model_keys)
    word_count = 1
    sentence = starts_with

    models_used = []
    model_using = 0

    while word_count <= min_words:
        probas = {}
        diff = 0

        while probas == {}:
            # Tokenize the sentence
            sentence_tokenized = vocab.chain_to_ids(sentence).split()

            # Select the model to use, if possible
            try:
                if len(sentence_tokenized[-max_models+diff:]) == 1:
                    last_n_tokens = int(sentence_tokenized[-1])
                    model = models[1]
                    model_using = 1
                else:
                    last_n_tokens = tuple(map(int, sentence_tokenized[-max_models+diff:]))
                    model = models[len(last_n_tokens)]
                    model_using = len(last_n_tokens)
            except:
                diff += 1

            # Select probas associated with the actual word/sequence of the selected model
            probas = model.chain_frequency.get(last_n_tokens, {})

            if probas == {}:
                diff += 1

        models_used.append(model_using)

        # Select the next word
        next_word = random.choices(list(probas.keys()), weights=list(probas.values()), k=1)[0]

        # Add the new word to the sentence
        sentence_tokenized.append(str(next_word))

        # Un-Tokenize
        sentence = vocab.ids_to_chain(" ".join(sentence_tokenized))
        word_count = len(sentence.split())

        if word_count > min_words and sentence[-1] not in end_char:
            min_words += 1


    result = Sentence()
    result.s = sentence
    result.models_used = models_used

    return result

def main():
    config = load_config()
    generate_name = config["generate_name"]
    nb_sentences_to_generate = config["nb_sentences_to_generate"]
    starts_with = config["starts_with"]
    delay = config["delay"]
    starts_with = config["starts_with"]
    min_words = config["min_words"]
    end_char = config["end_char"]
    display_model_used = config["display_model_used"]
    max_ngram_to_use = config["max_ngram_to_use"]

    logging.info(f"Loading vocabulary...")
    vocab = vocabulary.Vocabulary()
    vocab.load(f"data/vocabs/{generate_name}.vocab")
    logging.info(f"Loaded.")

    models = load_models(generate_name, max_ngram_to_use)
    logging.info(f"{len(models)} models loaded.")

    logging.info(f"Generating {nb_sentences_to_generate} sentences...")
    sentences = [generate_sentence(models, vocab, starts_with, min_words, end_char, display_model_used) for _ in range(nb_sentences_to_generate)]

    for sentence in sentences:
        time.sleep(random.uniform(0, delay+1))
        logging.info(sentence.s)
        if display_model_used:
            logging.info(sentence.models_used)
        print()

if __name__ == '__main__':
    main()
