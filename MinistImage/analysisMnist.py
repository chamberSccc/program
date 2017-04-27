# -*- coding: utf-8 -*-

#把mnist数据集解析出来
from PIL import Image
import struct


def read_image(filename):
    f = open(filename, 'rb')

    index = 0 #偏移量
    buf = f.read()

    f.close()

    magic, images, rows, columns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')

    for i in xrange(images):
        # for i in xrange(2000):
        image = Image.new('L', (columns, rows))

        for x in xrange(rows):
            for y in xrange(columns):
                image.putpixel((y, x), int(struct.unpack_from('>B', buf, index)[0]))
                index += struct.calcsize('>B')

        print 'save ' + str(i) + 'image'
        image.save('test/' + str(i) + '.png')


def read_label(filename, saveFilename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()

    f.close()

    magic, labels = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')

    labelArr = [0] * labels
    # labelArr = [0] * 2000


    for x in xrange(labels):
        # for x in xrange(2000):
        labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')

    save = open(saveFilename, 'w')

    save.write(','.join(map(lambda x: str(x), labelArr)))
    save.write('\n')

    save.close()
    print 'save labels success'


if __name__ == '__main__':
    read_image('t10k-images.idx3-ubyte')
    read_label('train-labels.idx1-ubyte', 'test/label.txt')
