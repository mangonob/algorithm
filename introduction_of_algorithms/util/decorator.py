import time

def time_profile(configures=None):
    """
    configures is a profile to control some behavior such as output.

    example configures: {
        'show_entrance': True,
    }
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            show_entrance = configures and "show_entrance" in configures and configures["show_entrance"]

            if show_entrance:
                print("Entrance function %s. {" % func.__name__)

            begin_time_profile('Run %s' % (func.__wrapper_name__ if hasattr(func, "__wrapper_name__") else func.__name__))
            result = func(*args, **kwargs)
            commit_time_profile()

            if show_entrance:
                print("} Exit function %s." % func.__name__)

            return result
        wrapper.__wrapper_name__ = "@%s" % (func.__wrapper_name__ if hasattr(func, "__wrapper_name__") else func.__name__)
        return wrapper
    return decorator


class SessionError(Exception):
    pass

class _TimeProfileSession(object):
    shared_session_pool = list()

    def __init__(self, description):
        self.description = description
        self.start_time = time.time()

    @property
    def session_pool(self):
        return _TimeProfileSession.shared_session_pool

    def begin(self):
        if self in self.session_pool:
            raise SessionError()
        self.session_pool.append(self)

    def commit(self):
        seconds = time.time() - self.start_time
        duration = seconds
        h = duration / (60 * 60)
        duration %= (60 * 60)
        m = duration / 60
        duration %= 60
        s = duration
        duration %= 1
        duration *= 1000
        mm = duration
        duration %= 1
        duration *= 1000
        um = duration
        duration %= 1
        duration *= 1000
        nm = duration

        if h // 1 > 0:
            des = "%.2fh" % h
        elif m // 1 > 0:
            des = "%.2fm" % m
        elif s // 1 > 0:
            des = "%.2fs" % s
        elif mm // 1 > 0:
            des = "%.2fms" % mm
        elif um // 1 > 0:
            des = "%.2fum" % um
        elif nm // 1 > 0:
            des = "%.2fnm" % nm
        else:
            des = "no time"

        print(self.description, "used", des)
        pass

_auto_increase_session_id = 1

def begin_time_profile(session_description = None):
    _TimeProfileSession(description=session_description or "session_%s" % _auto_increase_session_id).begin()
    pass

def commit_time_profile():
    session = _TimeProfileSession.shared_session_pool.pop()
    session.commit()
