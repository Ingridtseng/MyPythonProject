"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)

        # ----- Write your code below this line ----- #
        info = soup.tbody.text.split()[0:1001]
        male = 0
        female = 0
        for i in range(len(info)//5):
            m_number_lst = info[2+5*i].split(',')
            for j in range(len(m_number_lst)):
                male += int(m_number_lst[j])*(1000**(len(m_number_lst)-j-1))
            f_number_lst = info[4 + 5 * i].split(',')
            for k in range(len(f_number_lst)):
                female += int(f_number_lst[k])*(1000**(len(f_number_lst)-k-1))

        print('Male Number: ' + str(male))
        print('Female Number: ' + str(female))


if __name__ == '__main__':
    main()
