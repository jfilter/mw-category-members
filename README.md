# mw-category-members

Using MediaWiki's API: retrieve pages that belong to a given category

## Installation

## Usage

```python
import category_members

result = category_members.retrieve('Category:Presidents_of_the_United_States')

for r in result:
    print(r['name'], r['link'])
```

### Arguments

```python
def retrieve(cat_name, mw_instance='https://en.wikipedia.org', types=['page', 'subcat', 'file'], clean_subcat_names=False):
    """Retrieve pages that belong to a given category.
        Args:
            cat_name: Category name e.g. 'Category:Presidents_of_the_United_States'.
            mw_instance: Which MediaWiki instance to use (the URL 'origin'). Defaults to 'https://en.wikipedia.org'.
            types: Which types of pages to retrieve. Defaults to `['page', 'subcat', 'file']`.
            clean_subcat_names: If `True`, removes the e.g. 'Category:' prefix of the titles. Defaults to `False`.
        Returns:
            Array of pages where a page is a dictionary of `{'name': 'some name', 'link': 'some absolute link'}`.
    """
```

## License

MIT.
