# The Stock's Average Yearly Performance Calculator

This script calcualtes a given stock's average yearly performance throughout its existence.

## Usage:

Create the virtual environment:

```shell
python3 -m virtualenv venv
```

Activate the virtual environment:

```shell
source venv/bin/activate
```

Install `yfinance`:

```
pip3 install yfinance
```

Try a ticker:

```shell
python3 stock.py
```

The output:

```
Enter a valid stock Ticker: SCHD
Average Yearly Performance of SCHD (excluding the current year): 11.68%
Total Years: 14
```

Bye!
