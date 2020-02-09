## LevelUp _ Task 1.5

### The Problem

We have a database for an ads provider system that worked as free. But some premium features be added now, so I should change DB to new model. In this task (problem) we want an script to do this migration for large data.


### Quick Start
For running the script, use a list as database config \[__postgreSQL used__\].
```python
dbConfig = ["postgres", "root", "task1o5", "127.0.0.1", "5432"]
```

Because of using asyncio and asyncpg for streaming large data from db, we use following command as loop for do own modifying on our db.
```python
loop = asyncio.get_event_loop()
loop.run_until_complete(run(dbConfig))
```

If the last code executaion determined suddenly during the process, use datas in log's file and bellow function:
```python
loop.run_until_complete(run(dbConfig, last_id, product_orders))
```

### DB
You can use `initilization_random_db.py` for create a random db to test functionality.

| table name | columns |
|--|--|
| customer | id, name, premium_source |
| product | id, name, customer_id |
| source | id, name, type |
| offer | id, product_id, source_id, order_num |

### Performance
I use [__guppy3__](https://pypi.org/project/guppy3/) for analysing the performance of script. For 2M records is offer table, and 10K entries in product table, the process completed in ~1h and maximum ~9MB memory.

### Unit Test
Will be commplete as soon as possibel ;)