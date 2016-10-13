django-indian-numbers
=====================
``django-indian-numbers`` is a reusable Django application for which provides
filters for Django templates for formatting numbers in Indian Number System .


Installation
============

.. code-block:: python

    pip install git+https://github.com/narenchoudhary/django-indian-numbers#egg=django-indian-numbers



Usage
=====

To activate filters, add ``"indian_numbers"`` to INSTALLED_APPS settings and
use ``{% load indian_numbers_tags %}`` in template to access filters.

.. code-block:: python

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
        ...
        'indian_numbers',
    ]


Load the `indian_numbers_tags` template filters library.

.. code-block:: html

        {% load indian_numbers_tags %}


Filters
=======

intcomma_indian
---------------

Similar to `intcomma <https://docs.djangoproject.com/en/dev/ref/contrib/humanize/#intcomma>`_ in
`django.contrib.humanize <https://docs.djangoproject.com/en/dev/ref/contrib/humanize/>`_ app of Django library.
It converts a number to a string formatted with commas as per Indian number system.
It works for integer, floating-point and string values which can be converted to integers.

Examples:

- **100000** becomes **1,00,000**
- **1259647552** becomes **1,25,96,47,552**
- **126500.25** becomes **1,26,500**
- **-126500** becomes **-1,26,500**
- **'100000'** becomes **1,00,000**

floatcomma_indian
-----------------

It works exactly likes ``intcomma``, except that it preserves decimal places.

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


License
=======

BSD
