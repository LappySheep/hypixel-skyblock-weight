


overall = 168/185*2 # 10.5k*2

lv60 = 111672425
factors = [
  0.8970917856434051,
  0.9038421238097485,
  0.88836322872987277,
  0.929383683888072,
  0.9329795030275141,
  0.9348318885884501,
  0.9368106217543707,
  0.9401081007640278,
]

overflow_skill_multipliers = [
  6.3207, # ench
  9.2003, # tame
  4.1641, # alch
  77.2840, # mine
  123.5962, # farm
  163.0884, # comb
  227.5907, # fora
  504.2361, # fish
]

def effective_xp(xp, factor):
  ht = xp / lv60
  z = 0
  r = xp
  if ht < 1:
    return float(xp)
  for i in range(int(ht)+1):
    if r >= lv60:
      r -= lv60
      z += factor**i
  return (z*lv60)

def calc_skills(stat_set, srw, exp):
  ench, tame, alch, mine, farm, fora, comb, fish = stat_set[:8]
  
  shorthand = ["ench", "tame", "alch", "mine", "farm", "fora", "comb", "fish"]
  sAvg = (ench + tame + alch + mine + farm + fora + comb + fish) / 8

  sAvgCapped = (
    ench + (tame if tame<=50 else 50) + (alch if alch<=50 else 50) + mine + farm + (fora if fora<=50 else 50) + comb + (fish if fish<=50 else 50)
  ) / 8

  n = 12 * ((sAvg / 60) ** 2.44780217148309)

  p = 1 #5/11
  r2 = 1.4142135623730950

  temp = []

  for index,skill in enumerate(["enchanting", "taming", "alchemy", "mining", "farming", "foraging", "combat", "fishing"]):
    skill_stuff = srw[skill]
    lvl = eval(str(shorthand[index]))
    temp.append(
      (n * skill_stuff[lvl] * skill_stuff[-1]) # avg mult * skill mult * type mult
      + 
      (skill_stuff[-1] * (lvl/60)**(r2) * p) # type mult * skill ratio mult
    )

  skill_rating = (sum(temp) * overall)

  overflow_rating = 0
  for ind, xp in enumerate(exp[0:8]):
    if xp > lv60:
      fct = factors[ind]
      effective_over = effective_xp(xp - lv60, fct)
      rating = effective_over / lv60
      osm = overflow_skill_multipliers[ind]
      t = rating * osm
      if t > 0:
        overflow_rating += (2 * rating * osm)


  return skill_rating, sAvg, overflow_rating, sAvgCapped
