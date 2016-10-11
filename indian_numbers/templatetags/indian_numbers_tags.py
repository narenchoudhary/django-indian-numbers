from __future__ import unicode_literals

import locale

from django import template

register = template.Library()


@register.filter(is_safe=True)
def intcomma_indian(value):
    """
    Converts a number into comma notation as per Indian number system.

    This function accepts integer, float, and string value, but strips
    decimal part before computing indian number notation of integral part.
    For example:
        100000 becomes 1,00,000
        1259647552 becomes 1,25,96,47,552
        126500.25 becomes 1,26,500
        -126500 becomes -1,26,500

    :param value: integer, float, string
    :return: string
    """

    try:
        # Second argument to setlocale must be a byte string.
        # Passing unicode string will throw ValueError in <= 2.7.11.
        # Only 2.7.12 accepts unicode string.
        locale.setlocale(locale.LC_ALL, b'en_IN')
    except locale.Error:
        return value

    try:
        if isinstance(value, (float, int)):
            value = int(value)
        elif isinstance(value, str):
            value = int(float(value))
    except (ValueError, TypeError):
        return value

    new_number = locale.format("%d", value, grouping=True)
    return new_number


@register.filter(is_safe=True)
def floatcomma_indian(value):
    """
    Convert a number into comma notation as per Indian number system.

    This function accepts integer, float, and string value. If the value passed
    does not have any decimal places, then 2 decimal places are added by
    default. Decimal places are preserved in all other cases.

    Example:
        25 becomes 25.00
        121250.6 becomes 1,125.6
        25.675 becomes 25.675
        126500.25 becomes 1,26,500.25
        -126500.75 becomes -1,26,500.75

    :param value: integer or float
    :return:
    """

    try:
        # Second argument to setlocale must be a byte string.
        # Passing unicode string will throw ValueError in <= 2.7.11.
        # Only 2.7.12 accepts unicode string.
        locale.setlocale(locale.LC_ALL, b'en_IN')
    except locale.Error:
        return value

    value_str_split = str(value).split('.')
    decimal_places = 2
    if len(value_str_split) == 2:
        decimal_places = len(value_str_split[1])

    try:
        if isinstance(value, (int, float, str)):
            value = float(value)
    except (ValueError, TypeError):
        return value

    format_str = "%.{}f".format(decimal_places)
    new_value = locale.format(format_str, value, grouping=True)
    return new_value


@register.filter(is_safe=True)
def intword_indian(value, args):
    """
    Converts a large integer number into a friendly text representation.
    Denominations used are:
        Hundred
        Thousand
        Lakh
        Crore

    :return:
    """
    pass
