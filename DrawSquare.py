def squares (w, h, *par):
    mat = ["".ljust (h, ".") for _ in range (w)]
    for rect in par:
        for wid in range (rect[0], rect[0] + rect[2]):
            mat[wid] = mat[wid][:rect[1]] + len(mat[wid][rect[1] : (rect[1] + rect[2])]) * rect[3] + mat[wid][(rect[1] + rect[2]):]



    for i in range (h):
        toprnt = ""
        for j in range (w):
            toprnt += mat[j][i]
        print (toprnt)