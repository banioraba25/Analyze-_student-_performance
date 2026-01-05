scores = [20, 88, 49, 51]
threshold = 50

weakCount = 0
goodCount = 0

for score in scores:
    if score < threshold:
        weakCount += 1
    else:
        goodCount += 1

print("Number of Weak modules:", weakCount)
print("Number of Good modules:", goodCount)
