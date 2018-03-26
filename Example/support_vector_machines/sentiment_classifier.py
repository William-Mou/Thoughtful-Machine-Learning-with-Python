import io
import os

from numpy import ndarray

from sklearn import svm

from corpus import Corpus
from corpus_set import CorpusSet


class SentimentClassifier(object):
  ext_to_sentiment = {'.pos': 'positive',
                      '.neg': 'negative'}

  number_to_sentiment = {-1: 'negative',
                         1: 'positive'}

  @classmethod
  def present_answer(cls, answer):
    if isinstance(answer, ndarray):
      answer = answer[0]
    return cls.number_to_sentiment[answer]

  @classmethod
  def build(cls, files):
    corpora = []
    for file in files:
      ext = os.path.splitext(file)[1]
      corpus = Corpus(io.open(file, errors='ignore'),
                      cls.ext_to_sentiment[ext])
      corpora.append(corpus)
    corpus_set = CorpusSet(corpora)
    return SentimentClassifier(corpus_set)

  def __init__(self, corpus_set):
    self._trained = False
    self._corpus_set = corpus_set
    self._c = 2 ** 7
    self._model = None

  @property
  def c(self):
    return self._c

  @c.setter
  def c(self, cc):
    self._c = cc

  def reset_model(self):
    self._model = None

  def words(self):
    return self._corpus_set.words

  def classify(self, string):
    if self._model is None:
      self._model = self.fit_model()
    prediction = self._model.predict(self._corpus_set.feature_vector(string))
    return self.present_answer(prediction)

  def fit_model(self):
    self._corpus_set.calculate_sparse_vectors()
    y_vec = self._corpus_set.yes
    x_mat = self._corpus_set.xes
    clf = svm.SVC(C=self.c,
                  cache_size=1000,
                  gamma=1.0 / len(y_vec),
                  kernel='linear',
                  tol=0.001)
    clf.fit(x_mat, y_vec)
    return clf
