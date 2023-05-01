import sys
from pathlib import Path

import sqlparse

if __name__ == "__main__":
    root_dir = Path(sys.argv[1])
    for file_name in root_dir.rglob("*.sql"):
        with open(file_name, "r") as fd:
            sql = fd.read()
        parsed_sql = sqlparse.format(
            sql,
            keyword_case="upper",
            identifier_case="lower",
            strip_comments=False,
            reindent_aligned=True,
            use_space_around_operators=True,
            indent_width=4,
        )
        if parsed_sql != sql:
            with open(file_name, "w") as fd:
                fd.write(parsed_sql)
