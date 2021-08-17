import asyncio
import math


worth = [ # index = floor, 0 = entrance, 8-14 = master, item = worth per run
  0.0827,
  2.1034, 4.5966,
  7.9383, 13.4018, # 4
  23.1071, 43.7857,
  63.3437, # 7

  24, # m1
  33.5, 46.575, # m3
  81.9553, 99.6368, # m5
  154.4188, # 488.376 # m7
] # worth is not rating, but is the multiplier
max_1000 = sum(worth[:8]) * 1000
m_max_1000 = sum(worth[8:]) * 1000

buffs = {
  "1": 125, "2": 250,
  "3": 450, "4": 775,
  "5": 1000, "6": 1400,
  "7": 1750
}

"""
upper bound buffs:
  m1 completion: +125
  m2 completion: +250
  m3 completion: +450
  m4 completion: +775
  m5 completion: +1000
  m6 completion: +1400
  m7 completion: +1750
"""


async def ordered(d):
  l = []
  for i in range(8):
    if str(i) in d:
      l.append((i, d[str(i)]))
  return l

async def calc_dgc(data, master_data):
  upper_bound = 1500 # caps at 5500,7250 for m6/m7
  beaten, m_beaten = data, master_data
  b, mb = await ordered(beaten), await ordered(m_beaten)


  score = 0 # turns into weight later
  for floor, amt in [((floor,int(amt))) for floor,amt in b]:
    if amt > 1000:
      excess = amt-1000
      amt = 1000
    else:
      excess = 0

    s = (amt * worth[floor])

    if excess: # more than 0
      s *= math.log(((excess / 1000)+1), 7.5)+1

    score += s

  
  rating = (score / max_1000) * upper_bound





  try:
    for f, v in mb:
      if str(f) in buffs:
        threshold = 20
        if v >= threshold:
          upper_bound += buffs[str(f)]
        else: # less
          upper_bound += (buffs[str(f)] * (v/threshold)**1.840896416)

    m_score = 0
    for floor, amt in [(((floor-1),int(amt))) for floor,amt in mb]:
      if amt > 1000:
        excess = amt-1000
        amt = 1000
      else:
        excess = 0

      try:
        s = (amt * worth[8:][floor])
      except:
        s = 0 # floor not in worth dict

      if excess: # more than 0
        s *= math.log(((excess / 1000)+1), 5)+1

      m_score += s

    m_rating = (m_score / m_max_1000) * upper_bound
  except:
    m_rating = 0

  return rating, m_rating