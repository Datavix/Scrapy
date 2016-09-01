import pandas as pd
import json
import codecs

with open('20160823_mp_result_utf8.jl') as f:
	data = pd.DataFrame(json.loads(line, strict=False) for line in f)
