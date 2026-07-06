import requests

GAMMA_URL = "https://gamma-api.polymarket.com/markets"

def fetch_markets(limit=200):
    params = {
        "limit": limit,
        "active": True
    }
    r = requests.get(GAMMA_URL, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def find_world_cup_market(markets):
    """
    Finds World Cup Winner market automatically.
    """
    keywords = ["world cup", "winner", "fifa"]

    for m in markets:
        title = (m.get("title") or "").lower()
        if all(k in title for k in ["world cup", "winner"]):
            return m

    # fallback fuzzy search
    for m in markets:
        title = (m.get("title") or "").lower()
        if any(k in title for k in keywords):
            return m

    raise ValueError("World Cup market not found")
