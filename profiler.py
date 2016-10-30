import datetime

timers = list()

def timedelta_total_seconds(timedelta):
    return (
        timedelta.microseconds + 0.0 +
        (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6

def print_time(msg):
    end = datetime.datetime.now()
    start = timers.pop()
    delta = end - start
    print(msg + ": " + str(delta.total_seconds() * 1000) + "ms")


def start_timer():
    start = datetime.datetime.now()
    timers.append(start)

def print_request_status(resp):
    out = "{resp.status_code}: {resp.reason}".format(resp)
    print(out)



def profdec(f):

    def measure_time(*args, **kwargs):
        start_timer()
        f(*args, **kwargs)
        print_time(f.__name__)

    return measure_time