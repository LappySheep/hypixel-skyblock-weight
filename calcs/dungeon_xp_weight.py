from constants import cata_lvl_50, cata_exp_table, cata_xp_overall


def get_cata_xp_weight(exp: float) -> float:
    """Calculates the dungeon xp weight of the player.

    Parameters
    -----------
    exp: float
        Catacombs experience.

    Returns
    -------
    float
        The amount of weight from catacombs xp

    Example
    -------
    >>> get_cata_xp_weight(1000)
    """
    lvl = -1
    for level in cata_exp_table:
        if exp >= level:
            lvl += 1
        else:
            break

    if lvl != 50:
        dist = cata_exp_table[int(lvl // 1) + 1] - cata_exp_table[int(lvl // 1)]
        progress = ((((exp - cata_exp_table[int(lvl // 1)]) / dist) * 1000) // 1) / 1000
        lvl += progress

    if exp < 569809640:
        n = 0.2 * (lvl / 50) ** 1.538679118869934
    else:
        part = 142452410  # 25% of level 50
        temp_lvl = 50 + ((exp - cata_lvl_50) / part)  # cata 50 x2 = temp level 54
        extra = (500 * ((exp - cata_lvl_50) / part) ** (1 / 1.781925776625157))

    if lvl != 0:
        try:
            temp_lvl
        except:
            return cata_xp_overall * ((1.18340401286164044 ** (lvl + 1) - 1.05994990217254) * (1 + n))
        else:
            return (4100 + extra) * 2
    else:
        return 0
