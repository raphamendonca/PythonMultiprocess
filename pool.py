from multiprocessing import Pool

def doubler(number):
    return number *2

if __name__ =='__main__':
    #number = [5,10,20]
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    #print(pool.map(doubler, number))
    print(result.get(timeout=1))

    