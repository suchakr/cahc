#%%
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from lxml import html
from selenium.webdriver.support.ui import Select
import re
import os
import pandas as pd
import requests

#%%

driver = webdriver.Safari()
driver.get('https://insa.nic.in/UI/journaldetails.aspx?AID=Mw==')
sleep(1)
driver.maximize_window()
select_element = Select(driver.find_element(value='ContentPlaceHolder1_ddlvolumeDetails'))
options = select_element.options
opt_vals_map = { option.get_attribute('value') : option.text for option in options }

def get_issue_id(k, val) :
    _,yr, _,vol, _, iss = re.split( r"[\s\,]+", val)
    try :
        z=f'{int(yr):4d}_{int(vol):02d}_{int(iss):02d}'
    except :
        z=f'{int(yr):4d}_{int(vol):02d}_0{iss}'
    z= z.replace(r'and', '-')
    z= z.replace(r'to', '-')
    z= z.replace(r'&', '-')
    z = f'ijhs_{z}'
    return z

for k in list(opt_vals_map.keys())[:] :
    try :
        issue_id = get_issue_id(k, opt_vals_map[k])
        html_file = f'./scraped/ijhs/{issue_id}~.html'
        # skip if html_file exists
        if os.path.exists(html_file) : 
            size_in_bytes = os.path.getsize(html_file)
            size_in_kb = size_in_bytes // (1024)
            print(f'Skipping. Already scraped {html_file} - {size_in_kb} KB')
            continue

        print(f'Scraping {html_file}')
        driver.get('https://insa.nic.in/UI/journaldetails.aspx?AID=Mw==')
        sleep(1)
        select_element = Select(driver.find_element(value='ContentPlaceHolder1_ddlvolumeDetails'))
        select_element.select_by_value(k)
        # driver.implicitly_wait(3) # seconds
        sleep(2)
        submit_button = driver.find_element(value='ContentPlaceHolder1_btnsubmit')
        form1 = driver.find_element(value='form1')
        submit_button.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.url_changes(driver.current_url))
        print(driver.current_url)
        # write driver.page_source to file named f'{issue_id}~.html'
        with open(f'{issue_id}~.html', 'w') as f :
            f.write(driver.page_source)
        # append issue_id, driver.current_url to file named f'log~.html' 
        with open(f'log~.html', 'a') as f :
            f.write(f'{issue_id} {driver.current_url}\n')
        size_in_bytes = os.path.getsize(f'{issue_id}~.html')
        size_in_kb = size_in_bytes // (1024)
        print(f'Size of {issue_id} is {size_in_kb} KB')
        print("=====================================\n")
    except Exception as e :
        print(e)
        continue
driver.quit()



#%%
from lxml import html
from glob import glob
import pandas as pd

acc = []
for file in sorted(glob('./scraped/ijhs/html~/ij*58_03*.html')) :
    print (file)
    try :
        tree = html.parse(file)
        
        # Perform the XPath queries and manipulate the results
        # papers = [(a.get('href'), a.text, a.getnext().getnext().text) for a in tree.xpath('//*[@class="question col-xs-11"]/a')]
        papers = [(a.get('href'), a.text, e.getnext().getnext().text 
        ) for e in 
        tree.xpath('//*[@class="question col-xs-11"]')
        for a in e.xpath('./a')
        ]
        journal = [td.text for td in tree.xpath('//*[@class="col-xs-8"]//tbody/tr/td')]

        journal = re.sub(r'Indian Journal of History of Science', 'IJHS', '-'.join(journal))
        journal = re.sub(r'\s+', '-', journal)

        # Print the results
        for url, paper, author in papers:
            url = 'https://insa.nic.in/' + url.replace('..', '')
            acc.append((journal, paper, author, url))
        print("=====================================\n")
    except Exception as e :
        print(f'EEEE {e}')
        continue

insa_df = pd.DataFrame(acc, columns=['journal', 'paper', 'author', 'url'])#.to_csv('ijhs.csv', index=False)    
#%%
import requests
def size_in_kb(url) :
    resp = requests.head(url)
    size_in_bytes = int(resp.headers['Content-Length'])
    size_in_kb = size_in_bytes // (1024)
    print(f'{size_in_kb} KB - {url}')
    return size_in_kb
insa_df = insa_df.assign(
    size_in_kb = lambda x : x.url.apply(size_in_kb),
    cum_size_in_kb = lambda x : x.size_in_kb.cumsum()
)#.to_csv('ijhs.csv', index=False)

insa_df.to_csv('scraped/ijhs~.tsv', index=False, sep='\t')
insa_df

#%%
insa_df = pd.read_csv('scraped/ijhs.tsv', sep='\t')
insa_df.url.value_counts().sort_values(ascending=False).head(20)
# %%
xdf = insa_df.assign(
    md_url = lambda d : d.url.apply( lambda x: re.sub(r'^.*\/', '/assets/ijhs/', x)),
    year = lambda d : d.journal.apply( lambda x: re.match(r'^.*(\d{4}).*', x).group(1)),
    issue = lambda d : d.journal.apply( lambda x: re.match(r'^.*\-(.*)', x).group(1)),
    md_paper = lambda d : d.apply ( lambda r : f'[{r.paper.strip()}]({r.md_url.strip()})' , axis=1),
)[['year', 'issue', 'author', 'md_paper']]
xdf.index = xdf.index + 1
xdf.to_csv('scraped/ijhs~.md', sep='|', index=True)

# %%
insa_df[insa_df.journal.str.contains('58-2023-Issue-3')].url.tolist()


# %%
