import os
import urllib

# List of files to download e.g. (url, csv_name).
download = [
    ('https://raw.githubusercontent.com/opennepal/odp-health/master/Morbidity%20caused%20by%20mental%20problem%20(2009-10%20to%202013-14)/data.csv', 'mentalhealth.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-health/master/Communicable%20disease%20patients%20%20(HIV-AIDS%2CLeprosy%2CMeningitis)%20(2009-10%20to%202013-14)/data.csv', 'communicabledisease1.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-health/master/District%20wise%20Communicable%20and%20Immunizable%20diseases%2C%20(2008-09%20A.D%20-%202012-13%20A.D)/data.csv', 'communicabledisease2.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-health/master/District%20wise%20vaccinated%20number%20of%20children%20and%20women%20(2009-10%20to%202013-14)/data.csv', 'vaccinations.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-census/master/Population%20by%20caste_ethnic%20groups%20and%20sex/data.csv', 'caste.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-census/master/District%20wise%20Sex%20Ratio%20(male%20per%20100%20female%20)%2C%202011/data.csv', 'sexratio.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-poverty/master/Poverty%20Rates%20on%20District%20Level%2C%202001-2011/data.csv', 'poverty1.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-poverty/master/Human%20Poverty%20Index%20Value%20by%20Districts%20(2011)/data.csv', 'poverty2.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-development/master/District%20wise%20Human%20Development%20Index%20(2011)/data.csv', 'hdi2011.csv'),
    ('https://raw.githubusercontent.com/opennepal/odp-water-and-sanitation/master/District%20Coverage%20of%20Water%20Supply%20and%20Sanitation%20%20(2011)/data.csv', 'watersanitaion.csv'),
    
]

# Makes data directory if it doesn't exist.
if not os.path.exists('Data/'):
    os.makedirs('Data/')

# Writes csvs to data directory if they don't exist.
for i in download:
    url, name = i
    if name not in os.listdir('Data/'):
        csv = urllib.urlopen(url).read()
        with open('Data/' + name, 'w') as data:
            data.write(csv)
