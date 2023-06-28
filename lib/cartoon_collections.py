def roll_call_dwarves(dwarves):
    length = len(dwarves)
    for n in range(0,length):
        print(f"{n+1}. {dwarves[n]}")

def summon_captain_planet(calls):
    return [f"{call.title()}!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
        else:
            pass
    return False

def find_the_cheese(strs):
    cheeses = ["cheddar", "gouda", "camembert"]
    for str in strs:
        if str in cheeses:
            return str
    return None