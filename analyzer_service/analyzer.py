import re
from config import (
    HOSTILE_WORDLIST_BASE64,
    LESS_HOSTILE_WORDLIST_BASE64,
    BDS_THRESHOLD,
    MEDIUM_THRESHOLD,
    HIGH_THRESHOLD,
)
from decoder import decode_wordlist
from common.logger import Logger

logger = Logger.get_logger()

# here i'm bringing in the decoded wordlists
HOSTILE_WORDS = decode_wordlist(HOSTILE_WORDLIST_BASE64)
LESS_HOSTILE_WORDS = decode_wordlist(LESS_HOSTILE_WORDLIST_BASE64)

# use this func to split text into words (each word is token..)
def tokenize(text: str) -> list[str]:
    """
    for tokenize text into words (lowercased).
    """
    words = re.findall(r"\b\w+\b", text.lower())
    return words

# generate n-grams (connected words; every two words before and after are connected separately to form a pair) from tokenized words
def generate_ngrams(words: list[str], n: int) -> list[str]:
    """
    generate n-grams (like bigrams) from tokenized words
    """
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]


def analyze_transcription(transcription: str) -> dict:
    """
    and now analyze transcription to detect hostile content.
    and returns dict with bds_percent, is_bds, bds_threat_level (none, low, medium, high)
    """
    # first handle empty transcription (makeing these false, none)
    if not transcription:
        return {"bds_percent": 0.0, "is_bds": False, "bds_threat_level": "none"}
    
    # create counting words list
    # also generates a list of word pairs (bigrams)
    # and total word count
    words = tokenize(transcription)
    bigrams = generate_ngrams(words, 2)
    total_words = len(words)

    # counting hits lists
    hostile_hits = 0         # hostile hit count
    less_hostile_hits = 0    # less hostile hit count

    # counting hostile words/phrases (weight =2)
    for phrase in HOSTILE_WORDS:
        phrase_lower = phrase.lower()
        if " " in phrase_lower:  # phrase (there is a space in the string)
            hostile_hits += 2 * bigrams.count(phrase_lower)
        else:  # single word
            hostile_hits += 2 * words.count(phrase_lower)

    # now counting for less hostile words/phrases (weight=1)
    for phrase in LESS_HOSTILE_WORDS:
        phrase_lower = phrase.lower()
        if " " in phrase_lower:
            less_hostile_hits += bigrams.count(phrase_lower)
        else:
            less_hostile_hits += words.count(phrase_lower)

    # i calculate all hits together
    weighted_hits = hostile_hits + less_hostile_hits
    # and now calculate bds percent
    bds_percent = (weighted_hits / total_words) * 100 if total_words > 0 else 0.0

    # Binary classification (defined in config)
    is_bds = bds_percent >= BDS_THRESHOLD

    # Threat levels (divided into three categories: high, medium, none)
    if bds_percent >= HIGH_THRESHOLD:
        level = "high"
    elif bds_percent >= MEDIUM_THRESHOLD:
        level = "medium"
    else:
        level = "none"

    logger.info(f"Analyzed transcription: bds_percent={bds_percent:.2f}, is_bds={is_bds}, level={level}")

    # and finally return a dict with the three fields that i will later update in es
    return {
        "bds_percent": round(bds_percent, 2),
        "is_bds": is_bds,
        "bds_threat_level": level,
    }