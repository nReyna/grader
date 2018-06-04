import pandas as pd
import argparse



parser = argparse.ArgumentParser(description='Find top students')
parser.add_argument(  'filename', metavar='FileName', type=str)
parser.add_argument('percentage', metavar='Percentage', type=str)
args = parser.parse_args()

# python argparse assignments
filename = args.filename
percentage = args.percentage

df = pd.read_csv(filename)

# keep id and grades only
df1 = df.iloc[:,[0,1,3,5]]

# avg of grades
df1['final'] = df1.apply(lambda row: (row[1]+ row[2] + 2* row[3])/4, axis = 1 )

num_students = int(len(df1) * percentage)

indicies = df1.final.argsort()

filtered_students = df1.iloc[indicies[-num_students:]][::-1]

ids = filtered_students.student_id.values

print(ids)