
def brute_pass():
    from tqdm import tqdm
    from datetime import datetime
    import itertools, string, time, sys, os

    endless = 1
    while endless > 0:

        current_date = datetime.today()
        print('Type a password (Ctrl + C to abort program)')
        pwd = sys.stdin.readline().rstrip()
        pwd_len = len(pwd)
        pwd_tuple = tuple(pwd)

        sample1  = string.ascii_lowercase
        sample2 = string.ascii_uppercase
        sample3 = string.digits
        sample4 = string.punctuation

        sample12 = sample1 + sample2
        sample13 = sample1 + sample3
        sample14 = sample1 + sample4
        sample23 = sample2 + sample3
        sample24 = sample2 + sample4
        sample34 = sample3 + sample4
            
        lower = any([char.islower() for char in pwd])
        upper = any([char.isupper() for char in pwd])
        digit = any([char.isdigit() for char in pwd])
        special = any([not char.isalnum() for char in pwd]) 

        sample = ''

        if lower == True:
            sample = sample1
        if upper == True:
            sample += sample2
        if digit == True:
            sample += sample3
        if special == True:        
            sample += sample4

        start = time.time()
        combinations_len = (len(sample)**len(pwd))
        for i in tqdm(itertools.product(sample, repeat= pwd_len), total= combinations_len):
            if i == pwd_tuple:
                pass
        end = time.time()

        path_tmp = os.path.dirname(sys.executable)
        path_file = 'results_log.txt'
        full_path = os.path.join(path_tmp, path_file)

        if os.path.exists(full_path) == True:
            with open(full_path, 'a') as bfile:
                bfile.write(f'\n\n{current_date}:\nThe password \'{pwd}\' has been found in {end - start} seconds --> {combinations_len:,} combinations analyzed.')
                bfile.close()
        else:
            with open(full_path, 'w') as bfile:
                bfile.write(f'{current_date}:\nThe password \'{pwd}\' has been found in {end - start} seconds --> {combinations_len:,} combinations analyzed.')
                bfile.close()

        print(f'The password \'{pwd}\' has been found in {end - start} seconds --> {combinations_len:,} combinations analyzed.')
        print(f'The operation has been saved in \'{full_path}\'.')
        
        time.sleep(1)

    else:
        sys.exit()

brute_pass()
