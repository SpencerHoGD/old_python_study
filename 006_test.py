from datetime import datetime

import pandas as pd

FILENAME1 = "/home/hxm/test/2024_Q1th.md"
FILENAME2 = "/home/hxm/test/2024_Q2nd.md"
FILENAME3 = "/home/hxm/test/2024_Q3rd.md"
FILENAME4 = "/home/hxm/test/2024_Q4th.md"
dates = pd.date_range(start="20240901", end="20241231", freq="D")
now = datetime.now()

# print(
#     "["
#     + now.strftime("%d")
#     + "]"
#     + "("
#     + now.strftime("%Y/%m/%d %a")
#     + " day="
#     + now.strftime("%j")
#     + " week="
#     + now.strftime("%W")
#     + ")"
# )

# print('## ' + now.strftime('%a %b %d %H:%m'))
print(
    "## "
    + now.strftime("%Y/%m/%d %a")
    + " day="
    + now.strftime("%j")
    + " week="
    + now.strftime("%W")
)

with open(FILENAME4, "w", encoding="utf-8") as f:
    for date in dates:
        f.write(
            "## "
            + date.strftime("%Y/%m/%d %a")
            + ". day"
            + date.strftime("%j")
            + " week"
            + date.strftime("%W")
            + "\n"
        )
