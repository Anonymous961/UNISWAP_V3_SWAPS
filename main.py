from uniswap_query import get_swaps, get_one_month_ago_timestamp
from sqlite_setup import create_database, insert_swap

pools = [
    "0xC6962004f452bE9203591991D15f6b388e09E8D0",
    "0xC31E54c7a869B9FcBEcc14363CF510d1c41fa443"
]

def main():
    create_database()

    one_month_ago = get_one_month_ago_timestamp()
    for pool in pools:
        swaps = get_swaps(pool, one_month_ago)

        for swap in swaps:
            swap_data = (
                swap["id"],
                float(swap["amountIn"]),   
                float(swap["amountOut"]), 
                float(swap["amountInUSD"]),  
                float(swap["amountOutUSD"]),  
                int(swap["tick"]),
                int(swap["timestamp"])
            )
            insert_swap(swap_data)

if __name__ == "__main__":
    main()
