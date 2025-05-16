from fastapi import Query

from app.i18n import get_translator


def get_gettext(lang: str = Query("en")):
    translator = get_translator(lang)
    return translator.gettext
