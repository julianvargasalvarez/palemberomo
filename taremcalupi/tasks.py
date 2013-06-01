from celery import task

@task()
def add(x, y):
    return x + y

def suma(x, y):
    return x + y
