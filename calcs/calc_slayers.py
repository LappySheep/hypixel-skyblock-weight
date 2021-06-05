import asyncio
from calcs.calc_slayerscore import calc_slayerscore


def effective_int(integer_part):
  t = 0
  for k in range(integer_part):
    k += 1
    calc = (k**2 + k) * 0.79**k
    t += calc
  t = round(1000000 * t / 17, 2)
  return t


def actual(int_part):
  return ((int_part**3 / 6) + (int_part**2 / 2) + (int_part / 3))*100000


async def new_slayer(score, xp):
  step1 = int(score) # e.g. 1.5mil xp -> ~3.55
  step2 = effective_int(step1) # e.g. 3 -> 788.5k
  step3 = actual(step1) # e.g. slayer score 3 -> 1mil xp
  step4 = xp - step3 # distance -> 1.5mil - 1m = 500k xp
  step5 = step4 * 0.79**step1 # int is 3, 0.79**3 = ??, multiplied by 500k
  step6 = step2 + step5 # 788.5k + [reduced 500k] = oiufods
  return step6 # return step 6


async def calc_slayers(zombie, spider, wolf, enderman):
  zombie_score = await calc_slayerscore(zombie)
  spider_score = await calc_slayerscore(spider)
  wolf_score = await calc_slayerscore(wolf)
  eman_score = await calc_slayerscore(enderman)

  zombie2 = await new_slayer(zombie_score, zombie)
  spider2 = await new_slayer(spider_score, spider)
  wolf2 = await new_slayer(wolf_score, wolf)
  eman2 = await new_slayer(eman_score, enderman)

  individual = zombie2/6000 + spider2/4500 + wolf2/2000 + eman2/925
  extra = (zombie + spider + (2*wolf) + (2*enderman)) / 240000
  return (individual + extra), (zombie + spider + wolf + enderman)
