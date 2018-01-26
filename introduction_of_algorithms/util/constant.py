import math


def shared_nil():
    class Nil(object):
        """ Provide a sentinel object. """

        def __call__(self, *args, **kwargs):
            return self

        def __getattr__(self, item):
            return self

        def __bool__(self):
            return False

    if not hasattr(Nil, "shared"):
        Nil.shared = Nil()

    return Nil.shared

NIL = shared_nil()

PHI = (math.sqrt(5) - 1) / 2


