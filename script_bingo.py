from pybingo.BingoCard import *

### MAIN ###
if __name__ == "__main__":
    print ("Welcome to my pybingo Card example script")

    data = [
            [22,13,17,11,0],
            [8,2,23,4,24],
            [21,9,14,16,7],
            [6,10,3,18,5],
            [1,12,20,15,19],
        ]


    print (f"{data=}")
    myBingoCard = BingoCard(data)

    print ("-------------")
    print ("Bingo Card")
    print (myBingoCard)

    print ("Pick 22")
    myBingoCard.updateCard(22)
    print ("-------------")
    print (myBingoCard)
