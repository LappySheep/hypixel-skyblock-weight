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

# alternative
def s(x):d,z=x/10**5,3**(-5/2);j=((d-z)*(d+z))**0.5;return(3*(d+j))**(1/3)+(3*(d-j))**(1/3)-1if x>=6416else(4/3)**0.5*math.cos(math.accos(d*z)/3)-1
# thank you lucy
