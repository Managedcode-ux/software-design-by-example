import sys


def same_bytes(left_name, right_name):
    left_byte = open(left_name, 'rb').read()
    right_byte = open(right_name, 'rb').read()
    return left_byte == right_byte


def find_duplicates(filenames):
    matches = []
    for i_left in range(len(filenames)):
        left = filenames[i_left]
        print("CURRENT LEFT => ", left, end='\n')
        for i_right in range(i_left):
            right = filenames[i_right]
            print("CURRENT Right => ", right)

            if same_bytes(left, right):
                matches.append((left, right))
    return matches


if __name__ == '__main__':
    # take all the commandline argument except the script name when a running python duplicate_naive.py file1.txt file2.txt file3.txt
    duplicate = find_duplicates(sys.argv[1:])
    for (left, right) in duplicate:
        print(left, right)
