from setuptools import find_packages, setup

import indian_numbers

try:
    readme = open('README.rst').read()
except IOError:
    readme = ''

setup(
    name='django-indian-numbers',
    version='.'.join(str(i) for i in indian_numbers.VERSION),
    description='django-indian-numbers is a reusable Django application '
                'for formatting numbers in Indian Number System.',
    long_description=readme,
    packages=find_packages(exclude=('tests', 'docs', 'example', )),
    author='Narendra Choudhary',
    author_email='narendralegha.mail@gmail.com',
    url='http://github.com/narenchoudhary/django-indian-numbers/tree/master',
    install_requires=['Django>=1.7'],
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='django library development',
    zip_safe=False,
)
