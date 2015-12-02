from pyOCD.board import MbedBoard

with MbedBoard.chooseBoard() as board:
    target = board.target
    data = target.readBlockMemoryUnaligned8(0x3000, 32 * 1024)
    data = bytearray(data)
    f = open("dump.bin", "wb")
    f.write(data)
    f.close()
