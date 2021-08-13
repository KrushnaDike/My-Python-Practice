import time
from functools import lru_cache
cache = int(input("Enter the size of cache :"))

@lru_cache(maxsize=cache)
def some_work(n):
    # Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work...!")
    some_work(3)
    print("Done....Calling again")
    some_work(3)
    print("Called again")