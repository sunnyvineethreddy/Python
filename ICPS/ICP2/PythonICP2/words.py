
fname = input("Enter file name: ")

with open(fname, 'r') as f:
    for line in f:
        num_words = 0
        words = line.split(" ")
        num_words += len(words)
        print("%s, %d\n" % (line.rstrip("\n"),num_words))