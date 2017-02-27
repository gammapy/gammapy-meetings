"""Example for exercises.

Read Fermi-LAT 3FHL catalog subset from CSV file
(just the 10 most significant sources)
"""
def read_fermi_3fhl():
    """Read CSV file, return list of dicts."""
    with open('fermi_3fhl.csv') as fh:
        lines = fh.readlines()
    colnames = lines[0].strip().split(',')
    data = []
    for line in lines[1:]:
        parts = line.strip().split(',')
        row = dict(zip(colnames, parts))
        for name in ['Flux', 'GLON', 'GLAT', 'Signif_Avg']:
            row[name] = float(row[name])
        data.append(row)
    return data

fermi_3fhl = read_fermi_3fhl()

# What is the 3rd most significant source?
# What is the lowest GLAT source?
# What is the brightest source?
# How many different source classes are there?
# What is the total flux of all pulsars?
