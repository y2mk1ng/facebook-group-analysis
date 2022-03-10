'''
Python version: Python 3.8
Author: Yanling Guo (y2mk1ng)
Year: 2022
Usage: if you have manually scraped some data from a list of group members on Facebook, simply use this code to extract their names and save them into .csv format.
This is kind of data cleansing, but we are now using Python instead of SQL here.
Warning: you can only use this when you already have a .txt file that contains the group member information.
'''

import csv, pandas
with open ('members_20220311.txt') as f: ## open your .txt file with your group member info here
    for line in f:
        content = f.readlines()
        all_data = []
        counts = 0
        for num, specifics in enumerate(content, 1):
            if ('Added' in specifics) or ('Joined' in specifics) or ('Invited' in specifics) or ('Created' in specifics): ## there are usually lines with 'Added' or 'Joined' or 'Invited' or 'Created' right below the member's names
                l = ''.join(list(content[num - 2]))
                counts += 1
                all_data.append(l)
                with open('members_20220311.csv', 'w') as csv_file: ## you can change the file name if you want
                    writer = csv.writer(csv_file)
                    for word in all_data:
                        writer.writerow([word]) ## so that the names are added into specific rows in a column
