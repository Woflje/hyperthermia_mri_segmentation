from datetime import datetime


def pad_time(td):
    if len(td) < 2:
        return f'0{td}'
    else:
        return td


def tlog(log_n, message, newline=False):
    ct = datetime.now()
    day, month, year, hour, minute, second = str(ct.day), str(ct.month), str(ct.year), str(ct.hour), str(ct.minute), str(ct.second)
    nl = ''
    if newline:
        nl = '\n'
    print(f'{nl}{pad_time(day)}-{pad_time(month)}-{year} {pad_time(hour)}:{pad_time(minute)}:{pad_time(second)} | [{log_n}] {message}')