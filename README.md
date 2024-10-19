# Uniswap V3 Swaps Tracker

## Overview

The **Uniswap V3 Swaps Tracker** is a Python-based application that fetches historical swap data from Uniswap V3 pools on the Arbitrum network. This project allows you to analyze swap volumes, liquidity, and other relevant metrics over a specified timeframe.

## Features

- Retrieve historical swap data for specified Uniswap V3 pools.
- Store swap data in a SQLite database.
- Query data for the past month.
- Easy-to-use setup and configuration.

## Prerequisites

- Python 3.10 or higher
- `pip` for managing Python packages
- A `.env` file containing your Graph API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/uniswap-v3-swaps.git
   cd uniswap-v3-swaps

   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the project root and add your API key:

   ```plaintext
   SUBGRAPH_API_KEY=your_api_key_here
   ```

Usage

1. Run the main application:

   ```bash
   python main.py
   ```

2. The application will create a SQLite database (data/uniswap.db) and populate it with swap data from the specified pools.

## Project Structure

```bash
uniswap-v3-swaps/
├── data/
│   └── uniswap.db           # SQLite database file
├── .env                      # Environment variables
├── main.py                   # Main application logic
├── sqlite_setup.py           # Database setup and handling
├── uniswap_query.py          # Functions to interact with the Uniswap V3 subgraph
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Acknowledgements

1. (Uniswap V3)[https://app.uniswap.org/]
2. (The Graph)[https://thegraph.com/]
