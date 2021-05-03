"""Restaurant rating lister."""


# put your code here
# read a file
open_file = open("scores.txt")
# read lines of file
def ordered_ratings(open_file):
    ratings = {}
    ratings_list = []
    # ratings_list = ratings_list.sort()

# break each line into parts, whitestrip, maybe split by colon?
    for line in open_file:
        line = line.rstrip()
        words = line.split(":")
        ratings[words[0]] = words[1]
        ratings_list.append(f"{words[0]} is rated at {words[1]}.")
    
    #ratings_list = ratings_list.sort()
    sorted_ratings_list = sorted(ratings.items())

    for restaurant in sorted_ratings_list:
        print(f"{restaurant[0]} is rated at {restaurant[1]}.")
    #for rate in ratings_list:
    #    print(rate)

    #print(sorted(ratings))
    # print(sorted_ratings_list)
    #print(type(ratings_list))
    #print(ratings_list)
    #print(ratings_list.sort())

    #return ratings_list.sort()
    #return (sorted(ratings.items()))



    
# create dictionary (blank)
# use dict. get() to add key value pairs to dictionary, restaurant name is key
# put dictionary keys in alpha order

test = ordered_ratings(open_file)
#print(test)