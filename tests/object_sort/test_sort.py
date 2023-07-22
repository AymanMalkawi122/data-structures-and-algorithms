import pytest
from solutions.sorting.objects.sort import object_sort, by_title, by_year
movies = [
    
    {'title': 'An Inception', 'year': 2010},
    {'title': 'A Titanic', 'year': 1997},
    {'title': 'Iron Man', 'year': 2008},
    {'title': 'Avatar', 'year': 2009},
]



def test_by_year_sorting():
    sorted_movies = movies.copy()
    object_sort(sorted_movies, by_year)
    expected_sorted_years = [ 2010, 2009, 2008, 1997]
    assert [movie['year'] for movie in sorted_movies] == expected_sorted_years

def test_by_title_sorting():
    sorted_movies = movies.copy()
    object_sort(sorted_movies, by_title)
    expected_sorted_titles = [
        'Avatar',
        
        'An Inception',
        'Iron Man',
        'A Titanic',
    ]
    assert [movie['title'] for movie in sorted_movies] == expected_sorted_titles