The tool based on LSTM predicts stress position in each word in russian text depending on the word context. 
For more details about the tool see `«Automated Word Stress Detection in Russian» <http://www.aclweb.org/anthology/W/W17/W17-4104.pdf>`_, EMNLP-2017, Copenhagen, Denmark.

Installation
============

Simple installation with pip

::

    pip install russtress
        
Usage example
========================

To put stress marks to your text

::

    >>> from russtress import Accent
    >>> accent = Accent()
    >>> text = 'Проставь, пожалуйста, ударения'
    >>> accented_text = accent.put_stress(text)
    >>> accented_text
    "Проста'вь, пожа'луйста, ударе'ния"