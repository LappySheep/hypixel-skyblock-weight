overall = 168/185*2 # 10.5k*2

lv60 = 111672425
factors = [
  0.9560187460,     # 0.4
  0.9422102267,     # 0.3
  0.9227482118,     # 0.2
  0.9713042815,     # 0.55
  0.9861914807,     # 0.75
  0.9892892803,     # 0.8
  0.9892892803,     # 0.8
  0.9828798757,     # 0.7
]

overflow_skill_multipliers = [
  7, # ench
  4, # tame
  1.5, # alch
  25, # mine
  70, # farm
  125, # comb
  125, # fora
  85, # fish
]

effective_xp = lambda xp, factor: xp**factor


def calc_skills(stat_set, srw, exp):
  ench, tame, alch, mine, farm, fora, comb, fish = stat_set[:8]
  
  shorthand = ["ench", "tame", "alch", "mine", "farm", "fora", "comb", "fish"]
  sAvg = (ench + tame + alch + mine + farm + fora + comb + fish) / 8

  sAvgCapped = (
    ench + (tame if tame<=50else 50) + (alch if alch<=50else 50) + mine + farm + (fora if fora<=50else 50) + comb + (fish if fish<=50else 50)
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
        overflow_rating += (overall * rating * osm)


  return skill_rating, sAvg, overflow_rating, sAvgCapped



# skill_rating, sAvg, overflow_rating, sAvgCapped = calc_skills(stat_set, srw, exp)
# 'exp' is in this format: 
# exp = [
#   enchanting_exp, taming_exp, alchemy_exp, mining_exp,
#   farming_exp, foraging_exp, combat_exp, fishing_exp,
#   zombie_exp, spider_exp, wolf_exp, eman_exp, blaze_exp
# ]
# 'stat_set' is the same as 'exp', but all skill xp is converted to integer levels instead
# 'skill_rating' is the amount of non-overflow skill weight
# 'sAvg' is the player's skill average but counting every skill to level 60 regardless of in game cap
# 'sAvgCapped' is the player's skill average but using in game caps
# overflow_rating is the amount of overflow skill weight
