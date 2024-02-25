from inspect import signature


def assert_param_counts(callback, count: int):
    # inspect callback object to ensure it takes specified number of parameters
    sig = signature(callback)
    source_count = len(sig.parameters)
    assert source_count == count, "Callback signature must handle {} arguments but has {}".format(count, source_count)
