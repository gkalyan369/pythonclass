import sys, getopt

print("Total no. of arguments passed: ", len(sys.argv))
print("Program name is: ", sys.argv[0])
print("Program arguments are: ", sys.argv[1:])


def main(argv):
    inputfile = ""
    outputfile = ""
    try:
        opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Usage: test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Input file is : ', inputfile)
    print('Output file is : ', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
