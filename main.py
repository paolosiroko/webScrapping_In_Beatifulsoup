from bs4 import  BeautifulSoup
import requests
import time

print('add skill')
unfamiliar_skill = input('>')

print(f'filtering out{unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        posted_on = job.find('span', class_='sim-posted').span.text
        if 'few' in posted_on:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            link = job.header.h2.a['href']
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name : {company_name.strip()} \n")
                    f.write(f"Skills required : {skills.strip()} \n")
                    f.write(f" link : {link} \n")
                    f.write(f" published : {posted_on.strip()} \n")
                    f.write('')
                print(f'File saved :{index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.1
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait * 10)