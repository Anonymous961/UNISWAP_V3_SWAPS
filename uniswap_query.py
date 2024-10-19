import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

SUBGRAPH_API_KEY = os.getenv("SUBGRAPH_API_KEY")
GRAPH_URL = "https://gateway.thegraph.com/api/{}/subgraphs/id/FQ6JYszEKApsBpAmiHesRsd9Ygc6mzmpNRANeVQFYoVX".format(SUBGRAPH_API_KEY)

def get_swaps(pool_address,start_timestamp):
    query = f"""
    {{
        swaps(first: 1000, where: {{pool: "{pool_address}", timestamp_gt: {start_timestamp}}}, orderBy: timestamp, orderDirection: desc) {{
            id
            amountIn
            amountOut
            amountInUSD
            amountOutUSD
            tick
            timestamp
        }}
    }}
    """

    response= requests.post(GRAPH_URL,json={'query':query})

    if response.status_code == 200:
        return response.json()["data"]["swaps"]
    else:
        raise Exception(f"Query failed to run by returning code of {response.status_code}. {query}")
    

def get_one_month_ago_timestamp():
    return int(time.time())-(30*24*60*60)