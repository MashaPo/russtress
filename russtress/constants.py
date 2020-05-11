from pathlib import Path

VOWELS = 'аеиоуэюяыё'
REG = '[{}].*[{}]'.format(VOWELS, VOWELS)
MAXLEN = 40
CHARS = ["'", '-', '_', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к',
         'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
         'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'ё']
CHAR_INDICES = dict((c, i) for i, c in enumerate(CHARS))
BASE_DIR = Path(__file__).resolve().parent
MODEL_FILE = BASE_DIR / "text_model.json"
WEIGHTS_FILE = BASE_DIR / "weights.96.hdf5"
ALL_FORMS_FILENAME = BASE_DIR / "add_dictionary.sm"