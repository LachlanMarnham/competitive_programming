from .solution import popular_words


def checkio_main(text, words, solution):
    assert popular_words(text, words) == solution


def test():
    text = """
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    """
    words = ["i", "was", "three", "near"]
    solution = {
        "i": 4,
        "was": 3,
        "three": 0,
        "near": 0,
    }
    checkio_main(text, words, solution)
