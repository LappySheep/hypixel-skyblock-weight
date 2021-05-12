import asyncio
import math


worth = [ # index = floor, 0 = entrance, 8-14 = master, item = worth per run
  0.0827,
  2.1034, 4.5966,
  7.9383, 13.4018, # 4
  23.1071, 43.7857,
  93, # 7

  26, # m1
  37, 56.5, # m3
  92, 158.8, # m5
  289.04, # 488.376 # m7
] # worth is not rating, but is the multiplier
max_1000 = sum(worth) * 1000
m_max_1000 = sum(worth[8:]) * 1000

buffs = {
  "1": 250, "2": 350,
  "3": 500, "4": 700,
  "5": 1000, "6": 1500,
  "7": 2200
}

"""
upper bound buffs:
  m1 completion: +250
  m2 completion: +350
  m3 completion: +500
  m4 completion: +700
  m5 completion: +1000
  m6 completion: +1500
  m7 completion: +2200
"""


async def ordered(d):
  l = []
  for i in range(8):
    if str(i) in d:
      l.append((i, d[str(i)]))
  return l

async def calc_dgc(data, master_data):
  upper_bound = 2500 # caps at 9000
  beaten, m_beaten = data, master_data
  b, mb = await ordered(beaten), await ordered(m_beaten)


  score = 0 # turns into weight later
  for floor, amt in [((floor,int(amt))) for floor,amt in b]:
    if amt > 1000:
      excess = amt-1000
      amt = 1000
    else:
      excess = 0

    s = (amt * worth[:8][floor])

    if excess: # more than 0
      s *= math.log(((excess / 1000)+1), math.e)+1

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
        s *= math.log(((excess / 1000)+1), math.e)+1

      m_score += s

    m_rating = (m_score / m_max_1000) * upper_bound
  except:
    m_rating = 0

  return rating, m_rating
