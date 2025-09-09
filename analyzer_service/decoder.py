import base64

def decode_wordlist(encoded: str) -> list[str]:
    """
    here i decode a base64 encoded comma-separated wordlist into a Python list of words...
    """



def decode_pairs(encoded: str) -> list[tuple[str, str]]:
    """
    and decode comma-separated pairs (word1|word2) into a list of tuples
    like: "boycott|israel,apartheid|state"
    """