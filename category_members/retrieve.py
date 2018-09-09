import requests


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
    cmtype = f'&cmtype={"|".join(types)}'
    base_url = f'{mw_instance}/w/api.php?action=query&format=json&list=categorymembers&cmtitle={cat_name}&cmlimit=500{cmtype}'
    cont = ''

    result = []

    while True:
        url = f'{base_url}&cmcontinue={cont}'
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r_json = r.json()

        if 'query' in r_json:
            for item in r_json['query']['categorymembers']:
                title = item['title']
                if clean_subcat_names and ':' in title:
                    # cut away ':' and evertyhing before
                    index_sep = title.index(':')
                    title = title[index_sep + 1:]
                # spaces need to be converted in links
                link = f'{mw_instance}/wiki/{title.replace(" ", "_")}'
                result.append({'name': title, 'link': link})

        if 'continue' not in r_json:
            break
        else:
            cont = r_json['continue']['cmcontinue']

    return result
