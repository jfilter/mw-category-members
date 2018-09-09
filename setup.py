from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
]

setup(name='mw_category_members',
      version='0.1.0',
      description="Using MediaWiki's API, retrieve pages that belong to a given category",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jfilter/mw-category-members',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['category_members'],
      install_requires=['requests'],
      classifiers=classifiers)
