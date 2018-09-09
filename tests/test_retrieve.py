import category_members


def test_retrieve():
    res = category_members.retrieve('Category:Presidents_of_the_United_States')
    assert any(x['name'] == "Barack Obama" for x in res)
    assert any(
        x['link'] == "https://en.wikipedia.org/wiki/Barack_Obama" for x in res)
    assert any('Category:' in x['name'] for x in res)


def test_retrieve_page_only():
    res = category_members.retrieve(
        'Category:Presidents_of_the_United_States', types=['page'])
    assert any(x['name'] == "Barack Obama" for x in res)
    assert all('Category:' not in x['name'] for x in res)


def test_retrieve_clean_subcat():
    res = category_members.retrieve(
        'Category:Presidents_of_the_United_States', clean_subcat_names=True)
    assert all('Category:' not in x['name'] for x in res)
