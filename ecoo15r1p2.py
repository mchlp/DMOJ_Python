for _ in range(5):
    mlen = int(input())
    words = input().split()
    clen = 0
    for word in words:
        if (word != " "):
            if (len(word) + clen > mlen):
                print()
                clen = 0
            print(word, end=" ")
            clen += len(word)+1
    print("\n=====")
