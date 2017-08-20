import csv

fileName = raw_input('Enter file (csv) name: ')
text = 'var dt = new DataTable();\n\n'

with open(fileName, 'rt') as f:
    reader = csv.reader(f)
    firstRow = True
    for row in reader:
        try:
            if firstRow:
                text += 'var columns = new List<DataColumn>();\n'
                for r in row:
                    text += ('columns.Add(new DataColumn("%s"));\n' % r)
                text += 'dt.Columns.AddRange(columns.ToArray());\n\n'
                firstRow = False
            else:
                text += ('dt.Rows.Add("%s");\n' % '", "'.join(row))
        except Exception as e:
            pass

text += '\nGrid.DataSource = dt;\nGrid.DataBind();'

with open('result.txt', 'w') as w:
    w.write(text)