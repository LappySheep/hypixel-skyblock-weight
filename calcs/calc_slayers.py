import asyncio


async def new_slayer(s):
  if s > 25000000:
    return 7985000 + ((s - 25000000) * 0.1)
  elif s > 12500000: # 7.985mil @ 25mil xp
    return 6110000 + ((s - 12500000) * 0.25)
  elif s > 5000000: # 6.11mil @ 12.5mil xp
    return 3110000 + ((s - 5000000) * 0.4)
  elif s > 1500000: # 3.11mil @ 5mil xp
    return 1185000 + ((s - 1500000) * 0.55)
  elif s > 700000: # 1.185m @ 1.5mil xp
    return 625000 + ((s - 700000) * 0.7)
  elif s > 200000: # 625k @ 700k xp
    return 200000 + ((s - 200000) * 0.85)
  else: # x <= 200000
    return s


async def calc_slayers(zombie, spider, wolf):
  zombie2 = await new_slayer(zombie)
  spider2 = await new_slayer(spider)
  wolf2 = await new_slayer(wolf)

  individual = zombie2/6250 + spider2/4500 + wolf2/2250
  extra = (zombie + spider + wolf) / 150000
  return (individual + extra), (zombie + spider + wolf) # base + extra
