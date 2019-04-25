import binascii


def jostle_bits(bits):
    jostled = ""
    cnt = 0
    no1s = 0

    while not cnt == len(bits):
        r = bits[cnt]
        if r == "1":
            no1s += 1
        else:
            no1s = 0

        if no1s == 5:
            jostled += r
            jostled += "0"
            no1s = 0
            cnt += 1

        else:
            jostled += r
            cnt += 1

    return jostled


def make_frame():
    f = open("file.txt", "r")
    frames = []

    while True:

        bits = f.read(24)

        if len(bits) == 0:
            break

        nr = int(bits, 2).to_bytes(4, byteorder="big")
        crc = bin(binascii.crc32(nr))[2:].zfill(32)

        bits += crc
        jostled = jostle_bits(bits)

        frames.append(jostled.rstrip())

    for f in frames:
        print("01111110" + f + "01111110")


make_frame()
