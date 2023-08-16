class FileReader:
    def __init__(self, input):
        self.filename = input


    def read_file(self):
        file = open(self.filename)
        data = []
        for line in file:
            line = line.strip()
            line_as_list = line.split(';')
            element = {
                'name': line_as_list[0],
                'grade': float(line_as_list[1])
                }
            data.append(element)
        file.close()
        return data
    