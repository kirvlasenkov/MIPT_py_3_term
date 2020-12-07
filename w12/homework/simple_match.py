#!/usr/bin/env python3
import re

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = r'ab?'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r'\w{3}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'sofia\.mp[34]{1}$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'\w+[^r]\b'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'(a|b){3}$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r'(\w\w){3}\b'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'\w{3}\s\w{3}\s\w{3}'
"""
It's not obvious how to realize it by using groups,
as group "compile", when it's mentioned  for the first time
"""

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'^a(.|-)?b\1?c\1?[0 2-9]*$'
print(re.match(REGEXP_8, 'a.b.c.1'))
