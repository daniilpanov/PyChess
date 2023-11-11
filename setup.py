from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='speedfile',
    version='0.0.3',
    author='SergeyLebidko',
    author_email='it.sergeyler@mail.ru',
    description='Simple Chess Library. Free to use',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://hproger.ru/',
    packages=find_packages(),
    install_requires=['requests>=2.25.1'],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files speedfiles ',
    project_urls={
        'GitHub': 'https://github.com/SergeyLebidko/PyChess.git'
    },
    python_requires='>=3.6'
)
