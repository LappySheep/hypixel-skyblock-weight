Base Link: https://weight-api-314022.ew.r.appspot.com/

DM me if you want to get an API key.



https://weight-api-314022.ew.r.appspot.com/api/v1/weight/all/player?key=[YOUR_API_KEY]
  &hp_key=
    This is your Hypixel API key. Keys aren't stored. I don't have an elevated API key so until I do, you will have to provide your key in the request.
  &ign=
    String. In-game name of the player you want to check.
  Returns: Total weight, and each weight individually. This assumes the 'latest' profile of the player. Currently no way to specify but based on context it doesn't seem like it's needed.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/skills/main?key=[YOUR_API_KEY]
  &skills=
    Comma-separated (no spaces), 8 skills. Order: Enchanting / Taming / Alchemy / Mining / Farming / Foraging / Combat / Fishing.
  Returns: Skill levels, skill average, weight.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/skills/overflow?key=[YOUR_API_KEY]
  &skill=
    Must be in < "ench", "tame", "alch", "mine", "farm", "fora", "comb", "fish" >.
  &exp=
    Float. This is the skill's total exp, not the excess.
  Returns: Checked skill, excess exp, overflow weight.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/slayers/score?key=[YOUR_API_KEY]
  &exp=
    Integer. Slayer score does not depend on the slayer type.
  Returns: Slayer type exp, slayer score.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/slayers/rating?key=[YOUR_API_KEY]
  &zombie=
    Integer. Amount of zombie slayer exp.
  &spider=
    Integer. Amount of spider slayer exp.
  &wolf=
    Integer. Amount of wolf slayer exp.
  Returns: Slayer scores for each type, total slayer score, average slayer score, total slayer exp, total slayer weight.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/dungeons/level?key=[YOUR_API_KEY]
  &exp=
    Float. Amount of catacombs exp.
  Returns: Catacombs level, dungeons level weight, excess. Excess is the amount over catacombs 50; an excess of 3 means catacombs 50, x4.


https://weight-api-314022.ew.r.appspot.com/api/v1/weight/dungeons/collections?key=[YOUR_API_KEY]
  &beaten=
    Comma-separated (no spaces), 8 floors, entrance floor + floors 1-7. Amount of completions for each floor.
  &m_beaten=
    Comma-separated (no spaces), 6 floors (for now), master floors 1-6. Amount of completions for each floor.
  Returns: Amount of completions for each floor, weight, master weight.
