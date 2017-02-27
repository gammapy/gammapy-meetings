"""
Dump Fermi-LAT 3FHL catalog as example CSV file
"""
from astropy.table import Table

url = 'https://fermi.gsfc.nasa.gov/ssc/data/access/lat/3FHL/gll_psch_v11.fit.gz'
table = Table.read(url)
table.sort('Signif_Avg')

cols = ['Source_Name', 'CLASS', 'ASSOC1', 'GLON', 'GLAT', 'Signif_Avg', 'Flux']
table2 = table[cols][:10]

table2.write('fermi_3fhl.csv', format='ascii.csv')
