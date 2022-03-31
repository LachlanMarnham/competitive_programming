def left_join(phrases: tuple) -> str:
    return ','.join(phrases).replace('right', 'left')
