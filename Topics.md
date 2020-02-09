# Related topics

## Libraries
### [psycopg2](https://pypi.org/project/psycopg2/)
This library use in _initilization_random_db.py_ for handle postgresql db in python.

### asyncio, [asyncpg](https://pypi.org/project/asyncpg/)
These libraries use for stream data from db by coroutine and concurrency in python.

Note that you should use `group by id` in your query! If you lost this, your data retrive in random mode, because of it's concurrent behavior.
```python
values = await conn.fetch(f"SELECT * FROM offer ORDER BY id")
```

### [guppy3](https://pypi.org/project/guppy3/)
I use this library for monitoring the memory in analysing performance of code.

### [testing.postgresql](https://pypi.org/project/testing.postgresql/)
This library __WILL__ for unittest to create fake postgresql db that remove after test complete.

## Useful Links

- stream data retrive
    https://github.com/magicstack/asyncpg
    https://magicstack.github.io/asyncpg/current/index.html

- resource management
    https://www.pluralsight.com/guides/profiling-memory-usage-in-python
    https://www.geeksforgeeks.org/python-how-to-put-limits-on-memory-and-cpu-usage/
    