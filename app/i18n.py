import gettext

LOCALE_DIR = "./locales"


def get_translator(lang: str):
    try:
        return gettext.translation("messages", localedir=LOCALE_DIR, languages=[lang])
    except FileNotFoundError:
        return gettext.translation("messages", localedir=LOCALE_DIR, languages=["en"])
