import logging

import vocabulary
import ngram

import json
from glob import glob
from tqdm import tqdm
import time

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

def generate_sentence(models):
    pass

def load_models(generate_name):
    logging.info("Loading models...")
    sub_folders = glob(f"data/ngram/{generate_name}/*")
    models = {}
    for folder in sub_folders:
        n = folder.split("\\")[-1]
        logging.info(f"\tLoading Ngram model, n={n}...")

        temp_ngram = ngram.Ngram()
        path_model = glob(f"{folder}/*.ngram")
        temp_ngram.load(path_model[0])

        models[n] = temp_ngram

def main():
    config = load_config()
    generate_name = config["generate_name"]
    nb_sentences_to_generate = config["nb_sentences_to_generate"]
    delay = config["delay"]

    models = load_models(generate_name)
    logging.info(f"{len(models)} models loaded.")

    # 
    # logging.info(f"Generating {nb_sentences_to_generate} sentences...")
    # sentences = [generate_sentence(models) for _ in range(nb_sentences_to_generate)]
    #
    # for sentence in sentences:
    #     time.sleep(delay)
    #     logging.info(sentence)



if __name__ == '__main__':
    main()
