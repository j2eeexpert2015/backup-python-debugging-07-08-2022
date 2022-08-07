books = [
    {
        "author": ("Arthur Conan", "Doyle"),
        "title": "A Study in Scarlet",
        "published": 1887,
        "rating": 4.14,
    },
    {
        "author": ("Arthur Conan", "Doyle"),
        "title": "The Sign of Four",
        "published": 1890,
        "rating": 3.92,
    },
    {
        "author": ("Arthur Conan", "Doyle"),
        "title": "The Hound of the Baskervilles",
        "published": 1901,
        "rating": 4.13,
    },
    {
        "author": ("Agatha", "Christie"),
        "title": "Murder on the Orient Express (Hercule Poirot #4)",
        "published": 1926,
        "rating": 4.26,
    },
    {
        "author": ("Agatha", "Christie"),
        "title": "Death on the Nile (Hercule Poirot #17)",
        "published": 1937,
        "rating": 4.12,
    },
]

def find_by_author(books_list, last_name):
    """Find books by author's last name"""
    # Note, you could use list comprehensions, but I'm using
    # long form for loop to make debugging easier
    for book in books_list:
        output = []
        if book["author"] == last_name:
            output.append(book)
    return output

def find_by_rating(books_list, lower_bound):
    """Find books with a rating higher than lower_bound"""
    output = []
    for book in books_list:
        if book["rating"] == lower_bound:
            output.append(book)
    return output

doyle_books = find_by_author(books, "Doyle")
doyle_books_above_4 = find_by_rating(doyle_books, 4)

print(doyle_books_above_4)