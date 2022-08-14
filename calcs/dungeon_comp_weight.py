import math
from typing import Dict, Tuple

from constants import cata_comp_overall, cata_comp_max_1000, cata_comp_m_max_1000, cata_comp_worth, cata_comp_buffs

"""
upper bound buffs:
  m1 completion: +62.5
  m2 completion: +125
  m3 completion: +225
  m4 completion: +387.5
  m5 completion: +500
  m6 completion: +700
  m7 completion: +1500
"""


def ordered(d):
    r = []
    for i in range(8):
        if str(i) in d:
            r.append((i, d[str(i)]))
    return r


def get_dungeon_comp_weight(cata_compl: Dict, m_cata_compl: Dict) -> Tuple[float, float]:
    """Calculates the dungeon completion weight of the player.

    Parameters
    -----------
    cata_compl: dict
        A dictionary containing the amount of completions for each catacombs floor
        With the floor number as key and completions as value

    m_cata_compl: dict
        A dictionary containing the amount of completions for each mastermode catacombs floor
        With the floor number as key and completions as value

    Returns
    -------
    float
        The amount of weight from catacombs completions
    float
        The amount of weight from mastermode catacombs completions

    Example
    -------
    >>> cata_compl = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1}
    >>> m_cata_compl = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1}
    >>> get_dungeon_comp_weight(cata_compl, m_cata_compl)
    """
    upper_bound = 1500  # caps at 5000 for m7
    beaten, m_beaten = cata_compl, m_cata_compl
    b, mb = ordered(beaten), ordered(m_beaten)

    score = 0  # turns into weight later
    for floor, amt in [(floor, int(amt)) for floor, amt in b]:
        if amt > 1000:
            excess = amt - 1000
            amt = 1000
        else:
            excess = 0

        s = (amt * cata_comp_worth[floor])

        if excess:  # more than 0
            s *= math.log(((excess / 1000) + 1), 7.5) + 1

        score += s

    rating = (score / cata_comp_max_1000) * upper_bound * cata_comp_overall

    try:
        for f, v in mb:
            if str(f) in cata_comp_buffs:
                threshold = 20
                if v >= threshold:
                    upper_bound += cata_comp_buffs[str(f)]
                else:  # less
                    upper_bound += (cata_comp_buffs[str(f)] * (v / threshold) ** 1.840896416)

        m_score = 0
        for floor, amt in [((floor - 1), int(amt)) for floor, amt in mb]:
            if amt > 1000:
                excess = amt - 1000
                amt = 1000
            else:
                excess = 0

            try:
                s = (amt * cata_comp_worth[8:][floor])
            except:
                s = 0  # floor not in worth dict

            if excess:  # more than 0
                s *= math.log(((excess / 1000) + 1), 6) + 1

            m_score += s

        m_rating = (m_score / cata_comp_m_max_1000) * upper_bound * cata_comp_overall
    except:
        m_rating = 0

    return rating, m_rating
