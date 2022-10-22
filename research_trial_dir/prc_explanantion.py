precision, recall, prc_threshold = [0.1,0.2,0.4,0.9, 0.99, 0.22, 0.66], [0.1,0.2,0.4,0.9, 0.99, 0.22, 0.66], [0.1,0.2,0.4,0.9, 0.99, 0.22, 0.66]

nth_point = 3 
print(list(zip(precision, recall, prc_threshold)))
print(list(zip(precision, recall, prc_threshold))[::2])
print(list(zip(precision, recall, prc_threshold))[::nth_point])

# so here we can see that out of many values we are taking values 
# at every 2 interval.
# In our code we have taken every 1000th value