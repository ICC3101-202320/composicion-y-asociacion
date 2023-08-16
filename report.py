class Report:
    def __init__(self, filename):
        self._filename = filename

    # def write_file(self):
    #     file = open(self.filename, 'w')
    #     for element in self.data:
    #         line = f"{element['name']};{element['grade']}\n"
    #         file.write(line)
    #     file.close()

    def call(self, formatter):
        self._open_file()
        self._write_data(formatter)
        self._close_file()

    def _write_data(self, formatter):
        csv_line = formatter.next()
        while csv_line is not None:
            self._file.write(f"{csv_line}\n")
            csv_line = formatter.next()

    def _open_file(self):
        self._file = open(self._filename, 'w')

    def _close_file(self):
        self._file.close()
