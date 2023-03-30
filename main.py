from typing import List


def even_list(int_list: List[int]) -> List[int]:
    even_number = []
    for num in int_list:
        if num % 2 == 0:
            even_number.append(num)
    return even_number


# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    pass


# Main function
def main():
    # Example list
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    #output = sum_of_squares_of_even(even_int_list)
    print(even_int_list)


# Boilerplate code
if __name__ == "__main__":
    main()