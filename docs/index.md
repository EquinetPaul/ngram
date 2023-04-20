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

Dans la phrase *"The capital of France is..."*, ce qui nous pousse à répondre *"Paris"* est le fait que l'on a capté les mots *"capital"* et *"France"* et qu'en les associant, le mot qui nous vient ensuite est "Paris". En quelque sorte, notre esprit a fait la somme de ces deux termes et en a conclu qu'il en résultait *"Paris"*. On pourrait résumer ce mécanisme à:
> *"capital"* + *"France"* = *"Paris"*

Ce mecanisme qui est naturel chez nous est ce que l'on appelle un **mechanisme d'attention**. Notre cerveau a associé différentes informations via ce mechanisme pour produire quelque chose.

Maintenant, si l'on souhaite entraîner un modèle étant capable de reproduire de mechanisme d'attention, il faudrait se pencher sur les algorithmes de réseaux de neurones profonds utilisant une structure Transformer ou récurrente.

Cependant, étant donné que ce projet a pour but de nous initier aux modèles de langage génératifs, nous allons réfléchir à un moyen plus simple, en terme de compréhension, pour entraîner et utiliser ce genre de modèle.

Si je souhaite entraîner un modèle capable de prédire le mot qui suit une séquence donnée et que je vous donne la phrase:

* *the present and the future*

L'une des méthode qui nous vient en tête est de se dire: je prends les mots un à un et je regarde le mot qui vient après.

De cette manière j'obtiens la fréquence d'apparition d'un mot par rapport à un autre et donc la probabilité par exemple que le mot *"the"* soit suivi de "*present*" ou de *"future"*.

C'est de cette manière que l'on construire des modèles de langage probabilistes ou fréquentiels que l'on appelle aussi des N-gram.

<!-- ![Schéma](/img/ngram1.gif) -->

## Probabilistic Models

Comme vu précedemment, nous pouvons étudier des phrases en prenant chacun des mots qui la composent et déterminer la probabilité qu'un mot puisse succèder à un autre.

La méthode utilisée permet d'obtenir des probabilités pour des mots les uns après les autres.

C'est à dire que pour la phrase *"the present and <mark>the</mark>"* on ne se basera que sur le mot *<mark>the</mark>* pour prédire le prochain mot. Dans ce cas, on aurait:

- 50% de chance de prédire *future*
- 50% de chance de prédire *present*

Dans le GIF précedent on voit comment on peut calculer les probabilités sur une phrase (*the present and the future*) mais l'objectif serait d'avoir un corpus de phrase de grande taille pour varier les combinaisons de phrases et donc d'associations de mots. Ce qui nous permettrait de varier les générations et de limiter les répétitions.

Malgré cela, le fait de ne se contenter que du mot précédent pour prédire celui d'après peut mener à certaines générations non pertinentes voire absurdes.

Par exemple, si on entraîne un modèle sur les phrases:

-  *the chiken is in the farm*
-  *the shark is in the sea*

Il sera très probable si en entrée on lui donne *the chicken is in the* qu'il complète par **sea**.

- *the chiken is in the <mark>sea</mark>*

Surprenant! Mais bon c'est logique étant donné que le modèle s'est entraîné à prédire la suite d'une phrase en ne se basant que sur le dernier mot.

Pour remédier à ce problème, on pourrait envisager de prendre en considération plus d'éléments dans la phrase, plus de mots pour avoir plus de contexte.

C'est à ce moment qu'interviennent les N-grams!

## N-gram

En traitement du langage naturel (NLP), les N-grams font partie des modèles de langage génératifs probabilistes. Ils utilisent les séquences des "n" mots précédents pour s'entraîner et fournir la probabilité du mot suivant.

Dans les exemples précédents, nous prenions uniquement le mot précédent pour prédire celui d'après, nous étions dans le cas d'un 1-gram ou unigramme.

Voici la liste des différents types de n-grams et exemples de génération

<span style="background-color: #7FB3D5">input</span>
<span style="background-color: #F7DC6F">context</span>
<span style="background-color: #82E0AA">generated word</span>
<span style="background-color: #E5E8E8">associated probability</span>


- n=1, unigramme

    - *<span style="background-color: #7FB3D5">the</span> shark is in <span style="background-color: #F7DC6F">the</span> <span style="background-color: #82E0AA">chicken</span> - <span style="background-color: #E5E8E8">0.25</span>*
    - *<span style="background-color: #7FB3D5">the</span> shark is in <span style="background-color: #F7DC6F">the</span> <span style="background-color: #82E0AA">shark</span> - <span style="background-color: #E5E8E8">0.25</span>*

- n=2, bigramme

    - *<span style="background-color: #7FB3D5">the</span> shark is <span style="background-color: #F7DC6F">in the</span> <span style="background-color: #82E0AA">farm</span> - <span style="background-color: #E5E8E8">0.5</span>*


- n=3, trigramme

    - *<span style="background-color: #7FB3D5">the</span> shark <span style="background-color: #F7DC6F">is in the</span> <span style="background-color: #82E0AA">farm</span> - <span style="background-color: #E5E8E8">0.5</span>*

- n=4, quadrigramme

    - *<span style="background-color: #7FB3D5">the</span> <span style="background-color: #F7DC6F">shark is in the</span> <span style="background-color: #82E0AA">sea</span> - <span style="background-color: #E5E8E8">1.0</span>*

- ...

On pourrait construire des n-grams très grands pour conserver le plus de contexte possible et obtenir des prédictions justes mais il faut se rappeler que les n-grams sont des modèles probabilistes. C'est à dire qu'ils fournissent des probabilités uniquement sur les données sur lesquelles ils ont été entrainés. De ce fait, plus on agrandira la fenêtre de contexte, plus le modèle apprendra effectivement des relations précises mais ces relations seront fortement influencées par la taille du corpus d'entraînement.

Si dans mon corpus j'ai des phrases courtes, disons de longueure fixe maximale 6, et que j'entraîne un modèle n-gram où n=5, le modèle sera en mesure de reproduire exactement les phrases du corpus étant donné que sa fenêtre de contexte couvrira presque la phrase entière.

Mais à partir du moment où on agrandit le corpus, on augmente les combinaisons possibles et de cette manière on introduit plus de diversité dans les probabilités et donc dans les possiblités de génération.

Comme vu plus haut pour les unigrammes, les n-grams prendront des séquences des n prédécents mot pour prédire le prochains sur toute la phrase.

Exemple avec n=3:

<span style="background-color: #F7DC6F">n sequence</span>
<span style="background-color: #82E0AA">next</span>

- <span style="background-color: #F7DC6F">the chiken is</span> <span style="background-color: #82E0AA">in</span> the farm
- the <span style="background-color: #F7DC6F">chiken is in</span> <span style="background-color: #82E0AA">the</span> farm
- the chiken <span style="background-color: #F7DC6F">is in the</span> <span style="background-color: #82E0AA">farm</span>

Nous aurons donc un modèle n-gram où n=3, qui sur cette phrase, ressemblerait à:

```
{
  "the chiken is" : {"in" : 1},
  "chiken is in" : {"the" : 1},
  "is in the" : {"farm" : 1}
}
```


Ce projet a pour but de mettre en place un algorithme permettant d'entraîner et d'utiliser des n-grams.

## Ressources

More ressources for more understanding

* [N-gram Wikipedia](https://en.wikipedia.org/wiki/N-gram)
* [Understanding Word N-grams and N-gram Probability in Natural Language Processing](https://towardsdatascience.com/understanding-word-n-grams-and-n-gram-probability-in-natural-language-processing-9d9eef0fa058)
