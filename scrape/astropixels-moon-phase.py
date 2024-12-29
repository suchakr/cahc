#%%
from urllib.request import urlopen
from urllib.parse import quote, urljoin
from lxml import html
from glob import glob
import re
import os
import pandas as pd

#%%

def htmlof(url) :
  page = urlopen(url)
  html_bytes = page.read()
  html_str = html_bytes.decode("utf-8")
  return html_str

def get_a_hrefs_from_url(url, regex) :
    html_str = htmlof(url)
    tree = html.fromstring(html_str)
    a_hrefs = tree.xpath('//a/@href')
    return [ urljoin(url,x) for x in a_hrefs if re.match(regex, x) ]

# %%
def get_text_from_url(url, regex) :
    html_str = htmlof(url)
    tree = html.fromstring(html_str)
    texts = tree.xpath('//text()')
    print(f"Found {len(texts)} text elements in {url}")
    return [ x for x in texts if re.match(regex, x) ]

def flatten(l) :
  return [item for sublist in l for item in sublist]



#%%

def get_scrape_astropixels_moon_phases() :
    SCRAPED_MOON_PHASES = './scraped/astropixels-moon-phases.txt'
    BASEURL = 'http://astropixels.com/ephemeris/phasescat/phasescat.html'
    hrefs = get_a_hrefs_from_url(BASEURL,r"phases.*\.html")
    if not os.path.exists(SCRAPED_MOON_PHASES):
        with open(SCRAPED_MOON_PHASES, 'w') as fh:
            ans ="".join(flatten([get_text_from_url(href, r"^.*\d\d:\d\d.*") for href in hrefs]))
            fh.write(ans)
        print(f"Saved to {SCRAPED_MOON_PHASES}")
    else:
        print(f"File {SCRAPED_MOON_PHASES} already exists")

    with open(SCRAPED_MOON_PHASES, 'r') as fh:
        lines = [ re.sub("\n","",x) for x in fh.readlines() if len(x.strip()) > 1 ]

    return lines




#%%
import astropy.time as apt

MONTHS_ARR = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MONTHS_DICT  = { k:v for v,k in enumerate(MONTHS_ARR)}

def doJD(x, fix29=True) :
    try :
        return apt.Time(x).jd
    except Exception as e:
        if fix29 :
            return doJD(re.sub("29T","28T",x),False) # fix for some 02-29
        print (f"Failed to parse {x}")
        print (e)
        return None
        
def get_moon_phase_date_time_df() :
    JD_MOON_PHASES = './scraped/astropixels-moon-phases-jd.tsv'
    if os.path.exists(JD_MOON_PHASES) :
        print (f"File {JD_MOON_PHASES} already exists")
        return pd.read_csv(JD_MOON_PHASES, sep='\t')

    m1 = "".join([ r"(\s*\-?\d+)?" , r"(\s+\w+\s+\d+\s+\d\d:\d\d..)" ])
    m2 = "".join([m1, r"(\s+\w+\s+\d+\s+\d\d:\d\d..)"])
    m3 = "".join([m2, r"(\s+\w+\s+\d+\s+\d\d:\d\d..)"])
    m4 = "".join([m3, r"(\s+\w+\s+\d+\s+\d\d:\d\d..)"])

    lines = get_scrape_astropixels_moon_phases()
    year = 99999
    dt_len = len('Jan 01 11:23')
    acc =[]
    for seq, l in enumerate(lines) :
        ec = 0
        for m in [m4,m3,m2,m1] :
            try :
                ans = [ x.strip() for x in re.match(m, l).groups() if x is not None]
                try :
                    _year = int(ans[0])
                    year = _year
                    ans = ans[1:]
                except :
                    pass
                
                for x in ans :
                    elems = x.split()
                    month, day, time = elems[0], int(elems[1]), elems[2]
                    eclipse = elems[3] if len(elems) > 3 else None
                    acc.append([int(year),MONTHS_DICT[month]+1, int(day), time, eclipse, x])

                break
            except Exception as e:
                ec += 1
                if ec == 4 :
                    print (f"Failed to match {l} with {m}")
                    print (e)
                    break
                pass

    df = pd.DataFrame( acc , columns=['year','month', 'day', 'time', 'eclipse', 'raw'] ).assign (
        dtstr = lambda x: x.apply(lambda y: f"{'-0' if y.year<0 else ''}{abs(y.year):04d}-{y.month:02d}-{y.day:02d}T{y.time}:00", axis=1),
        jd = lambda x: x.dtstr.apply(doJD )
    ).sort_values('jd').to_csv(JD_MOON_PHASES, index=False, sep='\t')
    print (f"Found {len(acc)} lines of moon phases. Saved to {JD_MOON_PHASES}")
    return df

#%%
df = get_moon_phase_date_time_df().assign(
    jd_diff = lambda x: x.jd.diff().shift(-1),
)
pd.set_option('float_format', '{:.2f}'.format)
df[df.eclipse.notnull()]
df.eclipse.value_counts().sort_values(ascending=False)
# %%
ax = df[(df.eclipse=='H') & (df.year < 3000)].assign( 
    jd_diff = lambda x: x.jd.diff().shift(-1),
)[['year','jd_diff']].plot( figsize=(20,8), kind='scatter', x='year', y='jd_diff', title='Years between Subsequent Hybrid Solar eclipses(Annular to Total) over the last 4000 years', s=20)
df[(df.eclipse=='H') & (df.year < 3000)].assign( 
    jd_diff = lambda x: x.jd.diff().shift(-1),
)[['year','jd_diff']].plot( kind='line', x='year', y='jd_diff', lw=.5, ax=ax);
ax.grid( True, which='both', axis='both', alpha=.2)
ax.set_xticks( [ x for x in range(-2000,3001,100) ] )
ax.set_xticklabels( [ f"{x:.0f}" for x in range(-2000,3001,100) ] , rotation=90);
ax.set_yticks( [ x for x in range(0,44000+1,365*5) ] )
ax.set_yticklabels( [ f"{x//365:.0f}" for x in range(0,44000+1,365*5) ] , rotation=0);
ax.set_ylabel('Years between \n Subsequent Hybrid Solar eclipses' , fontdict={'fontsize': 14});
ax.set_xlabel('Year', fontdict={'fontsize': 14});
ax.set_title('Years between Subsequent Hybrid Solar eclipses(Annular to Total) over the last 4000 years', fontdict={'fontsize': 16});



# %%
