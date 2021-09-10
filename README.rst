django-indian-numbers
=====================

.. image:: https://app.travis-ci.com/narenchoudhary/django-indian-numbers.svg?branch=master
    :target: https://app.travis-ci.com/github/narenchoudhary/django-indian-numbers
.. image:: https://codecov.io/gh/narenchoudhary/django-indian-numbers/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/narenchoudhary/django-indian-numbers
.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
    :target: https://opensource.org/licenses/BSD-3-Clause

``django-indian-numbers`` is a reusable Django application for which provides
filters for Django templates for formatting numbers in Indian Number System .


Installation
============

.. code-block:: python

    pip install git+https://github.com/narenchoudhary/django-indian-numbers#egg=django-indian-numbers



Usage
=====

1. Add ``"indian_numbers"`` to INSTALLED_APPS settings.

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        ...
        'indian_numbers',
    ]

2. Add ``USE_THOUSAND_SEPARATOR = True`` in settings.


3. Load the `indian_numbers_tags` template filters library.

.. code-block:: html

        {% load indian_numbers_tags %}

4. See example project for examples.

Filters
=======

intcomma_indian
---------------

Similar to `intcomma <https://docs.djangoproject.com/en/dev/ref/contrib/humanize/#intcomma>`_ in
`django.contrib.humanize <https://docs.djangoproject.com/en/dev/ref/contrib/humanize/>`_ app of Django library.
It converts a number to a string formatted with commas as per Indian number system.
It works for integer, floating-point and string values which can be converted to integers. This tag also accepts an optional ``preserve_decimal`` parameter. If ``preserve_decimal`` is ``True``, then tag will preserve the decimal places for the provided number. By default, ``preserve_decimal`` is set to ``False``.

Examples:

- **100000** becomes **1,00,000**
- **1259647552** becomes **1,25,96,47,552**
- **126500.25** becomes **1,26,500**
- **-126500** becomes **-1,26,500**
- **100000** becomes **1,00,000**

floatcomma_indian
-----------------

It works exactly likes ``intcomma``, except that it preserves decimal places. This template tag also accepts an optional ``decimal_pos`` parameter which denotes number of decimal positions to add/preserve in the provided floating point number. By default, all decimal places are preserved (no decimal places are truncated/padded).

Examples:

- **25** becomes **25.00**
- **121250.6** becomes **1,125.6**
- **25.675** becomes **25.675**
- **126500.25** becomes **1,26,500.25**
- **126500.75** becomes **-1,26,500.75**

floatword_indian
----------------

Converts a large integer number into a friendly text representation.
Highest Denomination is used and 2 lower powers are considered for floating
points in text representation.
Numbers less than 99 are returned without conversion.

Denominations used are: *Hundred*, *Thousand*, *Lakh*, *Crore*

Examples:

- **1000** becomes **1 Thousand**
- **15000** becomes **15 Thousands**
- **15600** becomes **15.60 Thousands**
- **100000** becomes **1 Lakh**
- **1125000** becomes **11.25 Lakhs**
- **10000000** becomes **1 Crore**
- **56482485** becomes **5.64 Crore**
- **56482485.25** becomes **5.64 Crores**
