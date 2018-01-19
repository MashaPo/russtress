DEFAULT_CATEGORIES = [
    '0123456789',
    ' ',
    ',.;:!?()\"[]@#$%^&*_+=«»',
    'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ-\''
]


def tokenize(string, categories=DEFAULT_CATEGORIES):
    token = ''
    tokens = []
    category = None
    for char in string:
        if token:
            if category and char in category:
                token += char
            else:
                tokens.append(token)
                token = char
                category = None
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
        else:
            category = None
            if not category:
                for cat in categories:
                    if char in cat:
                        category = cat
                        break
            token += char
    if token:
        tokens.append(token)
    return tokens
