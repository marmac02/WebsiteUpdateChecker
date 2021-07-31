#Windows

import urllib.request
import time
import winsound


def findFirstPositions(textToFind):
    firstPositions = []
    for i in range(0, len(webText) - len(textToFind) - 1):
        if webText[i : i + len(textToFind)] == textToFind:
            firstPositions.append(i)
    return firstPositions


def findCurrInserateNumber(pos):
    i = pos
    while i > 0 and webText[i] != ">":
        i = i - 1
    return webText[i + 1 : pos - 1]


print("Program is running...")
prevNum = 0
numOfIter = 0
while True:
    urllib.request.urlretrieve("http://www.woko.ch/de/nachmieter-gesucht", "test.txt")
    file = open("test.txt")
    webText = file.read().replace("\n", " ")
    firstPositions = findFirstPositions("Inserate")
    ZurichInserate = firstPositions[1]
    currNum = int(findCurrInserateNumber(ZurichInserate))
    if numOfIter > 0 and prevNum < currNum:
        print(f"There is a change in the number of offers! (from {prevNum} to {currNum})")
        winsound.PlaySound('notification.wav', winsound.SND_FILENAME)
    prevNum = currNum
    numOfIter = numOfIter + 1
    time.sleep(10)




