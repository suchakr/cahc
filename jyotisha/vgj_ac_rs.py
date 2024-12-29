#%%
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl
import math
from matplotlib import colors
from scipy.interpolate import interp1d
from scipy import stats
import NasaMoonScrapeUtils as nmsu
import NaksUtils as nsu
import PlanetPos as PP
import JdUtils as ju
from IPython.display import display


#%%
def make_n27_lon_divisions() :
  lon_divisions = pd.read_csv("../datasets/n27_lon_divisions.csv").set_index('nid')
  lon_divisions['r_eq'] = np.roll(lon_divisions.Eq,1)
  lon_divisions['l_eq'] = np.roll(lon_divisions.Eq,0)
  lon_divisions['r_ue'] = np.roll(lon_divisions.Ue,1)
  lon_divisions['l_ue'] = np.roll(lon_divisions.Ue,0)

  lon_divisions['r_eq1'] = (lon_divisions.r_eq -350)%360
  lon_divisions['l_eq1'] = (lon_divisions.l_eq -350)%360
  return lon_divisions

n27_lon_divisions = make_n27_lon_divisions()

def between ( x, bounds) :
  bounds = sorted(bounds)
  if ( bounds[1] - bounds[0]) > 50 : # 3 and 350 case ; 50 is a safe number ; Bharani Case
    bounds[1] = (bounds[1] + 50 ) % 360
    bounds[0] = (bounds[0] + 50 ) % 360
    x = (x + 50 ) % 360
    bounds = sorted(bounds)
  return bounds[0] <= x <= bounds[1] 

def naks_lon_err(n27_df):
  def _naks_lon_err(ndf,nbase,attr):
    err = ndf.apply( lambda r : r.lon - nbase.loc[r.nid,attr], axis=1)
    err = (err + 360)%360
    err = err.apply( lambda e :  abs( 360 -e if e > 180 else e))
    return err
  
  long_err_left = _naks_lon_err(n27_df,n27_lon_divisions, 'l_eq')
  long_err_right = _naks_lon_err(n27_df,n27_lon_divisions, 'r_eq')
  n27_df['err_lon_sq_eq'] = min( (long_err_right**2).values.tolist(), (long_err_left**2).values.tolist())
  n27_df['err_lon_abs_eq'] = (long_err_right+long_err_left)/2
  n27_df['err_lon_bounds_eq'] = np.array(
    [min(r,l) for r,l in zip(long_err_right,long_err_left)]
  ) * n27_df.apply( lambda x : 0 if between (
        x.lon , [ n27_lon_divisions.loc[x.nid,'l_eq'] , n27_lon_divisions.loc[x.nid,'r_eq'] ]
      ) else 1, axis=1)

  long_err_left1 = _naks_lon_err(n27_df,n27_lon_divisions, 'l_eq1')
  long_err_right1 = _naks_lon_err(n27_df,n27_lon_divisions, 'r_eq1')
  n27_df['err_lon_bounds_eq1'] = np.array(
    [min(r,l) for r,l in zip(long_err_right1,long_err_left1)]
  ) * n27_df.apply( lambda x : 0 if between (
        x.lon , [ n27_lon_divisions.loc[x.nid,'l_eq1'] , n27_lon_divisions.loc[x.nid,'r_eq1'] ]
      ) else 1, axis=1)

  long_err_left = _naks_lon_err(n27_df,n27_lon_divisions, 'l_ue')
  long_err_right = _naks_lon_err(n27_df,n27_lon_divisions, 'r_ue')
  n27_df['err_lon_sq_ue'] = min( (long_err_right**2).values.tolist(), (long_err_left**2).values.tolist())
  n27_df['err_lon_abs_ue'] = (long_err_right+long_err_left)/2
  n27_df['err_lon_bounds_ue'] = np.array(
    [min(r,l) for r,l in zip(long_err_right,long_err_left)]
  ) * n27_df.apply( lambda x : 0 if between (
        x.lon , [ n27_lon_divisions.loc[x.nid,'l_ue'] , n27_lon_divisions.loc[x.nid,'r_ue'] ]
      ) else 1, axis=1)

  return n27_df

def naks_lon_mae(n27_err_df) :
  p27_mae_lon_eq = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_abs_eq.sum()/df.shape[0]), columns=['mae_lon_eq'])
  p27_mae_lon_ue = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_abs_ue.sum()/df.shape[0]), columns=['mae_lon_ue'])
  p27_mae_lon = pd.merge( p27_mae_lon_eq, p27_mae_lon_ue, on='year', how='left')
  return p27_mae_lon

def naks_lon_mse(n27_err_df) :
  p27_mse_lon_eq = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_sq_eq.sum()/df.shape[0]), columns=['mse_lon_eq'])
  p27_mse_lon_ue = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_sq_ue.sum()/df.shape[0]), columns=['mse_lon_ue'])
  p27_mse_lon = pd.merge( p27_mse_lon_eq, p27_mse_lon_ue, on='year', how='left')
  return p27_mse_lon

def naks_lon_mbe(n27_err_df) :
  p27_mbe_lon_eq = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_bounds_eq.sum()/df[df.err_lon_bounds_eq>0].shape[0]), columns=['mbe_lon_eq'])
  p27_mbe_lon_ue = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df.err_lon_bounds_ue.sum()/df[df.err_lon_bounds_ue>0].shape[0]), columns=['mbe_lon_ue'])
  #p27_mbe_lon_eq = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df[df.err_lon_bounds_eq>0].shape[0]), columns=['mbe_lon_eq'])
  #p27_mbe_lon_ue = pd.DataFrame(n27_err_df.groupby(by='year').apply(lambda df: df[df.err_lon_bounds_ue>0].shape[0]), columns=['mbe_lon_ue'])
  p27_mbe_lon = pd.merge( p27_mbe_lon_eq, p27_mbe_lon_ue, on='year', how='left')
  return p27_mbe_lon

def n27_extrapolate(n27_for_a_year_df, num_of_steps=60, years_per_step=50): 
  lon_df = pd.pivot_table(n27_for_a_year_df, columns='year', index=['nid', 'gname'],  values='lon' , aggfunc=max)
  start_year = n27_for_a_year_df.year.min()
  degrees_per_year = 1/72
  for y in range ( start_year,start_year + num_of_steps*years_per_step , years_per_step) :
    lon_df[y+years_per_step] = (lon_df[y]+ degrees_per_year*years_per_step)%360
  return lon_df.stack().reset_index().rename(columns={0:'lon'})

def load_naks_data(naks_tsv):
  naks_df = pd.read_csv(naks_tsv, sep="\t").drop_duplicates()
  naks_df = naks_df[naks_df.year <= 500]
  naks_df['gnid'] = naks_df.nid + ' ( ' + naks_df.gname + ' ) '
  lon_df = pd.pivot_table(naks_df, columns='year', index=['nid', 'gname', 'gnid'],  values='lon' , aggfunc=max)
  return lon_df.stack().reset_index().rename(columns={0:'lon'})

def  _do_plot_err(filtDf, err, filtTag, errTag, barColor='blue', chartType='bar'):
  _err_df = pd.DataFrame(filtDf.groupby(by='year').apply(lambda df: df[err].sum()/df.shape[0]), columns=[f'{errTag}'])
  ax =_err_df.plot(color=barColor,figsize=(15,5), 
    kind=chartType,
    #kind='line', marker='o',
    title=f'{errTag} - {filtTag}' if filtTag else '' , 
    logy=not True,
    grid=1,
    )
  # _mse.plot(kind='bar', ax=ax, x='year', y='MBE')
  # rect = patches.Rectangle((21, -5), 7,1400, linewidth=3, edgecolor='g', facecolor='none')
  # ax.add_patch(rect)
  ax.set_title(f'{errTag} - {filtTag}' if filtTag else '' , fontsize=40) 
  ax.yaxis.set_tick_params(labelsize=8, rotation=0)
  ax.xaxis.set_tick_params(labelsize=12, rotation=90)
  ax.set_yticks(range(0,31,1))
  if chartType == 'line' : ax.set_xticks(range(-2500,500,50))
  ax.set_ylabel("error", fontsize=30)
  ax.set_xlabel("year", fontsize=30)
  return _err_df

#do_plot_err_mbe(n27Feb24[n27Feb24.year<=0], chartType='line') #("Feb24-Set")
#do_plot_err_mbe(n27Feb24[n27Feb24.year<=0], chartType='bar') #("Feb24-Set")

def do_plot_err_mse(n27_df, tag) :
  p06 = n27_df[ [ x in  bright9Naks  for x in n27_df.nid ] ]
  _do_plot_err(p06 , 'err_lon_sq_eq', ','.join(bright9Lbls) + f' - Bright6 - {tag}', 'EquiSpacedNaks - MSE');
  #_do_plot_err(p06 , 'err_lon_sq_ue', ','.join(bright6Lbls) + f' - Bright6 - {tag}', 'NotEquiSpacedNaks - MSE', barColor='brown');

  _do_plot_err(n27_df , 'err_lon_sq_eq', f'All 27 Nakshatras - {tag}', 'EquiSpacedNaks - MSE')
  #_do_plot_err(n27_df , 'err_lon_sq_ue', f'All 27 Nakshatras - {tag}', 'NotEquiSpacedNaks - MSE', barColor='brown');

def do_plot_err_mae(n27_df, tag) :
  p06 = n27_df[ [ x in  bright9Naks  for x in n27_df.nid ] ]
  _do_plot_err(p06 , 'err_lon_abs_eq', ','.join(bright9Lbls) + f' - Bright6 - {tag}', 'EquiSpacedNaks - MAE');
  #_do_plot_err(p06 , 'err_lon_abs_ue', ','.join(bright6Lbls) + f' - Bright6 - {tag}', 'NotEquiSpacedNaks - MAE', barColor='brown');

  _do_plot_err(n27_df ,'err_lon_abs_eq', f'All 27 Nakshatras - {tag}', 'EquiSpacedNaks - MAE')
  #_do_plot_err(n27_df, 'err_lon_abs_ue', f'All 27 Nakshatras - {tag}', 'NotEquiSpacedNaks - MAE', barColor='brown');

def do_plot_err_mbe(n27_df, chartType='bar') :
  pbri = n27_df[ [ x in  bright9Naks  for x in n27_df.nid ] ]
  ns = len(bright9Naks)
  _do_plot_err(pbri , 'err_lon_bounds_eq', ','.join(bright9Lbls) + f' - Bright {ns}', 'MBE' , chartType=chartType)
  #_do_plot_err(p06 , 'err_lon_bounds_ue', ','.join(bright6Lbls) + f' - Bright6 - {tag}', 'NotEquiSpacedNaks - MBE', barColor='brown');

  _do_plot_err(n27_df ,'err_lon_bounds_eq', f'All 27 Nakshatras', 'MBE', chartType=chartType)
  #_do_plot_err(n27_df, 'err_lon_bounds_ue', f'All 27 Nakshatras - {tag}', 'NotEquiSpacedNaks - MBE', barColor='brown');

def bounded(df) :
  df_bounded = pd.merge(df,n27_lon_divisions, on='nid', how='left')
  df_bounded['lon_bounded_eq'] = df_bounded.apply ( lambda x: between(x.lon, [x.l_eq, x.r_eq] ), axis=1)
  df_bounded['lon_bounded_ue'] = df_bounded.apply ( lambda x: between(x.lon, [x.l_ue, x.r_ue] ), axis=1)
  df_bounded['nnid'] = df_bounded.nid.apply( lambda x: int(re.sub("\D","",x)))
  return df_bounded

def mbounded(df) :
  df_bounded = df
  df_bounded['nnid'] = df_bounded.nid.apply( lambda x: int(re.sub("\D","",x)))
  df_bounded['lon_bounded_eq'] = df_bounded.apply ( lambda x: between(x.lon, [(x.nnid-2)*30%360, (x.nnid-1)*30%360] ), axis=1)
  df_bounded['lon_bounded_ue'] = df_bounded.apply ( lambda x: between(x.lon, [(x.nnid-2)*30%360, (x.nnid-1)*30%360] ), axis=1)
  return df_bounded

def _do_plot_bounded(plt_df, title, ofs, sizes) :
  fig , ax = plt.subplots(figsize=(25,11))
  nnaks = plt_df.nnid.unique().shape[0]
  max_size = max(sizes)
  ax.scatter(y=plt_df.nnid , x=plt_df.year, 
    # s=[ 100*sizes[x] for x in plt_df.year ],
    s=[ 100*1 for x in plt_df.year ],
    c=[ 
           'red' if sizes[x] == max_size
      else 'red' if sizes[x] >= 21
      else (1-sizes[x]/max_size ,0,0) if sizes[x]/max_size >= .75
      else (1-sizes[x]/max_size,1-sizes[x]/max_size,0) if sizes[x] >= .50 
      else (1-sizes[x]/max_size,1-sizes[x]/max_size,1-sizes[x]/max_size) 
      for x in plt_df.year ],
    )
  ax.set_title(title, fontsize=40)
  ax.set_axisbelow(True)
  # ax.minorticks_on()
  ax.set_xlim(-2500, plt_df.year.max())
  ax.set_xticks(range(-2500,plt_df.year.max()+550,50))
  ax.set_xticklabels( [ str(x) for x in range(-2500,550,50)], rotation=90)

  ax.set_ylim(-1, 30)
  ax.set_yticks(range(-1,31,1))
  ax.set_yticklabels( [ str(x) for x in range(-1,31,)], rotation=0)
  ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
  # ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
  ax.yaxis.set_tick_params(labelsize=13)
  ax.xaxis.set_tick_params(labelsize=20)
  ax.set_ylabel("nakṣatra", fontsize=30)
  ax.set_xlabel("year", fontsize=30)
  rect = patches.Rectangle((-1450, -5), 450,40, linewidth=3, edgecolor='g', facecolor='none')
  # ax.add_patch(rect)

  if 'gname' in plt_df.columns:
    plt_df.nid = plt_df.nid + ' ( ' + plt_df.gname + ' ) '

  for n in plt_df.nid.unique().tolist() :
    #y = int(re.sub("\D","",n))   
    y = int(re.sub("^.","",re.sub("\-.*","",n)))
    ax.annotate( n, (ofs - 400*(y%2), y ), fontsize=20, color='purple', va='center')

  plt_df.apply( lambda x: ax.annotate( int(sizes[x.year]) , (x.year, -.5), fontsize=20, ha='center', rotation=90 , color='blue'), axis=1,  )

  plt.show();

def do_bounded_plot(n27_df, tag):
  p27_bounded = bounded(n27_df)
  plt_df=p27_bounded[p27_bounded.lon_bounded_eq]
  sizes = plt_df.groupby(by='year').agg(sum).lon_bounded_eq
  #_do_plot_bounded (plt_df, f"All 27 Naks within Bounds - Equal spacing case - {tag}", -3000+3000-100, sizes)
  _do_plot_bounded (plt_df, f"Bounds - {tag}", -3000+3000+100, sizes)

  plt_df=p27_bounded[p27_bounded.lon_bounded_ue]
  sizes = plt_df.groupby(by='year').agg(sum).lon_bounded_ue
  #_do_plot_bounded (plt_df, f"All 27 Naks within Bounds - Unequal spacing case - {tag}", -3000, sizes)

def sanity_plot_lon(n27_df, tag) :
  pd.pivot_table(n27_df, 
    index='year', columns='gnid', values='lon'
    ).diff().plot(
      figsize=(20,8)
    ).set_title(f'Sanity Plots - Longitudes Diffs - {tag}', fontsize=25)

  pd.pivot_table(n27_df, 
    index='year', columns='gnid', values='lon'
    ).diff().applymap(lambda x: 360+x if x <-180 else x).plot(
      figsize=(20,8)
    ).set_title(f'Sanity Plot - Longitudes Diffs Normed - {tag}')

  fig, ax = plt.subplots( 
    nrows=1, ncols=5, sharex=True, sharey=True, 
    figsize=(20,8)
    )
  axs = ax.flat
  for ax, y in zip( axs ,[ -2500, -1500, -500, 0, 500]) :
      n27_df[n27_df.year==y][['gnid', 'lon']].set_index('gnid').sort_index(ascending=False).plot.barh(
        ax=ax, grid=True, 
        title= f'longitude sanity check - {tag}\nfor year {y}' if y==-2500 else f'year {y}' 
        )
  plt.show()

def plot_smooth_mbe(n_df, tag) :
  discrete_df = pd.DataFrame(n_df.groupby(by='year').apply(lambda df: df['err_lon_bounds_eq'].sum()/df.shape[0]), columns=[f'mbe'])
  # smooth_fn = interp1d(discrete_df.index, discrete_df['mbe'],kind='cubic')
  smooth_fn = interp1d(discrete_df.index, discrete_df['mbe'],kind='cubic')
  smooth_df = pd.DataFrame()
  smooth_index = np.arange(-2500,501)
  #smooth_df['mbe'] = smooth_fn(smooth_index)
  smooth_df['mbe'] = [ x if x>0 else 0 for x in smooth_fn(smooth_index)]
  smooth_df.index = smooth_index

  major_ticks=np.arange(-2500,501,50)
  # minor_ticks=np.arange(-2500,501,20)

  ax = smooth_df.plot.line(figsize=(25,8), color='green')
  ax.set_title(f'Minimum Bound Error - {tag}', fontsize=30)
  ax.set_xlabel("year" , fontsize=20)
  ax.set_ylabel("error", fontsize=20)
  ax.set_xticks(major_ticks)
  ax.set_yticks(range(0,31))
  ax.set_xticklabels( 
    [str(x) for x in smooth_df.index if x%50 == 0], 
    rotation=90,
    fontsize=20
  )
  ax.set_yticklabels( 
    [str(x) for x in range(0,31)], 
    rotation=0,
    fontsize=12
  )
  ax.grid(which='major')
#%%
def plot_smooth_mbe2(n_df, n_dfAbh=None, tag="") :
  mark = '1' if 'Bha' in tag else ''
  discrete_df = pd.DataFrame(n_df.groupby(by='year').apply(lambda df: df[f'err_lon_bounds_eq{mark}'].sum()/df.shape[0]), columns=[f'mbe'])
  year_min = n_df.year.min()
  year_max = n_df.year.max()
  step = 250 #if year_max - year_min > 2000 else 10

  n_df2 = n_df[ [ x in  bright9Naks  for x in n_df.nid ] ]
  discrete_df2 = pd.DataFrame(n_df2.groupby(by='year').apply(lambda df: df[f'err_lon_bounds_eq{mark}'].sum()/df.shape[0]), columns=[f'mbe'])

  smooth_fn = interp1d(discrete_df.index, discrete_df['mbe'],kind='cubic' if step==50 else 'linear')
  smooth_fn2 = interp1d(discrete_df2.index, discrete_df2['mbe'],kind='cubic' if step==50 else 'linear')

  smooth_df = pd.DataFrame()
  smooth_index = np.arange(year_min,year_max)
  smooth_df['mbe_all_27'] = smooth_fn(smooth_index)
  smooth_df['mbe_bright_9'] = [ x if x>0 else 0 for x in smooth_fn2(smooth_index)]
  smooth_df.index = smooth_index
  smooth_df.to_csv(f"../datasets/mbe-{tag}.csv")
  major_xticks=np.arange(smooth_df.index.min(),smooth_df.index.max(), step) 
  major_xticks=np.arange(smooth_df.index.min()*0-2500,smooth_df.index.max()*0+501, step) 
  major_yticks=np.arange(0,36,5) 
  smooth_df = smooth_df.rolling(1).mean()
  if ( 'clip' in tag) :
    smooth_df = smooth_df[smooth_df.index <= -250]

  ax = smooth_df[['mbe_all_27']].plot.line(figsize=(25,10), linestyle='-', lw=2, color='green')
  smooth_df[['mbe_bright_9']].plot.line(linestyle='-.', ax=ax, lw=3, color='green')
  ax.set_xticks(major_xticks)
  ax.set_yticks(major_yticks)
  ax.set_xticklabels( 
    # [str(x) if x%250 ==0 else '' for x in smooth_df.index if x%step  == 0], 
    [str(x) if x%250 ==0 else '' for x in major_xticks if x%step  == 0], 
    rotation=0,
    fontsize=25
  )
  ax.set_yticklabels( 
    [f"{int(d)}°" if (d%5==0) else '' for d in major_yticks ], 
    rotation=0,
    fontsize=25
  )

  ylim = 35 - 20
  if n_dfAbh is not None :
    n27_mbe = n_dfAbh.groupby(by=['year']).agg( { 
        'err_lon_bounds_eq' : np.mean,
        'err_lon_bounds_eq1' : np.mean,
        } )
    n27_mbe.columns = ['N27_MBE_BHA_350', 'N27_MBE_BHA_0']
    # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_350 <=26]
    # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_0 <=26]
    n27_mbe = n27_mbe.rolling(1).mean()
    n27_mbe[(n27_mbe.N27_MBE_BHA_350 <=ylim) &  (n27_mbe.index  <= 300)][['N27_MBE_BHA_350']].plot.line(
      ax=ax, linewidth=5, style=[':', ':'], color='green')
  ax.legend([])

  ax.annotate("27 nakṣatra".upper(), (-1500,11), fontsize=25, color='black')
  ax.plot([-1050,-900 ] , [11.25,11.25], linestyle='-', linewidth=3, color='black')
  ax.annotate("9 seasonal nakṣatra".upper(), (-1500, 10), fontsize=25, color='black')
  ax.plot([-800,-650 ] , [10.25,10.25], linestyle='-.', linewidth=3, color='black')
  ax.annotate("Abhyankar's Yogatārā".upper(), (-1500, 9), fontsize=25, color='black')
  ax.plot([-750,-600 ] , [9.25,9.25], linestyle=':', linewidth=3, color='black')

  # ax.annotate("27 nakṣatra".upper(), (-1250, 22), fontsize=20, color='black')
  # ax.plot([-900,-750 ] , [22.5,22.5], linestyle='-', linewidth=3, color='black')
  # ax.annotate("9 seasonal nakṣatra".upper(), (-1250, 20), fontsize=20, color='black')
  # ax.plot([-700,-600 ] , [20.5,20.5], linestyle='-.', linewidth=3, color='black')

  ax.annotate("ādityacāra".upper(), (-2450, 12.5), fontsize=30, color='green')
  ax.annotate("year".upper(), (-2453, .2), fontsize=25, color='black')
  ax.annotate("postion error".upper(), (-2475, 2.8), fontsize=25, color='black', rotation=90)

  ax.minorticks_on()
  ax.yaxis.grid(which='major', linestyle='-', linewidth='1', color='gray')
  ax.yaxis.grid(which='minor', linestyle=':', linewidth='0.75', color='gray')
  ax.xaxis.grid(which='major', linestyle='-', linewidth='1.1', color='gray')
  ax.xaxis.grid(which='minor', linestyle=':', linewidth='0.75', color='gray')
  ax.set_ylim(ymin=0, ymax=15)


    #n27_mbe[(n27_mbe.N27_MBE_BHA_0 <=ylim) & (n27_mbe.index  >= -1500)][['N27_MBE_BHA_0']].plot.line(
    #  ax=ax, linewidth=2, style=[':', ':'], color='red')
  # ax.set_xlim(xmin=2500, xmax=500)

# plot_smooth_mbe2(n27Feb24_sensitivity, n_dfAbh=n27Feb24_abhyankar, tag="Sensitivity - Shr(β Del) Dha(β Aqr)")
#plot_smooth_mbe2(n27Feb24_sensitivity, "xx")
# plot_smooth_mbe2(n27Feb24_sensitivity, "clip")
#%%
#%%
def plot_n87():
  n87 = pd.read_csv("../datasets/n87_bce1400.csv")
  n87['nnid'] = n87.nid.apply( lambda x: int(re.sub("\D","",x)))
  cnt = n87.nid.unique().shape[0]
  def numof(n): return int(re.sub("\D","", n)); 
  def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values()]
  c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n87.nid ]

  fig, ax = plt.subplots(figsize=(15,7))
  ax.scatter(x=n87.lon, y=n87.lat, c=c, s=600*(1/n87.ncnt))

  ax.set_xticks(range(-30,361,30))
  ax.set_yticks(range(-30,90,10))
  ax.grid()
  ax.set_title(f'{n87.shape[0]} Taras over {n87.nid.unique().shape[0]} Nakshatras - Largely From PT Book, few from chats', fontsize=20)
  ax.set_ylabel("latitude - 1400BCE", fontsize=15)
  ax.set_xlabel("longitude - 1400BCE", fontsize=15)
  n28_mean = n87[['nid','lat', 'lon']].groupby(by='nid').agg(lambda x: np.mean((x-10)%360)+10)
  n28_mean['nnid'] = n28_mean.reset_index().nid.apply( lambda x: int(re.sub("\D","",x))).values
  n28_mean.reset_index().apply( lambda x: ax.annotate(x.nid, (x.lon , 40 + (x.nnid%3)), fontsize=12,rotation=90) ,axis=1);
  n87.reset_index().apply( lambda x: ax.annotate(x.nnid, (x.lon, x.lat), fontsize=13, color='blue', rotation=0 ) ,axis=1);
  plt.show()

# αβγδεσηθικλμνξοπρστυφχψω
def greekify(s) :
  _xlat = {
  'alf' : 'α',
  'bet' : 'β',
  'gam' : 'γ',
  'del' : 'δ',
  'eps' : 'ε',
  'zet' : 'ζ',
  'eta' : 'η',
  'tet' : 'θ', 
  'iot' : 'ι',
  'kap' : 'κ',
  'lam' : 'λ',
  'mu'  : 'μ',
  'nu'  : 'ν',
  'xi'  : 'ξ',
  'omi' : 'ο',
  'pi' :  'π',
  'rho' : 'ρ',
  'sig' : 'σ',
  'tau' : 'τ',
  'ups' : 'υ',
  'phi' : 'φ',
  'chi' : 'χ',
  'psi' : 'ψ',
  'ome' : 'ω'
  }
  xlat = {}
  for k,v in _xlat.items(): 
    xlat[k] = v
    for n in range(1,4):
      xlat[k+str(n)] = v + str(n)
  ans = ' '.join([  xlat[x] if x in xlat else x  for x in re.split("\s+", s)])
  for k,v in _xlat.items(): 
    if v in ans:
      ans = re.sub("^\*\s+","",ans)
      return ans
  return ans

# one time run .. unless bug fixes
def make_naks_meta():
  n87 = pd.read_csv("../datasets/n87.csv")[['nid', 'gname', 'sname', 'hip']]
  n87.hip =n87.hip.apply(
    lambda x: re.sub("HIP\s+","HIP ",x)
  ).apply(
    lambda x: re.sub("^\s+","",x)
  ).apply(
    lambda x: re.sub("\s+$","",x)
  )

  n27 = pd.read_csv("../datasets/n27.csv")[['nid', 'gname', 'sname', 'hip']]
  n27.hip =n27.hip.apply(
    lambda x: re.sub("HIP\s+","HIP ",x)
  ).apply(
    lambda x: re.sub("^\s+","",x)
  ).apply(
    lambda x: re.sub("\s+$","",x)
  )

  n87.gname = n87.gname.apply(lambda x: greekify(x))
  n27.gname = n27.gname.apply(lambda x: greekify(x))

  n27['tag'] = 'rep'
  n87['tag'] = 'other'
  nU=pd.concat( [n27, n87])

  naks_meta = pd.read_csv("../datasets/n27_limited_meta.csv").set_index('nid')
  nU = nU[['nid', 'gname', 'sname', 'hip', 'tag']].set_index('nid').join(naks_meta)
  nU = nU.dropna()

  ans=[]
  for g, df in nU.groupby(by='hip'):
      ans.append(df[df.tag == 'rep'] if df.shape[0] > 1  else df)
      # if df.index.unique().shape[0] > 1: display(df)
  meta_df=pd.concat(ans).sort_values(
    by=['nnid','tag','gname'],
    ascending=[True,False,True]
  )

  meta_df.nnid= [int(x) for x in meta_df.nnid]

  meta_df=meta_df[ ['nnid', 'tag', 'gname', 'sname', 'hip', 'naks', 'enaks', 'daivata'] ]
  meta_df.to_csv("../datasets/~naks_full_meta.csv")
  return meta_df

# make_naks_meta()

def read_naks_meta () :
  return pd.read_csv("../datasets/n83_full_meta.csv")

def bounded_years(n27Date) :
  n27_bounds = bounded(n27Date)[['nid', 'year', 'lon_bounded_eq' ]]
  n27_bounds = n27_bounds[n27_bounds.lon_bounded_eq][['nid', 'year']]
  n27_bounds = n27_bounds.groupby(by='nid').agg(['min','max'])
  n27_bounds.columns = [ '_'.join(x) for x in n27_bounds.columns]
  return n27_bounds

def make_naks_bounds_report(n_df):
  meta_df = read_naks_meta()
  bounded_df = bounded_years(n_df)

  ans = []
  for nid, df in meta_df.groupby(by=['nid']) :
    ans.append( [
      df.nnid.iloc[0],
      nid,
      df.enaks.iloc[0],
      df[df.tag == 'rep'].iloc[0].gname, 
      bounded_df.loc[nid].year_min,
      bounded_df.loc[nid].year_max,
      n27_lon_divisions.loc[nid].l_eq,
      n27_lon_divisions.loc[nid].r_eq,
      df.gname.shape[0],
      # ';'.join(df.gname.tolist()),
      ';'.join( pd.Series(df.gname).sort_values()),
      df.daivata.iloc[0],
      ]
      )

  return pd.DataFrame(ans, columns=[
    '#',
    'nid',
    'nakshatra',
    'rep_star',
    'vis_start_epoch',
    'vis_end_epoch',
    'left_bound',
    'right_bound',
    'num_stars_in_naks',
    'stars_in_naks',
    'daivata',
  ])
#%%

def get_n83_naks_df(yr=-1500) :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')
  n83a['ra_adj'] = n83a.ra - n83a.ra.min()
  # n83a['lon'] = (n83a.lon-330) % 360
  # ans = n83a[n83a.year == (yr if yr in n83a.year.unique() else -1500)]
  ans = n83a[n83a.year == yr] if yr in n83a.year.unique() else pd.DataFrame()  
  return ans

n83_naks_df = get_n83_naks_df()
bright6Naks = [ x for x in n27_lon_divisions.index if re.match('^.*(03|04|10|14|16|18).*$', x) ]
bright6Lbls = [ re.sub("^N\d\d.","", x) for x in n27_lon_divisions.index if re.match('^.*(03|04|10|14|16|18).*$', x) ]
#dhanishtha, revati, rohini, mrgashira, ashlesha, hasta, chitra, jyeshtha, shravana.
bright9Naks = [ x for x in n27_lon_divisions.index if re.match('^.*(dha|rev|roh|mrg|asl|has|chi|jye|shr).*$', x,re.IGNORECASE) ]
bright9Lbls = [ re.sub("^N\d\d.","", x) for x in bright9Naks ]



#%%
# rotate a dataframe by 1 row
def rotate_df(df, n=1):
  return df.iloc[n:].append(df.iloc[:n])

def zscore(x):
  return (x - x.mean()) / x.std()

# normalize a series to [-1,1]
def normalize_11(x):
  return (x - x.min()) / (x.max() - x.min()) * 2 - 1

# normalize a series to [0,1]
def normalize(x):
  return (x - x.min()) / (x.max() - x.min())

def remove_outliers_df(df, zscore_threshold=3):
  zscore_df = df.apply(zscore)
  return df[(zscore_df < zscore_threshold).all(axis=1)]

def remove_outliers(srs, zscore_threshold=1):
  zscore_srs = zscore(srs)
  return srs[(zscore_srs < zscore_threshold)]

def smart_mean(x): 
  # if x is monotonic, return the mean of the first and last elements
  ans = None
  if x.shape[0] == 1:
    ans = x.iloc[0]
  # if (np.all(np.diff(x) >= 0) or np.all(np.diff(x) <= 0)):# and (x.std() < 10):
  elif x.std() < 10:
    ans = np.mean(x)
  else :
    # print (x); print("======")
    ans = (x.iloc[x.shape[0]//2])
  return ans

#%%

def weights_of_two_numbers_so_weighted_average_yields_numbers_in_between(n1=2500, n2=500,step=50,scan=55) :
  return pd.DataFrame([ ( p1, p2 , np.average([n1,n2], weights=[p1,p2]) )for p1 in range(1,scan) for p2 in range(1,scan)]
      ).sort_values([2,0,1]
      ).assign (z = lambda x : x[2].diff()).fillna(999
      ).where ( lambda x: x.z !=0).dropna(
      ).where(lambda x: x[2].apply(int).apply(lambda k: k%step == 0)).dropna(
      ).assign(z2 = lambda x: x[2].diff().fillna(50)).astype(int)[[0,1,2]
      ].sort_values([2], ascending=False
      ).drop_duplicates(subset=[2]).sort_values([2,0,1], ascending=False).values.tolist()

def synth_weighted_array(yr=-1800) :
  lu =  {
    #yr: (n1 y1 n2 y2) => yr = mean ([y1]*n1, [y2]*n2)
    -2500: (1, -2500, 0, -2000),
    -2400: (4, -2500, 1, -2000),
    -2300: (3, -2500, 2, -2000),
    -2200: (2, -2500, 3, -2000),
    -2100: (1, -2500, 4, -2000),
    -2000: (1, -2000, 0, -1500),
    -1900: (4, -2000, 1, -1500),
    -1700: (2, -2000, 3, -1500),
    -1800: (3, -2000, 2, -1500),
    -1600: (1, -2000, 4, -1500),
    -1500: (1, -1500, 0, -1000),
    -1400: (4, -1500, 1, -1000),
    -1300: (3, -1500, 2, -1000),
    -1200: (2, -1500, 3, -1000),
    -1100: (1, -1500, 4, -1000),
    -1000: (1, -1000, 0, -500),
    -900: (4, -1000, 1, -500),
    -800: (3, -1000, 2, -500),
    -700: (2, -1000, 3, -500),
    -600: (1, -1000, 4, -500),
    -500: (1, -500, 0, 0),
    -400: (4, -500, 1, 0),
    -300: (3, -500, 2, 0),
    -200: (2, -500, 3, 0),
    -100: (1, -500, 4, 0),
    0: (1, 0, 0, 500),
    100: (4, 0, 1, 500),
    200: (3, 0, 2, 500),
    300: (2, 0, 3, 500),
    400: (1, 0, 4, 500),
  }
  yr = yr if yr in lu else -1800 # defaults to -1800

  n1, y1, n2, y2 = lu[yr]
  return [y1]*n1 + [y2]*n2

# synth_weighted_array(yr=-1900)

#%%
def plot_vgj_seasons (title = None, years=[-1500], equal_naks=True, tick_mode='deg', season_gap=False, savefig=False, bare_template=False) :
  VGJSeasons = '''
  श्रविष्ठादीनि चत्वारि पौष्णार्धञ्च दिवाकरः । वर्धयन् सरसस्तिक्तं मासौ तपति शैशिरे ॥   
  रोहिण्यन्तानि विचरन् पौष्णार्धाद्याच्च भानुमान् । मासौ तपति वासन्तौ कषायं वर्धयन् रसम् ॥          
  सार्पार्धान्तानि विचरन् सौम्याद्यानि तु भानुमान् । ग्रैष्मिकौ तपते मासौ कटुकं वर्धयन् रसम् ॥   
  सावित्रान्तानि विचरन् सार्पार्धाद्यानि भास्करः । वार्षिकौ तपते मासौ रसमम्लं विवर्धयन् ॥    
  चित्रादीन्यथ चत्वारि ज्येष्ठार्धञ्च दिवाकरः । शारदौ लवणाख्यं च तपत्याप्याययन् रसम् ॥                   
  ज्येष्ठार्धादीनि चत्वारि वैष्णवान्तानि भास्करः । हेमन्ते तपते मासौ मधुरं वर्धयन् रसम् ॥ 
  (Ādityacāra; v. 47, 48, 52, 53, 54, 55)
  '''
  # if years is not a list (scalar) make it a list by calling synth_weighted_array a
  if not isinstance(years, list) : years = synth_weighted_array(years)

  n83_df_bce = pd.concat([get_n83_naks_df(yr=year) for year in years])
  # display(n83_df_bce.head(2))
  # drop  rows where nid is N23-Dha as N23-Srvs is also added to the dataset 
  n83_df_bce = n83_df_bce[n83_df_bce.nid != 'N23-Dha']
  # display(n83_df_bce.jd.unique())
  # display(n83_df_bce.assign(zz=lambda x: x.ra-x.ra.min()).style.format(precision=2))
  n83_df_agg = n83_df_bce.copy()
  columns_to_drop = ['naks', 'gname', 'date']
  for column in columns_to_drop:
    if column in n83_df_agg.columns:
        n83_df_agg = n83_df_agg.drop(column, axis=1)

  n83_df_agg = n83_df_agg.groupby(['nid']).mean().assign( enaks= lambda x : [ y[4:] for y in x.index.values]).sort_values(['nid','year', 'lon','lat'])
  yr = n83_df_agg.year.values.mean()
  yrnum = (1000 - int(yr))//50
  # n83_df_agg = n83_df_bce.groupby('nid').agg(smart_mean).assign( enaks= lambda x : [ y[4:] for y in x.index.values])
  n83_df_cnt = n83_df_bce.groupby('nid').count().assign( cnt= lambda x : x.lon//len(years))[['cnt']]
  naks_cnt_lbl = n83_df_agg.apply( lambda x: f'{x.enaks}\n#{n83_df_cnt.loc[x.name].cnt}', axis=1)
  fig, ax = plt.subplots(subplot_kw={'projection': 'polar'},figsize=(10,10))
  #ax.set_theta_zero_location('E', offset=2*int(360/27))
  # north_angle =  int ( 
  #     n83_df_agg[n83_df_agg.enaks == 'Dha'].lon.values[0]
  #   - 0*n83_df_agg[n83_df_agg.enaks == 'Ash'].lon.values[0] 
  # )
  # display(n83_df_agg.year.values[0], north_angle, n83_df_agg[n83_df_agg.enaks == 'Dha'])
  #ax.set_theta_zero_location('N', offset=0*north_angle-346+269+13.3-1)
  # ax.set_theta_zero_location('N', offset=north_angle)
  # ax.set_theta_zero_location('N', offset=n83_df_agg[n83_df_agg.enaks == 'Dha'].lon.values[0])
  ax.set_theta_direction(-1)
  # naks = [ re.sub(r"^N...","",x) for x in  n27_lon_divisions.index]
  # n83_df_agg_chi = n83_df_agg['N14-Chi':].append(n83_df_agg[:'N13-Has'])
  n83_df_agg_chi = pd.concat([n83_df_agg['N14-Chi':],n83_df_agg[:'N13-Has']])
  # display(n83_df_agg_chi.shape, n83_df_agg_chi.head(2), n83_df_agg_chi.tail(2))
  angles = [ x/1000 for x in range(0, 360000, 13333)]
  # enaks = n83_df_agg_chi.enaks
  # naks_cnt_lbl = n83_df_agg_chi.apply( lambda x: f'{x.enaks}\n{x.lon:.0f}°\n#{n83_df_cnt.loc[x.name].cnt}', axis=1)
  chi_lon = n83_df_agg_chi[n83_df_agg_chi.enaks == 'Chi'].lon.values[0]
  angles = n83_df_agg_chi.lon if not equal_naks else (np.array(angles[:-1]) + chi_lon)%360 +2
  n83_df_agg_chi['angles'] = angles 
  # naks_cnt_lbl = n83_df_agg_chi.apply( lambda x: f'{x.enaks}\n{x.lon:.0f}°', axis=1)
  # naks_cnt_lbl = n83_df_agg_chi.apply( lambda x: f'{x.enaks} {x.angles:.0f}°', axis=1)
  naks_cnt_lbl = n83_df_agg_chi.apply( lambda x: f'{x.enaks}', axis=1)
  # naks_cnt_lbl = n83_df_agg_chi.apply( lambda x: f'', axis=1)
  # display(n83_df_agg)
  # angles = angles[:len(enaks)]
  # ax.set_rlabel_position(-32.5)  # Move radial labels away from plotted line
  lines, labels = plt.thetagrids((angles+1.2)%360, naks_cnt_lbl.apply(lambda x : ""), fontweight= 'bold' , fontsize=10, color='gray') 
  # draw radial lines from 2 units of origin to 20 units of origin
  colors = ['red','blue','green','purple', 'olive', 'magenta' ,'orange',] #['gray','brown','cyan']
  pd.DataFrame( {'a': (angles-6.5)*np.pi/180  , 'lbl': naks_cnt_lbl, }).assign (
    adeg = lambda x : x.a*180/np.pi%360,
    # rot1 = lambda x : (-x.a*180/np.pi)%270,
    rot1 = lambda x : (-x.adeg)%270,
    rot = lambda x :  x.rot1 + x.adeg.apply( lambda y : 90 if y > 270 else 0),
    posn = lambda x : [ (13+x)%27 for x in range(len(x.a))],
    near_cardinal = lambda x : [ min(((x % 90) ) , ((-x % 90)  )) for x in x.adeg  ],
    ).apply( 
    lambda x : ax.text(x.a, 9.7, 
                       (x.lbl.upper() if x.near_cardinal < 10 else x.lbl.lower()).upper() if not bare_template else '', 
                      #  f'{x.lbl}\n{x.adeg:.0f}\n{x.rot1:.0f}\n{x.rot:.0f}',
                      #  f'{x.lbl}\n{x.posn}',
                       fontsize=15 + ( 10 if x.near_cardinal < 10 else 0) , 
                       fontweight='bold' if x.near_cardinal < 10 else 'normal',
                       ha='center', va='center', alpha=.8, 
                       rotation=x.rot,
                       color= colors[x.posn%len(colors)] if not bare_template else 'black',
                       ),
    axis=1
  )

  # ax.set_rgrids(np.arange(10, 20, 2), angle=0, weight= 'bold' )
  ax.grid(True)
  

  # angles = np.linspace(0,359.99,num=54)
  # cidx = np.roll(np.array([ math.floor(x/(4.5*360/27)) for x in angles]),-1)

  ix =0
  for naks, _df in n83_df_bce.groupby( 'nid' ) :
    _df = _df.copy().sort_values(['year', 'lon', 'lat'])
    _df = _df[['gname', 'year', 'lon', 'lat']]
    if bare_template: break
    # plot the taras of the nakshatra
    ax.scatter( 
    # [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').min().lon if 'N02-Bha'==naks else  _df.groupby('gname').mean().lon )], 
      [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').lon.apply(smart_mean) )], 
      [6.1 + x/20 for x in _df.groupby('gname').mean().lat],
      s=150 ,#if 'Ash' in naks else 60, 
      # marker=f'${naks[4:6]}:{(_df.lon.median() if "N02-Bha"==naks else _df.lon.median() ):.0f}°$',
      alpha=0.5, zorder=2,
      c=colors[ix%len(colors)],
    )

    rads=[ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').lon.apply(smart_mean) )][0:1]
    # rads=[ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').lon.apply(min) )][0:1]
    degs = [ x*180/np.pi for x in rads]
    near_cardinal_deg = [ min(((x % 90) ) , ((-x % 90)  )) for x in degs  ][0]
    near_cardinal = near_cardinal_deg<7
    ax.scatter( 
      rads,
      6.3 + ix%2,
      s=800*0, #if 'Ash' in naks else 100, 
      marker=f'${naks[4:6]}:{smart_mean(_df.groupby("gname").lon.apply(smart_mean) ):.0f}°$' 
            if (False and near_cardinal) else f'${(naks[4:7]).lower()}$'
            ,
      alpha=1, zorder=1,
      c=colors[ix%len(colors)],
    )
    # if ( 'N01-Ash' in naks) : print (f'{yr:4.0f} {naks} :   {smart_mean(_df.groupby("gname").lon.apply(smart_mean) )} {_df.lon.to_list()}')
    ix+=1

  # for f,m in zip(range(0,6), list('o*^pds')) :
  #   ang=angles[cidx==f]
  #   cdx=cidx[cidx==f]

  #   c = ax.scatter(
  #     [x*np.pi/180 for x in ang], 
  #     [3+f%2 for x in ang], 
  #     c=[f for x in cdx], 
  #     s=[50*(1+0*f%2 ) + 0*25*cdx for x in ang], 
  #     cmap='rainbow', 
  #     marker=m,
  #     alpha=0.75)

  ax.set_rticks([8], labels=[''] )  # Less radial ticks

  delta = np.pi/27
  seasons = [ 'śiśira', 'vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta',]
  season_colors = [ 'cyan', 'red', 'green', 'orange', 'blue', 'maroon',]
  # let season_text_colors be contrasting to season_color
  season_text_colors = [ 'black', 'blue','black', 'blue', 'black', 'blue',]

  for s in range(-1,5) :
    S = 2*np.pi/6 
    _angles = [ x-1*delta*0 for x in [s*S, s*S, (s*S+S)] ]
    # print([ x*180/np.pi for x in _angles])
    if season_gap:
      if s==0 : _angles[2] = _angles[2] - delta/4 # रोहिण्यन्तानि
      if s==1 : _angles[1] = _angles[1] + delta/4 # सौम्याद्यानि

      if s==2 : _angles[2] = _angles[2] - delta/4 # सावित्रान्तानि
      if s==3 : _angles[1] = _angles[1] + delta/4 # चित्रादीन्य

      if s==4 : _angles[2] = _angles[2] - delta/4 # वैष्णवान्तानि
      if s==-1 : _angles[1] = _angles[1] + delta/4 # श्रविष्ठादीनि

    L = 8
    _vertex = [0,L,L]
    _angles = [ x-4.5*delta for x in _angles]
    if True or not bare_template:
      ax.plot(_angles, _vertex, 'b', lw=0, alpha=.2)
      ax.fill(_angles, _vertex,  alpha=.1, color=season_colors[s%len(season_colors)]) 
    if (s > -2 ) :
      season = seasons[(s+1)%len(seasons)]
      # print([ x*180/np.pi for x in _angles], season)
      # L=len(season)
      if not bare_template:
        # ax.text(_angles[1] + 2.7/L, L*.52 ,season , fontsize=12, ha='center', va='center')
        ax.text(_angles[1] + 30*np.pi/180, L*.52 ,season.upper() , fontsize=15, ha='center', va='center',
                rotation=-(_angles[2]+_angles[2])*180/np.pi/2- 90/2 -30/2,
                color=season_text_colors[(s+1)%len(season_colors)],
                alpha=.75,
        )

  vedic_maasa_lbls =  "madhu mādhava śuci śukra nabhaḥ nabhasya iṣa ūrja sahas sahasya tapas tapasya".split(" ")
  for s in range(-1,12-1) :
    L = 8
    S = 2*np.pi/12 
    _angles = [ x for x in [s*S, s*S, (s*S+S)] ]
    vedic_maasa = vedic_maasa_lbls[(s+1)%len(vedic_maasa_lbls)]
    if not bare_template:
      ax.text(_angles[1] + 20*np.pi/180, L*.38 ,vedic_maasa.lower() , 
              fontsize=12, ha='center', va='center',
              rotation=-(_angles[2]+_angles[2])*180/np.pi/2 + 1*30/2 ,
              color=season_text_colors[((s+1)//2)%len(season_colors)],
              alpha=.75,
              fontfamily='monospace',
      )

    # four solar quarters 
    for i in range(4) : ax.plot([0, 90*i*np.pi/180], [0, 7.9], 'maroon', lw=1, alpha=.2)

    # 10 day ticks
    tick_mode = 'day' if 'day' in tick_mode else 'deg' if 'deg' in tick_mode else 'day' if bool(tick_mode) else None
    num_ticks = 366 if tick_mode == 'day' else 360 if tick_mode == 'deg' else 0
    tick_ofs = 1 if tick_mode == 'day' else 0 
    if tick_mode:
      for i in range(0+tick_ofs, num_ticks+1+tick_ofs,1) :
        # a = (i-1)*2*(np.pi/num_ticks) + np.pi
        a = (i-tick_ofs)*2*(np.pi/num_ticks) + np.pi
        a += 1.5*np.pi
        # if i==tick_ofs : ax.text(a, 8.9, f'{i}', fontsize=12, ha='center', va='center', alpha=.5)
        tick_marks_day = [1,10, 30, 61, 92, 122, 152, 184, 214, 244, 275, 305, 335, 360 ]
        tick_marks_deg = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330 ]
        tick_marks = tick_marks_day if tick_mode == 'day' else tick_marks_deg #if tick_mode == 'deg' else []
        deg = '°' if tick_mode == 'deg' else ''
        if i in tick_marks :
          mark = i if tick_mode == 'day' else (i+90)%360 
          ax.text(a, 8.95, f'{mark}{deg}', fontsize=12, 
                  ha='center', va='center', alpha=.35,
                  rotation=90-(a*180/np.pi)%180
          )
        ax.plot([a, a], [8, 8.5 if i%10 else 8.8  ], 'gray' if ((i%10) or (i==1)) else 'red', lw=1, alpha=.05 if i%5 else .3)
        
  # title =  f"Year {n83_df_agg.year.values.mean():.0f}" if not title else title
  # title =  f"Year {yr:.0f}" if not title else title
  yyyy = int(n83_df_agg.year.values.mean())
  gyans = { 
    # -2100 : "VGJ 11 Ādityacāra/Lagaha",
    -1800 : "Brāhmanda Purāṇa 1.21.141/MAU",
    -1300 : "VGJ 11 Ādityacāra/Lagaha",
    -500 : "VGJ 59 Ṛtusvabhāva",
  }

  gyan = f" {gyans[yyyy]}" if yyyy in gyans else ""
  if gyan :
    ax.text(-np.pi/2, 11, f"{gyan}", fontsize=20, ha='center', va='center', alpha=.8, color='blue', 
            fontfamily='monospace', fontweight='bold', rotation=0) 

  caption = f"The drift of seasonal nakṣatras - at about one nakṣatra/millenia.\nA celestial clock driven by the precession of the equinoxes." if not bare_template else ""
  ax.text(np.pi/2+ 0*np.pi/30, 11.2, caption, fontsize=13, ha='center', va='center', alpha=.5, color='blue', 
          fontfamily='monospace', fontweight='bold', rotation=0 ) 

  title =  f"{abs(yyyy)} {'BCE' if yyyy<0 else 'CE'}" if not title else title
  ax.set_title(title, y=1.12, fontdict={'fontweight':'bold', 'fontsize':20, 'color':'gray'})
  ax.set_facecolor('white')
  # draw the ecliptic - latitude 0
  theta = np.linspace(0, 2*np.pi, 60)
  ax.plot(theta, [6.1]*len(theta), '--', lw=1, color='gray', alpha=.5)

  # save the figure as a png
  if savefig :
    fn = f"./images/naks-366/ticks-{tick_mode}-{yrnum:04d}-{yr:04.0f}.jpg" if tick_mode else f"./images/naks-366/noticks-{yrnum:04d}-{yr:04.0f}.jpg"
    print(f"Saving {fn}")
    plt.savefig(fn)


def plot_adityachaara_seasons() :
    title =  "Vṛddha-Gārgīya Jyotiṣa Seasons in Ādityacāra: v. 47, 48, 52, 53, 54, 55\nYear - 1250BCE"
    plot_vgj_seasons(years=[-1500,-1000], equal_naks=True, title=title, tick_mode='day', season_gap=True, savefig=False)

  # print(VGJSeasons)

if __name__ == '__mainx__' :
  for yr in range(-2500, 401, 100*5) :
    plot_vgj_seasons(years=yr, equal_naks=not False, title="", tick_mode='day', savefig=True )
    plot_vgj_seasons(years=yr, equal_naks=not False, title="", tick_mode='deg', savefig=True )

  wts_fn = weights_of_two_numbers_so_weighted_average_yields_numbers_in_between
  for n1 in range(-2500, 1, 500) :
    continue
    n2 = n1 + 500
    wts = wts_fn(n1,n2,step=100)
    wts += [ [1,0,n1] ] #[ [0,1,n2] ]
    wts = sorted(wts, key=lambda x: x[2])#[-2:]
    for w1, w2 , _ in wts :
      yr = [n1]*w1 + [n2]*w2
      plot_vgj_seasons(years=yr, equal_naks=not False, title="", tick_mode='day', savefig=True )
      plot_vgj_seasons(years=yr, equal_naks=not False, title="", tick_mode='deg', savefig=True )
      # break
    # break
#%%

def plot_mbounds(inm12, tag) :
  m12 = mbounded(inm12)
  m12_pvt=pd.pivot_table(m12, index='year', columns='nnid', values='lon_bounded_eq', aggfunc=sum)
  m12_pvt_sum = m12_pvt.apply(sum, axis=1)
  fig, ax = plt.subplots(figsize=(15,7))
  m12_pvt_sum.plot.bar(figsize=(25,7), grid=True, ax=ax), 
  ax.set_title(f'Monthly Bounds - {tag}', fontsize='30')

  plt.show();

def prev_plot_mbe2_83() :
  # n83_err = naks_lon_err (load_naks_data("../datasets/n83_base_Feb24_bce2500_to_ce0500.tsv"))
  n83_err = naks_lon_err (load_naks_data("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv"))
  n83_lon = n83_err[ n83_err.year ==  -1500][ ['gname', 'lon']]
  n83_err = pd.merge ( n83_err , n83_lon , on='gname', how='left')
  n83_err = n83_err[ ['nid', 'gname', 'year', 'lon_x', 'err_lon_bounds_eq' , 'err_lon_bounds_eq1', 'lon_y'] ]
  n83_mbe = n83_err.groupby(by=['year']).agg( { 
      'err_lon_bounds_eq' : np.mean,
      'err_lon_bounds_eq1' : np.mean,
      } )
  n83_mbe.columns = ['N83_MBE_BHA_350', 'N83_MBE_BHA_0']
  n83_mbe = n83_mbe[['N83_MBE_BHA_350']]
      
  ax = n83_mbe.plot.line(figsize=(25,10), grid=True, style=['-.'], linewidth=2)
  # ax = n83_mbe.plot.line(figsize=(20,10), grid=True, style=['-.'], linewidth=2)
  n27_mbe = n27Feb24.groupby(by=['year']).agg( { 
      'err_lon_bounds_eq' : np.mean,
      'err_lon_bounds_eq1' : np.mean,
      } )
  n27_mbe.columns = ['N27_MBE_BHA_350', 'N27_MBE_BHA_0']
  n27_mbe = n27_mbe[['N27_MBE_BHA_350']]
  ax = n27_mbe.plot.line(ax=ax, linewidth=2)
  ax.set_title ("Minimum Bound Error wrt \n Bharani(41 Ari) from 350, equivalently\n Dhanista (β Del) from 270", fontsize=30)
  r0_35 = range(0,36)
  ax.set_xticks(n27_mbe.index)
  ax.set_xlabel('year', fontsize=20)
  ax.set_ylabel('error', fontsize=20)
  ax.set_yticks(r0_35)
  ax.set_xticklabels(n27_mbe.index, rotation=90, fontsize=25)
  ax.set_yticklabels(r0_35, rotation=0, fontsize=15)
  ax.legend( 
    ['Error using all 83 taras', 'Error using 27 representative taras'], 
    fontsize=30)
  ax.grid(True)

#%%
def plot_mbe2_83(n_df, n_df2 = None, only_abhyankar_27=False) :
  n83_err = naks_lon_err (load_naks_data("../datasets/n83_base_Feb24_bce2500_to_ce0500.tsv"))
  # n83_err = naks_lon_err (load_naks_data("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv"))
  n83_lon = n83_err[ n83_err.year ==  -1500][ ['gname', 'lon']]
  n83_err = pd.merge ( n83_err , n83_lon , on='gname', how='left')
  n83_err = n83_err[ ['nid', 'gname', 'year', 'lon_x', 'err_lon_bounds_eq' , 'err_lon_bounds_eq1', 'lon_y'] ]
  n83_mbe = n83_err.groupby(by=['year']).agg( { 
      'err_lon_bounds_eq' : np.mean,
      'err_lon_bounds_eq1' : np.mean,
      } )
  n83_mbe.columns = ['N83_MBE_BHA_350', 'N83_MBE_BHA_0']
  # n83_mbe = n83_mbe[n83_mbe.N83_MBE_BHA_350 <=26]
  # n83_mbe = n83_mbe[n83_mbe.N83_MBE_BHA_0 <=26]
  n83_mbe = n83_mbe.rolling(1).mean()

  # n83_mbe = n83_mbe[['N83_MBE_BHA_350']]

  DELTA=20 
  ylim = 35 - 20
  #ax = n83_mbe.plot.line(figsize=(25,10), grid=True, style=['--', '--'], linewidth=2)
  #See if you can terminate the Green curves at -250 and start the red at -1500
  fig, ax = plt.subplots(figsize=(25, 10), facecolor='white')
  ax.set_facecolor('white')
  ax = n83_mbe[(n83_mbe.N83_MBE_BHA_350 <=ylim) &  (n83_mbe.index  <= -250) ][['N83_MBE_BHA_350']].plot.line( ax=ax,
    figsize=(25,10), grid=True, style=['--', '--'], linewidth=2 if not only_abhyankar_27 else 0, color='green')
  n83_mbe[(n83_mbe.N83_MBE_BHA_0 <=ylim) & (n83_mbe.index  >= -1500)][['N83_MBE_BHA_0']].plot.line(
    style=['--', '--'], linewidth=2 if not only_abhyankar_27 else 0, ax=ax, color='red')

  n27_mbe = n_df.groupby(by=['year']).agg( { 
      'err_lon_bounds_eq' : np.mean,
      'err_lon_bounds_eq1' : np.mean,
      } )
  n27_mbe.columns = ['N27_MBE_BHA_350', 'N27_MBE_BHA_0']
  # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_350 <=26]
  # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_0 <=26]
  n27_mbe = n27_mbe.rolling(1).mean()
  n27_mbe[(n27_mbe.N27_MBE_BHA_350 <=ylim) &  (n27_mbe.index  <= -250)][['N27_MBE_BHA_350']].plot.line(
    ax=ax, linewidth=2
    , style=['-', '-'] if not only_abhyankar_27 else [':', ':']
    , color='green')
  n27_mbe[(n27_mbe.N27_MBE_BHA_0 <=ylim) & (n27_mbe.index  >= -1500)][['N27_MBE_BHA_0']].plot.line(
    ax=ax, linewidth=2
    , style=['-', '-'] if not only_abhyankar_27 else [':', ':']
    , color='red')

  if n_df2 is not None :
    n27_mbe = n_df2.groupby(by=['year']).agg( { 
        'err_lon_bounds_eq' : np.mean,
        'err_lon_bounds_eq1' : np.mean,
        } )
    n27_mbe.columns = ['N27_MBE_BHA_350', 'N27_MBE_BHA_0']
    # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_350 <=26]
    # n27_mbe = n27_mbe[n27_mbe.N27_MBE_BHA_0 <=26]
    n27_mbe = n27_mbe.rolling(1).mean()
    n27_mbe[(n27_mbe.N27_MBE_BHA_350 <=ylim) &  (n27_mbe.index  <= -250)][['N27_MBE_BHA_350']].plot.line(
      ax=ax, linewidth=2, style=[':', ':'], color='green')
    n27_mbe[(n27_mbe.N27_MBE_BHA_0 <=ylim) & (n27_mbe.index  >= -1500)][['N27_MBE_BHA_0']].plot.line(
      ax=ax, linewidth=2, style=[':', ':'], color='red')

  n09_df = n_df[ [ x in  bright9Naks  for x in n_df.nid ] ]
  n09_mbe = n09_df.groupby(by=['year']).agg( { 
    'err_lon_bounds_eq' : np.mean,
    'err_lon_bounds_eq1' : np.mean,
    } )
  n09_mbe.columns = ['N27_MBE_BHA_350', 'N27_MBE_BHA_0']
  # n09_mbe = n09_mbe[n09_mbe.N27_MBE_BHA_350 <=26]
  # n09_mbe = n09_mbe[n09_mbe.N27_MBE_BHA_0 <=26]
  n09_mbe = n09_mbe.rolling(1).mean()
  ax = n09_mbe[(n09_mbe.N27_MBE_BHA_350 <=ylim) & (n09_mbe.index <=-250)][['N27_MBE_BHA_350']].plot.line(
    ax=ax, linewidth=2 if not only_abhyankar_27 else 0, style=['-.'], color='green')
  # ax = n09_mbe[n09_mbe.N27_MBE_BHA_0 <=ylim][['N27_MBE_BHA_0']].plot.line(ax=ax, linewidth=3, style=['-.'], color='red')

  # ax.set_title ("Minimum Bound Error wrt \n Bharani(41 Ari) from 350, equivalently\n Dhanista (β Del) from 270", fontsize=30)
  r0_35 = range(0,ylim+1,5)
  # ax.set_xticks([ y for y in n27_mbe.index])
  xrange = [ y for y in range(-2500,501,int(500/2))]
  ax.set_xticks(xrange)
  ax.set_xlabel('', fontsize=20)
  ax.set_ylabel('', fontsize=20)
  ax.set_yticks(r0_35)
  # ax.set_xticklabels([ z if z in [-2500, -2000, -1500, -13000, -1000, -500, 0, 500 ] else '' for z in n27_mbe.index], rotation=0, fontsize=25)
  ax.set_xticklabels(xrange, rotation=0, fontsize=25)
  ax.set_yticklabels( [ f"{d}°" if (d %1 == 0 ) else ''  for d in r0_35], rotation=0, fontsize=25)
  # print(dir(ax.get_legend().texts[0]))
  ax.legend( [ ], # [ l.get_text() for l in ax.get_legend().texts],
    # ['83 constituent taras'.upper(), '      ', 
    #  '27 nakṣatras'.upper(),         '      ' ], 
    loc="lower left",
  fontsize=0)
  # ax.annotate("83 stars            --- dotted line".upper(), (-1250, 24), fontsize=20, color='black')
  # ax.annotate("27 nakṣatra         - solid line".upper(), (-1250, 22), fontsize=20, color='black')
  # ax.annotate("9 seasonal nakṣatra - dash-dot line".upper(), (-1250, 20), fontsize=20, color='black')
  if not only_abhyankar_27 :
    ax.annotate("83 stars ".upper(), (-1250, 24/2), fontsize=25, color='black')
    ax.plot([-1000+100,-850+100 ] , [24.5/2,24.5/2], linestyle='--', linewidth=3, color='black')
    ax.annotate(f"27 nakṣatra".upper(), (-1250, 22/2), fontsize=25, color='black')
    ax.plot([-900+100,-750+100 ] , [22.5/2,22.5/2], linestyle='-' if not only_abhyankar_27 else ':' , linewidth=3, color='black')
    ax.annotate(" 9 seasonal nakṣatra".upper(), (-1250, 20/2), fontsize=25, color='black')
    ax.plot([-700+150,-600+150 ] , [20.5/2,20.5/2], linestyle='-.', linewidth=3, color='black')
  else :
    ax.annotate("27 nakṣatra Abhyankar".upper(), (-1250, 18/2), fontsize=25, color='black')
    ax.plot([-600+150,-500+150 ] , [18.5/2,18.5/2], linestyle=':', linewidth=3, color='black')
  if n_df2 is not None:
    ax.annotate("27 nakṣatra Abhyankar".upper(), (-1250, 18/2), fontsize=25, color='black')
    ax.plot([-600+150,-500+150 ] , [18.5/2,18.5/2], linestyle=':', linewidth=3, color='black')
  ax.annotate("ṛtusvabhāva".upper(), (0, 25/3), fontsize=30, color='red')
  ax.annotate("ādityacāra".upper(), (-2450, 11+0*25/3), fontsize=30, color='green')
  ax.annotate("year".upper(), (-2453, .2), fontsize=25, color='black')
  ax.annotate("position error".upper(), (-2475, 3), fontsize=25, color='black', rotation=90)
  # for x1 in range( -2500, 499, 100) :
    # ax.plot ( [x1, x1], [-1,1 + 1 if x1%500==0 else 0], linewidth=2, color='black')
  ax.minorticks_on()
  # ax.grid(True)
  ax.yaxis.grid(which='major', linestyle='-', linewidth='1.2', color='gray')
  ax.yaxis.grid(which='minor', linestyle=':', linewidth='0.75', color='gray')
  ax.xaxis.grid(which='major', linestyle='-', linewidth='1.2', color='gray')
  ax.xaxis.grid(which='minor', linestyle=':', linewidth='0.75', color='gray')
  ax.set_ylim(ymin=0, ymax=30-15)
  ax.set_xlim(xmin=-2500, xmax=500)

  # save the figure as a png with 300 dpi and tight bounding box
  plt.savefig(f"./images/ms-book/pg21-ac-rs-epoch.png", dpi=300, bbox_inches='tight')

# init_globals()
# plot_mbe2_83(n27Feb24, n27Feb24_abhyankar)
# plot_mbe2_83(n27Feb24)
# plot_mbe2_83(n27Feb24)
# plot_mbe2_83(n27Feb24, n27Feb24_abhyankar, only_abhyankar_27=False)
# plot_mbe2_83(n27Feb24_abhyankar, only_abhyankar_27=True)

#%%
def plot_n83_ll(yrs=[-500]) :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')

  def numof(n): return int(re.sub("\D","", n)); 
  # def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values() if '3' in x]
  n83a['ra_adj'] = n83a.ra - n83a.ra.min()
  n83a['lon'] = (n83a.lon-330) % 360

  # yrs = [-500] if rni_only else [-1500,-500]
  for yr in  yrs :
    n83 = n83a[ n83a.year ==  yr]#[ ['gname', 'lon']]
    c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n83.nid ]
    # n27lbls  = [re.sub('N\d\d\-','', f'{k}:{v}') for k,v in n83.nid.value_counts().sort_index().items()]
    n27_mean = n83.groupby(by='nid').agg( {
      'lon': np.median, 
      'lat': np.median, 
      'ra': np.median, 
      'dec': np.median, 
      'nid': len
      }).rename( columns={'nid': 'cnt'} )
    n27_mean_lbls  = n27_mean.reset_index().sort_values(by=['lon']).apply( 
      lambda x: re.sub('N\d\d\-','', f'{x.nid}:{x.cnt}'), axis =1)
    n27_mean_lon  = n27_mean.reset_index().sort_values(by=['lon']).lon 
    n27_mean_lat  = n27_mean.reset_index().sort_values(by=['lon']).lat
    # n27_mean_ra  = n27_mean.reset_index().sort_values(by=['ra']).ra 
    # n27_mean_dec  = n27_mean.reset_index().sort_values(by=['ra']).dec
    if ( yr == -500 +10000): # 10k to mask the hack
      n83.at[403, 'lon'] = 359 # 408 UBha	उत्तराभाद्रपदा	γ Peg 4.512 => 359 for visual simplicity hack
    # display(n83.sort_values(by='lon').head())

    yspan = np.linspace(-40,40,9) 
    xspan = np.linspace(0,360,13)
    ax = n83.plot.scatter(x="lon", y="lat", c=c, 
      s = 100,
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 100), 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 2.5**x.right), 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 25*x.right), 
      figsize=(25,10)

    )

    #ayana_lbls = ['visuvat', 'd-ayana', 'visuvat', 'u-ayana']
    #for ayana, l in zip( np.linspace(0,360,5), ayana_lbls) :
    #  ax.plot( [ ayana for x in yspan[:2]], [ x for x in yspan[:2]], linestyle="-", linewidth=4 )
    #  ax.annotate( l, (ayana, yspan[:2].mean() ), fontsize=20, color='black', va='center', ha='center', rotation=0)

    louaki_maasa_lbls = "caitra vaiśākha jyeṣṭha āṣāḍha śrāvaṇa bhādra\npada āśvayuja kārtika mārga\nśira pauṣa māgha phālguna".split(" ")
    vedic_maasa_lbls =  "madhu mādhava śuci śukra nabhaḥ nabhasya iṣa ūrja sahas sahasya tapas tapasya".split(" ")
    for lon, l , v in zip( np.linspace(0,360,13), louaki_maasa_lbls, vedic_maasa_lbls) :
      ax.plot( [ lon for x in yspan[:4]], [ x for x in yspan[:4]], linestyle="-", linewidth=0 )
      lon = (lon+15)%360
      # ax.annotate( l, (lon-4, yspan[2:4].mean() ), fontsize=21, color='black', va='center', ha='center', rotation=90)
      # ax.annotate( v, (lon+4, yspan[2:4].mean() ), fontsize=21, color='blue', va='center', ha='center', rotation=90)
      ax.annotate( v.upper(), (30* lon//30, yspan[2:4].mean()-8 ), fontsize=20, color='blue', va='top', ha='center', rotation=0)
      ax.annotate( l.upper(), (30 *lon//30, yspan[2:4].mean()-12 ), fontsize=20, color='black', va='top', ha='center', rotation=0)


    rtu_lbls = ['vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta', 'śiśira']
    for rtu,l in zip((np.linspace(0,360,7)- 330) %360 , rtu_lbls) :
      ax.plot( [ rtu-30 for x in yspan[-2:]], [ x for x in yspan[-2:]], linestyle="-.", linewidth=4 )
      ax.plot( [ rtu+30 for x in yspan[-2:]], [ x for x in yspan[-2:]], linestyle="-.", linewidth=4 )
      ax.annotate( l.upper(), (rtu + 0*30, yspan[-2:].mean() ), fontsize=20, color='black', va='center', ha='center', rotation=0)

    ax.plot( [ x for x in xspan], [ 0 for x in xspan] )
    # ax.set_title(f'VGJ - 83 Taras - 27 Nakshatras - Rtu - Ayana\n Longitude Latitude Plot for year {yr}', fontsize=30)
    ax.set_xticks( [ x for x in xspan] )
    # ax.set_xlabel( 'longitude', fontsize=20, rotation=0)
    ax.set_xlabel( '', fontsize=20, rotation=0)
    ax.annotate( 'longitude'.upper(), (3.5, -33 ), fontsize=22, color='black', va='center', ha='left', rotation=0)
    ax.annotate( 'latitude'.upper(), (4.6, -15 ), fontsize=22, color='black', va='bottom', ha='center', rotation=90)
    if ( yr == -500):
      ax.annotate(f"ṛtusvabhāva\n({yr})".upper(), (220, 20), fontsize=30, color='red', ha='left')
    if ( yr == -1500):
      ax.annotate(f"Year\n({yr})".upper(), (220, 20), fontsize=30, color='red', ha='left')
    # ax.set_xticklabels( ['%.2f'%x for x in xspan], fontsize=20, rotation=90)
    # ax.set_xticklabels( ["%02d°%02d'"% (math.floor(x), math.floor(60*(x-math.floor(x))) ) for x in xspan], fontsize=20, rotation=90)
    ax.set_xticklabels( ["%0d°"% ((math.floor(x)+330)%360) for x in xspan], fontsize=25, rotation=0)
    ax.set_yticks( [ x for x in yspan] )
    ax.set_ylabel( '', fontsize=20, rotation=90)
    ax.set_yticklabels( ['%d°'%int(x) if -40 <=x <=40 else '' for x in yspan], fontsize=25, rotation=0)
    # for x, l  in zip( xspan[0:27] + (xspan[1]-xspan[0])/2 , n27lbls) :
    for x, y, l, n  in zip( n27_mean_lon, n27_mean_lat, n27_mean_lbls, range(n27_mean_lon.shape[0])) :
      xdelta = 0
      ydelta = 0
      xdelta = -5 if 'Pus' in l else xdelta 
      xdelta = +5 if 'Asl' in l else xdelta
      xdelta = 5 if 'UPal' in l else xdelta 
      xdelta = 178 if 'UBha' in l else xdelta 
      xdelta = -8 if 'PBha' in l else xdelta 

      ydelta = 0 if 'Ash' in l else ydelta
      ydelta = 0 if 'Bha' in l else ydelta
      ydelta = 0 if 'Kri' in l else ydelta
      ydelta = 20 if 'Roh' in l else ydelta
      ydelta = 20 if 'Mrg' in l else ydelta
      ydelta = 20 if 'Ard' in l else ydelta
      ydelta = 0 if 'Pun' in l else ydelta
      ydelta = 5 if 'Pus' in l else ydelta
      ydelta = 18 if 'Asl' in l else ydelta
      ydelta = 0 if 'Mag' in l else ydelta
      ydelta = -20 if 'PPal' in l else ydelta
      ydelta = -20 if 'UPal' in l else ydelta
      ydelta = 25 if 'Has' in l else ydelta
      ydelta = +5 if 'Chi' in l else ydelta
      ydelta = -20 if 'Swa' in l else ydelta
      ydelta = 20 if 'Anu' in l else ydelta
      ydelta = 20 if 'Mul' in l else ydelta
      ydelta = 25 if 'PAsh' in l else ydelta
      ydelta = 20 if 'UAsh' in l else ydelta
      ydelta = -20 if 'Shr' in l else ydelta
      ydelta = -20 if 'Dha' in l else ydelta
      ydelta = 5 if 'Sha' in l else ydelta
      ydelta = -20 if 'PBha' in l else ydelta
      ydelta =  -10 if 'UBha' in l else ydelta
      ydelta = -2 if 'Rev' in l else ydelta

      sname = "Kṛt Roh Mṛg Ārd Pun Puṣ Āśl Mag PPha UPha Has Cit Svā Viś Anū Jye Mūl PAṣā UAṣā Śra Śrv Śat PPro UPro Rev Aśv Bha".split(" ")
      ename = "Kri Roh Mrg Ard Pun PuS Asl Mag PPal UPal Has Chi Swa Vis Anu Jye Mul PAsh UAsh Śhr Dha Sha PBha UBha Rev Ash Bha".split(" ")

      for e ,s in zip ( ename, sname) :
        l = l.replace(e,s)

      # l = l.replace("Dha:", 'Shrvst:')
      ax.annotate( l, (x + xdelta , y + (-1 if y<0 else 1 ) *10 + ydelta), fontsize=25, color='purple', va='center', ha='center', rotation=90)

    # patch swati for smoothening purpose
    n27_mean_lon[14] =  n27_mean_lon[14] + 10

    smooth_fn = interp1d(n27_mean_lon, n27_mean_lat, kind='cubic')
    smooth_x = np.arange(n27_mean_lon.min(), n27_mean_lon.max(), 1)
    smooth_y = smooth_fn(smooth_x)
    ax.plot( smooth_x, smooth_y, linewidth=2, color='olive')

    if (yr == -1500) :
      moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      moon_df = moon_df[moon_df.sz.diff() != 0]
      # print(yr)
      m = moon_df[moon_df.year == moon_df.year.unique()[0]] 
      smooth_fn = interp1d(m.lon, m.lat, kind='cubic')
      smooth_x = np.arange(m.lon.min(), m.lon.max(), 30)
      smooth_y = smooth_fn(smooth_x)
      ax.plot( smooth_x, smooth_y, linewidth=1, color='gray', marker='$\odot$', markersize=.30)
      ax.plot( m.lon, m.lat, linewidth=0, color='gray', marker='$\odot$', markersize=30)

    ax.set_xlim(xmin=0, xmax=360)
    ax.set_ylim(ymin=-34, ymax=38)
    ax.grid(True)
    # return ax

# plot_n83_ll()
# axis.get_figure().savefig("../_info/fig4.png")
#%%
class Graha_Kolam(object):  # formerly Venus_Pentagram 
  def __init__(self, gruha="venus", corners_per_year=5, num_years=2, year=1200):
    self.gruha = gruha
    self.corners_per_year = corners_per_year
    self.num_years = num_years
    self.pvis_dump = f'../datasets/{gruha}-pvis-dump-{year:04d}bce.tsv'
    self.visibility = f'../datasets/{gruha}-visibility-{year:04d}bce.tsv'

  def make_gruha_visibility_df_from_pvis_dump(self) :  # convert RNI's pvis html to dataframe
    try:
      return pd.read_csv(self.visibility, sep="\t")
    except Exception as e:
      vns = pd.read_csv(self.pvis_dump, sep="\t")[['year','event','date', 'sun_lon', 'obj_lon']]
      def toJD(date):
        (y,m,d) = (int(x) for x in tuple(date.split("-")[1:]))
        return ju.julianJD(-y,m,d)
        # return(-y,m,d)

      vns['jd'] = vns.date.apply(toJD)
      vns = vns[['jd', 'date' , 'year' , 'event', 'sun_lon', 'obj_lon']]
      vns.to_csv(self.visibility, sep="\t", index=False)
      # vns.to_csv("../datasets/venus-visibility-1200BCE.tsv", sep="\t", index=False)
      return vns

  def plot(self) :
    fig, axs = plt.subplots(
      subplot_kw={'projection': 'polar'},figsize=(8*2,8*2), 
      nrows=2, ncols=2, sharex=True, sharey=True,
      gridspec_kw={'hspace':.3, 'wspace':.3, 'height_ratios':[1,1], 'width_ratios':[1,1],}, 
      )

    grh = self.make_gruha_visibility_df_from_pvis_dump()
    self.grh = grh
    slices = [
      'morning_first_visibility', 'evening_first_visibility'
      , 'morning_last_visibility', 'evening_last_visibility'
      , 'last_visibility', 'first_visibility'
      , 'acronychal_rising', 'cosmical_setting', 'acronychal_setting', 'cosmical_rising'
      ]

    for i, slice in enumerate([ x for x in slices if x in grh.event.unique()]) :
      grh_slice= grh[grh.event == slice].reset_index().drop(columns=['index']).assign(
        day_num = lambda x: x.jd.diff().fillna(0).cumsum().astype(int)
      )
      ax = axs[i%2, i//2]  # type: ignore
      ax.set_theta_zero_location('E', offset=1*int(360/27))
      ax.set_theta_direction(-1)
      naks = [ re.sub(r"^N...","",x) for x in  n27_lon_divisions.index]
      angles = [ x/1000 for x in range(0, 360000, 13333)]
      angles = angles[:len(naks)]
      n83_1500_bce = n83_naks_df[n83_naks_df.year == -1500]#.iloc[4:14]

      # display(n83_1500_bce)
      lines, labels = plt.thetagrids(angles, naks, size=15) 
      # plt.scatter( [ x*np.pi/180 for x in angles], [9.9 for x in angles])
      for _, _df in n83_1500_bce.groupby('naks'):
        ax.scatter( 
          [ (x-13.33)*np.pi/180 for x in _df.lon], 
          [7.7 + x/20 for x in _df.lat]
        )
      # ax.set_rticks([10], alpha =.91)  # Less radial ticks
      ax.set_rlim(0,10)
      ax.set_yticklabels([], size=10)
      ax.set_xticklabels(ax.get_xticklabels(), size=13)
      # ax.set_rlabel_position(-32.5)  # Move radial labels away from plotted line
      # ax.set_rmax(10)
      ax.set_facecolor('#f2f2f2' if i%2==0 else 'lightcyan')
      ax.grid(not False, color='blue', linestyle=':', linewidth=.2, alpha=.92)

      colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'black']
      corners_per_year = self.corners_per_year
      num_years = self.num_years
      grh_slice = grh_slice.head(1+corners_per_year*num_years)
      for cycle in range(0,len(grh_slice)//corners_per_year):
        grh_mfv1 = grh_slice.iloc[0+cycle*corners_per_year:1+(1+cycle)*corners_per_year] # what is mfv1? .. sunder, code properly
        grh_angles = [ x*np.pi/180 for x in grh_mfv1.obj_lon]
        grh_radii = [8 for x in grh_mfv1.sun_lon]

        ax.plot( 
          grh_angles, 
          grh_radii,
          # marker='*',
          color=colors[ cycle % len(colors)],
          alpha=0.5, 
          linewidth=5 if cycle==0 else 2,
          ls='-' if cycle==0 else ':',

          )

        ax.scatter(grh_angles[0:1]*1, [8.8], s=2000*0 if cycle==0 else 0, 
          color='purple', alpha=.8, marker=f'$start$', zorder=-1000)
        
        for x in range(1,4):
          for angle, dt, seq in zip ( grh_angles[:-1], grh_mfv1.date.values[:-1], range(0, len(grh_angles[:-1]))):  # type: ignore
            dt1 = dt.split("-")[x:x+1][0]
            ax.scatter(
              angle, [8-1.5*x], 
              s=len(dt1)*300 if cycle==0 else 0, 
              color='red' if x%2==0 else 'blue', 
              alpha=.8, marker=f'${dt1}{chr(32)}$')
            # seq = chr(49+seq)
            ax.scatter(
              angle, [8.8], 
              s=400 + (800 if seq==0 else 0)if cycle==0 else 0, 
              color='brown' ,
              alpha=.2, marker=f'$({seq+1}{"" if seq==0 else ""})$')

      max_dt, min_dt = (
        grh_slice[grh_slice.jd == grh_slice.jd.max()].date.values[0], 
        grh_slice[grh_slice.jd == grh_slice.jd.min()].date.values[0]
        )
      ax.set_title(f"\n{slice} \nfrom {min_dt} to {max_dt}", fontsize=15, color='blue')
      # ax.set_title(f"\n{slice} \nfrom {vns_slice.year.min()} to {vns_slice.year.max()}", fontsize=15, color='blue')
      
    plt.suptitle(f"{self.gruha.capitalize()}", fontsize=25)
    
if __name__ == "__main__":
  # Gruha_Kolam(year=1200).plot() 
  # Gruha_Kolam(year=400).plot() 
  # Graha_Kolam(gruha="mercury",corners_per_year=7, num_years=40, year=400).plot() 
  Graha_Kolam(gruha="mars",corners_per_year=8, num_years=40, year=400).plot() 
  Graha_Kolam(gruha="venus",corners_per_year=8, num_years=40, year=400).plot() 
#%%

#%%
def make_gruha_visibility_df (
  gruha_names=['Mars'], 
  visibility_thresholds=[20],
  start=None, numdays=None , 
  ) :
  bce501 = ju.julianJD(-590, 6, 1)
  start = start or bce501
  numdays = numdays or 365*2
  
  pp = PP.PlanetPos()
  gruha_sun = pd.concat([
    pp.get_planet_pos(jd=j+start).loc[gruha_names +['Sun']] for j in range(0, numdays, 1)
  ])
  gruhas = gruha_sun.loc[gruha_names]
  sun = gruha_sun.loc[['Sun']]

  nu = nsu.NaksUtils()

  gruha_ans =[]
  visibility_thresholds = [ x for x in visibility_thresholds*len(gruha_names)][0:len(gruha_names)]
  for gn, visibility_threshold in zip ( gruha_names, visibility_thresholds) :
    gruha = gruhas.loc[gn].copy()
    ra_decl = gruha.apply( lambda x : pd.Series(nu.ll_to_rd(x.elati, x.elong)[-2:]), axis=1)
    ra_decl.columns = ['ra', 'decl']  # type: ignore
    gruha['year'] = gruha.date.apply(lambda x: -int(x.split("-")[1]))
    lon_factor = (gruha.elong.diff().apply(lambda x: 0 if x > -300 else 1).cumsum()-1)*360
    gruha['lon'] = gruha.elong + lon_factor
    ra_factor = lon_factor #(ra_decl.ra.diff().apply(lambda x: 0 if x > -300 else 1).cumsum()-1)*360
    gruha['_raf'] = ra_factor
    gruha['_ra'] = ra_decl.ra #+ ra_factor
    gruha['ra'] = ra_decl.ra + ra_factor

    gruha['lat'] = gruha.elati
    gruha['decl'] = ra_decl.decl
    gruha['sun_elong'] = list(sun.elong)
    sun_lon_factor = (gruha.sun_elong.diff().apply(lambda x: 0 if x > -300 else 1).cumsum()-1)*360
    gruha['sun_lon'] = gruha.sun_elong + sun_lon_factor
    gruha['gs_gap'] = (gruha.lon  - gruha.sun_lon)%360 # gs_gap is elongation
    gruha['gs_gap'] = gruha.gs_gap.apply(lambda x: x if x < 180 else x-360) 
    gruha['gruha_visibility'] = gruha.gs_gap.apply ( 
      lambda x:  0 if (-visibility_threshold<x< visibility_threshold) else 1 if (x>visibility_threshold) else -1 
    )
    # gruha['gruha_visibility'] = gruha.gs_gap.apply(lambda x: 1 if np.abs(x)>visibility_threshold else -1)
    utt = (gruha.sun_elong-270).apply(np.abs).diff().apply(np.sign).diff().fillna(0)
    dks = (gruha.sun_elong-90).apply(np.abs).diff().apply(np.sign).diff().fillna(0)
    gruha['ayana'] = [ 'uttara' if u==2 else 'dakshina' if d==2 else '-' for u,d in zip(utt,dks)]

    gruha = gruha.assign(
      day_num = lambda x: range(len(x))
      , dl1 = lambda x: x.gs_gap.diff().apply(np.sign).fillna(0) 
      , dl2 = lambda x: x.dl1.diff().apply(np.sign).fillna(0) 
      # , lon_bend = lambda x: x.gs_gap.diff().apply(np.sign).diff().fillna(0)*-1 # max/min elongation
      , lon_bend = lambda x: x.dl2.apply(lambda x: 'east' if x> 0 else 'west' if x<0 else '-')
      , west_visibility = lambda x: (x.gs_gap-visibility_threshold).apply(np.sign).diff().fillna(0).apply(lambda x: 'first' if x>0 else 'last' if x<0 else '-')
      , east_visibility = lambda x: (x.gs_gap+visibility_threshold).apply(np.sign).diff().fillna(0).apply(lambda x: 'last' if x>0 else 'first' if x<0 else '-')
      )

    interesting_events = ['ayana', 'lon_bend', 'east_visibility'	,'west_visibility']
    gruha['key_events'] = gruha.apply( lambda x : ",".join([f'{y}_{x[y]}'  for y in interesting_events if  x[y] != '-' ]) ,axis=1)
    gruha.key_events = gruha.key_events.apply(lambda x: x if x else '-')
  
    gruha= gruha.reset_index()[[
      'day_num', 'jd', 'date', 'year', 'lon', 'lat', 'ra' , 'decl' , 'elong', 
      'sun_elong', 'sun_lon', 
      'gs_gap' , 
      'dl1', 'dl2' ,  # derivative in gs_gap - first and second derivative
      'gruha_visibility',
      'lon_bend',
      'east_visibility', 'west_visibility', 'ayana',
      'key_events',
    ]]
    gruha_ans.append(gruha)

  # display(gruha)
  return tuple(gruha_ans)

(mars_1299_15yrs,venus_1299_15yrs, mercury_1299_15yrs) = make_gruha_visibility_df(
  gruha_names=['Mars', 'Venus' , 'Mercury'],
  visibility_thresholds=[9,9,9],
  start=ju.julianJD(-1299, 6, 1),
  numdays=365*15,
)

# display(
#   venus_1299_15yrs.head(600).tail(300).head(50).tail(30).tail(8).T
#   , venus_1299_15yrs.head(8).T
# )

#%%
def plot_gruha_elongation(gr, tag):
  # display(gr[gr.dl1>0].head(10).style.set_precision(2).set_caption(tag))
  ax = gr.plot.scatter(
      x='day_num',
      # x='lon',
      y='gs_gap', 
      # c=gr.gs_gap.apply(lambda x: 'gray' if -20<x<20 else 'orange' if x> 20 else 'pink'), 
      # c=gr.apply(lambda x: 'gray' if x.gruha_visibility-1 else 'orange', axis=1 ), 
      c=gr.gruha_visibility.apply(lambda x: 'gray' if x==0 else 'orange' if x>0 else 'pink'), 
      figsize=(25,5), 
      grid=True,
      legend = None
  )

  # gr.assign(
  #   dl1 = lambda x: 10*x.dl1
  #   , dl2 = lambda x: 20*x.dl2
  # ).plot( x='day_num', y=['dl1','dl2'], ax=ax, legend=None)


  # utt = (gr.sun_elong-270).apply(np.abs).diff().apply(np.sign).diff().fillna(0)
  # gr['utt'] = utt
  # dks = (gr.sun_elong-90).apply(np.abs).diff().apply(np.sign).diff().fillna(0)
  # gr['dks'] = dks
  # utt = utt[utt==2]
  # dks = dks[dks==2]
  # for row in gr.loc[utt.index].itertuples():
  for row in gr[gr.ayana =='uttara'].itertuples():
    ax.annotate(
      f'Uttarayana({row.day_num})',
      (row.day_num, row.gs_gap), 
      textcoords="offset points", 
      xytext=(0,0), 
      ha='center',
      fontsize=20,
      color='red',
      alpha=.5,
    )
  for row in gr[gr.ayana =='dakshina'].itertuples():
    ax.annotate(
      f'Dakshinayana({row.day_num})',
      (row.day_num, row.gs_gap), 
      textcoords="offset points", 
      xytext=(0,0), 
      ha='center',
      fontsize=20,
      color='green',
      alpha=.5,
    )

  not_none = lambda x: x not in [ '-', 'none']
  slicers = ['lon_bend', 'east_visibility' ,'west_visibility' ]
  markers = ['o', '^', 's']
  colors = [('pink', 'orange') , ( 'red' , 'maroon'), ( 'green', 'olive')]

  for slicer, marker, color in zip(slicers, markers, colors):
    gr_slice = gr[gr[slicer].apply( not_none ) ]
    # display(gr_slice.T.style.set_precision(2).set_caption(slicer))
    sub_slices = gr_slice[slicer].unique()
    for sub_slice in sub_slices :
      gr_sub_slice = gr_slice[ gr_slice[slicer] == sub_slice]
      # display(gr_sub_slice.T.style.set_precision(2).set_caption(sub_slice))
      ax = gr_sub_slice.plot.scatter(
          x='day_num',
          y='gs_gap', ax=ax,
          s=400,
          marker=marker,
          # c=gr_slice[slicer].apply(lambda x: 'red' if x in [ 'east', 'first'] else 'blue'), figsize=(25,5), grid=True
          c=gr_sub_slice[slicer].apply(lambda x: color[0] if x in [ 'east', 'first'] else color[1]), 
          figsize=(25,5), 
          grid=True,
          label=slicer+'_'+sub_slice,
      )

    for row in gr_slice.itertuples():
      ax.annotate(
        # f'{row.day_num} {row.date} {row.lon:.1f} {row.gs_gap:.1f} {row.lon_bend} {row.east_visibility} {row.west_visibility}',
        f'{row.day_num}\n(N{row.elong//13:.0f})',
        (row.day_num, row.gs_gap), 
        textcoords="offset points", 
        xytext=(-10,10), 
        ha='center',
        fontsize=20,
        color='black',
        alpha=.8
      )

    ax.set_title(tag, fontsize=25, color='gray', pad=20, fontweight='bold', fontfamily='serif', loc='left')

    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.tick_params(axis='both', which='minor', labelsize=20)
    ax.set_xlabel('Day Number', fontsize=20)
    ax.set_ylabel('Elongation', fontsize=20)
    # set minor grid lines at 1/2 of major grid lines
    ax.minorticks_on()
    ax.grid(axis='x' , which='major', linestyle='-', linewidth='2', color='black')
    ax.grid(axis='x', which='minor', linestyle=':', linewidth='0.5', color='black')
    # ax.legend(fontsize=15, loc='upper left')


    ax.legend( loc='center right', prop={'size': 20 , 'style': 'oblique'}, ncol=1)
    # legend = ax.get_legend()
    # for ix, c in enumerate([ c2 for c2 in colors for c1 in c2]) :
    #   print(ix)
    #   legend.legendHandles[ix].set_color(c)


def plot_gruha_elongation_and_visibility ():
  for gr, gr_df, num_years in zip( 
    ['Mercury', 'Venus', 'Mars'], 
    [mercury_1299_15yrs, venus_1299_15yrs, mars_1299_15yrs],
    [2,7,10]
  ):
    _gr_df = gr_df.head(num_years*365).tail(num_years*365-100).copy()
    _gr_df =_gr_df.assign( day_num = lambda x: x.day_num - _gr_df.day_num.min() )
    plot_gruha_elongation(_gr_df, f"{gr}, {_gr_df.year.min()} to {_gr_df.year.max()}\n")

    fn = f"../datasets/{gr.lower()}-events.tsv"

    print ("Writing to file", fn)
    _df = gr_df[
      gr_df.key_events.apply(len)>2
    ][
      re.split("\s+","day_num	date	year	sun_elong	elong	lat	ra	decl	key_events")
    ].reset_index(drop=True)
    _df.index += 1 
    _df.index.name = 'seq'
    _df.date = _df.date.apply(lambda x: re.sub(r'T.*', r'', x))
    _df.to_csv(fn, sep="\t", float_format='%.2f')

    fn_slice = f"../datasets/{gr.lower()}-slice-events~.tsv"
    # print ("Writing to file", fn_slice)
    _df = _gr_df[
      _gr_df.key_events.apply(len)>2
    ][
      re.split("\s+","day_num	date	year	sun_elong	elong	lat	ra	decl	key_events")
    ].reset_index(drop=True)
    _df.index += 1
    _df.index.name = 'seq'
    _df.date = _df.date.apply(lambda x: re.sub(r'T.*', r'', x))
    _df.to_csv(fn_slice, sep="\t", float_format='%.2f')

if __name__ == '__main__': 
  plot_gruha_elongation_and_visibility()

#%%
def plot_n83_ll_with_mars_overlay(yrs=[-500]) :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')

  START_LON = 270
  nu = nsu.NaksUtils()
  def numof(n): return int(re.sub("\D","", n)); 
  # def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values() if '3' in x]
  n83a['ra_adj'] = n83a.ra - n83a.ra.min()
  n83a['lon'] = (n83a.lon-START_LON) % 360

  # yrs = [-500] if rni_only else [-1500,-500]
  for yr in  yrs :
    n83 = n83a[ n83a.year ==  yr]#[ ['gname', 'lon']]
    ra_decl = n83.apply( lambda x : pd.Series(nu.ll_to_rd(x.lat, x.lon)[-2:]), axis=1)
    ra_decl.columns = ['ra', 'decl']
    n83.ra = ra_decl.ra
    n83['decl'] = ra_decl.decl
    n83_copy = n83.copy()
    n83_copy['lon'] = n83_copy.lon + 360
    n83_copy['ra'] = n83_copy.ra + 360
    n83_copy['nid'] = n83_copy.nid.apply(lambda x: x +'_1')
    # n83 = n83.append(n83_copy)
    n83 = pd.concat([n83, n83_copy])
    # display(n83.shape, n83.head(), n83.tail())
    # return
    c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n83.nid ]
    # n27lbls  = [re.sub('N\d\d\-','', f'{k}:{v}') for k,v in n83.nid.value_counts().sort_index().items()]
    n27_mean = n83.groupby(by='nid').agg( {
      'lon': np.median, 
      'lat': np.median, 
      'ra': np.median, 
      'dec': np.median, 
      'nid': len
      }).rename( columns={'nid': 'cnt'} )
    n27_mean_lbls  = n27_mean.reset_index().sort_values(by=['lon']).apply( 
      lambda x: re.sub('N\d\d\-','', f'{x.nid}:{x.cnt}'), axis =1)
    n27_mean_lon  = n27_mean.reset_index().sort_values(by=['lon']).lon 
    n27_mean_lat  = n27_mean.reset_index().sort_values(by=['lon']).lat
    # display(n27_mean.sort_values(by=['lon']).reset_index().head(30))
    # n27_mean_ra  = n27_mean.reset_index().sort_values(by=['ra']).ra 
    # n27_mean_dec  = n27_mean.reset_index().sort_values(by=['ra']).dec
    if ( yr == -500 +10000): # 10k to mask the hack
      n83.at[403, 'lon'] = 359 # 408 UBha	उत्तराभाद्रपदा	γ Peg 4.512 => 359 for visual simplicity hack
    # display(n83.sort_values(by='lon').head())

    yspan = np.linspace(-40,40,9) 
    xspan = np.linspace(0,360*2,13)
    ax = n83.plot.scatter(x="lon", y="lat", c=c, 
      s=100,
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 100), 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 2.5**x.right), 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 25*x.right), 
      # figsize=(60,10)
      figsize=(30,10)

    )

    #ayana_lbls = ['visuvat', 'd-ayana', 'visuvat', 'u-ayana']
    #for ayana, l in zip( np.linspace(0,360,5), ayana_lbls) :
    #  ax.plot( [ ayana for x in yspan[:2]], [ x for x in yspan[:2]], linestyle="-", linewidth=4 )
    #  ax.annotate( l, (ayana, yspan[:2].mean() ), fontsize=20, color='black', va='center', ha='center', rotation=0)

    loukika_maasa_lbls = "caitra vaiśākha jyeṣṭha āṣāḍha śrāvaṇa bhādra\npada āśvayuja kārtika mārga\nśira pauṣa māgha phālguna".split(" ")
    vedic_maasa_lbls =  "madhu mādhava śuci śukra nabhaḥ nabhasya iṣa ūrja sahas sahasya tapas tapasya".split(" ")
    loukika_maasa_lbls = loukika_maasa_lbls[8:] + loukika_maasa_lbls[:8]
    vedic_maasa_lbls  = vedic_maasa_lbls[8:] + vedic_maasa_lbls[:8]

    for lon, l , v in zip( np.linspace(0,360*2,2*12+1), loukika_maasa_lbls+loukika_maasa_lbls, vedic_maasa_lbls+vedic_maasa_lbls) :
      ax.plot( [ lon for x in yspan[:4]], [ x for x in yspan[:4]], linestyle="-", linewidth=0 )
      _yr = lon//360
      lon = (lon+15)%(360*2)
      # ax.annotate( v.upper() if _yr==0 else v.lower(), (30* lon//30, yspan[2:4].mean()-8 ), fontsize=20, color='blue' if _yr==0 else 'black', va='top', ha='center', rotation=0)
      # ax.annotate( l.upper() if _yr==0 else l.lower(), (30 *lon//30, yspan[2:4].mean()-12 ), fontsize=20, color='black' if _yr==0 else 'blue', va='top', ha='center', rotation=0)


    rtu_lbls = ['vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta', 'śiśira']
    for rtu,l in zip((np.linspace(0,360*2,6*2+1)- START_LON) , rtu_lbls+rtu_lbls) :
      _yr = rtu//360
      rtu = (rtu+0)%(360*2)
      ax.plot( [ rtu-30 for x in yspan[-2:]], [ x for x in yspan[-2:]], linestyle="-.", linewidth=4 )
      ax.plot( [ rtu+30 for x in yspan[-2:]], [ x for x in yspan[-2:]], linestyle="-.", linewidth=4 )
      ax.annotate( l.upper() if _yr==0 else l.lower(), (rtu + 0*30, yspan[-2:].mean() ), fontsize=20, color='black' if _yr==0 else 'blue', va='center', ha='center', rotation=0)

    ax.plot( [ x for x in xspan], [ 0 for x in xspan] )
    # ax.set_title(f'VGJ - 83 Taras - 27 Nakshatras - Rtu - Ayana\n Longitude Latitude Plot for year {yr}', fontsize=30)
    ax.set_xticks( [ x for x in xspan] )
    # ax.set_xlabel( 'longitude', fontsize=20, rotation=0)
    ax.set_xlabel( '', fontsize=20, rotation=0)
    ax.annotate( 'longitude'.upper(), (40, -33 ), fontsize=22, color='black', va='center', ha='left', rotation=0)
    ax.annotate( 'latitude'.upper(), (4.6, 5 ), fontsize=22, color='black', va='bottom', ha='center', rotation=90)
    # if ( yr == -500):
      # ax.annotate(f"ṛtusvabhāva\n({yr})".upper(), (220, 20), fontsize=30, color='red', ha='left')
    # if ( yr == -1500):
      # ax.annotate(f"Year\n({yr})".upper(), (220, 20), fontsize=30, color='red', ha='left')
    # ax.set_xticklabels( ['%.2f'%x for x in xspan], fontsize=20, rotation=90)
    # ax.set_xticklabels( ["%02d°%02d'"% (math.floor(x), math.floor(60*(x-math.floor(x))) ) for x in xspan], fontsize=20, rotation=90)
    ax.set_xticklabels( ["%0d°"% ((math.floor(x)+ START_LON)%360) for x in xspan], fontsize=25, rotation=0)
    ax.set_yticks( [ x for x in yspan] )
    ax.set_ylabel( '', fontsize=20, rotation=90)
    ax.set_yticklabels( ['%d°'%int(x) if -40 <=x <=40 else '' for x in yspan], fontsize=25, rotation=0)
    # for x, l  in zip( xspan[0:27] + (xspan[1]-xspan[0])/2 , n27lbls) :
    for x, y, l, n  in zip( n27_mean_lon, n27_mean_lat, n27_mean_lbls, range(n27_mean_lon.shape[0])) :
      xdelta = 0
      ydelta = 0
      xdelta = -5 if 'Pus' in l else xdelta 
      xdelta = +5 if 'Asl' in l else xdelta
      xdelta = 5 if 'UPal' in l else xdelta 
      xdelta = 178 if 'UBha' in l else xdelta 
      xdelta = -8 if 'PBha' in l else xdelta 

      ydelta = 0 if 'Ash' in l else ydelta
      ydelta = 0 if 'Bha' in l else ydelta
      ydelta = 0 if 'Kri' in l else ydelta
      ydelta = 20 if 'Roh' in l else ydelta
      ydelta = 20 if 'Mrg' in l else ydelta
      ydelta = 20 if 'Ard' in l else ydelta
      ydelta = 0 if 'Pun' in l else ydelta
      ydelta = 5 if 'Pus' in l else ydelta
      ydelta = 18 if 'Asl' in l else ydelta
      ydelta = 0 if 'Mag' in l else ydelta
      ydelta = -20 if 'PPal' in l else ydelta
      ydelta = -20 if 'UPal' in l else ydelta
      ydelta = 25 if 'Has' in l else ydelta
      ydelta = +5 if 'Chi' in l else ydelta
      ydelta = -20 if 'Swa' in l else ydelta
      ydelta = 20 if 'Anu' in l else ydelta
      ydelta = 20 if 'Mul' in l else ydelta
      ydelta = 25 if 'PAsh' in l else ydelta
      ydelta = 20 if 'UAsh' in l else ydelta
      ydelta = -20 if 'Shr' in l else ydelta
      ydelta = -20 if 'Dha' in l else ydelta
      ydelta = 5 if 'Sha' in l else ydelta
      ydelta = -20 if 'PBha' in l else ydelta
      ydelta =  -10 if 'UBha' in l else ydelta
      ydelta = -2 if 'Rev' in l else ydelta

      sname = "Kṛt Roh Mṛg Ārd Pun Puṣ Āśl Mag PPha UPha Has Cit Svā Viś Anū Jye Mūl PAṣā UAṣā Śra Śrv Śat PPro UPro Rev Aśv Bha".split(" ")
      ename = "Kri Roh Mrg Ard Pun PuS Asl Mag PPal UPal Has Chi Swa Vis Anu Jye Mul PAsh UAsh Śhr Dha Sha PBha UBha Rev Ash Bha".split(" ")

      _yr = n//27
      for e ,s in zip ( ename, sname) :
        l = l.replace(e,s)

      # l = l.replace("Dha:", 'Shrvst:')
      ax.annotate( re.sub("_1","",re.sub(":.*","",l)), (x + xdelta , y + (-1 if y<0 else 1 ) *10 + ydelta), fontsize=20, color='purple' if _yr==0 else "magenta", va='center', ha='center', rotation=90)

    # patch swati for smoothening purpose
    # n27_mean_lon[24] =  n27_mean_lon[24] + 10
    # n27_mean_lon[24+27] =  n27_mean_lon[24+27] + 10
    n27_mean_lon[22] +=  0
    n27_mean_lon[23] +=  0
    n27_mean_lon[24] +=  0 


    smooth_fn = interp1d(n27_mean_lon, n27_mean_lat, kind='linear')
    smooth_x = np.arange(n27_mean_lon.min(), n27_mean_lon.max(), 1)
    smooth_y = smooth_fn(smooth_x)
    ax.plot( smooth_x, smooth_y, linewidth=1, color='olive', linestyle=":")

    if (yr == -1500) :
      moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      moon_df = moon_df[moon_df.sz.diff() != 0]
      # print(yr)
      m = moon_df[moon_df.year == moon_df.year.unique()[0]] 
      smooth_fn = interp1d(m.lon, m.lat, kind='cubic')
      smooth_x = np.arange(m.lon.min(), m.lon.max(), 30)
      smooth_y = smooth_fn(smooth_x)
      ax.plot( smooth_x, smooth_y, linewidth=1, color='gray', marker='$\odot$', markersize=.30)
      ax.plot( m.lon, m.lat, linewidth=0, color='gray', marker='$\odot$', markersize=30)

    ax.set_xlim(xmin=0, xmax=360*2)
    ax.set_ylim(ymin=-34, ymax=38)

    ax.set_xticks( [ x for x in xspan] ) 

    mars = mars_1299_15yrs.copy()
    mars.lon = mars.lon - 210*3
    mars = mars[(mars.lon >= 0) & (mars.lon <= 360*2)]
    # display(mars.describe())
    mars.plot.scatter(x="lon", y="lat", 
      s=mars.gruha_visibility.apply(lambda x: 10 if x==20 else 30),
      c=mars.gruha_visibility.apply(lambda x: 'red' if x==0 else 'blue' if x>0 else 'green'),
      alpha=0.95, ax=ax)
    # mars.plot.scatter(x="lon", xy="lat", s=mars.tag.apply(lambda x: 20*(x//40)+10),  c="tag", cmap="RdPu", alpha=0.95, ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.grid(True)


    return ax

# axx=plot_n83_ll_with_mars_overlay()
# axis.get_figure().savefig("../_info/fig4.png")

if __name__ == "__main__" :
  plot_n83_ll_with_mars_overlay()

#%%
def plot_n83_rd_with_mars_overlay(yrs=[-500]) :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')

  START_LON = 210 -210 +270
  nu = nsu.NaksUtils()
  def numof(n): return int(re.sub("\D","", n)); 
  # def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values() if '3' in x]
  n83a['ra_adj'] = n83a.ra - n83a.ra.min()
  n83a['lon'] = (n83a.lon-START_LON) % 360

  # yrs = [-500] if rni_only else [-1500,-500]
  for yr in  yrs :
    n83 = n83a[ n83a.year ==  yr]#[ ['gname', 'lon']]
    # ra_decl = n83.apply( lambda x : pd.Series(nu.ll_to_rd(x.lat, x.lon)[-2:]), axis=1)
    # ra_decl.columns = ['ra', 'decl']
    # n83.ra = ra_decl.ra.apply( lambda x: x + (360 if x < 0 else 0))
    # n83['decl'] = ra_decl.decl
    n83.ra = n83.ra.apply( lambda x: x + (360 if x < 0 else 0))
    n83['decl'] = n83['dec'] 
    n83a.to_csv("../datasets/n83~.tsv", float_format='%.2f')
    n83_copy = n83.copy()
    n83_copy['lon'] = n83_copy.lon + 360
    n83_copy['ra'] = n83_copy.ra + 360
    n83_copy['nid'] = n83_copy.nid.apply(lambda x: x +'_1')
    # n83 = n83.append(n83_copy)
    n83 = pd.concat([n83,n83_copy])
    # display(n83.shape, n83.head(), n83.tail())
    # return
    c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n83.nid ]
    # n27lbls  = [re.sub('N\d\d\-','', f'{k}:{v}') for k,v in n83.nid.value_counts().sort_index().items()]
    n27_mean = n83.groupby(by='nid').agg( {
      'lon': np.median, 
      'lat': np.median, 
      'ra': np.median, 
      'dec': np.median, 
      'nid': len
      }).rename( columns={'nid': 'cnt'} )
    n27_mean_lbls  = n27_mean.reset_index().sort_values(by=['lon']).apply( 
      lambda x: re.sub('N\d\d\-','', f'{x.nid}:{x.cnt}'), axis =1)
    n27_mean_lon  = n27_mean.reset_index().sort_values(by=['lon']).lon 
    n27_mean_lat  = n27_mean.reset_index().sort_values(by=['lon']).lat
    n27_mean_ra  = n27_mean.reset_index().sort_values(by=['ra']).ra 
    n27_mean_dec  = n27_mean.reset_index().sort_values(by=['ra']).dec
    if ( yr == -500 +10000): # 10k to mask the hack
      n83.at[403, 'lon'] = 359 # 408 UBha	उत्तराभाद्रपदा	γ Peg 4.512 => 359 for visual simplicity hack
    # display(n83.sort_values(by='lon').head())

    yspan = np.linspace(-60,40,11) 
    xspan = np.linspace(0,360*2,25)
    ax = n83.plot.scatter(x="lon", y="decl", c=c, 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 100), 
      # figsize=(60,10)
      figsize=(30,10)

    )
    
    # display(n83.head(43), n83.tail(43), n83.describe())

    if False : # maasa names
      loukika_maasa_lbls = "caitra vaiśākha jyeṣṭha āṣāḍha śrāvaṇa bhādra\npada āśvayuja kārtika mārga\nśira pauṣa māgha phālguna".split(" ")
      vedic_maasa_lbls =  "madhu mādhava śuci śukra nabhaḥ nabhasya iṣa ūrja sahas sahasya tapas tapasya".split(" ")
      loukika_maasa_lbls = loukika_maasa_lbls[8:] + loukika_maasa_lbls[:8]
      vedic_maasa_lbls  = vedic_maasa_lbls[8:] + vedic_maasa_lbls[:8]

      for lon, l , v in zip( np.linspace(0,360*2,2*12+1), loukika_maasa_lbls+loukika_maasa_lbls, vedic_maasa_lbls+vedic_maasa_lbls) :
        ax.plot( [ lon for x in yspan[:4]], [ x for x in yspan[:4]], linestyle="-", linewidth=0 )
        _yr = lon//360
        lon = (lon+15)%(360*2)
        # ax.annotate( v.upper() if _yr==0 else v.lower(), (30* lon//30, yspan[2:4].mean()-8 ), fontsize=20, color='blue' if _yr==0 else 'black', va='top', ha='center', rotation=0)
        # ax.annotate( l.upper() if _yr==0 else l.lower(), (30 *lon//30, yspan[2:4].mean()-12 ), fontsize=20, color='black' if _yr==0 else 'blue', va='top', ha='center', rotation=0)
        1

    rtu_lbls = ['vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta', 'śiśira']
    for rtu,l in zip((np.linspace(0,360*2,6*2+1)- START_LON) , rtu_lbls+rtu_lbls) :
      _yr = rtu//360
      rtu = (rtu+0)%(360*2)
      ax.plot( [ rtu-30 for x in yspan[-2:]+10], [ x for x in yspan[-2:]+10+5], linestyle="-", linewidth=4 )
      ax.plot( [ rtu+30 for x in yspan[-2:]+10], [ x for x in yspan[-2:]+10+5], linestyle="-", linewidth=4 )
      ax.annotate( l.upper() if _yr==0 else l.lower(), (rtu + 0*30, yspan[-2:].mean()+10+5 ), fontsize=20, color='black' if _yr==0 else 'blue', va='center', ha='center', rotation=0)


    ax.plot( [ x for x in xspan], [ 0 for x in xspan] )
    ax.annotate( 'longitude'.upper(), (-20, -50 ), fontsize=22, color='black', va='center', ha='left', rotation=0)
    ax.annotate( 'declination'.upper(), (-20, -40 ), fontsize=22, color='black', va='bottom', ha='center', rotation=90)
    # ax.set_title(f'VGJ - 83 Taras - 27 Nakshatras - Rtu - Ayana\n Longitude Latitude Plot for year {yr}', fontsize=30)
    ax.set_xticks( [ x for x in xspan] )
    # ax.set_xlabel( 'longitude', fontsize=20, rotation=0)
    ax.set_xlabel( '', fontsize=20, rotation=0)
    ax.set_xticklabels( 
        ["%0d°"%((x+START_LON)%360)  for x in (xspan)%360], 
        fontsize=20, 
        rotation=90)
    # return
    # ax.set_xticklabels( ["%0d°"% ((math.floor(x)+ START_LON)%360) for x in xspan], fontsize=25, rotation=0)
    ax.set_yticks( [ x for x in yspan] )
    ax.set_ylabel( '', fontsize=20, rotation=90)
    ax.set_yticklabels( ['%d°'%int(x) if -40 <=x <=80 else '' for x in yspan], fontsize=25, rotation=0)

    # return

    # for x, l  in zip( xspan[0:27] + (xspan[1]-xspan[0])/2 , n27lbls) :
    for x, y, l, n  in zip( n27_mean_lon, n27_mean_dec, n27_mean_lbls, range(n27_mean_lon.shape[0])) :
      # break
      xdelta = 0
      # ydelta = 0
      xdelta = -2 if 'Pus' in l else xdelta 
      xdelta = +2 if 'Asl' in l else xdelta
      xdelta = -3 if 'Chi' in l else xdelta 
      xdelta = +3 if 'Swa' in l else xdelta

      # ydelta = 0 if 'Ash' in l else ydelta
      # ydelta = 0 if 'Bha' in l else ydelta
      # ydelta = 0 if 'Kri' in l else ydelta
      # ydelta = 20 if 'Roh' in l else ydelta
      # ydelta = 20 if 'Mrg' in l else ydelta
      # ydelta = 20 if 'Ard' in l else ydelta
      # ydelta = 0 if 'Pun' in l else ydelta
      # ydelta = 5 if 'Pus' in l else ydelta
      # ydelta = 18 if 'Asl' in l else ydelta
      # ydelta = 0 if 'Mag' in l else ydelta
      # ydelta = -20 if 'PPal' in l else ydelta
      # ydelta = -20 if 'UPal' in l else ydelta
      # ydelta = 25 if 'Has' in l else ydelta
      # ydelta = +5 if 'Chi' in l else ydelta
      # ydelta = -20 if 'Swa' in l else ydelta
      # ydelta = 20 if 'Anu' in l else ydelta
      # ydelta = 20 if 'Mul' in l else ydelta
      # ydelta = 25 if 'PAsh' in l else ydelta
      # ydelta = 20 if 'UAsh' in l else ydelta
      # ydelta = -20 if 'Shr' in l else ydelta
      # ydelta = -20 if 'Dha' in l else ydelta
      # ydelta = 5 if 'Sha' in l else ydelta
      # ydelta = -20 if 'PBha' in l else ydelta
      # ydelta =  -10 if 'UBha' in l else ydelta
      # ydelta = -2 if 'Rev' in l else ydelta

      sname = "Kṛt Roh Mṛg Ārd Pun Puṣ Āśl Mag PPha UPha Has Cit Svā Viś Anū Jye Mūl PAṣā UAṣā Śra Śrv Śat PPro UPro Rev Aśv Bha".split(" ")
      ename = "Kri Roh Mrg Ard Pun PuS Asl Mag PPal UPal Has Chi Swa Vis Anu Jye Mul PAsh UAsh Śhr Dha Sha PBha UBha Rev Ash Bha".split(" ")

      _yr = n//27
      for e ,s in zip ( ename, sname) :
        l = l.replace(e,s)

      # l = l.replace("Dha:", 'Shrvst:')
      ax.plot( 
        [x, x], 
        [-50,50], 
        linestyle=":",
        color='purple' if _yr==0 else "magenta", alpha=0.2)

      l1 = re.sub("_1","",re.sub(":.*","",l))
      ax.annotate( 
        # f'{l1}:{x:.0f}°',
        re.sub("_1","",re.sub(":.*","",l)), 
        # (x + xdelta , y + (-1 if y<0 else 1 ) *10 + ydelta), 
        (x + 1*xdelta , -50+50+42 if n%2==0 else 42), 
        fontsize=20-20+13, color='purple' if _yr==0 else "magenta", 
        va='center', ha='center', rotation=90)

    # for x, y, l, n  in zip( n27_mean_ra, n27_mean_dec, n27_mean_lbls, range(n27_mean_ra.shape[0])) :
    #   ax.annotate( l, (x, y + (-1 if yr<0 else 1 ) * (10 if abs(yr)<24 else -10) ), fontsize=20, color='purple', va='center', ha='center', rotation=90)

    # patch swati for smoothening purpose
    # n27_mean_lon[24] =  n27_mean_lon[24] + 10
    # n27_mean_lon[24+27] =  n27_mean_lon[24+27] + 10
    # return
    smooth_fn = interp1d(n83.lon, n83.decl, kind='linear')
    smooth_x = np.arange(n83.lon.min(), n83.lon.max(), 1)
    smooth_y = smooth_fn(smooth_x)
    smooth_y1 = [x if x<=60 else 60 for x in smooth_y]
    smooth_y1 = [x if x>=-40 else -40 for x in smooth_y1]
    ax.plot( smooth_x, smooth_y1, linewidth=1, color='olive', linestyle=":")
    
    # return
    if (yr == -1500) :
      moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      moon_df = moon_df[moon_df.sz.diff() != 0]
      # print(yr)
      m = moon_df[moon_df.year == moon_df.year.unique()[0]] 
      smooth_fn = interp1d(m.lon, m.lat, kind='cubic')
      smooth_x = np.arange(m.lon.min(), m.lon.max(), 30)
      smooth_y = smooth_fn(smooth_x)
      ax.plot( smooth_x, smooth_y, linewidth=1, color='gray', marker='$\odot$', markersize=.30)
      ax.plot( m.lon, m.lat, linewidth=0, color='gray', marker='$\odot$', markersize=30)

    mars = mars_1299_15yrs.copy()
    ofs = START_LON*3 
    ofs = 210*3 # why is this hack needed ? 
    mars = mars[(mars.lon >= ofs) & (mars.lon <= ofs+360*2)]
    lon_factor = (mars.elong.diff().apply(lambda x: 0 if x > -300 else 1).cumsum()-1)*360
    mars['lon1'] = mars.elong + lon_factor - START_LON
    mars['lon1diff'] = mars.lon1.diff().apply(np.sign).diff().apply(lambda x: 111111*x)
    title = " to ".join ([re.sub("T.*","",str(d)) for d in (mars.date.iloc[0], mars.date.iloc[-1])])
    daynums = (mars.jd  - mars.jd.iloc[0])
    mars['daynum'] = daynums
    vakra_spot = mars[mars.lon1diff < -222]
    vakra_dates = ",".join([ re.sub("T.*","", x) for x in vakra_spot.date.values])

    mars.reset_index().to_csv("../datasets/n83-mars~.csv", float_format='%.2f')
    mars.plot.scatter(x="lon1", y="decl", 
      # s=mars.tag.apply(lambda x: 1 if x<=20 else 1),
      c=mars.gruha_visibility.apply(lambda x: 'red' if x==0 else 'blue' if x >0 else 'green'),
      # c=mars.lon1.apply(lambda x: 
      #   # 'blue' if (x>=110 and x<=(110+100)) else
      #   # 'blue' if (x>=535 and x<=(535+70)) 
      #   'red' if (x>=(90+66) and x<=(90+132)) else
      #   'red' if (x>=(360+90+98) and x<=(360+90+168))
      #   else 'blue'),
      alpha=0.95, ax=ax) 
    ax.set_title(f'Mars Path from {title} \n Vakra at {vakra_dates}', fontsize=30)

    # mars = mars_501_4yrs.copy()
    # mars.ra = mars.ra - START_LON*3
    # mars = mars[(mars.ra >= 0) & (mars.ra <= 360*2)]
    # daynums = (mars.jd  - mars.jd.iloc[0])
    # mars.plot.scatter(x="ra", y="decl", 
    #   s=mars.tag.apply(lambda x: 1 if x<=20 else 1),
    #   c=mars.tag.apply(lambda x: 'red' if x<=20 else 'blue'),
    #   alpha=0.95, ax=ax)

    # display(daynums.max())
    # mars.plot.scatter(x="lon", xy="lat", s=mars.tag.apply(lambda x: 20*(x//40)+10),  c="tag", cmap="RdPu", alpha=0.95, ax=ax)
    for daynum,lon in zip(daynums.apply(int), mars.lon) :
      cardinal_pts = [ 0, 540, daynums.apply(int).max(),]  # cardinal points
      invisible1 = [228, 332] #[160, 160+150]
      vakra =  [590, 765]
      invisible2 = [990, 1098]# [970, 970+110]
      if daynum in cardinal_pts + invisible1 + vakra + invisible2 :
        ax.annotate( 
        f'day {daynum}', (lon -ofs, 
            -33 if daynum in vakra 
            else -33 if daynum in invisible1
            else -33 if daynum in invisible2 
            else -40),
        fontsize=15, 
        color=
          'blue' if daynum in vakra else
          'red' if daynum in invisible1 else 
          'red' if daynum in invisible2 else 
           'black',
        va='center', ha= 'center' if daynum>0 else 'left', rotation=90)
    ax.set_xlabel("")
    ax.set_ylabel("")


    return ax

if __name__ == "__main__" :
  axx=plot_n83_rd_with_mars_overlay()
# axis.get_figure().savefig("../_info/fig4.png")

#%%

def get_fm_df():
  df = nmsu.get_full_moon_planet_pos()
  df = df[df.planet == 'Moon']
  df = df.reset_index().drop(['index' , 'geo_r', 'geoc_x', 'geoc_y', 'geoc_z' , 'planet'], axis=1)
# #year	mm	phase	lon	lat	ra	dec	sz
  df = df.assign (
    year = lambda x: x.date.apply( lambda e: int(re.sub("......T.*", "" , e)))
    , mm =  lambda x: x.date.apply( lambda e: int([x for x in e.split("-") if len(x) >0][1]))
    # , phase =  lambda x: x.jd.apply( lambda e: .99)
    , lon = lambda x: x.elong
    , lat = lambda x: x.elati
  
  ).drop( columns = ['elong', 'elati',])
  nu =  nsu.NaksUtils()
  ra_decl = df.apply(lambda x: nu.ll_to_rd(x.lat, x.lon), axis=1)
  df = df.assign (
    ra = ra_decl.apply(lambda x: x[2]),
    dec = ra_decl.apply(lambda x: x[3]),
    dist = lambda x: x.r,
    sz = lambda x: x.dist/x.dist.mean()
  )
  return df.drop( columns = ['r'])


# fm_df = get_fm_df()
# fm_df

#%%

def get_moon_31_df(jd=PP.JD_BCE_1000_JAN_1-500*365.25+4, ndays=31):
  df = nmsu.get_moon_for_one_month(jd,ndays)
  # df = df[df.planet == 'Moon']
  # df = df.reset_index().drop(['index' , 'geo_r', 'geoc_x', 'geoc_y', 'geoc_z' , 'planet'], axis=1)
# #year	mm	phase	lon	lat	ra	dec	sz
  df = df.assign (
    year = lambda x: x.date.apply( lambda e: int(re.sub("......T.*", "" , e)))
    , mm =  lambda x: x.date.apply( lambda e: int([x for x in e.split("-") if len(x) >0][1]))
    # , phase =  lambda x: x.jd.apply( lambda e: .99)
    , lon = lambda x: x.elong
    , lat = lambda x: x.elati
  
  ).drop( columns = ['elong', 'elati',])
  nu =  nsu.NaksUtils()
  ra_decl = df.apply(lambda x: nu.ll_to_rd(x.lat, x.lon), axis=1)
  df = df.assign (
    ra = ra_decl.apply(lambda x: x[2]),
    dec = ra_decl.apply(lambda x: x[3]),
    dist = lambda x: x.r,
    sz = lambda x: x.dist/x.dist.mean()
  )
  return df.drop( columns = ['r'])


if __name__ == "__main__" :
  get_moon_31_df()

#%%
def plot_n83_rd_with_moon_overlay(yrs=[-500]) :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')

  START_LON = 210 -210 +270
  nu = nsu.NaksUtils()
  def numof(n): return int(re.sub("\D","", n)); 
  # def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values() if '3' in x]
  n83a['ra_adj'] = n83a.ra - n83a.ra.min()
  n83a['lon'] = (n83a.lon-START_LON) % 360

  # yrs = [-500] if rni_only else [-1500,-500]
  for yr in  yrs :
    n83 = n83a[ n83a.year ==  yr]#[ ['gname', 'lon']]
    # ra_decl = n83.apply( lambda x : pd.Series(nu.ll_to_rd(x.lat, x.lon)[-2:]), axis=1)
    # ra_decl.columns = ['ra', 'decl']
    # n83.ra = ra_decl.ra.apply( lambda x: x + (360 if x < 0 else 0))
    # n83['decl'] = ra_decl.decl
    n83.ra = n83.ra.apply( lambda x: x + (360 if x < 0 else 0))
    n83['decl'] = n83['dec'] 
    n83a.to_csv("../datasets/n83~.tsv", float_format='%.2f')
    n83_copy = n83.copy()
    n83_copy['lon'] = n83_copy.lon + 360
    n83_copy['ra'] = n83_copy.ra + 360
    n83_copy['nid'] = n83_copy.nid.apply(lambda x: x +'_1')
    # n83 = n83.append(n83_copy)
    n83 = pd.concat([n83,n83_copy])
    # display(n83.shape, n83.head(), n83.tail())
    # return
    c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n83.nid ]
    # n27lbls  = [re.sub('N\d\d\-','', f'{k}:{v}') for k,v in n83.nid.value_counts().sort_index().items()]
    n27_mean = n83.groupby(by='nid').agg( {
      'lon': np.median, 
      'lat': np.median, 
      'ra': np.median, 
      'dec': np.median, 
      'nid': len
      }).rename( columns={'nid': 'cnt'} )
    n27_mean_lbls  = n27_mean.reset_index().sort_values(by=['lon']).apply( 
      lambda x: re.sub('N\d\d\-','', f'{x.nid}:{x.cnt}'), axis =1)
    n27_mean_lon  = n27_mean.reset_index().sort_values(by=['lon']).lon 
    n27_mean_lat  = n27_mean.reset_index().sort_values(by=['lon']).lat
    n27_mean_ra  = n27_mean.reset_index().sort_values(by=['ra']).ra 
    n27_mean_dec  = n27_mean.reset_index().sort_values(by=['ra']).dec
    if ( yr == -500 +10000): # 10k to mask the hack
      n83.at[403, 'lon'] = 359 # 408 UBha	उत्तराभाद्रपदा	γ Peg 4.512 => 359 for visual simplicity hack
    # display(n83.sort_values(by='lon').head())

    yspan = np.linspace(-60,40,11) 
    xspan = np.linspace(0,360*2,25)
    ax = n83.plot.scatter(x="lon", y="decl", c=c, 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 100), 
      # figsize=(60,10)
      figsize=(30,10)

    )
    
    # display(n83.head(43), n83.tail(43), n83.describe())

    if False : # maasa names
      loukika_maasa_lbls = "caitra vaiśākha jyeṣṭha āṣāḍha śrāvaṇa bhādra\npada āśvayuja kārtika mārga\nśira pauṣa māgha phālguna".split(" ")
      vedic_maasa_lbls =  "madhu mādhava śuci śukra nabhaḥ nabhasya iṣa ūrja sahas sahasya tapas tapasya".split(" ")
      loukika_maasa_lbls = loukika_maasa_lbls[8:] + loukika_maasa_lbls[:8]
      vedic_maasa_lbls  = vedic_maasa_lbls[8:] + vedic_maasa_lbls[:8]

      for lon, l , v in zip( np.linspace(0,360*2,2*12+1), loukika_maasa_lbls+loukika_maasa_lbls, vedic_maasa_lbls+vedic_maasa_lbls) :
        ax.plot( [ lon for x in yspan[:4]], [ x for x in yspan[:4]], linestyle="-", linewidth=0 )
        _yr = lon//360
        lon = (lon+15)%(360*2)
        # ax.annotate( v.upper() if _yr==0 else v.lower(), (30* lon//30, yspan[2:4].mean()-8 ), fontsize=20, color='blue' if _yr==0 else 'black', va='top', ha='center', rotation=0)
        # ax.annotate( l.upper() if _yr==0 else l.lower(), (30 *lon//30, yspan[2:4].mean()-12 ), fontsize=20, color='black' if _yr==0 else 'blue', va='top', ha='center', rotation=0)
        1

    # rtu_lbls = ['vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta', 'śiśira']
    # for rtu,l in zip((np.linspace(0,360*2,6*2+1)- START_LON) , rtu_lbls+rtu_lbls) :
    #   _yr = rtu//360
    #   rtu = (rtu+0)%(360*2)
    #   ax.plot( [ rtu-30 for x in yspan[-2:]+10], [ x for x in yspan[-2:]+10+5], linestyle="-", linewidth=4 )
    #   ax.plot( [ rtu+30 for x in yspan[-2:]+10], [ x for x in yspan[-2:]+10+5], linestyle="-", linewidth=4 )
    #   ax.annotate( l.upper() if _yr==0 else l.lower(), (rtu + 0*30, yspan[-2:].mean()+10+5 ), fontsize=20, color='black' if _yr==0 else 'blue', va='center', ha='center', rotation=0)


    ax.plot( [ x for x in xspan], [ 0 for x in xspan] )
    ax.annotate( 'longitude'.upper(), (-20, -50 ), fontsize=22, color='black', va='center', ha='left', rotation=0)
    ax.annotate( 'declination'.upper(), (-20, -40 ), fontsize=22, color='black', va='bottom', ha='center', rotation=90)
    # ax.set_title(f'VGJ - 83 Taras - 27 Nakshatras - Rtu - Ayana\n Longitude Latitude Plot for year {yr}', fontsize=30)
    ax.set_xticks( [ x for x in xspan] )
    # ax.set_xlabel( 'longitude', fontsize=20, rotation=0)
    ax.set_xlabel( '', fontsize=20, rotation=0)
    ax.set_xticklabels( 
        ["%0d°"%((x+START_LON)%360)  for x in (xspan)%360], 
        fontsize=20, 
        rotation=90)
    # return
    # ax.set_xticklabels( ["%0d°"% ((math.floor(x)+ START_LON)%360) for x in xspan], fontsize=25, rotation=0)
    ax.set_yticks( [ x for x in yspan] )
    ax.set_ylabel( '', fontsize=20, rotation=90)
    ax.set_yticklabels( ['%d°'%int(x) if -40 <=x <=80 else '' for x in yspan], fontsize=25, rotation=0)

    # return

    # for x, l  in zip( xspan[0:27] + (xspan[1]-xspan[0])/2 , n27lbls) :
    for x, y, l, n  in zip( n27_mean_lon, n27_mean_dec, n27_mean_lbls, range(n27_mean_lon.shape[0])) :
      # break
      xdelta = 0
      # ydelta = 0
      xdelta = -2 if 'Pus' in l else xdelta 
      xdelta = +2 if 'Asl' in l else xdelta
      xdelta = -3 if 'Chi' in l else xdelta 
      xdelta = +3 if 'Swa' in l else xdelta

      # ydelta = 0 if 'Ash' in l else ydelta
      # ydelta = 0 if 'Bha' in l else ydelta
      # ydelta = 0 if 'Kri' in l else ydelta
      # ydelta = 20 if 'Roh' in l else ydelta
      # ydelta = 20 if 'Mrg' in l else ydelta
      # ydelta = 20 if 'Ard' in l else ydelta
      # ydelta = 0 if 'Pun' in l else ydelta
      # ydelta = 5 if 'Pus' in l else ydelta
      # ydelta = 18 if 'Asl' in l else ydelta
      # ydelta = 0 if 'Mag' in l else ydelta
      # ydelta = -20 if 'PPal' in l else ydelta
      # ydelta = -20 if 'UPal' in l else ydelta
      # ydelta = 25 if 'Has' in l else ydelta
      # ydelta = +5 if 'Chi' in l else ydelta
      # ydelta = -20 if 'Swa' in l else ydelta
      # ydelta = 20 if 'Anu' in l else ydelta
      # ydelta = 20 if 'Mul' in l else ydelta
      # ydelta = 25 if 'PAsh' in l else ydelta
      # ydelta = 20 if 'UAsh' in l else ydelta
      # ydelta = -20 if 'Shr' in l else ydelta
      # ydelta = -20 if 'Dha' in l else ydelta
      # ydelta = 5 if 'Sha' in l else ydelta
      # ydelta = -20 if 'PBha' in l else ydelta
      # ydelta =  -10 if 'UBha' in l else ydelta
      # ydelta = -2 if 'Rev' in l else ydelta

      sname = "Kṛt Roh Mṛg Ārd Pun Puṣ Āśl Mag PPha UPha Has Cit Svā Viś Anū Jye Mūl PAṣā UAṣā Śra Śrv Śat PPro UPro Rev Aśv Bha".split(" ")
      ename = "Kri Roh Mrg Ard Pun PuS Asl Mag PPal UPal Has Chi Swa Vis Anu Jye Mul PAsh UAsh Śhr Dha Sha PBha UBha Rev Ash Bha".split(" ")

      _yr = n//27
      for e ,s in zip ( ename, sname) :
        l = l.replace(e,s)

      # l = l.replace("Dha:", 'Shrvst:')
      ax.plot( 
        [x, x], 
        [-50,50], 
        linestyle=":",
        color='purple' if _yr==0 else "magenta", alpha=0.2)

      l1 = re.sub("_1","",re.sub(":.*","",l))
      ax.annotate( 
        # f'{l1}:{x:.0f}°',
        re.sub("_1","",re.sub(":.*","",l)), 
        # (x + xdelta , y + (-1 if y<0 else 1 ) *10 + ydelta), 
        (x + 1*xdelta , -50+50+42 if n%2==0 else 42), 
        fontsize=20-20+13, color='purple' if _yr==0 else "magenta", 
        va='center', ha='center', rotation=90)


    smooth_fn = interp1d(n83.lon, n83.decl, kind='linear')
    smooth_x = np.arange(n83.lon.min(), n83.lon.max(), 1)
    smooth_y = smooth_fn(smooth_x)
    smooth_y1 = [x if x<=60 else 60 for x in smooth_y]
    smooth_y1 = [x if x>=-40 else -40 for x in smooth_y1]
    ax.plot( smooth_x, smooth_y1, linewidth=1, color='olive', linestyle=":")

    moon_overlay='phase'
    if moon_overlay=='phase'  :
      # moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      # moon_df = get_fm_df()
      moon_df = get_moon_31_df(PP.JD_BCE_1000_JAN_1+(1000+yr)*365.25,ndays=55)
      moon_df['ra_adj'] = [ 360+x if x<0 else x  for x in  moon_df.ra]
      moon_df= moon_df.assign( 
        lon1 = (moon_df.lon-moon_df.lon.iloc[0])%360, 
        ra_adj = moon_df.ra_adj+((moon_df.lon-moon_df.lon.iloc[0])%360).diff().fillna(1).apply(np.sign).diff().fillna(-2).apply(lambda x: 1 if x<0 else 0).cumsum().apply(lambda x: 360*(x-1)))#[['lon','lon1', 'lon2']].head(50) 
      moon_df = moon_df[moon_df.sz.diff() != 0] #drop noise
      for nmoon in range(0,1) :
        # m = moon_df[moon_df.year == moon_df.year.unique()[nmoon]] 
        # m = moon_df[moon_df.year == -1399] 
        m = moon_df[moon_df.year == yr] 
        m['cycle'] = (m.lon.values- m.lon.values[0])
        m.cycle = m.cycle.apply(lambda x: 1 if abs(x)<12.8 else 0) .cumsum()
        # m = m[m.cycle == 2]
        # display(m.cycle.sum(), m)
        smooth_fn = interp1d(m.ra_adj, m['dec'], kind='cubic')
        smooth_x = np.arange(m.ra_adj.min(), m['dec'].max(), 30)
        smooth_y = smooth_fn(smooth_x)

        ax.scatter( 
          x=m.ra_adj, y=m.dec, marker='$\odot$', 
          s=15*(m.phase)*np.sign(m.phase),
          c = m.paksha.apply(lambda x: 'black' if x=='krishna' else 'blue')
        )

    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_title(f'Moon Path - two nakshatra cycles - at {moon_df.year.iloc[0]}\n Blue is shukla paksha and black krishna', fontsize=30)


    return ax

if __name__ == "__main__" :
  axx=plot_n83_rd_with_moon_overlay()
# axis.get_figure().savefig("../_info/fig4.png")

#%%
def n83_drift_rate(n83a = None ):
  if n83a is None:
    n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")

  ans =[]
  # for n, _df in n83a[(n83a.gname == "ω1 Sco") | (n83a.gname  =="* 17 Tau")][['gname', 'lat', 'lon' , 'ra', 'dec']].groupby('gname') :
  for n, _df in n83a[['gname', 'lat', 'lon' , 'ra', 'dec']].groupby('gname') :
    # display(_df)
    _df = (_df.set_index('gname').diff()).dropna()#.applymap(lambda x: x)
    # display(_df, pd.DataFrame(stats.zscore(_df)))
    _df = _df[(np.abs(stats.zscore(_df)) < 2).all(axis=1)] # remove outliers
    ans.append(_df)
    # display(_df)
  drifts = pd.concat(ans).groupby('gname').mean()
  drifts.rename( columns = { c : f"{c}_drift_per_500_years"  for c in drifts.columns}, inplace=True)
  return drifts

# ans = n83_drift_rate()
# display(ans.sort_values(by =['gname']) , ans.describe())

#%%
def get_year_n83(yr=-2500, n83a=None, n83_drifts=None) :
  if n83a is None:
    n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")

  if n83_drifts is None:
    n83_drifts = n83_drift_rate(n83a)

  years = n83a.year.unique()
  if yr in years: return n83a[n83a.year == yr]
  min_year = n83a.year.min()
  min_jd = n83a.jd.min()
  delta = yr - min_year
  base_df = n83a[n83a.year == min_year]
  ans = base_df.assign(
    year = lambda x: yr
    , date = lambda x: f"{yr}-12-31T06:00:00"
    , jd = lambda x: min_jd + delta*365.25
    , lon = lambda x: x.lon + x.gname.apply(lambda y: n83_drifts.loc[y, 'lon_drift_per_500_years'])*delta/500
    , lat = lambda x: x.lat + x.gname.apply(lambda y: n83_drifts.loc[y, 'lat_drift_per_500_years'])*delta/500
    , ra = lambda x: x.ra + x.gname.apply(lambda y: n83_drifts.loc[y, 'ra_drift_per_500_years'])*delta/500
    , dec = lambda x: x.dec + x.gname.apply(lambda y: n83_drifts.loc[y, 'dec_drift_per_500_years'])*delta/500
  )

  return ans

def test_get_year_n83(yr=-2500):
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')
  n83_drifts = n83_drift_rate(n83a)
  return get_year_n83(yr, n83a, n83_drifts)

# test_get_year_n83(yr=-2570)

#%%

def plot_n83_rd(yrs=[-1500], moon_overlay='fullmoon') :
  n83a = pd.read_csv("../datasets/n83_lat_lon_ra_dec_bce2500_ce1000.tsv", sep="\t")
  n83_mag = pd.read_csv("../datasets/n83_mag.tsv", sep="\t")[['gname','mag']]
  n83a = pd.merge(n83a, n83_mag, on='gname', how='left')
  n83_drifts = n83_drift_rate(n83a)
  # n83a = pd.merge(n83a, n83_drifts, on='gname', how='left')

  def numof(n): return int(re.sub("\D","", n)); 
  # def clrof(n): z=numof(n); return((z%2)*z/cnt,((z+1)%2)*z/cnt,((z+2)%2)*z/cnt)
  mcolors = [ x for x in colors.XKCD_COLORS.values() if '3' in x]

  # for yr in  [-1500, -500] :
  for yr in  yrs :
    # n83 = n83a[ n83a.year ==  yr]#[ ['gname', 'lon']]
    n83 = get_year_n83(yr, n83a, n83_drifts)
    n83['ra_adj'] = [ 360+x if x<0 else x  for x in  n83.ra] 
    c=[ mcolors[numof(x)*66 % len(mcolors) ]for x in n83.nid ]
    # n27lbls  = [re.sub('N\d\d\-','', f'{k}:{v}') for k,v in n83.nid.value_counts().sort_index().items()]
    n27_mean = n83.groupby(by='nid').agg( {
      'lon': np.median, 
      'lat': np.median, 
      'ra_adj': np.median, 
      'dec': np.median, 
      'nid': len
      }).rename( columns={'nid': 'cnt', 'ra_adj': 'ra'} )
    n27_mean_lbls  = n27_mean.reset_index().sort_values(by=['ra']).apply( 
      lambda x: re.sub('N\d\d\-','', f'{x.nid}:{x.cnt}'), axis =1)
    n27_mean_lon  = n27_mean.reset_index().sort_values(by=['lon']).lon 
    n27_mean_lat  = n27_mean.reset_index().sort_values(by=['lon']).lat
    n27_mean_ra  = n27_mean.reset_index().sort_values(by=['ra']).ra 
    n27_mean_dec  = n27_mean.reset_index().sort_values(by=['ra']).dec 

    # yspan = np.linspace(-42,57,14) 
    yspan = np.linspace(-60,60,15) 
    xspan = np.linspace(0,360,28)
    ax = n83.plot.scatter(x="ra_adj", y="dec", c=c, 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 2.5**x.right), 
      # s=pd.cut(n83.mag.max()-n83.mag+1,5).apply(lambda x: 25*x.right), 
      figsize=(24,10))

    ayana_lbls = ['visuvat', 'd-ayana', 'visuvat', 'u-ayana']
    for ayana, l in zip( np.linspace(0,360,5), ayana_lbls) :
      ax.plot( [ ayana for x in yspan[:2]], [ x for x in yspan[:2]], linestyle="-", linewidth=4 )
      ax.annotate( l, (ayana, yspan[:2].mean() ), fontsize=20, color='black', va='center', ha='center', rotation=0)

    rtu_lbls = [ 'śiśira', 'vāsanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta',]
    for rtu,l in zip((np.linspace(0,360,7)+ 270) %360 , rtu_lbls) :
      ax.plot( [ rtu for x in yspan[-2:]], [ x for x in yspan[-2:]], linestyle="-.", linewidth=4 )
      ax.annotate( l, (rtu + 30, yspan[-2:].mean() ), fontsize=20, color='black', va='center', ha='center', rotation=0)


    ax.plot( [ x for x in xspan], [ 0 for x in xspan] )
    # ax.set_title(f'VGJ - 83 Taras - 27 Nakshatras\n RA Declination Plot for year {yr}', fontsize=30)
    ax.set_title(f'RA Declination Plot for year {yr}', fontsize=20)
    ax.set_xticks( [ x for x in xspan] )
    ax.set_xlabel( 'ra', fontsize=20, rotation=0)
    # ax.set_xticklabels( ['%.2f'%x for x in xspan], fontsize=20, rotation=90)
    ax.set_xticklabels( ["%02d°\n%02d'"% (math.floor(x), math.floor(60*(x-math.floor(x))) ) for x in xspan+ 0*n83a.ra.min()], fontsize=15, rotation=00)
    ax.set_yticks( [ x for x in yspan] )
    ax.set_ylabel( 'declination', fontsize=15, rotation=90)
    ax.set_yticklabels( ['%d'%int(x) for x in yspan], fontsize=20, rotation=0)
    # for x, l  in zip( xspan[0:27] + (xspan[1]-xspan[0])/2 , n27lbls) :
    for x, y, l, n  in zip( n27_mean_ra, n27_mean_dec, n27_mean_lbls, range(n27_mean_ra.shape[0])) :
      ax.annotate( l, (x, y + (-1 if yr<0 else 1 ) * (10 if abs(yr)<24 else -10) ), fontsize=20, color='purple', va='center', ha='center', rotation=90)

    ax.plot( n27_mean_ra, n27_mean_dec , linestyle=':')
    # n27_mean_lon[14] =  n27_mean_lon[14] + 10

    smooth_fn = interp1d(n27_mean_ra, n27_mean_dec, kind='cubic')
    smooth_x = np.arange(n27_mean_ra.min(), n27_mean_ra.max(), 1)
    smooth_y = smooth_fn(smooth_x)
    ax.plot( smooth_x, smooth_y, linewidth=2, color='olive')

    if moon_overlay=='fullmoon' : #or (yr == -1500) :
      # moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      moon_df = get_fm_df()
      # moon_df = get_moon_31_df(PP.JD_BCE_1000_JAN_1+(1000+yr)*365.25)
      moon_df['ra_adj'] = [ 360+x if x<0 else x  for x in  moon_df.ra] 
      moon_df = moon_df[moon_df.sz.diff() != 0] #drop noise
      for nmoon in range(0,1) :
        # m = moon_df[moon_df.year == moon_df.year.unique()[nmoon]] 
        # m = moon_df[moon_df.year == -1399] 
        m = moon_df[moon_df.year == yr] 
        smooth_fn = interp1d(m.ra_adj, m['dec'], kind='cubic')
        smooth_x = np.arange(m.ra_adj.min(), m['dec'].max(), 30)
        smooth_y = smooth_fn(smooth_x)
        # ax.plot( smooth_x, smooth_y, linewidth=0, color='gray', marker='$\odot$', markersize=30)
        # ax.plot( 
        #   m.ra_adj, m.dec, linewidth=0, color='gray', marker='.', 
        #   markersize=30
        # )
        ax.scatter( 
          x=m.ra_adj, y=m.dec, marker='$\odot$', 
          s=500 + 40000*(m.sz - m.sz.min()),
          c = c[15*nmoon%len(c)]
        )

    if moon_overlay=='phase'  :
      # moon_df = pd.read_csv("../datasets/full_moon_bce1500.tsv", sep="\t")
      # moon_df = get_fm_df()
      moon_df = get_moon_31_df(PP.JD_BCE_1000_JAN_1+(1000+yr)*365.25,ndays=35)
      moon_df['ra_adj'] = [ 360+x if x<0 else x  for x in  moon_df.ra] 
      moon_df = moon_df[moon_df.sz.diff() != 0] #drop noise
      for nmoon in range(0,1) :
        # m = moon_df[moon_df.year == moon_df.year.unique()[nmoon]] 
        # m = moon_df[moon_df.year == -1399] 
        m = moon_df[moon_df.year == yr] 
        m['cycle'] = (m.lon.values- m.lon.values[0])
        m.cycle = m.cycle.apply(lambda x: 1 if abs(x)<12.8 else 0) .cumsum()
        # m = m[m.cycle == 2]
        # display(m.cycle.sum(), m)
        smooth_fn = interp1d(m.ra_adj, m['dec'], kind='cubic')
        smooth_x = np.arange(m.ra_adj.min(), m['dec'].max(), 30)
        smooth_y = smooth_fn(smooth_x)

        ax.scatter( 
          x=m.ra_adj, y=m.dec, marker='$\odot$', 
          s=15*(m.phase)*np.sign(m.phase),
          c = m.paksha.apply(lambda x: 'black' if x=='krishna' else 'blue')
        )

    
 

    ax.grid(True)

if __name__ == '__main__' :
  plot_n83_rd(yrs=list(range( -500,-2000,-500)))
  plot_n83_rd(yrs=list(range( -500,-2100,-500)), moon_overlay='phase')


#%%
def fig1(): return plot_mbe2_83(n27Feb24, n27Feb24_abhyankar)
def fig2(): return plot_smooth_mbe2(n27Feb24_sensitivity, n27Feb24_abhyankar, tag="Sensitivity - Shr(β Del) Dha(β Aqr)")
def fig3(): return plot_n83_ll()  

def rni_paper_plots() :
  # ĀDITYACĀRA and ṚTUSVABHĀVA plots
  # plot_mbe2_83(n27Feb24) 
  fig1() ; fig2() ; fig3()
  # plot_mbe2_83(n27Feb24_abhyankar)
  # plot_smooth_mbe2(n27Feb24, "Base - Minima around 1200 BCE")
  # plot_smooth_mbe2(n27Feb24_sensitivity, "Sensitivity - Shr(β Del) Dha(β Aqr)- clip")

# if __name__ == '__main__' :
#   rni_paper_plots()

#%%
def all_plots() :
  print("Plots for Transit of sun through the seasonal nakṣatra cycle in the Vṛddha-Gārgīya Jyotiṣa")
  print("Indian Journal of History of Science, 56.3(2021)")
  rni_paper_plots(); plt.show()

  print("Other Plots")
  plot_n83_ll(yrs=[-1500])
  plot_n83_rd()
  do_bounded_plot(n27Feb24, "All 27")
  plot_vgj_seasons()
  print("End Other Plots")

#%%
n27Feb24 = None
n27Feb24_sensitivity = None
n27Feb24_abhyankar = None
naks_eq_bounds_report = None
m12 = None

def init_globals () :
  global n27Feb24
  global n27Feb24_sensitivity
  global n27Feb24_abhyankar
  global naks_eq_bounds_report
  global m12

  # This TSH has incorrect ASHadas .. no need to patch as below
  # patch Feb24 which had wrong ASH with Feb20 info which has correct ASH - from stell
  n27Feb24 = load_naks_data("../datasets/n27_base_Feb24_bce2500_to_ce0500.tsv")
  n27Feb24 = naks_lon_err(n27Feb24)
  n27Feb20_delta  = load_naks_data("../datasets/n27_delta_Feb20_bce2500_to_ce0500.tsv")
  n27Feb20_delta = naks_lon_err(n27Feb20_delta)
  ash_patch = n27Feb20_delta[ [('20' in x) or ('21' in x) for x in n27Feb20_delta.nid ]]
  n27Feb24_nonash = n27Feb24[ [not(('20' in x) or ('21' in x)) for x in n27Feb24.nid ]]
  n27Feb24Patched = pd.concat( [n27Feb24_nonash, ash_patch])
  n27Feb24 = n27Feb24Patched.sort_values(['nid', 'year'])

  # Generate table for the IJHS paoer
  naks_eq_bounds_report = make_naks_bounds_report(n27Feb24)
  # naks_eq_bounds_report.to_csv("../datasets/naks_eq_bounds_report.csv", index=None)
  # naks_eq_bounds_report

  # patch Shr and Dha for sensitivity plots
  n27Feb24_shr_dha_delta  = load_naks_data("../datasets/n27_delta_shr_dha_bce2500_to_ce0500.tsv")
  n27Feb24_shr_dha_delta = naks_lon_err(n27Feb24_shr_dha_delta )
  n27Feb24_non_shr_dha = n27Feb24[ [not(('Shr' in x) or ('Dha' in x)) for x in n27Feb24.nid ]]
  n27Feb24_sensitivity = pd.concat([ n27Feb24_non_shr_dha, n27Feb24_shr_dha_delta])
  n27Feb24_sensitivity = n27Feb24_sensitivity.sort_values(['nid', 'year'])

  # n27Feb24zoom = load_naks_data("../datasets/n27_base_Feb24_bce1400_to_bce0900_zoom.tsv")
  # n27Feb24zoom = naks_lon_err(n27Feb24zoom)

  m12 = load_naks_data("../datasets/m12_base_mar20_bce2500_to_ce0500.tsv")
  n27Feb24_abhyankar_delta = load_naks_data("../datasets/n27_delta_abhyankar_bce2500_to_ce0500.tsv")
  n27Feb24_abhyankar_delta = naks_lon_err(n27Feb24_abhyankar_delta)
  n27Feb24_non_abhyankar = n27Feb24[ [not(
    ('Mag' in x) or ('Has' in x) or ('Jye' in x) or ('Mul' in x) 
    or ('PAsh' in x) or ('UAsh' in x) or ('Shr' in x) or ('Dha' in x)
    or ('Sha' in x) or ('Rev' in x)
    ) for x in n27Feb24.nid ]]
  n27Feb24_abhyankar = pd.concat([ n27Feb24_non_abhyankar, n27Feb24_shr_dha_delta, n27Feb24_abhyankar_delta])
  n27Feb24_abhyankar = n27Feb24_abhyankar.sort_values(['nid', 'year'])

# %%
#### NON CORE STUFF

def spot_check():
  rni = n27Feb24[ 
    ( n27Feb24.year < 10000) 
    # (n27Feb24.gname == 'β Del') & (n27Feb24.err_lon_bounds_eq < 2) 
    # (n27Feb24.nid == 'N23-Dha') & (n27Feb24.err_lon_bounds_eq < 2)
    # (n27Feb24.err_lon_bounds_eq < 2)
    #(abs(n27Feb24.lon - 270) < 1)
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])

  sens = n27Feb24_sensitivity [ 
    ( n27Feb24_sensitivity.year < 10000) 
    # (n27Feb24_sensitivity.gname == 'β Del') & (n27Feb24_sensitivity.err_lon_bounds_eq < 2) 
    # (n27Feb24_sensitivity.nid == 'N23-Dha') & (n27Feb24_sensitivity.err_lon_bounds_eq < 2) 
    # (n27Feb24_sensitivity.err_lon_bounds_eq < 2) 
    # (abs (n27Feb24_sensitivity.lon -270) < 1)
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])


  abh = n27Feb24_abhyankar [ 
    ( n27Feb24_abhyankar.year < 10000) 
    # (n27Feb24_sensitivity.gname == 'β Del') & (n27Feb24_sensitivity.err_lon_bounds_eq < 2) 
    # (n27Feb24_abhyankar.nid == 'N23-Dha') & (n27Feb24_abhyankar.err_lon_bounds_eq < 2) 
    # (n27Feb24_abhyankar.err_lon_bounds_eq < 2) 
    # (abs(n27Feb24_abhyankar.lon - 270) <1)
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])

  ans = sens.sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(
  ) + sens[sens.nid.apply(lambda x: bool(re.match("^.*(2\d).*$",str(x))))].sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(  
  ) + rni.sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(
  ) + rni[rni.nid.apply(lambda x: bool(re.match("^.*(2\d).*$",str(x))))].sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(  
  ) + abh.sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(
  ) + abh[abh.nid.apply(lambda x: bool(re.match("^.*(2\d).*$",str(x))))].sample(10).sort_values(['nid','gname','year']).apply(lambda x: x.tolist(), axis=1).tolist(  
  )
  
  naks_divisions  = n27_lon_divisions[['r_eq', 'l_eq', 'r_eq1', 'l_eq1']].rename(
    columns={'r_eq':'Ādityacāra_lo', 'l_eq':'Ādityacāra_hi', 'r_eq1':'Ṛtusvabhāva_lo', 'l_eq1':'Ṛtusvabhāva_hi'}
  )

  proxy_stars = pd.merge (
    pd.merge (
    rni[['nid', 'gname']].drop_duplicates(), #.set_index('nid'),
    sens[['nid', 'gname']].drop_duplicates(), #.set_index('nid'), 
    how='left', on='nid'
  ),
    abh[['nid', 'gname']].drop_duplicates(), #.set_index('nid'),
    how='left', on='nid'
  ).rename(columns={'gname_x':'rni_proxy', 'gname_y':'sens_proxy', 'gname':'abh_yoga'})

  display (
    "Naks Span", naks_divisions,
    "================",
    "ProxyStars", proxy_stars , 
    "================",
    "Seasonal 9", bright9Naks , 
    )

def _verify_plot(rni,abh,sens, seasonal=[]):
  if seasonal :
    # print ( "Seasonal", len(seasonal), seasonal )
    rni = rni[ [n in seasonal for n in rni.nid] ]
    abh = abh[ [n in seasonal for n in abh.nid] ]
    sens = sens[ [n in seasonal for n in sens.nid] ]

  pvt=pd.pivot_table(rni, 
    index=['nid'], 
    columns=['year'], 
    values='err_lon_bounds_eq', 
    aggfunc=np.mean).T
  ax=pvt.apply(np.mean , axis=1).plot(
    figsize=(6,2), 
    lw=1 if len(seasonal)!=9 else 4,
    ls=':' if len(seasonal)!=9 else '-.',
    
    #color='pink' if len(seasonal)!=9 else 'blue',
    #legend=None
    )

  # pvt=pd.pivot_table(abh, 
  #   index=['nid'], 
  #   columns=['year'], 
  #   values='err_lon_bounds_eq', 
  #   aggfunc=np.mean).T
  # ax=pvt.apply( np.mean , axis=1).plot( 
  #   color='red', ax=ax)

  # pvt=pd.pivot_table(sens, 
  #   index=['nid'], 
  #   columns=['year'], 
  #   values='err_lon_bounds_eq', 
  #   aggfunc=np.mean).T
  # ax=pvt.apply( np.mean , axis=1).plot( 
  #   color='orange', ax=ax) 
  ax.set_title(
    f"{ 'Seasonal' if seasonal else ''} Adityachara Error\n{seasonal if seasonal else 'All 27'} \n Individual-dotted  All9-thick",
    fontsize=8
  )
  #plt.show()

def verify_plot():
  rni = n27Feb24[ 
    ( n27Feb24.year < 10000) 
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])

  sens = n27Feb24_sensitivity [ 
    ( n27Feb24_sensitivity.year < 10000) 
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])

  abh = n27Feb24_abhyankar [ 
    ( n27Feb24_abhyankar.year < 10000) 
    ][
      ['nid','gname', 'year', 'lon', 'err_lon_bounds_eq']
      ].sort_values(['nid', 'year'])
  for ss in range(1,9):
    naks_9 = rni[['nid']].drop_duplicates().sample(9).sort_values(['nid'])['nid'].tolist()
    for ss in range(1,9):
      _verify_plot(rni,abh,sens, seasonal=naks_9[ss-1:ss])
    _verify_plot(rni,abh,sens, seasonal=naks_9[:])
    plt.show()

# %%
if __name__ == "__main__":
  init_globals()
  all_plots()
  print ("****************************************************")
  spot_check()
  print ("****************************************************")
  verify_plot()

# %%
def plot_naks_dial () :
  fig, ax = plt.subplots(subplot_kw={'projection': 'polar'},figsize=(10,10))
  ax.set_theta_zero_location('S', offset=0)#-1*int(360/27))

  ax.set_theta_direction(-1)

  angles = [ (360/366)*x/100 for x in range(0+100, 36600, int(36600/27)) ]
  # ax.set_rlabel_position(-32.5)  # Move radial labels away from plotted line
  lines, labels = plt.thetagrids(angles, [f"{x:.0f}" for x in angles], fontweight= 'bold' , fontsize=10, color='gray') 
  # draw radial lines from 2 units of origin to 20 units of origin
  # pd.DataFrame( {'a': (angles-6.5)*np.pi/180  , 'lbl': naks_cnt_lbl }).apply( 
  #   lambda x : ax.text(x.a, 9.7, x.lbl if not bare_template else '', fontsize=10, ha='center', va='center', alpha=.8),
  #   axis=1
  # )

  ax.set_rgrids(np.arange(10, 20, 12))
  ax.grid(True)
  return

if __name__ == "__main__":
  plot_naks_dial()
#%%
#%%
def zzz_plot_n83_rd_with_moon_overlay(yr=-1500, bare_template=False, season_gap=False) :
  # angles = np.linspace(0,359.99,num=54)
  # cidx = np.roll(np.array([ math.floor(x/(4.5*360/27)) for x in angles]),-1)
  colors = ['red','blue','green','purple', 'olive', 'magenta' ,'orange',] #['gray','brown','cyan']

  ix =0
  for naks, _df in n83_df_bce.groupby( 'nid' ) : 
    _df = _df.copy().sort_values(['year', 'lon', 'lat'])
    if bare_template: break
    ax.scatter( 
    # [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').min().lon if 'N02-Bha'==naks else  _df.groupby('gname').mean().lon )], 
      [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').lon.apply(smart_mean) )], 
      [6.1 + x/20 for x in _df.groupby('gname').mean().lat],
      s=150 ,#if 'Ash' in naks else 60, 
      # marker=f'${naks[4:6]}:{(_df.lon.median() if "N02-Bha"==naks else _df.lon.median() ):.0f}°$',
      alpha=0.5, zorder=2,
      c=colors[ix%len(colors)],
    )

  # for naks, _df in n83_df_bce.groupby( 'nid' ) : 
    # if naks not in ['N25-PBha', 'N26-UBha'] : continue
    # display (_df)
    ax.scatter( 
      # [ (x+13.33*1.4)*np.pi/180 for x in _df.groupby('gname').mean().lon], 
  # [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').min().lon if 'N02-Bha'==naks else  _df.groupby('gname').mean().lon )][0:1], 
      [ (x+13.33*1.6*0)*np.pi/180 for x in ( _df.groupby('gname').lon.apply(smart_mean) )][0:1], 
      # [7.3 + 0*x/20 for x in _df.groupby('gname').mean().lat][0:1],
      [7.3 - (3 if ('Asl' in naks)else 2 if ('Chi' in naks) else 1.5 if ('Bha' in naks)  else .5 if ('Shr' in naks) else 0)][0:1],
      s=2600, #if 'Ash' in naks else 100, 
      # marker=f'${naks[4:6]}:{(_df.lon.median() if "N02-Bha"==naks else _df.lon.median() ):.0f}°$',
      marker=f'${naks[4:6]}:{smart_mean(_df.groupby("gname").lon.apply(smart_mean) ):.0f}°$',
      # marker=f'${naks[4:6]}:{(_df.lon.median() ):.0f}°$',
      alpha=1, zorder=1,
      c=colors[ix%len(colors)],
    )
    # if ( 'N01-Ash' in naks) : print (f'{yr:4.0f} {naks} :   {smart_mean(_df.groupby("gname").lon.apply(smart_mean) )} {_df.lon.to_list()}')
    ix+=1

  # for f,m in zip(range(0,6), list('o*^pds')) :
  #   ang=angles[cidx==f]
  #   cdx=cidx[cidx==f]

  #   c = ax.scatter(
  #     [x*np.pi/180 for x in ang], 
  #     [3+f%2 for x in ang], 
  #     c=[f for x in cdx], 
  #     s=[50*(1+0*f%2 ) + 0*25*cdx for x in ang], 
  #     cmap='rainbow', 
  #     marker=m,
  #     alpha=0.75)

  ax.set_rticks([8], labels=[''] )  # Less radial ticks

  delta = np.pi/27
  seasons = [ 'śiśira', 'vasanta', 'grīṣma',  'varṣā', 'śarat', 'hemanta',]
  season_colors = [ 'cyan', 'red', 'green', 'orange', 'blue', 'maroon',]
  for s in range(-1,5) :
    S = 2*np.pi/6 
    L = 8
    _angles = [ x-1*delta*0 for x in [s*S, s*S, (s*S+S)] ]
    # print([ x*180/np.pi for x in _angles])
    if season_gap:
      if s==0 : _angles[2] = _angles[2] - delta/4 # रोहिण्यन्तानि
      if s==1 : _angles[1] = _angles[1] + delta/4 # सौम्याद्यानि

      if s==2 : _angles[2] = _angles[2] - delta/4 # सावित्रान्तानि
      if s==3 : _angles[1] = _angles[1] + delta/4 # चित्रादीन्य

      if s==4 : _angles[2] = _angles[2] - delta/4 # वैष्णवान्तानि
      if s==-1 : _angles[1] = _angles[1] + delta/4 # श्रविष्ठादीनि

    _vertex = [0,L,L]
    _angles = [ x-4.5*delta for x in _angles]
    if True or not bare_template:
      ax.plot(_angles, _vertex, 'b', lw=0, alpha=.2)
      ax.fill(_angles, _vertex,  alpha=.1, color=season_colors[s%len(season_colors)]) 
    if (s > -2 ) :
      season = seasons[(s+1)%len(seasons)]
      # print([ x*180/np.pi for x in _angles], season)
      L=len(season)
      if not bare_template:
        ax.text(_angles[1] + 2.7/L, L*.72 ,season , fontsize=12, ha='center', va='center')

    # four solar quarters 
    for i in range(4) : ax.plot([0, 90*i*np.pi/180], [0, 7.9], 'maroon', lw=1, alpha=.2)

    # 10 day ticks
    if day_ticks:
      for i in range(0+1, 367+1,1) :
        a = (i-1)*2*(np.pi/366) + np.pi
        a += 1.5*np.pi
        ax.plot([a, a], [8, 8.5 if i%10 else 8.8  ], 'gray' if ((i%10) or (i==1)) else 'red', lw=1, alpha=.1 if i%5 else .3)
        if i==1 : 
          # ax.text(a, 8.9, f'{i}\n(367)', fontsize=9, ha='center', va='center', alpha=.5)
          ax.text(a, 8.9, f'{i}', fontsize=9, ha='center', va='center', alpha=.5)
        if i%10 == 0 : 
          ax.text(a, 8.9, f'{i}', fontsize=9, ha='center', va='center', alpha=.5)
        

    # # 10 day ticks
    # if day_ticks:
    #   for i in range(0, 366,1) :
    #     a = i*2*np.pi/365
    #     ax.plot([a, a], [8, 8.5 if i%10 else 8.8 ], 'gray' if i%10 else 'red', lw=1, alpha=.1 if i%5 else .3)
    #     if i%10 == 0 : 
    #       ax.text(a, 8.9, f' {1+(i//10)*10}', fontsize=9, ha='center', va='center', alpha=.5)

  title =  f"Year {n83_df_agg.year.values.mean():.0f}" if not title else title
  # title =  f"Year {yr:.0f}" if not title else title
  ax.set_title(title, y=1.05, fontdict={'fontweight':'bold', 'fontsize':16, 'color':'gray'})
  ax.set_facecolor('white')
  # save the figure as a png
  if savefig :
    # fn = f"./images/naks{-366 if day_ticks else ''}-chakra-{yrnum:02d}-{yr:04.0f}.png"
    # fn = f"./images/naks-366/ticks-{yrnum:02d}-{yr:04.0f}.png" if day_ticks else f"./images/naks-366/noticks-{yrnum:02d}-{yr:04.0f}.png"
    fn = f"./images/naks-366/ticks-{yrnum:02d}-{yr:04.0f}.jpg" if day_ticks else f"./images/naks-366/noticks-{yrnum:02d}-{yr:04.0f}.jpg"
    print(f"Saving {fn}")
    plt.savefig(fn)


# %%
