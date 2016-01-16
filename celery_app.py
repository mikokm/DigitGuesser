from celery import Celery
import classifiers

REDIS = 'redis://localhost:6379/0'
celery_app = Celery('celery_app', broker=REDIS, backend=REDIS)
images, labels = [], []


@celery_app.task
def guess(data):
    idx = classifiers.knn_classifier(images, data)
    return labels[idx]


if __name__ == '__main__':
    images, labels = classifiers.initialize()

    celery_app.conf.update(
        CELERY_ACCEPT_CONTENT=['pickle', 'json'],
        CELERYD_POOL='solo'
    )

    celery_app.worker_main()
