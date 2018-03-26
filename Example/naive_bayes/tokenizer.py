"""
Chapter 4. Naive Bayesian Classification
Text tokenizer
"""
import re


class Tokenizer:
  """
  Splits lines by whitespaces, converts to lower case and builds n-grams.
  """
  NULL = u'\u0000'

  @staticmethod
  def tokenize(string):
    return re.findall("\w+", string.lower())

  @staticmethod
  def unique_tokenizer(string):
    return set(Tokenizer.tokenize(string))

  @staticmethod
  def ngram(string, ngram):
    tokens = Tokenizer.tokenize(string)

    ngrams = []

    for i in range(len(tokens)):
      shift = i - ngram + 1
      padding = max(-shift, 0)
      first_idx = max(shift, 0)
      last_idx = first_idx + ngram - padding

      ngrams.append(Tokenizer.pad(tokens[first_idx:last_idx], padding))

    return ngrams

  @staticmethod
  def pad(tokens, padding):
    padded_tokens = []

    for i in range(padding):
      padded_tokens.append(Tokenizer.NULL)

    return padded_tokens + tokens
