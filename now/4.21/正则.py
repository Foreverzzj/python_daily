import re
#
# s = '''<div class='西游记'><span id='10010'>中国联通</span></div>'''
# obj = re.compile(r'(\d+)\'>(.*?)</span>')
# for one in obj.findall(s):
#     print(one)
# # print(obj.findall(s))

s = '''<div class='西游记'><span id='10010'>中国联通</span></div>'''
obj = re.compile(r'')
for one in obj.finditer(s):
    print(one.group())
