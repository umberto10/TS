import binascii


def decode():
    f = open("/dev/stdin")

    while True:
        l = f.readline()

        if len(l) == 0:
            break

        tmp = l[8:-9]
        # print("tmp before", tmp)
        t = tmp.replace("111110", "11111")
        # print("tmp  after", t)

        crcO = t[-32:]
        # print("Message crc", crcO, len(crcO))

        data = t[:-32]
        # print("Message", data)

        nr = int(data, 2).to_bytes(4, byteorder="big")
        crc = bin(binascii.crc32(nr))[2:].zfill(32)

        if crc.rstrip().__eq__(crcO.rstrip()):
            print(data)
        else:
            print("err")
            print("crc", crc)
            print("crcO", crcO)
            print("data", data)


decode()
