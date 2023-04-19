# NGRAM for NLP

<!-- For full documentation visit [mkdocs.org](https://www.mkdocs.org). -->

## What is it?

**NGRAM for NLP** is a set of scripts and algorithms for training and using probabilistic/statistical ** generative language models** such as n-grams

Since the emergence of Transformer models in 2017 with the scientific paper ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762), which led to the appearance of highly performant generative language models demonstrating capabilities never seen before, this project was initiated based on a state-of-the-art of generative language models proposed by Paul Equinet as part of his final year project to complete his engineering degree in applied mathematics at CyTech Pau.

The aim of this project and its associated documentation is to provide pedagogical tools for understanding language models.

## Generative Language Models
Generative language models are artificial intelligence models that learn to produce text, speech, or other forms of linguistic data similar to those produced by humans.

If I give you the phrase

- The capital of France is...

you would be tempted to answer 'Paris'.

For the phrase

- The cat eats the...

you would probably answer 'mouse'.

Well, that's what language models do. They use the data given to them and select/predict THE next word that has the highest probability of appearing next.

In an iterative process, it uses the input sequence given to it and the sequences it has generated to produce the next sequence. In this way, it constructs entire sentences or entire paragraphs.
