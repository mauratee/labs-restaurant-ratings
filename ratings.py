"""Restaurant rating lister."""


# put your code here
# read a file
open_file = open("scores.txt")
# read lines of file
def ordered_ratings(open_file):
    ratings = {}
# break each line into parts, whitestrip, maybe split by colon?
    for line in open_file:
        line = line.rstrip()
        words = line.split(":")
        ratings[words[0]] = words[1]
        rest_name, rating = ratings
        print(f"{rest_name} is rated at {rating}.")
    #print(sorted(ratings))
    return (sorted(ratings.items(print(f"{rest_name} is rated at {rating}."))))
    
# create dictionary (blank)
# use dict. get() to add key value pairs to dictionary, restaurant name is key
# put dictionary keys in alpha order

test = ordered_ratings(open_file)
print(test)