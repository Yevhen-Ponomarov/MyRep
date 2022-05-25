from time import process_time_ns
from random import randint


# printing out key spaces by the rule that:
# number of key spaces = 2**n, where n is the number of used bits
def powers(__power, __two):
    while __power <= 4096:
        print("the ", __power, "-bit keyspace consists of ", two**__power, " possible options", sep='')
        __power *= 2


# getting random numbers for each keyspace
# via using "random"-module
def rand(__i, __power):
    while __i <= 9:
        rand_val[__i] = randint(0, two ** __power)
        __i += 1
        __power *= 2


# firstly, we count how long it takes the processor to go through 750 000 options by bruthforse method
# then using this info, we can easily calculate the exceeded time
# even though the calculations are approximate, this solution is the best, as the script does not run for years
def time_mod(_i, _j, _time_):
    while _j <= 512:
        # to round the large values that can be larger than maximum float value
        # we just turn it into a string and cut off its last 4 digits
        time_exceeded = _time_ * rand_val[_i]
        if time_exceeded > 10 ** 307:
            time_exceeded = str(time_exceeded)
            print("time exceeded for finding the proper key value in ", _j, "-bit keyspace is ",
                  time_exceeded[:len(time_exceeded) - 4], " ms.", sep='')
        else:
            time_exceeded = int(time_exceeded / 10000)
            print("time exceeded for finding the proper key value in ", _j, "-bit keyspace is ", time_exceeded, " ms.",
                  sep='')
        _j *= 2
        _i += 1
    while _j <= 4096:
        # to round the large values that can be larger than maximum float value
        # we just turn it into a string and cut off its last 4 digits
        time_exceeded = _time_ * rand_val[_i]
        if time_exceeded > 10 ** 307:
            time_exceeded = str(time_exceeded)
            print("time exceeded for finding the proper key value in ", _j, "-bit keyspace is ",
                  time_exceeded[:len(time_exceeded) - 4], " ms.", sep='')
        else:
            time_exceeded = int(time_exceeded / 10000)
            print("time exceeded for finding the proper key value in ", _j, "-bit keyspace is ", time_exceeded, " ms.",
                  sep='')
        _j *= 2
        _i += 1


# finding key-spaces
power = 8
two = 2
i = 0
powers(power, two)
print("\n")

# initialization of 10 random values
power = 8
rand_val = [0] * 10
rand(i, power)

# counting the time needed
i = 0
j = 8
start = process_time_ns()
k = 0
while k <= 750000:
    k += 1
end = process_time_ns()
time_ = int((end-start) / 100 / 750000)  # time needed to check a k-option initialized in hebdo-seconds
time_mod(i, j, time_)
