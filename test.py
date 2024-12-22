

def generate_santa_pairs(names):
    from random import shuffle
    
    receivers = names.copy()
    
    while any(giver == receiver for giver, receiver in zip(names, receivers)):
        shuffle(receivers)
    
    return list(zip(names, receivers))

nameList = ["Henrik", "Karl", "Rasmus", "Arne", "Art"]
pairs = generate_santa_pairs(nameList)

for giver, receiver in pairs:
    print(f"{giver} -> {receiver}")