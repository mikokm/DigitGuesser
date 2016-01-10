from celery import Celery

REDIS = 'redis://localhost:6379/0'
celery_app = Celery('celery_app', broker=REDIS, backend=REDIS)


@celery_app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    celery_app.conf.update(
        CELERY_ACCEPT_CONTENT=['pickle', 'json'],
        CELERYD_POOL='solo'
    )

    celery_app.worker_main()
