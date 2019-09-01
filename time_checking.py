def time_before_round(t):
    t = min(0, t)
    t = abs(t)
    days = t // (60 * 60 * 24)
    t %= 60 * 60 * 24
    hours = t // (60 * 60)
    t %= 60 * 60
    minutes = t // 60
    t %= 60
    seconds = t
    return days, hours, minutes, seconds


def need_post(t):
    now = time_before_round(t)
    if now[0] > 0:
        return (now[0], 0, 0, 0) == now
    times_need = [(1, 0, 0, 0), (0, 8, 0, 0), (0, 6, 0, 0), (0, 3, 0, 0), (0, 2, 0, 0), (0, 1, 0, 0), (0, 0, 30, 0),
                  (0, 0, 20, 0), (0, 0, 10, 0), (0, 0, 5, 0), (0, 0, 2, 0), (0, 0, 1, 0), (0, 0, 0, 30), (0, 0, 0, 10)]
    return t in times_need
