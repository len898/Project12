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
                current_arr[index] = int(list_from_file[j+2])
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
    def dot_product(list1, list2):
        total = 0
        for i in range(0,len(list1)):
            total += (list1[i] * list2[i])
        return total
    #List with reviews from the user we're comparing the others to
    user_to_be_checked = ratings.pop(user)

    list_of_similar_scores = []

    for user in ratings:
        dot_p = dot_product(user_to_be_checked, ratings[user])
        list_of_similar_scores.append(tuple([dot_p, user]))

    list_of_similar_scores.sort(reverse=True)
    print(list_of_similar_scores)
    return list_of_similar_scores        

def recommended(sims:list,books:list,ratings:dict) -> list:
    books_to_rec_ratings = []
    for i in range(0,len(books)):
        books_to_rec_ratings.append(0)
    def create_averages(list1:list, list2:list, list3:list):
        averages_list = []
        non_zero_count = 0
        for i in range(0,len(list1)):
            if(list1[i] != 0):
                non_zero_count += 1
            if(list2[i] != 0):
                non_zero_count += 1
            if(list3[i] != 0):
                non_zero_count += 1
            if(non_zero_count != 0):
                averages_list.append((list1[i] + list2[i] + list3[i]) / non_zero_count)
            else:
                averages_list.append(0)
            non_zero_count = 0
        return averages_list
    name1 = sims[0][1]
    name2 = sims[1][1]
    name3 = sims[2][1]
    list1 = ratings.pop(name1)
    list2 = ratings.pop(name2)
    list3 = ratings.pop(name3)
    average_list_vals = create_averages(list1, list2, list3)
    print(average_list_vals)
    average_list_vals_and_names = []
    for i in range(0, len(average_list_vals)):
        average_list_vals_and_names.append(tuple([average_list_vals[i], books[i]]))
    average_list_vals_and_names.sort(reverse=True)
    print(average_list_vals_and_names)



books, ratings = construct_ratings()
averages(books, ratings)
sims = similarities('Kalid',ratings)
recommended(sims,books,ratings)