def read_and_process_file(path):
    try:
        with open(path) as file:
            data = file.read()
            print(data)        
    except:
        print('Cannot open file. Check the file path')
