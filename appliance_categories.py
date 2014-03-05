#!/usr/bin/env python

"""
Produces a CSV file with these columns:

    ApplianceCode,ApplianceName,GroupCode,GroupName
    0,upright freezer 1,1001,Cold appliances
    1,upright freezer 2,1001,Cold appliances
    ...

Removes all rows with NaNs.

Usage
-----
Alter the PATH constant and then run it!
"""

import pandas as pd
from os.path import join

PATH = '/data/HES_cleaned'

appliances = pd.read_csv(join(PATH, 'appliance_codes.csv'), 
                         index_col=0, header=0,
                         names=['ApplianceCode', 'ApplianceName'])

map_appliance_code_to_group_code = pd.read_csv(join(PATH, 'appliance_types.csv'),
                                               index_col=0, header=0,
                                               names=['ApplianceCode', 'GroupCode'])


groups = pd.read_csv(join(PATH, 'appliance_type_codes.csv'), 
                     index_col=0, header=0,
                     names=['GroupCode', 'GroupName'])

joined = appliances.join(map_appliance_code_to_group_code).join(groups, on='GroupCode')
joined = joined.dropna()
joined['GroupCode'] = joined['GroupCode'].astype(int)
joined.to_csv(join(PATH, 'appliance_names_with_group_names.csv'))

print "done!"
