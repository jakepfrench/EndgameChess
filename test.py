# https://www.flaticon.com/authors/victoruler

alphaToIndex = {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7}

indexToAlpha = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h"}

def possibleMoves(piece, m, n):
    p = piece.lower()
    possibleMoves = []
    if 'k' in p:    # king
        for sign in ['+ ', '- ', ' +', ' -', '++', '--', '-+', '+-']:
            if '+ ' in sign:
                mNew, nNew = m + 1, n
            elif '- ' in sign:
                mNew, nNew = m - 1, n
            elif ' +' in sign:
                mNew, nNew = m, n + 1
            elif ' -' in sign:
                mNew, nNew = m, n - 1
            elif '++' in sign:
                mNew, nNew = m + 1, n + 1
            elif '--' in sign:
                mNew, nNew = m - 1, n - 1
            elif '-+' in sign:
                mNew, nNew = m - 1, n + 1
            else:
                mNew, nNew = m + 1, n - 1
            if mNew >= 0 and nNew >= 0:
                possibleMoves.append((mNew, nNew))
    elif 'q' in p:  # queen
        for sign in ['+ ', '- ', ' +', ' -', '++', '--', '-+', '+-']:
            for i in range(1, 8):
                if '+ ' in sign:
                    mNew, nNew = m + i, n
                elif '- ' in sign:
                    mNew, nNew = m - i, n
                elif ' +' in sign:
                    mNew, nNew = m, n + i
                elif ' -' in sign:
                    mNew, nNew = m, n - i
                elif '++' in sign:
                    mNew, nNew = m + i, n + i
                elif '--' in sign:
                    mNew, nNew = m - i, n - i
                elif '-+' in sign:
                    mNew, nNew = m - i, n + i
                else:
                    mNew, nNew = m + i, n - i
                if (mNew >= 0) and (mNew <= 7) and (nNew >= 0) and (nNew <= 7):
                    possibleMoves.append((mNew, nNew))
    elif 'b' in p: # bishop
        for sign in ['++', '+-', '-+', '--']:
            for i in range(1, 8):
                if '++' in sign:
                    mNew, nNew = m + i, n + i
                elif '+-' in sign:
                    mNew, nNew = m + i, n - i
                elif '-+' in sign:
                    mNew, nNew = m - i, n + i
                else:
                    mNew, nNew = m - i, n - i
                if (mNew >= 0) and (mNew <= 7) and (nNew >= 0) and (nNew <= 7):
                    possibleMoves.append((mNew, nNew))
    elif 'n' in p:
        for sign in ["1L2U", "1R2U", "2L1U", "2R1U", "2L1D", "2R1D", "1L2D", "1R2D"]:
                if "1L2U" in sign:
                    mNew, nNew = m - 1, n + 2
                elif "1R2U" in sign:
                    mNew, nNew = m + 1, n + 2
                elif "2L1U" in sign:
                    mNew, nNew = m - 2, n + 1
                elif "2R1U" in sign:
                    mNew, nNew = m + 2, n + 1
                elif "2L1D" in sign:
                    mNew, nNew = m - 2, n - 1
                elif "2R1D" in sign:
                    mNew, nNew = m + 2, n - 1
                elif "1L2D" in sign:
                    mNew, nNew = m - 1, n - 2
                else:
                    mNew, nNew = m + 1, n - 2
                if (mNew >= 0) and (mNew <= 7) and (nNew >= 0) and (nNew <= 7):
                    possibleMoves.append((mNew, nNew))
    elif 'r' in p:
        for sign in ["L", "R", "U", "D"]:
            for i in range(1, 8):
                if "L" in sign:
                    mNew, nNew = m - i, n
                elif "R" in sign:
                    mNew, nNew = m + i, n
                elif "U" in sign:
                    mNew, nNew = m, n + i
                else:
                    mNew, nNew = m, n - i
                if (mNew >= 0) and (mNew <= 7) and (nNew >= 0) and (nNew <= 7):
                    possibleMoves.append((mNew, nNew))
    else:
        pass
    return set(possibleMoves)





pos = 'c4'
m, n = alphaToIndex[pos[0]], int(pos[1]) - 1
piece = 'k'

print(m,n)
print("****")
for each in possibleMoves(piece, m, n):
    print(each)





print('done')
