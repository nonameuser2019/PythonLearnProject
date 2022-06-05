def is_subset(list1, list2):
    '''
    Напишите функцию, которая возвращает True, если первый список является подмножеством второго списка,
    и False в противном случае.
    '''

    for item in list1:
        if item not in list2:
            return False
    return True