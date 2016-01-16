import struct
import numpy as np
import scipy.spatial.distance as dist
from sklearn.preprocessing import Binarizer


def validate_data(data, header, length):
    return struct.unpack('>II', data.read(8)) == (header, length)


def load_mnist_data():
    try:
        label_data = open('train-labels-idx1-ubyte', 'rb')
        image_data = open('train-images-idx3-ubyte', 'rb')
    except IOError:
        print "Failed to open MNIST data!"
        return False

    if not validate_data(label_data, 2049, 60000) or not validate_data(image_data, 2051, 60000):
        print "MNIST data is invalid!"
        return False

    labels = np.fromfile(label_data, dtype=np.int8)

    rows, cols = struct.unpack('>II', image_data.read(8))
    images = np.fromfile(image_data, dtype=np.uint8).reshape(len(labels), rows * cols)

    return images, labels


def knn_classifier(images, instance):
    dists = dist.cdist(images, [instance])
    return dists.argmin(0)


def initialize():
    images, labels = load_mnist_data()

    binarizer = Binarizer().fit(images)
    images_binarized = binarizer.transform(images)

    print labels[0:5]

    print labels[knn_classifier(images_binarized, images[0])]
    print labels[knn_classifier(images_binarized, images[1])]

if __name__ == '__main__':
    initialize()