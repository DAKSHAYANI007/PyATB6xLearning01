for i in range(0, 10, 1):
    if i == 6:
        print (i)
    else:
        print(" No O/P")

       # Always draw the ERT
    # |i | Condition |  O/P |
    # |0 |  0 =/= 6 -> False | No O/P
    # |1 |  1 ==6 -> False |   No  O/P
    # |2 |  2 ==6 -> False |   No  O/P
    # |3 |  3 ==6 -> False |  No  O/P
    # |4 |  4 ==6 -> False |  No  O/P
    # |5 |  5 ==6 -> False |  No  O/P
    # |6 |  6 ==6 -> True |  6
    # |7 |  7==6 -> False |  No  O/P
    # |8|   8 ==6 -> False |  No  O/P
    # |9 |  9 ==6 -> False |  No  O/P