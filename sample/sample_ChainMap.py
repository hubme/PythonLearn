# ChainMap是由Python标准库提供的一种数据结构，允许你将多个字典视为一个。

from collections import ChainMap

toys = {"Blocks": 30, "Monopoly": 20}
computers = {"iMac": 1000, "Chromebook": 800, "PC": 400}
clothing = {"Jeans": 40, "T-Shirt": 10}

inventory = ChainMap(toys, computers, clothing)
print(inventory["iMac"])
print(inventory["Jeans"])
print(inventory.get("IMac", "aaa"))