
'''
작성자 : 장영은
날짜 : 210719

'''

from util import cut_by_min, file_to_list

if __name__ == '__main__':

    list_temp = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 2, 3, 4, 5, 6, 7, 8],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    ]

    #print(cut_by_min(list_temp))

    example_path = './example/*'

    file_list = file_to_list(example_path) 

    print(cut_by_min(file_list))

    