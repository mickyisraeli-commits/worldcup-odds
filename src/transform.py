import pandas as pd

def extract_odds(market):
    """
    Converts Polymarket outcome prices into clean structure.
    """
    outcomes = market.get("outcomes", [])
    prices = market.get("outcomePrices", [])

    rows = []

    for i, outcome in enumerate(outcomes):
        price = None

        if i < len(prices):
            try:
                price = float(prices[i])
            except:
                price = None

        rows.append({
            "market": market.get("title"),
            "outcome": outcome,
            "probability": price
        })

    return pd.DataFrame(rows)


def to_wide(df):
    """
    Convert long format -> wide format
    """
    return df.pivot(index="market", columns="outcome", values="probability").reset_index()
