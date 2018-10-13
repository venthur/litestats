#!/usr/bin/env python


from setuptools import setup

meta = {}
exec(open('./litestats/version.py').read(), meta)
meta['long_description'] = open('./README.md').read()

setup(
    name='litestats',
    version=meta['__VERSION__'],
    description='Convert cprofile/pstats files into sqlite databases.',
    long_description=meta['long_description'],
    long_description_content_type='text/markdown',
    keywords='litestats pstats cprofile',
    author='Bastian Venthur',
    author_email='mail@venthur.de',
    url='https://github.com/venthur/litestats',
    python_requires='>=3',
    extras_require={
      'dev': [
          'pytest',
          'pytest-cov',
          'flake8',
      ]
    },
    packages=['litestats'],
    entry_points={
        'console_scripts': [
            'litestats = litestats.__main__:main'
        ]
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
