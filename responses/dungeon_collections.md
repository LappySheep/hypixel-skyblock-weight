# Function - calc_dgc()

*Arguments*: **data, master_data**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**data**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data refers to the `["profiles"][index]["members"][uuid]["dungeons"]["dungeon_types"]["catacombs"]["tier_completions"]` entry in the JSON object returned by the Hypixel API's /skyblock/profiles/ endpoint.

&nbsp;&nbsp;&nbsp;&nbsp;**master_data**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;master_data refers to the `["profiles"][index]["members"][uuid]["dungeons"]["dungeon_types"]["master_catacombs"]["tier_completions"]` entry in the JSON object returned by the Hypixel API's /skyblock/profiles/ endpoint.

<br />*Responses*: **rating, m_rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;**rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rating is the amount of dungeons weight awarded by the first 8 floors.

&nbsp;&nbsp;&nbsp;&nbsp;**m_rating**<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;m_rating is the amount of dungeons weight awarded by the master floors.
