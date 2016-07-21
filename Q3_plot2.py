from bokeh.charts import Bar, show, output_file, defaults
from bokeh.charts.attributes import CatAttr
from bokeh.models import PrintfTickFormatter
from bokeh.models.widgets import Panel, Tabs
import pandas as pd
import numpy as np

loan_defs = pd.read_excel("data/peps300.xlsx")
output_file("chart_2.html", title="Student Loan Defaults")

#pre-processing the data

programme_length_cats={
    0: "0-Short-Term (300-599 hours)",
    1: "1-Graduate/Professional (>= 300 hours)",
    2: "2-Non-Degree (600-899 hours)",
    3:"3-Non-Degree 1 Year (900-1799 hours)",
    4:"4-Non-Degree 2 Years (1800-2699 hours)",
    5:"5-Associate's Degree",
    6:"6-Bachelor's Degree",
    7:"7-First Professional Degree",
    8:"8-Master's Degree or Doctor's Degree",
    9:'9-Professional Certification',
    10:'10-Undergraduate (Previous Degree Required)',
    11:'11- Non-Degree 3 Plus Years (>= 2700 hours)',
    12:'12-Two-Year Transfer'
}

sch_type_cats={
    1: '1-Public',
    2: '2-Private, Nonprofit',
    3: '3-Proprietary',
    5: '5-Foreign Public',
    6: '6-Foreign Private',
    7: '7-Foreign For-Profit'
}

ethnic_code_cats={
    1:'1-Native American',
    2:'2-HBCU',
    3:'3-Hispanic',
    4:'4-Traditionally Black College',
    5:'5-Ethnicity Not Reported'
}

loan_defs.fillna(value=0, inplace=True)
loan_defs["Program Length"]=loan_defs["Program Length"].map(programme_length_cats)
loan_defs["Program Length"]=loan_defs["Program Length"].astype('category')

loan_defs["Sch Type"]=loan_defs["Sch Type"].map(sch_type_cats)
loan_defs["Sch Type"]=loan_defs["Sch Type"].astype('category')

loan_defs["Ethnic Code"]=loan_defs["Ethnic Code"].map(ethnic_code_cats)
loan_defs["Ethnic Code"]=loan_defs["Ethnic Code"].astype('category')

tbl1=pd.melt(loan_defs, id_vars='OPEID', value_vars=['Year 1', 'Year 2', 'Year 3'], value_name="Year")
tbl2=pd.melt(loan_defs, id_vars='OPEID', value_vars=['Num 1', 'Num 2', 'Num 3'], value_name="Numerator")
tbl3=pd.melt(loan_defs, id_vars='OPEID', value_vars=['Denom 1', 'Denom 2', 'Denom 3'], value_name="Denominator")

tbl1['Numerator']=tbl2['Numerator']
tbl1['Denominator']=tbl3['Denominator']

final_tbl=tbl1.merge(loan_defs.loc[:,['OPEID', 'Name', 'Address','City','State','Zip Code','Zip Ext','Program Length','Sch Type', 'Ethnic Code']], on='OPEID')


defaults.width=1000
defaults.height=800

#plot grid by different parameters
df=final_tbl.groupby(['Program Length']).sum()
df=df.reindex(programme_length_cats.values()).fillna(value=0)
p1=Bar(df, values='Numerator', title='Student Defaults by Program Length', legend=None, label=CatAttr(sort=False))
p1.xaxis.major_label_orientation=np.pi/2
p1.xaxis.axis_label="Program Length"
p1.yaxis.axis_label="Total Defaults"
p1.yaxis[0].formatter = PrintfTickFormatter(format="%d")
tab1=Panel(child=p1, title="by Program Length")

df=final_tbl.groupby(['Sch Type']).sum()
df=df.reindex(sch_type_cats.values()).fillna(value=0)
p2=Bar(df, values='Numerator', title='Student Defaults by Scheme Type', legend=None, label=CatAttr(sort=False))
p2.xaxis.major_label_orientation=np.pi/2
p2.xaxis.axis_label="Scheme"
p2.yaxis.axis_label="Total Defaults"
p2.yaxis[0].formatter = PrintfTickFormatter(format="%d")
tab2=Panel(child=p2, title="by Scheme Type")

df=final_tbl.groupby(['Ethnic Code']).sum()
df=df.reindex(ethnic_code_cats.values()).fillna(value=0)
p3=Bar(df, values='Numerator', title='Student Defaults by Ethnic Code', legend=None, label=CatAttr(sort=False))
p3.xaxis.major_label_orientation=np.pi/2
p3.xaxis.axis_label="Ethnic Code"
p3.yaxis.axis_label="Total Defaults"
p3.yaxis[0].formatter = PrintfTickFormatter(format="%d")
tab3=Panel(child=p3, title="by Ethnic Code")

tabs=Tabs(tabs=[tab1,tab2, tab3])

show(tabs)

