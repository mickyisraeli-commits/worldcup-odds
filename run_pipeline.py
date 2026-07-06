from src.fetch_polymarket import fetch_markets, find_world_cup_market
from src.transform import extract_odds, to_wide
from src.utils import should_stop

DATA_DIR = "data"

def main():
    if should_stop():
        print("Pipeline ended (post World Cup date).")
        return

    markets = fetch_markets()
    wc_market = find_world_cup_market(markets)

    df_long = extract_odds(wc_market)
    df_wide = to_wide(df_long)

    os.makedirs(DATA_DIR, exist_ok=True)

    long_path = f"{DATA_DIR}/odds_long.csv"
    wide_path = f"{DATA_DIR}/odds_wide.csv"

    df_long.to_csv(long_path, index=False)
    df_wide.to_csv(wide_path, index=False)

    print("Updated data saved.")

if __name__ == "__main__":
    main()
