import sys
import hashlib


def same_byte(left_name, right_name):
    left = open(left_name, 'rb').read()
    right = open(right_name, 'rb').read()
    return left == right


def naive_hash(data):
    return sum(data) % 13


def find_group(filenames):
    groups = {}
    for fn in filenames:
        data = open(fn, 'rb').read()
        hash_code = hashlib.sha256()
        hash_code.update(data)
        if hash_code.hexdigest() not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        for i_right in range(i_left):
            right = filenames[i_right]
            if same_byte(left, right):
                matches.append((left, right))
    return matches


# main function when using sha256 Hashing
if __name__ == '__main__':
    groups = find_group(sys.argv[1:])
    print(groups)
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))

# main function when using naive hashing
# if __name__ == "__main__":
#     groups = find_group(sys.argv[1:])
#     print("GROUPS =>", groups)
#     # print(groups.values())
#     for filenames in groups.values():
#         # print(filenames)
#         duplicates = find_duplicates(list(filenames))
#         for (left, right) in duplicates:
#             print(left, right)
