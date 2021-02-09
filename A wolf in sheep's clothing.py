def warn_the_sheep(queue):
    return 'Oi! Sheep number {0}! You are about to be eaten by a wolf!'.format(queue[::-1].index("wolf")) if queue[::-1].index("wolf") else 'Pls go away and stop eating my sheep' 

print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf']))