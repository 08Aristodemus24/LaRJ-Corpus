import concurrent
import multiprocessing
from multiprocessing import Process
import time


def sample(seconds):
    print(f'will sleep in {seconds} seconds')
    time.sleep(seconds)
    # return f'slept in {seconds}'
    


if __name__ == "__main__":
    processes = []
    for second in [5, 4, 3, 2, 1, 3, 7, 8]:
        p = Process(target=sample, args=(second, ))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()