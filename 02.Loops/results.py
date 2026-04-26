results = ["Mario", "Luigi"]
results.append("Princess")
print(results)

results.extend(["Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."])
print(results)

results.remove("Bowser")
print(results)

results.insert(0, "Bowser")
print(results)

results.reverse()
print(results)
