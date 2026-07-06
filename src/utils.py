from datetime import datetime

END_DATE = datetime(2026, 7, 19)

def should_stop():
    return datetime.utcnow() > END_DATE
