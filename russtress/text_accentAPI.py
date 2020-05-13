import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout, Activation

import numpy as np
import re
from pathlib import Path
from .tokenizer import tokenize
from .constants import MODEL_FILE, WEIGHTS_FILE, MAXLEN, CHAR_INDICES, REG
from .utils import *


class Accent(object):

    def __init__(self):
        self.model_file = MODEL_FILE
        self.weights_file = str(WEIGHTS_FILE)
        with open(self.model_file, 'r') as content_file:
            json_string = content_file.read()

        tf.keras.backend.clear_session()

        self.model = tf.keras.models.model_from_json(json_string)
        self.model.load_weights(self.weights_file)

    def _predict(self, word):
        x = np.zeros((1, MAXLEN, len(CHAR_INDICES)), dtype=np.bool)
        for index, letter in enumerate(word):
            pos = MAXLEN - len(word.replace("'", "")) + index
            x[0, pos, CHAR_INDICES[letter]] = 1
        preds = self.model.predict(x, verbose=0)[0]
        preds = preds.tolist()
        max_value = max(preds)
        index = preds.index(max_value)
        # cut left context "ные_мечты" -> "мечты"
        word = word[word.index('_') + 1:]
        index = len(word) - MAXLEN + index
        if index > len(word) - 1:
            print('no %s-th letter in %s' % (index + 1, word))
        else:
            acc_word = word[:index + 1] + '\'' + word[index + 1:]
            return(acc_word)

    def put_stress(self, text, stress_symbol="'"):
        """This function gets any string as an input and returns the same string
        but only with the predicted stress marks.

        All the formating is preserved using this function.
        """
        words = parse_the_phrase(text)
        tokens = tokenize(text)
        accented_phrase = []
        pluswords = add_endings(words)

        for w in pluswords:
            if not bool(re.search(REG, w)):
                pass
            else:
                accented_phrase.append(self._predict(w))
        final = []

        for token in tokens:
            if is_small(token):
                final.append(token)
            else:
                try:
                    temp = accented_phrase[0].replace("'", '')
                except IndexError:
                    temp = ''
                if temp == token.lower():
                    stress_position = accented_phrase[0].find("'")
                    final.append(token[:stress_position] +
                                    stress_symbol + token[stress_position:])
                    accented_phrase = accented_phrase[1:]
                else:
                    final.append(token)
        final = ''.join(final)
        return final
