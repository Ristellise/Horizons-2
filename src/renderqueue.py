renderqueue = []


def addrenderqueue(spritegroup, image, x, y):
    renderqueue.append([spritegroup, image, x, y])
if __name__ == "__main__":
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
