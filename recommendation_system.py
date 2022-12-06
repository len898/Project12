def construct_ratings():
    list_from_file = []
    book_list = []
    name_set = set([])
    ratings_list = []

    #Open the file and read all the content into a list
    with open('ratings-small.txt', 'r') as f:
        for line in f:
            list_from_file.append(line.rstrip())

    #Take only the names of books which occurs every 3 and parse them into a list
    for i in range(1,len(list_from_file), 3):
        book_list.append(list_from_file[i])

    #Takes the names from the list which appear every 3 and parses them into a set
    for i in range(0,len(list_from_file), 3):
        name_set.add(list_from_file[i])


    print(name_set)
    user_rating_dict = {}
    for i in name_set:
        user_rating_dict[i] = []

    #Iterate through the dictionary with only names and find the corresponding ratings for each name
    for i in user_rating_dict:
        ratings_list = []
        for j in range(2,len(list_from_file),3):
            if list_from_file[j-2] == i:
                ratings_list.append(list_from_file[j])
        user_rating_dict[i] = ratings_list
    
    print(user_rating_dict)


construct_ratings()