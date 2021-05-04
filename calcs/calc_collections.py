import asyncio
import math


coll_weights = {
  # farming
  "PUMPKIN": 1280,
  "POTATO_ITEM": 2560,
  "PORK": 160,
  "LEATHER": 160,
  "MUTTON": 160,
  "CACTUS": 10240,
  "WHEAT": 640,
  "SEEDS": 1280,
  "MELON": 5120,
  "FEATHER": 320,
  "RAW_CHICKEN": 320,
  "CARROT_ITEM": 2560,
  "RABBIT": 160,
  "MUSHROOM_COLLECTION": 320,
  "SUGAR_CANE": 2560,
  "NETHER_STALK": 1920,
  "INK_SACK:3": 5120, # cocoa beans

  # mining
  "COBBLESTONE": 640,
  "INK_SACK:4": 2560, # lapis lazuli
  "DIAMOND": 320,
  "GOLD_INGOT": 320,
  "IRON_INGOT": 320,
  "REDSTONE": 1280,
  "QUARTZ": 120,
  "OBSIDIAN": 160,
  "COAL": 320,
  "GLOWSTONE_DUST": 640,
  "GRAVEL": 160,
  "NETHERRACK": 320,
  "SAND": 160,
  "ICE": 160,
  "ENDER_STONE": 1280,
  "EMERALD": 320,
  "MITHRIL": 640,

  # combat
  "ENDER_PEARL": 1920,
  "BLAZE_ROD": 280,
  "GHAST_TEAR": 960,
  "ROTTEN_FLESH": 280,
  "STRING": 420,
  "SPIDER_EYE": 420,
  "SULPHUR": 280,
  "SLIME_BALL": 480,
  "BONE": 280,
  "MAGMA_CREAM": 360,

  # foraging
  "LOG_2:1": 1920, # dark oak wood
  "LOG:3": 960, # jungle wood
  "LOG": 720, # oak wood
  "LOG:2": 650, # birch wood
  "LOG:1": 810, # spruce wood
  "LOG_2": 960, # acacia wood

  # fishing
  "CLAY_BALL": 5120,
  "RAW_FISH": 200, # raw fish
  "RAW_FISH:1": 160, # raw salmon
  "RAW_FISH:3": 120, # pufferfish
  "RAW_FISH:2": 100, # clownfish
  "PRISMARINE_CRYSTALS": 80,
  "PRISMARINE_SHARD": 80,
  "INK_SACK": 50, # ink sacs
  "WATER_LILY": 25, # lily pads
  "SPONGE": 12.5,
}
# "ITEMNAME": <amount in collection per 0.001 weight>,


async def calc_collections(coll_data):
  coll_weight = 0
  for mat in coll_data:
    if mat in coll_weights.keys():
      w, w2 = (coll_data[mat] / coll_weights[mat]) / 1000, 0
      if w > 100:
        w, e = 100, w - 100
        w2 = 2.5536676800365615 ** math.log(e, math.e)
      coll_weight += (w + w2)

  return coll_weight
