import re
fileobj=open("day-4-input.txt")

lines=fileobj.read()
lines=re.split('-|,|\n', lines)
print(lines)


ascore = 0
bscore = 0

def chunker(iter, size):
    chunks = [];
    if size < 1:
        raise ValueError('Chunk size must be greater than 0.')
    for i in range(0, len(iter), size):
        chunks.append(iter[i:(i+size)])
    return chunks

chunklines = chunker(lines, 4)
print(chunklines)

for chonk in chunklines:
    chonk[0] = int(chonk[0])
    chonk[1] = int(chonk[1])
    chonk[2] = int(chonk[2])
    chonk[3] = int(chonk[3])
    print(chonk)
    a1, a2, b1, b2, = chonk[0], chonk[1], chonk[2], chonk[3]
    aset = {a1, a2}
    bset = {b1, b2}
    print(aset)
    print(bset)
    chonk_sort = sorted(chonk)
    if ((chonk_sort[0] in aset) and (chonk_sort[3] in aset) and (chonk_sort[1] in bset) and (chonk_sort[2] in bset)) or ((chonk_sort[0] in bset) and (chonk_sort[3] in bset) and (chonk_sort[1] in aset) and (chonk_sort[2] in aset)):
        ascore += 1
        print(ascore)
    if (chonk_sort[0] in aset and chonk_sort[1] in bset) or (chonk_sort[0] in bset and chonk_sort[1] in aset):
        bscore += 1
        print(bscore)


print("a:", ascore)
print("b:", bscore)



