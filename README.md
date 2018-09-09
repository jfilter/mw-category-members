# mw-category-members [![Build Status](https://travis-ci.com/jfilter/mw-category-members.svg?branch=master)](https://travis-ci.com/jfilter/mw-category-members) [![PyPI](https://img.shields.io/pypi/v/mw-category-members.svg)](https://pypi.org/project/mw-category-members/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mw-category-members.svg)](https://pypi.org/project/mw-category-members/)

Using MediaWiki's API: retrieve pages that belong to a given category

## Installation

`pip install mw_category_members`

## Usage

```python
import category_members

results = category_members.retrieve('Category:Presidents_of_the_United_States')
for r in results:
    print(r['name'], r['link'])
```

### Arguments

```python
def retrieve(cat_name, mw_instance='https://en.wikipedia.org', types=['page', 'subcat', 'file'], clean_subcat_names=False):
```

-   cat_name: Category name e.g. 'Category:Presidents_of_the_United_States'.
-   mw_instance: Which MediaWiki instance to use (the URL 'origin'). Defaults to 'https://en.wikipedia.org'.
-   types: Which types of pages to retrieve. Defaults to `['page', 'subcat', 'file']`.
-   clean_subcat_names: If `True`, removes the e.g. 'Category:' prefix of the titles. Defaults to `False`.

### Returns

Array of pages where a page is a dictionary of `{'name': 'some name', 'link': 'some absolute link'}`.

## License

MIT.
