numbers = [3, 7, 12, 18, 21, 30]

peers = []

for n in numbers:
    if n % 2 == 0:
        peers.append(n)

print(peers)
