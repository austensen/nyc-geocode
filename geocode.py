import pandas as pd
import multiprocessing
import functools
import sys

from lib.geocode_record import geocode_record

input_csv = sys.argv[1]
output_csv = sys.argv[2]
addr_col = sys.argv[3]
if sys.argv[4:] == []:
    keep_cols = [addr_col]
elif sys.argv[4:] == ['*']:
    keep_cols = lambda x: x
else:
    keep_cols = sys.argv[3:]

df = pd.read_csv(
    input_csv, 
    dtype = str,
    index_col = False, 
    usecols=keep_cols,
    keep_default_na=False
)

records = df.to_dict('records')

with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
    it = pool.map(functools.partial(geocode_record, addr_col=addr_col), records, 10000)

pd.DataFrame(it).to_csv(output_csv, index=False)
