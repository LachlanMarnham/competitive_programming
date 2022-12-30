from .solution import Editor


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    outputs = []
    editor = Editor()
    q = int(input_lines.pop(0))
    for _ in range(q):
        instruction = input_lines.pop(0).strip()
        arg = instruction[2:]
        if instruction.startswith("1"):
            editor.append(arg)
        elif instruction.startswith("2"):
            editor.delete(int(arg))
        elif instruction.startswith("3"):
            output = editor.print(int(arg))
            outputs.append(output)
        elif instruction.startswith("4"):
            editor.undo()
    return outputs


TEST_CASE_0 = """8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1"""


def test():
    assert hackerrank_main(TEST_CASE_0) == ["c", "y", "a"]
