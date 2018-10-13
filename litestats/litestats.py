import sqlite3
import pstats
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


SCHEMA = """
drop table if exists functions;
create table functions(
    id integer primary key,
    filename text not null,
    line integer not null,
    function text not null,

    constraint funcs_unique unique (filename, line, function)
);

drop table if exists stats;
create table stats(
    function integer,

    cc integer,   -- primitive calls (i.e. non-recursive)
    nc integer,   -- number of calls
    tt float,     -- total time (excluding calls to sub-functions)
    ct float,     -- cumulative time spent (including sub-functions)

    foreign key(function) references functions(id)
);

drop table if exists calls;
create table calls(
    caller integer,
    callee integer,

    foreign key(caller) references functions(id),
    foreign key(callee) references functions(id)
);
"""


def insert_func(conn, func):
    stmt = """
    insert into functions(filename, line, function)
    values(?, ?, ?)
    """
    try:
        conn.execute(stmt, func)
    except sqlite3.IntegrityError:
        # function already exists
        pass


def insert_call(conn, caller, callee):
    caller_id = get_func_id(conn, caller)
    callee_id = get_func_id(conn, callee)

    stmt = """
    insert into calls(caller, callee)
    values(?, ?)
    """
    conn.execute(stmt, (caller_id, callee_id))


def insert_stats(conn, func, cc, nc, tt, ct):
    stmt = """
    insert into stats(function, cc, nc, tt, ct)
    values(?, ?, ?, ?, ?)
    """
    conn.execute(stmt, (func, cc, nc, tt, ct))


def get_func_id(conn, func):
    stmt = """
    select
        id
    from
        functions
    where
        filename = ? and
        line = ? and
        function = ?
    """
    res = conn.execute(stmt, func)
    func_id = res.fetchone()[0]
    return func_id


def main(statsfile, outfile):

    conn = sqlite3.connect(outfile)
    conn.executescript(SCHEMA)

    stats = pstats.Stats(statsfile)
    for func, (cc, nc, tt, ct, callers) in stats.stats.items():
        insert_func(conn, func)
        func_id = get_func_id(conn, func)
        insert_stats(conn, func_id, cc, nc, tt, ct)
        for c in callers:
            insert_func(conn, c)
            insert_call(conn, c, func)
    conn.commit()


if __name__ == '__main__':
    statsfile = 'profile.profile3'
    outfile = statsfile + '.sqlite'
    main(statsfile, outfile)
