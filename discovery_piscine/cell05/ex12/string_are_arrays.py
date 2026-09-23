import sys

if len(sys.argv) != 2:
    print("none")
else:
    count = sys.argv[1].count('z')
    if count == 0:
        print("none")
    else:
        print("z" * count)
