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
# print(opt_vals_map)


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

excnt = 0
for k in list(opt_vals_map.keys())[:] :
    try :
        issue_id = get_issue_id(k, opt_vals_map[k])
        html_file = f'./scraped/ijhs/html~/{issue_id}~.html'
        # print(f'Scraping {html_file}')
        # skip if html_file exists
        if os.path.exists(html_file) : 
            size_in_bytes = os.path.getsize(html_file)
            size_in_kb = size_in_bytes // (1024)
            if size_in_bytes > 1 :
                # print(f'Skipping. Already scraped {html_file} - {size_in_kb} KB')
                tree = html.parse(html_file)
                papers = [(a.get('href'), a.text, e.getnext().getnext().text 
                    ) for e in tree.xpath('//*[@class="question col-xs-11"]') for a in e.xpath('./a') ]
                if len(papers) > 0 :
                    # print(f'Skipping. Already scraped {html_file} - {size_in_kb} KB')
                    continue
                else :
                    print(f'No Papers - Rescraping {html_file} - {size_in_kb} KB  - no papers found in html file')
            else :
                print(f'Small File - Rescraping {html_file} - {size_in_kb} KB')

        driver.get('https://insa.nic.in/UI/journaldetails.aspx?AID=Mw==')
        sleep(1)
        select_element = Select(driver.find_element(value='ContentPlaceHolder1_ddlvolumeDetails'))
        # print(select_element.options)
        print(k)
        select_element.select_by_value(k)
        # driver.implicitly_wait(3) # seconds
        sleep(2+0*3)
        # submit_button = driver.find_element(value='ContentPlaceHolder1_btnsubmit')
        btnid = 'ContentPlaceHolder1_btnsubmit'
        # btnid = 'ctl00$ContentPlaceHolder1$btnsubmit'
        submit_button = driver.find_element(value=btnid)
        form1 = driver.find_element(value='form1')
        submit_button.click()
        # form1.submit()
        wait = WebDriverWait(driver, 1)
        wait.until(EC.url_changes(driver.current_url))
        print(driver.current_url)
        print(html_file)
        # write driver.page_source to file named f'{issue_id}~.html'
        with open(html_file, 'w') as f :
            f.write(driver.page_source)
        # append issue_id, driver.current_url to file named f'log~.html' 
        with open(f'log~.html', 'a') as f :
            f.write(f'{issue_id} {driver.current_url}\n')
        size_in_bytes = os.path.getsize(html_file)
        size_in_kb = size_in_bytes // (1024)
        print(f'Size of {issue_id} is {size_in_kb} KB')
        print("=====================================\n")
    except Exception as e :
        excnt = excnt + 1
        print(f"{excnt}) Exception {e}")
    if excnt > 2 : break
driver.quit()



#%%
from lxml import html
from glob import glob
import pandas as pd

acc = []
nx = 0
# for file in sorted(glob('./scraped/ijhs/html~/ij*58_03*.html')) :
for file in sorted(glob('./scraped/ijhs/html~/ij*.html')) :
    try :
        tree = html.parse(file)
        
        # Perform the XPath queries and manipulate the results
        # papers = [(a.get('href'), a.text, a.getnext().getnext().text) for a in tree.xpath('//*[@class="question col-xs-11"]/a')]
        papers = [(a.get('href'), a.text, e.getnext().getnext().text 
        ) for e in 
        tree.xpath('//*[@class="question col-xs-11"]')
        for a in e.xpath('./a')
        ]
        print(f"{len(papers)} papers found in {file}")
        journal = [td.text for td in tree.xpath('//*[@class="col-xs-8"]//tbody/tr/td')]

        journal = re.sub(r'Indian Journal of History of Science', 'IJHS', '-'.join(journal))
        journal = re.sub(r'\s+', '-', journal)

        # Print the results
        for url, paper, author in papers:
            url = 'https://insa.nic.in/' + url.replace('..', '')
            acc.append((journal, paper, author, url))
        if not len(papers) :
            nx = nx+1
            print(f"{nx} {file} =====================================\n")

    except Exception as e :
        print(f'EEEE {e}')
        continue

insa_df = pd.DataFrame(acc, columns=['journal', 'paper', 'author', 'url'])#.to_csv('ijhs.csv', index=False)    
insa_df.shape



#%%

def size_in_kb(url):
    try:
        sz = prev_df[prev_df.url == url].size_in_kb.values[0]
        return sz
    except :
        pass

    try:
        # Send a GET request with Range header to request only the first byte
        headers = {'Range': 'bytes=0-0'}
        response = requests.get(url, headers=headers, stream=True, allow_redirects=True)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Retrieve the Content-Range from headers
        content_range = response.headers.get('Content-Range')
        content_length = response.headers.get('Content-Length')

        if content_range:
            # Content-Range is in format: 'bytes 0-0/total_size'
            # Extract the total size
            total_size = int(content_range.split('/')[-1])
        elif content_length:
            # Fallback to Content-Length if Content-Range is not available
            total_size = int(content_length)
        else:
            print("Unable to retrieve file size from headers.")
            return None

        size_in_kb = total_size // 1024
        print(f"{size_in_kb:.2f} KB - {url}")
        return size_in_kb

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    
#%%

import requests
try:
    prev_df = pd.read_csv('scraped/ijhs.csv')
except :
    prev_df = pd.DataFrame(columns=['journal', 'paper', 'author', 'url', 'size_in_kb', 'cum_size_in_kb'])

insa_df = insa_df.assign(
    size_in_kb = lambda x : x.url.apply(size_in_kb),
    cum_size_in_kb = lambda x : x.size_in_kb.cumsum()
)#.to_csv('ijhs.csv', index=False)

insa_df.to_csv('scraped/ijhs.tsv', index=False, sep='\t')
insa_df

#%%
insa_df = pd.read_csv('scraped/ijhs.tsv', sep='\t')
insa_df.url.value_counts().sort_values(ascending=False).head(20)

#%%

# Patch  url with (S(eh1ucortlbqqezipwgliy3mn)) for rows with missing size_in_kb
badurls = insa_df.size_in_kb.isna()
insa_df.loc[insa_df.size_in_kb.isna(), 'url'] = insa_df.loc[insa_df.size_in_kb.isna(), 'url'].apply(
    lambda x: x.replace(
        '/writereaddata', '(S(eh1ucortlbqqezipwgliy3mn))/writereaddata'
        ).replace('/Vol9_', '/Vol09_')
)

insa_df.loc[insa_df.size_in_kb.isna(), 'url'] = insa_df.loc[insa_df.size_in_kb.isna(), 'url'].apply(
    # add .pdf to url if it does not end with .pdf
    lambda x: x if x.endswith('.pdf') else x + '.pdf'
)
insa_df.loc[insa_df.size_in_kb.isna(), 'size_in_kb'] = insa_df.loc[insa_df.size_in_kb.isna(), 'url'].apply(size_in_kb)

#%%
insa_df = insa_df.assign(
    cum_size_in_kb = lambda x : x.size_in_kb.cumsum()
)
insa_df

#%%

insa_df.to_csv('scraped/ijhs.tsv', index=False, sep='\t')



# %%
zdf = insa_df.assign(
    encoded_url  = lambda d : d.url.apply( lambda x: requests.utils.quote(x).replace('https%3A', 'https:')).replace('http%3A', 'http:'),
    md_url = lambda d : d.encoded_url.apply( lambda x: re.sub(r'^.*\/', '/assets/ijhs/', x)),
    year = lambda d : d.journal.apply( lambda x: re.match(r'^.*(\d{4}).*', x).group(1)),
    issue = lambda d : d.journal.apply( lambda x: re.match(r'^.*\-(.*)', x).group(1)),
    paper_chittor = lambda d : d.apply ( lambda r : f'[{r.paper.strip()}]({r.md_url.strip()})' , axis=1),
    paper_ijhs = lambda d : d.apply ( lambda r : f'[{r.paper.strip()}]({r.encoded_url.strip()})' , axis=1),
)

patch_md_header ='''|#|year|issue|author|paper
|---|---|---|---|---'''
# md with local url 
for tag in ['chittor', 'ijhs'] :
    md_file = f'scraped/ijhs-paper-{tag}~.md'
    xdf = zdf[['year', 'issue', 'author', f'paper_{tag}']]
    xdf.index = xdf.index + 1
    xdf.to_csv(md_file, sep='|', index=True)
    # replace the first line with patch_md_header
    with open(md_file, 'r') as f:
        lines = [ f'|{l}' for l in f.readlines()]
        lines[0] = patch_md_header + '\n'
        footer = '[INSA - IJHS ➚](https://insa.nic.in/UI/journaldetails.aspx?AID=Mw==)'
        lines = lines + ['\n', footer + '\n']
    with open(md_file, 'w') as f:
        f.writelines(lines)

    print(f'Wrote {md_file}')




# %%
# insa_df[insa_df.journal.str.contains('58-2023-Issue-3')].url.tolist()
# insa_df[insa_df.url.str.contains('Vol49')].sort_values(by='url').style.format({'url': lambda x: f'<a href="{x}">{x}</a>'})  
insa_df.sort_values(by='url')[['url']].to_csv('scraped/ijhs~.urls', index=False)

# %%
asset_dir = '/Users/sunder/projects/cahcblr.github.io/assets/ijhs'
# list files in asset_dir
asset_files = [x.lower() for x in os.listdir(asset_dir)]
asset_pdfs = [x for x in asset_files if x.endswith('.pdf')]

ijhs_urls = insa_df.url.tolist()
ijhs_pdfs = {re.sub(r'^.*\/', '', x).lower() : x for x in ijhs_urls if x.lower().endswith('.pdf')}

# f, nf = 0, 0
# for pdf in asset_pdfs :
#     pdf = pdf.lower()
#     if pdf in ijhs_pdfs :
#         pass
#         f = f + 1
#         #print(f'# {f:03d} Found {pdf} in ijhs_pdfs')
#     else :
#         nf = nf + 1
#         print(f'# {nf:03d} Not Found {pdf} in ijhs_pdfs')

wget_bash_file = f'{asset_dir}/wget-insa-ijhs.sh'

total_not_found_files = [ pdf for pdf in ijhs_pdfs if pdf.lower() not in asset_pdfs]
total_not_found = len(total_not_found_files)
print(f'Total Not Found {total_not_found} out of {len(ijhs_pdfs)} ijhs_pdfs')

#%%

f, nf = 0, 0
acc = []
for pdf in ijhs_pdfs :
    pdf = pdf.lower()
    if pdf in asset_pdfs :
        f = f + 1
        acc += [ f'# {f:03d} - Found {pdf} in asset_pdfs']
    
    else :
        pass
        nf = nf + 1
        acc += [ 
            f'# {nf:04d} Not Found {pdf} in asset_pdfs' ,
            # wget pdf from ijhs_pdfs
            # f'$D wget -N -O {asset_dir} "{ijhs_pdfs[pdf]}"',
            f'$D wget -N "{ijhs_pdfs[pdf]}"',
            f'echo Processing "{pdf}" - {nf}/{total_not_found} - {100*nf/total_not_found:.2f}%'
        ]

with open(wget_bash_file, 'w') as f :
    # write the current time as a comment
    f.write(f'# {pd.Timestamp.now()}\n')
    # define a variable DO to echo the commands
    f.write('D=echo\n')
    acc += ['echo "All done"']
    f.write('\n'.join(acc))

print(f'Wrote {wget_bash_file}')



# %%
xdf.year.value_counts().sort_index().plot(kind='bar', figsize=(20,5))

# %%
def extract_pdf_text(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            first_page_text = reader.pages[0].extract_text()  # Extract text from the first page only.
            return first_page_text.strip() #Remove extra spaces
    except FileNotFoundError:
        print(f"Warning: PDF file not found: {pdf_path}")
        return ""  # Return empty string if file not found
    except PyPDF2.errors.PdfReadError as e:
        print(f"Warning: Error reading PDF file {pdf_path}: {e}")
        return ""
    

# %%
