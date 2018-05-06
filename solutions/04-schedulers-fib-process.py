process_pool = concurrent.futures.ProcessPoolExecutor(max_workers=4)
results = process_pool.map(fib, [34, 34, 34, 34])
%time list(results)