import os
import sys
from setuptools import setup
from setuptools.extension import Extension

this_dir = os.path.dirname(os.path.abspath(__file__))

jamspell = Extension(
    name='_jamspell',
    include_dirs=['.', 'jamspell'],
    sources=[
        os.path.join('jamspell', 'lang_model.cpp'),
        os.path.join('jamspell', 'spell_corrector.cpp'),
        os.path.join('jamspell', 'utils.cpp'),
        os.path.join('jamspell', 'perfect_hash.cpp'),
        os.path.join('jamspell', 'bloom_filter.cpp'),
        os.path.join('contrib', 'cityhash', 'city.cc'),
        os.path.join('contrib', 'phf', 'phf.cc'),
        'jamspell_wrap.cpp',
    ],
    extra_compile_args=['-std=c++11', '-O2'],
)

if sys.platform == 'darwin':
    jamspell.extra_compile_args.append('-stdlib=libc++')

VERSION = '0.0.12'

setup(
    name='jamspell',
    version=VERSION,
    author='Filipp Ozinov',
    author_email='fippo@mail.ru',
    url='https://github.com/bakwc/JamSpell',
    download_url='https://github.com/bakwc/JamSpell/tarball/' + VERSION,
    description='spell checker',
    long_description='context-based spell checker',
    keywords=['nlp', 'spell', 'spell-checker', 'jamspell'],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
    py_modules=['jamspell'],
    ext_modules=[jamspell],
    zip_safe=False,
    include_package_data=True,
)
