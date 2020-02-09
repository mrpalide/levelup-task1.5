import asyncio
from typing import List

import asyncpg


def LastStatusLogger(data: str):
    log_file = open("lastStatus.log", "w")
    log_file.write(data)
    log_file.close()


async def run(dbConfig: List, start_id: int = 0, product_orders: List[int] = []):
    try:
        conn = await asyncpg.connect(
            user=dbConfig[0],
            password=dbConfig[1],
            database=dbConfig[2],
            host=dbConfig[3],
            port=dbConfig[4],
        )
    except ConnectionError:
        raise ConnectionError("Not Connect!")

    free_source_ids_query: List = await conn.fetch(
        "SELECT id FROM source WHERE type = 0"
    )
    free_source_id_list: List[int] = [i["id"] for i in free_source_ids_query]

    product_count: List = await conn.fetch("SELECT COUNT(*) FROM product")
    if product_orders == []:
        product_orders = [0] * product_count[0][0]

    values = await conn.fetch(f"SELECT * FROM offer WHERE id >= {start_id} ORDER BY id")
    for i in values:
        if i["source_id"] in free_source_id_list:
            new_order_num: int = product_orders[i["product_id"] - 1] + 1
            product_orders[i["product_id"] - 1] = new_order_num
            await conn.execute(
                f"UPDATE offer SET order_num = {new_order_num} WHERE id = {i['id']}"
            )
            LastStatusLogger(f"last_id={i['id']}\nproduct_orders={product_orders}")
        else:
            await conn.execute(f"UPDATE offer SET order_num = 0 WHERE id = {i['id']}")
            LastStatusLogger(f"last_id={i['id']}\nproduct_orders={product_orders}")

    await conn.close()


dbConfig = ["postgres", "root", "task1o5", "127.0.0.1", "5432"]

loop = asyncio.get_event_loop()
loop.run_until_complete(run(dbConfig))
