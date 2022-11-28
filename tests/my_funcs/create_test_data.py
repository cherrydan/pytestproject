def create_test_data(test_data):
    with open('./testfile.txt', 'a') as FILE:
        FILE.writelines(test_data)
