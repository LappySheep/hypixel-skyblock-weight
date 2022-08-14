def get_skill_lvl(exp):
    levels = {
        "0": 0, "1": 50, "2": 175, "3": 375, "4": 675, "5": 1175, "6": 1925, "7": 2925, "8": 4425, "9": 6425,
        "10": 9925, "11": 14925, "12": 22425, "13": 32425, "14": 47425, "15": 67425, "16": 97425, "17": 147425,
        "18": 222425, "19": 322425, "20": 522425, "21": 822425, "22": 1222425, "23": 1722425, "24": 2322425,
        "25": 3022425, "26": 3822425, "27": 4722425, "28": 5722425, "29": 6822425, "30": 8022425, "31": 9322425,
        "32": 10722425, "33": 12222425, "34": 13822425, "35": 15522425, "36": 17322425, "37": 19222425,
        "38": 21222425, "39": 23322425, "40": 25522425, "41": 27822425, "42": 30222425, "43": 32722425,
        "44": 35322425, "45": 38072425, "46": 40972425, "47": 44072425, "48": 47472425, "49": 51172425,
        "50": 55172425, "51": 59472425, "52": 64072425, "53": 68972425, "54": 74172425, "55": 79672425,
        "56": 85472425, "57": 91572425, "58": 97972425, "59": 104672425, "60": 111672425
    }  # A dictionary of the xp required for each level

    for level in levels:  # Loop through the levels
        if levels[level] > exp:
            # If the xp required for the current level is greater than the level must be between the previous level and the current level
            lowexp = levels[f"{int(level) - 1}"]  # Get the xp required for the previous level
            highexp = levels[level]  # Get the xp required for the current level
            difference = highexp - lowexp  # Get the difference between the two xp required levels
            extra = exp - lowexp  # Get the extra xp required
            percentage = (extra / difference)  # Get the decimal of the level progress
            return (int(level) - 1) + percentage  # Return the previous level plus the decimal
    return 60

