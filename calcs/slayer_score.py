import asyncio
import numpy


from math import log


async def resolve(y):
  return max([round(n.real, 10)for n in numpy.roots([(1/6), (1/2), (1/3), -y])if numpy.isreal(n)])


async def calc_slayerscore(xp):
  y = xp / 100000
  # y = (x^3 / 6) + (x^2 / 2) + (x / 3)
  x = await resolve(y)
  return x
