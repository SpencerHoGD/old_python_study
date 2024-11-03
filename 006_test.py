import pathlib
from datetime import datetime

import pandas as pd

PATH = "/home/hxm/test/mds"

pathlib.Path(PATH).mkdir(exist_ok=True)


FILENAME4 = "/home/hxm/test/2024_Q4th.md"

monthes = pd.date_range(start="20240101", end="20241231", freq="M")
dates = pd.date_range(start="20240101", end="20241231", freq="D")
now = datetime.now()

# print('## ' + now.strftime('%a %b %d %H:%m'))
# print(
#     "## "
#     + now.strftime("%Y/%m/%d %a")
#     + " day="
#     + now.strftime("%j")
#     + " week="
#     + now.strftime("%W")
# )

for month in monthes:
    print(month)

#     with open(f"{PATH}/{month}.md", "w", encoding="utf-8") as fp:
#         fp.write(f"hello, pathlib {month}")
#
# with open(FILENAME4, "w", encoding="utf-8") as f:
#     for date in dates:
#         f.write(
#             "## "
#             + date.strftime("%Y/%m/%d %a")
#             + ". day"
#             + date.strftime("%j")
#             + " week"
#             + date.strftime("%W")
#             + "\n"
#             + "\n"
#             + "\n"
#             + "\n"
#         )
