import sys
from logic import create_matrix_from_file, get_longest_seq


def start(args):
    for x in args:
        x = "tests/" + x
        matrix = create_matrix_from_file(x)
        if matrix is not None:
            res = get_longest_seq(matrix)
            print(res)


def main():
    if len(sys.argv) > 5:
        print("No more than 4 args are allowed!")
        return
    args = []
    for i in range(1, len(sys.argv)):
        args.append(sys.argv[i])
    start(args)


if __name__ == '__main__':
    main()
