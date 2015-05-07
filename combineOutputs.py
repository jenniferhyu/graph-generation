T = 495
fout = open( "answer.out", "w+")
for t in range(1, T+1):
    try:
        fin = open( str(t) + ".out", "r")
        result = fin.readline()
        if len(result) == 0:
            print("Missing output file for case " + str(t))
            fout.write("\n")
        fout.write(result)
        fin.close()
    except IOError as err:
        pass
fout.close()
