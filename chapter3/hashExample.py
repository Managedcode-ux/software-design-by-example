def naive_hash(data):
    print("DATA RECEIVED => ", data)
    print(sum(data))
    return sum(data) % 13


example = bytes("hashing", "utf+8")
print("BYTE representation => ", example)
for i in range(1, len(example) + 1):
    substring = example[:i]
    hash = naive_hash(substring)
    print(f"HASH => {hash:2}  SUBSTRING => {substring}")
