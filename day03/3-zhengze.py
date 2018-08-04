import re
string = "<div><div>天青色等烟雨，天青色等烟雨</div></div>"

pattern = re.compile(r'<div>.*</div>')
pattern_1 = re.compile(r'<div>.*?</div>')
res = pattern.search(string).group()
res1 = pattern_1.search(string).group()
# print(res)  <div><div>天青色等烟雨，天青色等烟雨</div></div>

# *? 混用 非贪婪

# print(res1) <div><div>天青色等烟雨，天青色等烟雨</div>
