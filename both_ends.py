def both_ends(s):
    if len(s) >= 2:
        begin = s[:2]
        end = s[-2::]
        return begin + end
    else:
        return ''


print(both_ends('Fala galera'))
