import base64

def decode_wordlist(encoded: str) -> list[str]:
    """
    here i decode a base64 encoded comma-separated wordlist into a Python list of words...
    """
    if not encoded:
        return []
    decoded = base64.b64decode(encoded).decode("utf-8")
    return [w.strip() for w in decoded.split(",") if w.strip()]