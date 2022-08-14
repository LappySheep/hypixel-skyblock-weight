import math

from constants import slayer_overall, slayer_depreciation_scaling


def cuberoot(x):
    if x < 0:
        x = abs(x)
        cube_root = x ** (1 / 3) * (-1)
    else:
        cube_root = x ** (1 / 3)
    return cube_root


def calc_slayerscore(exp):
    # thank you Lucy - Desco
    d = exp / 100000
    if exp >= 6416:
        D = (d - math.pow(3, (-5 / 2))) * (d + math.pow(3, -5 / 2))
        u = cuberoot(3 * (d + math.sqrt(D)))
        v = cuberoot(3 * (d - math.sqrt(D)))
        return u + v - 1
    else:
        return math.sqrt(4 / 3) * math.cos(math.acos(d * math.pow(3, 5 / 2)) / 3) - 1


def get_effective_xp(integer_part, ind):
    scaling = slayer_depreciation_scaling[ind]
    total = 0
    for k in range(integer_part):
        k += 1
        calc = (k ** 2 + k) * scaling ** k
        total += calc
    total = round(1000000 * total * (0.05 / scaling), 2)
    return total


def get_actual_xp(int_part):
    return ((int_part ** 3 / 6) + (int_part ** 2 / 2) + (int_part / 3)) * 100000


def new_slayer(score, xp, ind):  # example uses depreciation_scaling = 0.85
    # e.g. 1.5mil xp -> ~3.55 -> 3
    score_rdown = int(score)
    # e.g. 3 -> 788.5k
    effective_rdown = get_effective_xp(score_rdown, ind)
    # e.g. slayer score 3 -> 1mil xp
    actual_rdown = get_actual_xp(score_rdown)
    # distance -> 1.5mil - 1m = 500k xp
    distance = xp - actual_rdown
    # int is 3, 0.85**3 = 0.614125, multiplied by 500k
    effective_distance = distance * slayer_depreciation_scaling[ind] ** score_rdown
    # 788.5k + [reduced 500k] = oiufods
    total_effective = effective_rdown + effective_distance
    return total_effective


def get_slayer_weight(zombie: float, spider: float, wolf: float, enderman: float, blaze: float) -> float:
    """Calculates the slayer weight of the player.

    Parameters
    -----------
    zombie: float
        zombie slayer experience

    spider: float
        spider slayer experience

    wolf: float
        wolf slayer experience

    enderman: float
        enderman slayer experience

    blaze: float
        blaze slayer experience

    Returns
    -------
    float
        The amount of slayer weight.

    Example
    -------

    """
    zombie_score = calc_slayerscore(zombie)
    spider_score = calc_slayerscore(spider)
    wolf_score = calc_slayerscore(wolf)
    eman_score = calc_slayerscore(enderman)
    blaze_score = calc_slayerscore(blaze)

    zombie2 = new_slayer(zombie_score, zombie, 0)
    spider2 = new_slayer(spider_score, spider, 1)
    wolf2 = new_slayer(wolf_score, wolf, 2)
    eman2 = new_slayer(eman_score, enderman, 3)
    blaze2 = new_slayer(blaze_score, blaze, 4)

    individual = zombie2 / 9250 + spider2 / 7019.57 + wolf2 / 2982.06 + eman2 / 996.3003 + blaze2 / 935.0455
    extra = (zombie + 1.6 * spider + 3.6 * wolf + 10 * enderman + 10 * blaze) / 1000000
    return slayer_overall * (individual + extra)

# slayer_rating, total_slayers = calc_slayers(*slayers)
