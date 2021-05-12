import asyncio


lv60 = 111672425
overflow_skill_multipliers = [
    8, # ench
    12.2, # tame
    5, # alch
    125, # mine
    200, # farm
    260, # comb
    350, # fora
    650, # fish
]

async def calc_skills(stat_set, srw, exp):
    ench, tame, alch, mine, farm, fora, comb, fish, zombie, spider, wolf = stat_set
    
    shorthand = ["ench", "tame", "alch", "mine", "farm", "fora", "comb", "fish"]

    sAvg = (ench + tame + alch + mine + farm + fora + comb + fish) / 8

    n = 12 * ((sAvg / 60) ** 2)

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

    skill_rating = sum(temp)

    overflow_skills = {}
    overflow_rating = 0
    for ind, xp in enumerate(exp[0:8]):
        if xp > lv60:
            rating = (xp - lv60) / lv60
            osm = overflow_skill_multipliers[ind]
            t = rating * osm
            if t > 0:
                overflow_rating += (rating * osm)


    return skill_rating, sAvg, overflow_rating
