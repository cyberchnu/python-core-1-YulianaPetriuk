def mean(number):
    sum = 0
    count = 0
    number_str = str(number)
    for i in (number_str):
        inti = int(i)
        sum = sum + inti
        count = count + 1
    average = sum / len(number_str)
    return average
