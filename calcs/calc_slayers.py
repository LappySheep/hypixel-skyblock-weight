from .slayer_score import calc_slayerscore

depreciation_scaling = [0.75030106128, 0.7732512436, 0.80852054920, 0.8374104242, 0.87]
overall = 2


def effective_int(integer_part, ind):
  scaling = depreciation_scaling[ind]
  total = 0
  for k in range(integer_part):
    k += 1
    calc = (k**2 + k) * scaling**k
    total += calc
  total = round(1000000 * total * (0.05/scaling), 2)
  return total


def actual(int_part):
  return ((int_part**3 / 6) + (int_part**2 / 2) + (int_part / 3))*100000


def new_slayer(score, xp, ind): # example uses depreciation_scaling = 0.85
  # e.g. 1.5mil xp -> ~3.55 -> 3
  score_rdown = int(score)
  # e.g. 3 -> 788.5k
  effective_rdown = effective_int(score_rdown, ind)
  # e.g. slayer score 3 -> 1mil xp
  actual_rdown = actual(score_rdown)
  # distance -> 1.5mil - 1m = 500k xp
  distance = xp - actual_rdown
  # int is 3, 0.85**3 = 0.614125, multiplied by 500k
  effective_distance = distance * depreciation_scaling[ind]**score_rdown
  # 788.5k + [reduced 500k] = oiufods
  total_effective = effective_rdown + effective_distance
  return total_effective


def calc_slayers(zombie, spider, wolf, enderman, blaze):
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

  individual = zombie2/8390.64 + spider2/7019.57 + wolf2/2982.06 + eman2/1118.81 + blaze2/751.281
  extra = (zombie + 1.6*spider + 3.6*wolf + 10*enderman + 15*blaze) / 1000000
  return overall * (individual + extra), (zombie + spider + wolf + enderman + blaze)
