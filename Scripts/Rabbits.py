def rabbits(month):
    if month <= 1:
        return 1
    else:
        return rabbits(month-1) + rabbits(month-2)
        