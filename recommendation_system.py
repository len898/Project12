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

    #print(user_rating_dict)

    for i in user_rating_dict:
        current_arr = create_array(len(book_list))
        for j in range(0, len(list_from_file)):
            if i == list_from_file[j]:
                index = book_list.index(list_from_file[j+1])
                current_arr[index] = list_from_file[j+2]
        user_rating_dict[i] = current_arr
    
    print(user_rating_dict)
    
    return book_list,user_rating_dict

def averages(books:set, ratings:dict):
    list_from_file = []
    book_rating_dict = {}
    
    for i in books:
        book_rating_dict[i] = []

    with open('test.txt', 'r') as f:
        for line in f:
            list_from_file.append(line.rstrip())
        for i in book_rating_dict:
            ratings_for_current_book = []
            for j in range(0, len(list_from_file)):
                if i == list_from_file[j]:
                    ratings_for_current_book.append(int(list_from_file[j+1]))
            book_rating_dict[i] = ratings_for_current_book
    
    #print(book_rating_dict)
    ratings_list = []

    for i in book_rating_dict.keys():
        pos_count = 0
        current_tuple = []
        for j in book_rating_dict[i]:
            if int(j) > 0:
                pos_count += 1
        current_tuple.append(sum((book_rating_dict[i]))/pos_count)
        current_tuple.append(i)
        current_tuple = tuple(current_tuple)
        ratings_list.append(current_tuple)
    ratings_list.sort(reverse=True)
    return ratings_list

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
#averages(books, ratings)
#similarities('kalid',ratings)