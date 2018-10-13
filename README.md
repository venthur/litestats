## Usage

```bash
$ # run the profiler and dump the output
$ python3 -m cProfile -o example.prof example.py
$ # convert dump to sqlite3 db
$ litestats example.prof
$ # example.prof.sqlite created
```

You can now use the sqlite3 data base to investigate the profiler dump:

```sql
sqlite> select *
   ...> from pstats
   ...> order by cumtime desc
   ...> limit 20;

ncalls      tottime     ttpercall             cumtime     ctpercall   filename:lineno(function)
----------  ----------  --------------------  ----------  ----------  ------------------------------------
18/1        0.000161    8.94444444444444e-06  0.067797    0.067797    ~:0(<built-in method builtins.exec>)
1           1.0e-06     1.0e-06               0.067755    0.067755    <string>:1(<module>)
1           4.0e-06     4.0e-06               0.067754    0.067754    /usr/lib/python3.7/runpy.py:195(run_
1           6.0e-06     6.0e-06               0.066135    0.066135    /usr/lib/python3.7/runpy.py:62(_run_
1           1.1e-05     1.1e-05               0.066113    0.066113    /home/venthur/Documents/projects/lit
1           6.6e-05     6.6e-05               0.055152    0.055152    /home/venthur/Documents/projects/lit
1           4.1e-05     4.1e-05               0.0549      0.0549      /home/venthur/Documents/projects/lit
1           0.050196    0.050196              0.050196    0.050196    ~:0(<method 'executescript' of 'sqli
20/3        8.9e-05     4.45e-06              0.011064    0.003688    <frozen importlib._bootstrap>:978(_f
20/3        4.8e-05     2.4e-06               0.011005    0.00366833  <frozen importlib._bootstrap>:948(_f
20/3        7.5e-05     3.75e-06              0.01083     0.00361     <frozen importlib._bootstrap>:663(_l
15/3        3.5e-05     2.33333333333333e-06  0.01073     0.00357666  <frozen importlib._bootstrap_externa
29/5        2.5e-05     8.62068965517241e-07  0.010215    0.002043    <frozen importlib._bootstrap>:211(_c
3           6.0e-06     2.0e-06               0.010087    0.00336233  ~:0(<built-in method builtins.__impo
28/6        9.0e-06     3.21428571428571e-07  0.008977    0.00149616  <frozen importlib._bootstrap>:1009(_
1           9.0e-06     9.0e-06               0.00841     0.00841     /home/venthur/Documents/projects/lit
16          0.000138    8.625e-06             0.004802    0.00030012  <frozen importlib._bootstrap_externa
1           4.5e-05     4.5e-05               0.004143    0.004143    /usr/lib/python3.7/logging/__init__.
1           0.004038    0.004038              0.004038    0.004038    ~:0(<method 'commit' of 'sqlite3.Con
13          3.3e-05     2.53846153846154e-06  0.002368    0.00018215  <frozen importlib._bootstrap_externa
```
