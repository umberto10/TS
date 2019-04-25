from time import sleep
import random


def simulation():
    arr = [{"type": 0, "dir": 0}] * 10
    arr[0] = {"type": 1, "dir": 1}
    arr[9] = {"type": 2, "dir": -1}
    cntR = 0
    cntL = 0
    colL = 0
    colR = 0
    sleepL = 0
    sleepR = 0
    while True:

        if sleepL == 0:
            if arr[0]["type"] == 1 or arr[0]["type"] == 0:
                if cntL < 20:
                    cntL += 1
                    arr[0] = {"type": 1, "dir": 1}
                else:
                    arr[0] = {"type": 0, "dir": 1}
                    cntL = 0
            elif arr[0]["type"] == 3:
                colL += 1
                sleepL = 10 * random.randint(0, colL)
                arr[0] = {"type": 0, "dir": 1}
                cntL = 0

        else:
            sleepL -= 1

        if sleepR == 0:
            if arr[9]["type"] == 2 or arr[9]["type"] == 0:
                if cntR < 20:
                    cntR += 1
                    arr[9] = {"type": 2, "dir": -1}
                else:
                    arr[9] = {"type": 0, "dir": -1}
                    cntR = 0
            elif arr[0]["type"] == 3:
                colR += 1
                sleepR = 10 * random.randint(0, colR)
                arr[9] = {"type": 0, "dir": -1}
                cntR = 0
        else:
            sleepR -= 1

        for x in arr:
            if x.get("type") == 0:
                print(end='.')
            elif x.get("type") == 3:
                print(end='#')
            elif x.get("type") == 2:
                print(end='2')
            else:
                print(end='1')
        print(end='\r')

        next = [{"type": 0, "dir": 0}] * 10

        for x in range(arr.__len__()):
            curr = arr[x]

            if curr["type"] != 0:
                if (curr["dir"] == -1 and x > 0) or (curr["dir"] == 1 and x < arr.__len__() - 1):
                    if curr["dir"] != 3 and next[x + curr["dir"]]["type"] == 3:
                        continue

                    next[x + curr["dir"]] = curr

                    if not arr[x + curr["dir"]]["type"] == 0 and not arr[x + curr["dir"]]["type"] == arr[x]["type"]:
                        next[x + curr["dir"]]["type"] = 3

        if arr[0]["type"] == 3 and arr[0]["dir"] == -1 and arr[1]["type"] == 3:
            next[0] = arr[0]

        if arr[9]["type"] == 3 and arr[9]["dir"] == -1 and arr[8]["type"] == 3:
            next[9] = arr[9]

        for x in range(arr.__len__()):
            arr[x] = next[x]

        for x in range(arr.__len__()-2):
            if arr[x+1]["type"] == 0 and arr[x]["type"] == 3 and arr[x+2]["type"] == 3 and arr[x]["dir"] == arr[x+2]["dir"]:
                arr[x +1] = arr[x]

        sleep(.5)


simulation()

print('')
