from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        profit_today = price - min_price
        max_profit = max(profit_today, max_profit)

        min_price = min(min_price, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
