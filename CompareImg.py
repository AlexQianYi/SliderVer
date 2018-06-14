import cv2

def aHash(img):

    img=cv2.resize(img, (20, 20), interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    s = 0
    hash_str = ''

    for i in range(20):
        for j in range(20):
            s += gray[i,j]

    avg = s/400

    for i in range(20):
        for j in range(20):
            if gray[i, j] > avg:
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str

def dHash(img):

    img = cv2.resize(img, (21,20), interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''

    for i in range(20):
        for j in range(20):
            if gray[i,j] > gray[i,j+1]:
                hash_str += '1'
            else:
                hash_str += '0'

    return hash_str


def cmpHash(hash1, hash2):
    n = 0

    if len(hash1) != len(hash2):
        return -1

    for i in range(len(hash1)):

        if hash1[i] != hash2[i]:
            n += 1

    return n

if __name__ == '__main__':

    img1 = cv2.imread('./1.png')
    img2 = cv2.imread('./2.jpg')

    hash1 = aHash(img1)
    hash2 = aHash(img2)

    n = cmpHash(hash1, hash2)
    print(n)

    hash1 = dHash(img1)
    hash2 = dHash(img2)

    n = cmpHash(hash1, hash2)
    print(n)