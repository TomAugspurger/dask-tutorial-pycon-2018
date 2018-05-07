with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
    results = pool.map(fib, [34, 34, 34, 34])
    %time _ = list(results)