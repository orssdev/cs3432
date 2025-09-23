try:
    def sun_time(rise_hour, rise_min, set_hour, set_min):
        hour = set_hour - rise_hour
        min = set_min - rise_min
        if set_min < rise_min:
            hour -= 1
            min += 60
        return hour, min
    while True:
        month, day, year, sun_rise, sun_set = input().split()

        rise_hour, rise_min = sun_rise.split(':')
        set_hour, set_min = sun_set.split(':')

        hour, min = sun_time(int(rise_hour), int(rise_min), int(set_hour), int(set_min))

        print(f'{month} {day} {year} {hour} hours {min} minutes')
except:
    pass