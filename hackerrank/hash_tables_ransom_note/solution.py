from collections import defaultdict


def build_frequency_map(word_list):
    frequency_map = defaultdict(int)
    for word in word_list:
        frequency_map[word] += 1
    return frequency_map


def check_magazine(magazine, note):
    note_words = set(note)
    magazine_words = set(magazine)

    if not note_words.issubset(magazine_words):
        # The magazine has a smaller vocabulary
        # than the note
        return 'No'
    else:
        note_word_frequency = build_frequency_map(note)
        magazine_word_frequency = build_frequency_map(magazine)

        for note_word, note_word_count in note_word_frequency.items():
            magazine_word_count = magazine_word_frequency[note_word]
            if note_word_count > magazine_word_count:
                # The magazine has all the required words,
                # but at least one of them doesn't occur enough
                # times
                return 'No'

        # All words from the note occur in the magazine, and
        # with the required frequency
        return 'Yes'
