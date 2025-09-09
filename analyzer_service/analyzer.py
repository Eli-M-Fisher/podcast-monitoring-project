from common.logger import Logger

logger = Logger.get_logger()


def analyze_text(
    text: str,
    hostile_words: list[str],
    less_hostile_words: list[str],
    hostile_pairs: list[tuple[str, str]]) -> dict:
    """
    and now analyze text for hostile content and return a dict with:
    bds_percent, is_bds, bds_threat_level ()
    """
    # first count hostile and less-hostile words


    # and check hostile pairs


    # the thresholds (percentages) for determining bds and threat level