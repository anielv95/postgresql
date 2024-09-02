# Latent Dirichlet Allocation

1. This model is useful to create clusters of topics 
2. The core ideas behind this model is finding 2 probabilities distributions
    1. First probability distribution is the topic distribution over the documents
    2. Second probability distribution is the word distribution over the topics
3. As it is a bag of words model the preprocessing stage is too much relevant
4. As English is weakly inflected language we can see that many words are derived from anothers words. For example "normality" is derived from the word "norm", which is the root form. All inflected languages consist of words with common root forms, but the degree of inflection varies based on the language. [Source](https://www.datacamp.com/tutorial/stemming-lemmatization-python)
5. Stemming and Lemmatization are process in NLP to find the root part in inflected words and are very important in preprocesing stages. [NLTK](https://www.nltk.org) library let us do it easily. [Source](https://www.datacamp.com/tutorial/stemming-lemmatization-python)
    1. Stemming is a technique used to reduce an inflected word down to its word stem. For example, the words “programming,” “programmer,” and “programs” can all be reduced down to the common word stem “program.” [Source](https://www.datacamp.com/tutorial/stemming-lemmatization-python)
    2. Lemmatization is another technique used to reduce inflected words to their root word. It describes the algorithmic process of identifying an inflected word’s “lemma” (dictionary form) based on its intended meaning. For example, you can expect a lemmatization algorithm to map “runs,” “running,” and “ran” to the lemma, “run.” [Source](https://www.datacamp.com/tutorial/stemming-lemmatization-python)
6. The training process could be performed with Gibbs sampling method which tries to match as much as possible the following premises:
    1. Every document has a central topic.
    2. Every word belongs to a single topic.

## References:

[Training Latent Dirichlet Allocation: Gibbs Sampling (Part 2 of 2)](https://www.youtube.com/watch?v=BaM1uiCpj_E)
[Latent Dirichlet Allocation (Part 1 of 2)](https://www.youtube.com/watch?v=T05t-SqKArY)
[LDA Topic Models](https://www.youtube.com/watch?v=3mHy4OSyRf0)
[Latent Dirichlet Allocation](https://radimrehurek.com/gensim/models/ldamodel.html)
[Topic Modeling in Python: Latent Dirichlet Allocation (LDA)](https://towardsdatascience.com/end-to-end-topic-modeling-in-python-latent-dirichlet-allocation-lda-35ce4ed6b3e0)
