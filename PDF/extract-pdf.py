import camelot

tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)

# zip with list of tables 
tables.export('tables.csv', f='csv', compress=True)

# return first table into csv
tables[0].to_csv('first_table.csv')