#-*- coding: utf-8 -*-
"""
@file
@brief Small functions.
"""
import datetime


def convert_into_days(date, lang="fr", format="%Y-%m-%dT%H:%M:%S"):
    """
    Convert a date into the number of days from today.

    @param      date        str or datetime
    @param      lang        language
    @param      format      format to use
    @return                 string
    """
    if lang != "fr":
        raise NotImplementedError(
            "Language '{0}' is not supported.".format(lang))
    now = datetime.datetime.now()
    if isinstance(date, str):
        date = datetime.datetime.strptime(date, format)
    delta = now - date
    delay = delta.days
    if delay == 0:
        hour = delta.seconds // 3600
        if hour <= 1:
            return "il y a moins d'une heure"
        elif hour <= 2:
            return "il y a deux heures"
        elif hour <= 3:
            return "il y a trois heures"
        elif hour <= 6:
            return "il y a six heures"
        elif hour <= 12:
            return "il y a douze heures"
        else:
            return "aujourd'hui"
    elif delay == 1:
        return "hier"
    elif delay == 2:
        return "avant-hier"
    elif delay < 0:
        return "dans le futur"
    else:
        return "il y a {0} jours".format(delay)
