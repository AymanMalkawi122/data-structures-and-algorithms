def object_sort(arr, compare_func):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare_func(arr[j], arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

def remove_leading_articles(title):
    articles = ["A ", "An ", "The "]
    for article in articles:
        if title.startswith(article):
            print(title)
            return title[len(article):]

    return title

def by_year(obj1, obj2):
    return obj1['year'] < obj2['year']

def by_title(obj1, obj2):
    return remove_leading_articles(obj1['title']) > remove_leading_articles(obj2['title'])
