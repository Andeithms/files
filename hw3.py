data_files = []


def read_files(file_path, count):
    for i in range(1, count + 1):
        name = str(i) + '.txt'
        lines = 0
        for line in open(file_path + str(i) + '.txt'):
            lines += 1
        data_files.append({'name': name, 'lines': lines})


def creating(file_path):
    file_result = open(file_path + 'new_text.txt', 'w')
    for i in range(len(data_files)):
        min_lines = data_files[0]['lines']
        min_name = data_files[0]['name']
        min_index = 0

        for index, item in enumerate(data_files):
            if item['lines'] < min_lines:
                min_lines = item['lines']
                min_name = item['name']
                min_index = index
        data_files.pop(min_index)
        file_result.write(min_name + '\n')
        file_result.write(str(min_lines) + '\n')

        for line in open(file_path + min_name):
            file_result.write(line)
        else:
            file_result.write('\n')


read_files('files for hw/', 3)
creating('files for hw/')
