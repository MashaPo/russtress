import re
from .constants import ALL_FORMS_FILENAME, REG

all_forms = {}
with open(ALL_FORMS_FILENAME, encoding='utf-8') as all_forms_file:
    for form in all_forms_file:
        if "'" in form:
            form = form.strip('\n')
            unstressed_form = re.sub("['`]", '', form)
            if unstressed_form in all_forms:
                all_forms[unstressed_form].append(form.find("'"))
            else:
                all_forms[unstressed_form] = [form.find("'")]

def parse_the_phrase(text):
    text = text.replace("c", "с")  # latin to cyrillic
    regex1 = "[…:,.?!\n]"
    text = re.sub(regex1, " _ ", text).lower()  # mark beginning of clause
    # get rid of "#%&""()*-[0-9][a-z];=>@[\\]^_{|}\xa0'
    regex2 = "[^а-яё'_ -]"
    text = re.sub(regex2, "", text)
    words = text.split(' ')
    return words

def add_endings(wordlist):
    pluswords = []
    for i, word in enumerate(wordlist):
        if not bool(re.search(REG, word)):
            # won't predict, just return (less then two syllables )
            pluswords.append(word)
        elif i == 0 or wordlist[i - 1] == '_':
            pluswords.append('_' + word)
        else:
            context = wordlist[i - 1].replace("'", "")
            if len(context) < 3:
                ending = context
            else:
                ending = context[-3:]
            plusword = ending + '_' + word
            pluswords.append(plusword)
    return pluswords

def is_in_dictionary(word):
    if word.lower() in all_forms:
        return True
    else:
        return False

def dictionary_stress(word):
    stressed_word = ''
    lword = word.lower()
    if len(all_forms[lword]) == 1:
        stressed_word = word[:all_forms[lword][0]] + "'" + \
            word[all_forms[lword][0]:]
    else:
        return None
    return stressed_word

def is_small(word):
    counter = 0
    for letter in word:
        if letter in 'ёуеыаоэяиюЁУЕЫАОЭЯИЮ':
            counter = counter + 1
    if counter <= 1:
        return True