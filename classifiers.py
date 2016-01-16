import gzip
import struct
import numpy as np
import scipy.spatial.distance as dist
from sklearn.preprocessing import Binarizer


def validate_data(data, header, length):
    return struct.unpack('>II', data[0:8]) == (header, length)


def load_mnist_data():
    try:
        label_data = gzip.open('train-labels-idx1-ubyte.gz', 'rb').read()
        image_data = gzip.open('train-images-idx3-ubyte.gz', 'rb').read()
    except IOError:
        print "Failed to open MNIST data!"
        return False

    if not validate_data(label_data, 2049, 60000) or not validate_data(image_data, 2051, 60000):
        print "MNIST data is invalid!"
        return False

    labels = np.frombuffer(label_data[8:], dtype=np.int8)

    rows, cols = struct.unpack('>II', image_data[8:16])
    images = np.frombuffer(image_data[16:], dtype=np.uint8).reshape(len(labels), rows * cols)

    return images, labels


def knn_classifier(images, instance):
    data = np.array(instance, np.int8).T
    dists = dist.cdist(images, [data.flatten()])
    return dists.argmin(0)


def initialize():
    images, labels = load_mnist_data()

    binarizer = Binarizer().fit(images)
    images_binarized = binarizer.transform(images)

    return images_binarized, labels


if __name__ == '__main__':
    initialize()
