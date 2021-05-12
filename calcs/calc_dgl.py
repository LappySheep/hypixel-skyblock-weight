import asyncio

overall = 0.6211258376589867
lv50 = 569809640

exp_table = [
  0,
  50, 125, 235, 395, 625, 955, 1425, 2095, 3045, 4385, # 10
  6275, 8940, 12700, 17960, 25340, 35640, 50040, 70040, 97640, 135640, # 20
  188140, 259640, 356640, 488640, 668640,
  911640, 1239640, 1684640, 2284640, 3084640, # 30
  4149640, 5559640, 7459640, 9959640, 13259640,
  17559640, 23159640, 30359640, 39559640, 51559640, # 40
  66559640, 85559640, 109559640, 139559640, 177559640,
  225559640, 285559640, 360559640, 453559640, 569809640, # 50
  2147483647
]


async def calc_dgl(exp):
  lvl = -1
  for level in exp_table:
    if exp >= level:
      lvl += 1
    else:
      break

  if lvl != 50:
    dist = exp_table[int(lvl//1)+1] - exp_table[int(lvl//1)]
    progress = ((((exp - exp_table[int(lvl//1)]) / dist)*1000)//1)/1000
    lvl += progress

  if exp < 569809640:
    n = 0.2 * (lvl / 50) ** 2.967355422
  else:
    part = 142452410 # 25% of level 50
    temp_lvl = 50+((exp-lv50)/part) # cata 50 x2 = temp level 54
    n = 0.2 * (1+((temp_lvl-50) / 50)) ** 2.967355422


  excess = 0
  if lvl != 0:
    try:
      temp_lvl
    except:
      weight = overall * ((1.18340401286164044**(lvl+1) - 1.05994990217254) * (1 + n))
      return lvl, weight, 0
    else:
      weight = 4000 * (n/0.2)
      excess = (temp_lvl - 50)/4
      return lvl, weight, excess
  else:
    return 0,0,0
