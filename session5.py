import time
import math


def print_f(args, kwargs):
    object = args
    sep1 = kwargs.get('sep')
    end1 = kwargs.get('end')
    print(*object,sep=sep1,end=end1)
    return

def temp_converter_f(args, kwargs):
    temperature, *args = args
    temp_given_in = (kwargs.get('temp_given_in')).lower()
    if temp_given_in == 'c' and temperature >= -273.15:
        temp_in_f = temperature * 9 / 5 + 32
        temp_in_k = temperature + 273.15
        print(f'For given temperature in {temperature:.3f} C is equivelent to  {temp_in_f:.3f} F or {temp_in_k:.3f} K ')
        temp1 = temp_in_f
        temp1_b = "F"
        temp2 = temp_in_k
        temp2_b = "K"
    elif temp_given_in == 'f' and temperature > -459.67:
        temp_in_c = (temperature - 32) / 1.8
        temp_in_k = (temperature - 32) / 1.8 + 273.15
        print(f'For given temperature in {temperature:.3f} F is equivelent to  {temp_in_c:.3f} C or {temp_in_k:.3f} K ')
        temp1 = temp_in_c
        temp1_b = "C"
        temp2 = temp_in_k
        temp2_b = "K"
    elif temp_given_in == 'k' and temperature >= 0:
        temp_in_c = temperature - 273.15
        temp_in_f = (temperature - 273.15) * 9 / 5 + 32
        print(f'For given temperature in {temperature:.3f} K is equivelent to  {temp_in_c:.3f} C or {temp_in_f:.3f} F ')
        temp1 = temp_in_c
        temp1_b = "C"
        temp2 = temp_in_f
        temp2_b = "F"
    else:
        lis = ['c', 'f', 'k']
        if temp_given_in not in lis:
            print("Check input temperature base")
            temp1 = temp1_b = temp2 = temp2_b = None
        elif temp_given_in == 'c' and temperature < -273.15:
            print("For Celius Temperature cannot be less than -273.15")
            temp1 = temp1_b = temp2 = temp2_b = None
        elif temp_given_in == 'f' and temperature > -459.67:
            print("For fahrenheit Temperature cannot be less than -459.67")
            temp1 = temp1_b = temp2 = temp2_b = None
        else:
            print("For Kelvin Temperature cannot be less than 0")
            temp1 = temp1_b = temp2 = temp2_b = None
    return temp1, temp1_b, temp2, temp2_b


def polygon_area_f(args, kwargs):
    side_length, *args = args
    n_sides = kwargs.get('sides')
    if n_sides >= 3 and n_sides <= 6 and isinstance(n_sides, int) and side_length >= 0:
        b = math.tan(math.pi / n_sides)
        polygon_area = (side_length ** 2) * n_sides / (4 * b)
        print(f'Area of {n_sides} sided Polygon is {polygon_area:.2f}')
    elif not isinstance(n_sides, int):
        print("Number of sides should be a integer between 3 to 6")
        polygon_area = None
    elif side_length < 0:
        print("Length of side cannot be zero")
        polygon_area = None
    else:
        print("Number of sides cannot be less than 3 or more than 6")
        polygon_area = None
    return polygon_area


def squared_power_list_f(args, kwargs):
    number, *args = args
    start_nu = kwargs.get('start')
    end_nu = kwargs.get('end')
    squared_power_list = []
    if start_nu >= 0 and start_nu <= end_nu:
        for i in range(start_nu, (end_nu + 1)):
            squared_power_list.append(number ** i)
        print(squared_power_list)
    else:
        if start_nu < 0:
            print("Start number cannot be less than 0")
        else:
            print("Start number cannot be less end Number")
    return squared_power_list


def speed_converter_f(args, kwargs):
    speed, *args = args
    dist = kwargs.get('dist')
    t = kwargs.get('time')
    table_dist = {"km": 1, 'm': 1000, "ft": 3280.84, "yrd": 1093.61, "mile": 0.621371}
    time_dist = {"ms": 1 / (3.6 * 10 ** 6), "s": 1 / 3600, "min": 1 / 60, "hr": 1, "day": 24}
    if speed >= 0 and dist in table_dist and t in time_dist:
        d_value = table_dist.get(dist)
        t_value = time_dist.get(t)
        speed_converted = speed * d_value * t_value
        print(f'Speed in {speed:.3e} in kmph is equal to {speed_converted:.3e} in {dist}/{t}')
    elif dist not in table_dist and t not in time_dist:
        speed_converted = None
        print('Provide time(ms,s,min,hr,day) and distnace(km,m,mile,yrd or ft) in proper units  ')
    elif dist not in table_dist:
        speed_converted = None
        print('Provide proper distance  units')
    elif t not in time_dist:
        speed_converted = None
        print('Provide proper  time  units ')
    else:
        speed_converted = None
        print('speed cannot be negative')
    return speed_converted


def time_it(fn, *args, repetitions=1, **kwargs):
    time_start = time.perf_counter()
    for i in range(repetitions):
        if fn == 'print':
            print_f(args, kwargs)
            output=None
        elif fn == 'squared_power_list':
            output = squared_power_list_f(args, kwargs)
        elif fn == 'polygon_area':
            output = polygon_area_f(args, kwargs)
        elif fn == 'temp_converter':
            output = temp_converter_f(args, kwargs)
        elif fn == 'speed_converter':
            output = speed_converter_f(args, kwargs)
        else:
            print('function not Supported')
            output = None
    time_end = time.perf_counter()
    delta = time_end - time_start
    avg_time = delta / repetitions
    print(f'avg time taken={avg_time:.10f}')
    return output, avg_time


