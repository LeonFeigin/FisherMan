import pickle

balance = 0
# 'hands', 'Basic Bamboo Rod', 'Sturdy Wooden Rod', 'Fiberglass Rod', 'Carbon Fiber Rod', 'Professional Titanium Rod'
fishingRod = 'hands'
# 'none', 'Worms', 'Bread Crumbs', 'Minnow', 'Artificial Lure', 'Magic Fish'
fishingBait = 'none'
# [fish, weight, value, amount]
fishInventory = []


file = open('save', 'wb')
pickle.dump([balance,fishingRod,fishingBait,fishInventory], file)
file.close()