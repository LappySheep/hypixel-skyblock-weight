from typing import Dict, Tuple

from constants import srw, level60skill, overflow_skill_multipliers, skill_overall

effective_xp = lambda xp, factor: xp ** factor


def get_skill_weight(skill_level_dict: Dict, skill_experience_dict: Dict) -> Tuple[float, float]:
    """Calculates the skill weight of the player.

    Parameters
    -----------
    skill_level_dict: dict
        A dictionary containing the level of each skill.
        With skill type as key and level as value.

    skill_experience_dict: dict
        A dictionary containing the experience of each skill.
        With skill type as key and experience as value.

    Returns
    -------
    float
        The amount of non-overflow skill weight.
    float
        The amount of overflow skill weight.

    Example
    -------
    >>> skill_level_dict = {
    ...     "enchanting": 10,
    ...     "taming": 10,
    ...     "alchemy": 10,
    ...     "mining": 10,
    ...     "farming": 10,
    ...     "foraging": 10,
    ...     "combat": 10,
    ...     "fishing": 10,
    ... }
    >>> skill_experience_dict = {
    ...     "enchanting": 100000,
    ...     "taming": 100000,
    ...     "alchemy": 100000,
    ...     "mining": 100000,
    ...     "farming": 100000,
    ...     "foraging": 100000,
    ...     "combat": 100000,
    ...     "fishing": 100000,
    ... }
    >>> get_skill_weight(skill_level_dict, skill_experience_dict)
    """
    skill_average = sum(skill_level_dict.values()) / len(skill_level_dict)  # Calculate the average skill level

    n = 12 * ((skill_average / 60) ** 2.44780217148309)

    # p = 1  # 5/11
    r2 = 1.4142135623730950

    temp = []

    for skill, level in skill_level_dict.items():
        skill_weights = srw[skill]
        temp.append(
            (n * skill_weights[level] * skill_weights[-1])  # avg mult * skill mult * type mult
            +
            (skill_weights[-1] * (level / 60) ** r2)  # type mult * skill ratio mult
        )

    skill_rating = (sum(temp) * skill_overall)

    overflow_rating = 0
    for skill_type, xp in skill_experience_dict.items():
        if xp > level60skill:
            factor = overflow_skill_multipliers[skill_type]["factor"]
            effective_over = effective_xp(xp - level60skill, factor)
            rating = effective_over / level60skill
            overflow_mult = overflow_skill_multipliers[skill_type]["overflow_multiplier"]
            t = rating * overflow_mult
            if t > 0:
                overflow_rating += (skill_overall * rating * overflow_mult)

    return skill_rating, overflow_rating
