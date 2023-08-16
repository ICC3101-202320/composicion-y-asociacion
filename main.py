from file_reader import FileReader
from csv_formatter import CsvFormatter
from txt_formatter import TxtFormatter
from report import Report

reader = FileReader('notas.csv')
data = reader.read_file()
formatter = CsvFormatter(data)
txt_formatter = TxtFormatter(data)

report = Report('reporte.csv')
report.call(formatter)
report.call(txt_formatter)

