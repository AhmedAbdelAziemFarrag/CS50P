results = ["Mario", "Luigi"]

results.append("Princess")
results.insert(0, "Bowser")
print(results)

results.remove("Bowser")
print(results)

results.append(["Yoshi", "Koopa Troopa", "Toad"])
print(results)
results.remove(["Yoshi", "Koopa Troopa", "Toad"])
print(results)

results.extend(["Yoshi", "Koopa Troopa", "Toad"])
print(results)

results.reverse()
print(results)