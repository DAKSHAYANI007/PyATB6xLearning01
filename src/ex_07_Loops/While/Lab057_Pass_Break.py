for i in range(0,10,1):
    if i == 5 or i == 6:
        print(i)
    else:
        pass

    # Always draw the ERT
    # |i | Condition |  O/P |
    # |0 |  0 == 6 or 5  -> False | do nothing
    # |1|   1 == 6 or 5  -> False | do nothing
    # |2|   2  == 6 or 5  -> False | do nothing
    # |3 |  3== 6 or 5  -> False | do nothing
    # |4 |  4 == 6 or 5  -> False | do nothing
    # |5 |  5 == 6 or 5  -> True | 5
    # |6 |  6 == 6 or 5  -> True | 6
    # |7 |  7 == 6 or 5  -> False | do nothing
    # |8 |  8 == 6 or 5  -> False | do nothing
    #|9 |  9== 6 or 5  -> False | do nothing


