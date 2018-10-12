This tool converts a Python3 profile file in a SQLLite database.

## Example usage

Assuming you have the file `example.py`:

    python3 -m cProfile -o profile_example.cprof example.py
    python3 -m litestats profile_example.cprof
    sqlite3 profile_example.cprof.sqlite3 'select f.function, s.tt from functions f join stats s on f.id =s.function order by 2 desc;'

This will show the function names sorted by total execution time