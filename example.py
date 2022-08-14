from typing import Tuple

import requests

from calcs.dungeon_comp_weight import get_dungeon_comp_weight
from calcs.dungeon_xp_weight import get_cata_xp_weight
from calcs.skill_weight import get_skill_weight
from calcs.slayer_weight import get_slayer_weight
from example_functions import get_skill_lvl

uuid = "329eea92f5f74580a4b68ef98870c525"  # minecraft uuid
apikey = "0948daf9-289b-4c4f-9fbf-8dd4bfe725f3"  # hypixel api key

response = requests.get("https://api.hypixel.net/skyblock/profiles", params={
    "key": apikey,
    "uuid": uuid
})  # Request the profiles
response_json = response.json()  # Get the json response

# Sort the profile by last save and select the one which is the most recent
all_profile_data = sorted(response_json.get("profiles", []), key=lambda x: x["members"][uuid]["last_save"])[-1]
player_profile_data = all_profile_data["members"][uuid]  # Get the player profile data from all the profile data


def lily_skill_weight(profile: dict) -> Tuple[float, float]:
    """
    Get the skill weight of the player
    """
    skill_experience_dict = {}
    skill_level_dict = {}

    # Loop through all the skills lily weight uses
    for skill_type in ["enchanting", "taming", "alchemy", "mining", "farming", "foraging", "combat", "fishing"]:
        experience = profile.get(f"experience_skill_{skill_type}", 0)  # Get the experience of the skill if it exists
        skill_experience_dict[skill_type] = experience  # Add the experience to the experience skill dict
        skill_level_dict[skill_type] = int(get_skill_lvl(experience))  # Add the skill level to the counter

    return get_skill_weight(skill_level_dict, skill_experience_dict)  # Calculate the skill weight


def lily_catacombs_weight(profile: dict) -> float:
    # Get the catacombs weight of the player
    try:
        cata_completions = profile["dungeons"]["dungeon_types"]["catacombs"]["tier_completions"]
        # Try to get the catacombs completions
    except KeyError:
        # If the keys are not found set to default value
        cata_completions = {}
    try:
        m_cata_compl = profile["dungeons"]["dungeon_types"]["master_catacombs"]["tier_completions"]
    except KeyError:
        m_cata_compl = {}
    try:
        cata_xp = profile["dungeons"]["dungeon_types"]["catacombs"]["experience"]
    except KeyError:
        cata_xp = 0

    # Calculate the catacombs completion weight
    cata_weight, master_cata_weight = get_dungeon_comp_weight(cata_completions, m_cata_compl)

    cata_xp_weight = get_cata_xp_weight(cata_xp)  # Calculate the catacombs xp weight
    return cata_weight, master_cata_weight, cata_xp_weight


def lily_slayer_weight(profile: dict) -> float:
    kwargs = {  # Loop through the slayer bosses and get the xp if they key exists else default value
        boss_type: boss_data.get("xp", 0) for boss_type, boss_data in profile["slayer_bosses"].items()
    }
    return get_slayer_weight(**kwargs)  # Calculate the slayer weight and pass the kwargs to the function


skill_weight, skill_overflow = lily_skill_weight(player_profile_data)
cata_weight, master_cata_weight, cata_xp_weight = lily_catacombs_weight(player_profile_data)
slayer_weight = lily_slayer_weight(player_profile_data)

result = {
    "total": skill_weight + skill_overflow + cata_weight + master_cata_weight + cata_xp_weight + slayer_weight,
    "skill_weight": {
        "base": skill_weight,
        "overflow": skill_overflow
    },
    "catacombs": {
        "completion": {
            "base": cata_weight,
            "master": master_cata_weight
        },
        "experience": cata_xp_weight
    },
    "slayer": slayer_weight

}
print(result)
