# output of %%cargo_license_summary here
s=''''''.replace('#','').split('\n')
from license_expression import get_spdx_licensing
import operator
import functools
licensing = get_spdx_licensing()

res = functools.reduce( operator.and_, [licensing.parse(i) for i in s])
print(str(res.simplify()))
