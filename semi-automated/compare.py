'''
Python version: 3.8
Author: Yanling Guo (y2mk1ng)
'''
import pandas, csv
csv_1 = input('The file name of your first .csv file: ')
csv_2 = input('The file name of your second .csv file: ')
data_1 = set(pandas.read_csv(csv_1)['Name'].tolist())
data_2 = set(pandas.read_csv(csv_2)['Name'].tolist())
#print('Name_1: ', data_1)
diff = data_1.difference(data_2)
print(diff)
csv_diff = csv_1 + '-' + csv_2 + '_diff.csv'
with open(csv_diff, 'w') as f:
	headers = ['Name']
	writer = csv.writer(f)
	writer.writerow(headers)
	for word in diff:
		writer.writerow([word])
