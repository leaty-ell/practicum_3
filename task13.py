rows_per_page = int(input("Введите количество строк на каждой странице: "))
columns_per_page = int(input("Введите количество столбцов на странице: "))
record_number = int(input("Введите номер записи в справочнике: "))

records_per_page = rows_per_page * columns_per_page
page_number = (record_number - 1) // records_per_page + 1
record_index_on_page = (record_number - 1) % records_per_page
row_number = (record_index_on_page // columns_per_page) + 1
column_number = (record_index_on_page % columns_per_page) + 1

print(f"Номер страницы: {page_number}, Номер строки: {row_number}, Номер столбца: {column_number}")
