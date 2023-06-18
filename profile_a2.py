import sort_s2
import random
from time import perf_counter

__author__ = 'Rama Alkhouli'


def profile_bubble_sort(lst):
    time_start = perf_counter()
    sort_s2.bubble_sort(lst, len(lst))
    time_end = perf_counter()
    elapsed_time = time_end - time_start
    #print("Elapsed time in seconds: ", elapsed_time)
    return elapsed_time

def profile_selection_sort(lst):
    time_start = perf_counter()
    sort_s2.selection_sort(lst, len(lst))
    time_end = perf_counter()
    elapsed_time = time_end - time_start
    #print("Elapsed time in seconds: ", elapsed_time)
    return elapsed_time

def profile_merge_sort(lst):
    time_start = perf_counter()
    sort_s2.merge_sort(lst, len(lst))
    time_end = perf_counter()
    elapsed_time = time_end - time_start
    #print("Elapsed time in seconds: ", elapsed_time)
    return elapsed_time

def profile_insertion_sort(lst):
    time_start = perf_counter()
    sort_s2.insertion_sort(lst, len(lst))
    time_end = perf_counter()
    elapsed_time = time_end - time_start
    #print("Elapsed time in seconds: ", elapsed_time)
    return elapsed_time

def profile_heapsort(lst):
    time_start = perf_counter()
    sort_s2.heapsort(lst, len(lst))
    time_end = perf_counter()
    elapsed_time = time_end - time_start
    #print("Elapsed time in seconds: ", elapsed_time)
    return elapsed_time

def calculate_sample_average(data):
     return sum(data) / len(data)

def calculate_standard_deviation(data):
    n = len(data)
    average = calculate_sample_average(data)
    squared_diff_sum = sum((x - average) ** 2 for x in data)
    variance = squared_diff_sum / (n - 1)
    standard_deviation = variance ** 0.5
    return standard_deviation


if __name__ == '__main__':
    sizes = [1000, 2000, 5000, 25000]
    iterations = 5
    
    data = []

    # Generate random lists
    with open('a2.txt', 'w') as f:
        for size in sizes:
            for _ in range(iterations):
                randlst = [random.randint(0, 5000) for _ in range(size)]
                data.append(randlst)
                f.write(','.join(map(str, randlst)) + '\n')

    for size in sizes:
        bubble = []
        selection = []
        merge = []
        insertion = []
        heapsort = []

        for i in range(iterations):
            randlst = data[i]  # Retrieve the list from the data list
           
            # Profile bubble sort
            bubble_time = profile_bubble_sort(randlst)
            bubble.append(bubble_time)

            # Profile selection sort
            selection_time = profile_selection_sort(randlst)
            selection.append(selection_time)

            # Profile merge sort
            merge_time = profile_merge_sort(randlst)
            merge.append(merge_time)

            # Profile insertion sort
            insertion_time = profile_insertion_sort(randlst)
            insertion.append(insertion_time)

            # Profile heapsort
            heapsort_time = profile_heapsort(randlst)
            heapsort.append(heapsort_time)
        
        # Calculate sample averages and standard deviations
        bubble_avg = calculate_sample_average(bubble)
        selection_avg = calculate_sample_average(selection)
        merge_avg = calculate_sample_average(merge)
        insertion_avg = calculate_sample_average(insertion)
        heapsort_avg = calculate_sample_average(heapsort)

        bubble_std = calculate_standard_deviation(bubble)
        selection_std = calculate_standard_deviation(selection)
        merge_std = calculate_standard_deviation(merge)
        insertion_std = calculate_standard_deviation(insertion)
        heapsort_std = calculate_standard_deviation(heapsort)    
        
        # Write running times to text files
        with open('bubble_table.txt', 'a') as f:
            f.write(f"n\tlist ID\t     running time    \t      Sample Average  \t      Std Dev \n")
            for i, time in enumerate(bubble):
                list_id = f"list_{size:02d}_{i+1:02d}"
                f.write(f"{size}\t{list_id}\t{time}\t{bubble_avg}\t{bubble_std}\n")

        with open('selection_table.txt', 'a') as f:
            f.write(f"n\tlist ID\t     running time   \t      Sample Average  \t      Std Dev \n")
            for i, time in enumerate(selection):
                list_id = f"list_{size:02d}_{i+1:02d}"
                f.write(f"{size}\t{list_id}\t{time}\t{selection_avg}\t{selection_std}\n")
                

        with open('merge_table.txt', 'a') as f:
            f.write(f"n\tlist ID\t     running time   \t    Sample Average  \t       Std Dev \n")
            for i, time in enumerate(merge):
                list_id = f"list_{size:02d}_{i+1:02d}"
                f.write(f"{size}\t{list_id}\t{time}\t{merge_avg }\t{merge_std}\n")
                

        with open('insertion_table.txt', 'a') as f:
            f.write(f"n\tlist ID\t    running time    \t      Sample Average  \t      Std Dev \n")
            for i, time in enumerate(insertion):
                list_id = f"list_{size:02d}_{i+1:02d}"
                f.write(f"{size}\t{list_id}\t{time}\t{insertion_avg}\t{insertion_std}\n")
                

        with open('heapsort_table.txt', 'a') as f:
            f.write(f"n\tlist ID\t     running time   \t    Sample Average  \t      Std Dev \n")
            for i, time in enumerate(heapsort):
                list_id = f"list_{size:02d}_{i+1:02d}"
                f.write(f"{size}\t{list_id}\t{time}\t{heapsort_avg}\t{heapsort_std}\n")
                


