def construct_ratings():
    list_from_file = []
    book_list = set([])
    name_set = set([])
    ratings_list = []

    #Open the file and read all the content into a list
    with open('test.txt', 'r') as f:
        for line in f:
            list_from_file.append(line.rstrip())

    #Take only the names of books which occurs every 3 and parse them into a list
    for i in range(1,len(list_from_file), 3):
        book_list.add(list_from_file[i])

    #Takes the names from the list which appear every 3 and parses them into a set
    for i in range(0,len(list_from_file), 3):
        name_set.add(list_from_file[i])

    book_list = list(book_list)
    book_list.sort()
    
    #Get the dictionary for user and ratings set up by only adding the names as keys to start
    user_rating_dict = {}
    length_of_array = []

    for i in range(0,len(book_list)):
        length_of_array.append(0)

    for i in name_set:
        user_rating_dict[i] = length_of_array

    def create_array(length:int) -> list:
        array = []
        for i in range(0,length):
            array.append(0)
        return array

    for i in user_rating_dict:
        current_arr = create_array(len(book_list))
        for j in range(0, len(list_from_file)):
            if i == list_from_file[j]:
                index = book_list.index(list_from_file[j+1])
                current_arr[index] = list_from_file[j+2]
        user_rating_dict[i] = current_arr
        
    return book_list,user_rating_dict

def averages(books:list, ratings:dict):
    list_of_avgs = []
    for i in range(0, len(books)):
        running_tally = 0
        num_items = 0
        for user in ratings:
            running_tally += int(ratings[user][i])
            if ratings[user][i] != 0:
                num_items += 1
        list_of_avgs.append(tuple([running_tally/num_items, books[i]]))
    list_of_avgs.sort(reverse=True)
    return list_of_avgs

def similarities(user:str, ratings:dict):
    user = user.capitalize()
    user1 = ratings.pop(user)
    user_ratings = [int(j) for j in user1]
    similarity_list = []
    print(user_ratings)

    def dot_product(list1, list2):
        product = 0
        if len(list1) > len(list2):
            for i in range(0,len(list2)):
                temp = list1[i] * list2[i]
                product += temp
            return product
        else:
            for i in range(0,len(list1)):
                temp = list1[i] * list2[i]
                product += temp
            return product

    for i in ratings:
        list_to_multiply = [int(j) for j in ratings[i]]
        print(list_to_multiply)
        print(dot_product(list_to_multiply, user_ratings))  




books, ratings = construct_ratings()
averages(books, ratings)
#similarities('kalid',ratings)