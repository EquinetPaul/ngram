# import ngram
# import vocabulary
import random

def tokenize(vocab, text):
    return " ".join(str(vocab.word_to_id(t)) for t in text.split())

def reverse(vocab, tokens):
    return " ".join(str(vocab.id_to_word(int(t))) for t in tokens.split())

def generate(model, vocab, nb_samples, start):
    for _ in range(nb_samples):
        sentence = start
        # while len(sentence.split()) <= 50:
        #     tokens = tokenize(vocab, sentence)
        #     if gram.n>1:
        #         current_sequence = tuple(tokens.split()[-gram.n:])
        #     else:
        #         current_sequence = tokens.split()[-1]
        #     tokens += " " + random.choices(list(gram.chain[current_sequence].keys()), weights=list(gram.chain[current_sequence].values()))[0]
        #     sentence = reverse(vocab, tokens)
        while sentence[-1] not in [".", "!", "?"]:
            tokens = tokenize(vocab, sentence)
            if model.n>1:
                current_sequence = tuple(tokens.split()[-model.n:])
            else:
                current_sequence = tokens.split()[-1]
            tokens += " " + random.choices(list(model.chain[current_sequence].keys()), weights=list(model.chain[current_sequence].values()))[0]
            sentence = reverse(vocab, tokens)
        print(sentence)
        print()

# def main(nb_samples=10):
#     vocab = vocabulary.Vocabulary()
#     vocab.load("data/books.vocab")
#
#     gram = ngram.Ngram()
#     gram.load("data/books_11.ngram")
#
#
#     for _ in range(nb_samples):
#         sentence = "Le"
#         # while len(sentence.split()) <= 50:
#         #     tokens = tokenize(vocab, sentence)
#         #     if gram.n>1:
#         #         current_sequence = tuple(tokens.split()[-gram.n:])
#         #     else:
#         #         current_sequence = tokens.split()[-1]
#         #     tokens += " " + random.choices(list(gram.chain[current_sequence].keys()), weights=list(gram.chain[current_sequence].values()))[0]
#         #     sentence = reverse(vocab, tokens)
#         while sentence[-1] not in [".", "!", "?"]:
#             tokens = tokenize(vocab, sentence)
#             if gram.n>1:
#                 current_sequence = tuple(tokens.split()[-gram.n:])
#             else:
#                 current_sequence = tokens.split()[-1]
#             tokens += " " + random.choices(list(gram.chain[current_sequence].keys()), weights=list(gram.chain[current_sequence].values()))[0]
#             sentence = reverse(vocab, tokens)
#         print(sentence)
#         print()
#
#
#
# if __name__ == "__main__":
#     main()
