import tabula
table = tabula.read_pdf('Section-21 : PDFs/pdf-table/wr-rb.pdf', pages=2)

print(type(table[0]))

table[0].to_csv('Section-21 : PDFs/pdf-table/output.csv', index=None)
