from celery import Celery
import classifiers

REDIS = 'redis://localhost:6379/0'
celery_app = Celery('celery_app', broker=REDIS, backend=REDIS)
knn = None


@celery_app.task
def guess(data):
    label = classifiers.knn_classifier(knn, data)
    return label


if __name__ == '__main__':
    knn = classifiers.initialize()

    celery_app.conf.update(
        CELERY_ACCEPT_CONTENT=['pickle', 'json'],
        CELERYD_POOL='solo'
    )

    celery_app.worker_main()
