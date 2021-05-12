# Function - calc_skills()

*Arguments*: **stat_set, srw, exp**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**stat_set**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stat_set consists of an array of length 11. The first 8 items refer to the levels of each skill - enchanting, taming, alchemy, mining, farming, foraging, combat, and fishing. The last 3 are slayer values, but are not used in this function. This may be changed in the future.<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Each skill must be an integer between 0 and 60.

&nbsp;&nbsp;&nbsp;&nbsp;**srw**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;srw refers to the JSON object which can be found in srw.py.

&nbsp;&nbsp;&nbsp;&nbsp;**exp**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exp consists of an array of length 11. The first 8 items refer to the experience values of each skill - enchanting, taming, alchemy, mining, farming, foraging, combat, and fishing. The last 3 are slayer values, but are not used in this function. This may be changed in the future.

<br />*Responses*: **skill_rating, sAvg, overflow_rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**skill_rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;skill_rating is the player's skill weight. This does **not** include overflow weight.

&nbsp;&nbsp;&nbsp;&nbsp;**sAvg**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sAvg is the player's skill average. Note that *every* skill is considered to level 60, not just the ones found in-game.

&nbsp;&nbsp;&nbsp;&nbsp;**overflow_rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overflow_rating is the player's overflow skill weight. This does **not** include the main skills weight.
