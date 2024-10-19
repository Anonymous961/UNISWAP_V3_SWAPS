import sqlite3

def create_database():
    conn = sqlite3.connect('data/uniswap.db')
    cursor = conn.cursor()

    # Drop the swaps table if it exists
    cursor.execute('DROP TABLE IF EXISTS swaps')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS swaps (
            id TEXT PRIMARY KEY,
            amountIn REAL,
            amountOut REAL,
            amountInUSD REAL,
            amountOutUSD REAL,
            tick INTEGER,
            timestamp INTEGER
        )
    ''')

    conn.commit()
    conn.close()


def insert_swap(swap_data):
    conn = sqlite3.connect('data/uniswap.db')
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT OR IGNORE INTO swaps (id, amountIn, amountOut, amountInUSD, amountOutUSD, tick, timestamp) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', swap_data
    )

    conn.commit()
    conn.close()
