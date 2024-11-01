import ipdb


db = ipdb.City(r'C:\Users\hxm\Downloads\ipipfreedb\ipipfree.ipdb')

print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())
print(db.find("1.12.13.255", "CN"))
print(db.find_map("1.12.13.255", "CN"))
print(db.find_info("1.12.13.255", "CN").country_name)

