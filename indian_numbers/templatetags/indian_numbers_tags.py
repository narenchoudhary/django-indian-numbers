from __future__ import unicode_literals

from decimal import Decimal

from django import template
from django.utils import numberformat

register = template.Library()


@register.filter(is_safe=True)
def intcomma_indian(value, preserve_decimal=False):
    """
    Convert an integer to a string containing commas as per Indian Number System

    This function accepts integer, float, and string value, but strips
    decimal part before computing indian number notation of integral part.
    For example:
        100000 becomes 1,00,000
        1259647552 becomes 1,25,96,47,552
        126500.25 becomes 1,26,500
        -126500 becomes -1,26,500

    :param value: integer, float, string
    :param preserve_decimal: Keep decimal values
    :return: string
    """
    try:
        if not isinstance(value, (int, float, Decimal)):
            value = float(value)
    except (TypeError, ValueError):
        return value
    decimal_pos = None if preserve_decimal else 0
    return numberformat.format(value, decimal_sep='.', decimal_pos=decimal_pos, grouping=(3, 2), thousand_sep=',')


@register.filter(is_safe=True)
def floatcomma_indian(value, decimal_pos=None):
    """
    Convert a floating point number to a string containing commas as per Indian Number System

    This function accepts integer, float, and string value. If the value passed
    does not have any decimal places, then 2 decimal places are added by
    default. Decimal places are preserved in all other cases.

    Example:
        25 becomes 25
        121250.6 becomes 1,125.6
        25.675 becomes 25.675
        126500.25 becomes 1,26,500.25
        -126500.75 becomes -1,26,500.75

    :param value: integer or float
    :param decimal_pos: Number of decimal positions to add/preserve
    :return:
    """
    try:
        if not isinstance(value, (int, float, Decimal)):
            value = float(value)
    except (TypeError, ValueError):
        return value
    return numberformat.format(value, decimal_sep='.', decimal_pos=decimal_pos, grouping=(3, 2), thousand_sep=',')


@register.filter(is_safe=True)
def floatword_indian(value):
    """
    Converts a large integer number into a friendly text representation.
    Highest Denomination is used and 2 lower powers are considered for floating
    points in text representation.
    Numbers less than 99 are returned without conversion.

    Denominations used are: Hundred, Thousand, Lakh, Crore

    Examples:
        1000 becomes 1 Thousand
        15000 becomes 15 Thousands
        15600 becomes 15.60 Thousands
        100000 becomes 1 Lakh
        1125000 becomes 11.25 Lakhs
        10000000 becomes 1 Crore
        56482485 becomes 5.64 Crore
        56482485.25 becomes 5.64 Crores

    :return: String
    """
    if isinstance(value, int) and value < 100:
        return str(value)
    if isinstance(value, float) and value < 99:
        return str(value)

    try:
        if isinstance(value, str):
            if '.' not in value and int(value) < 99:
                return value
            if float(value) < 99:
                return value
    except (ValueError, TypeError):
        return value

    value_integer = str(value).split('.')[0]
    value_len = len(value_integer)
    if value_len > 7:
        crores = value_integer[:-7]
        lakhs = value_integer[-7:-5]
        if crores == '1' and lakhs == '00':
            return '1 Crore'
        if lakhs == '00':
            return '%s Crores' % crores
        return '%s.%s Crores' % (crores, lakhs)
    elif value_len > 5:
        lakhs = value_integer[:-5]
        thousands = value_integer[-5:-3]
        if lakhs == '1' and thousands == '00':
            return '1 Lakh'
        if thousands == '00':
            return '%s Lakhs' % lakhs
        return '%s.%s Lakhs' % (lakhs, thousands)
    elif value_len > 3:
        thousands = value_integer[:-3]
        hundreds = value_integer[-3:-1]
        if thousands == '1' and hundreds == '00':
            return '1 Thousand'
        if hundreds == '00':
            return '%s Thousands' % thousands
        return '%s.%s Thousands' % (thousands, hundreds)
    else:
        hundreds = value_integer[:-2]
        tens_ones = value_integer[-2:]
        if hundreds == '1' and tens_ones == '00':
            return '1 Hundred'
        if tens_ones == '00':
            return '%s Hundreds' % hundreds
        return '%s.%s Hundreds' % (hundreds, tens_ones)
