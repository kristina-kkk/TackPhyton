# TODO Найдите количество книг, которое можно разместить на дискете
disk_space_mb = 1.44
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4
chars_per_page = lines_per_page * chars_per_line
total_chars_per_book = pages_per_book * chars_per_page
book_size_bytes = total_chars_per_book * bytes_per_char
disk_space_bytes = disk_space_mb * 1024 * 1024
books_on_disk = int(disk_space_bytes / book_size_bytes)
print("Количество книг, помещающихся на дискету:", books_on_disk)
