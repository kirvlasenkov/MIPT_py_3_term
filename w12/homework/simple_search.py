#!/usr/bin/env python3
import re


# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно найти подстроку, а следом
# после стрелки (--->) указана сама искомая подстрока

# bab ---> a
# bcb ---> c
# bxb ---> x
str_1 = 'bab'
str_2 = 'bcb'
str_3 = 'bxb'


REGEXP_1 = r'[^b]'
print(f'for {str_1}:', re.search(REGEXP_1, str_1))
print(f'for {str_2}:', re.search(REGEXP_1, str_2))
print(f'for {str_3}:', re.search(REGEXP_1, str_3))
print('\n')


# ooooAAAooooo ---> AAA
# asdfasdAAAAfasdf ---> AAAA
# AAAAAAfasdf ---> AAAAAA
# iiiiiA ----> A
str_1 = 'ooooAAAooooo'
str_2 = 'asdfasdAAAAfasdf'
str_3 = 'AAAAAAfasdf'
str_4 = 'iiiiiA'


REGEXP_2 = r'A+'
print(f'for {str_1}:', re.search(REGEXP_2, str_1))
print(f'for {str_2}:', re.search(REGEXP_2, str_2))
print(f'for {str_3}:', re.search(REGEXP_2, str_3))
print(f'for {str_4}:', re.search(REGEXP_2, str_4))
print('\n')


# There is <html> tag ---> <html>
# color can be used as <font color='red'> ---> <font color='red'>
# There is x <> 10 and something was wrong with < or > brace. ---> < or >
str_1 = 'There is <html> tag'
str_2 = 'color can be used as <font color=\'red\'>'
str_3 = 'There is x <> 10 and something was wrong with < or > brace.'


REGEXP_3 = r'<[^>]+>'
print(f'for {str_1}:', re.search(REGEXP_3, str_1))
print(f'for {str_2}:', re.search(REGEXP_3, str_2))
print(f'for {str_3}:', re.search(REGEXP_3, str_3))
print('\n')


# C@n Y0u f1nd CaPoAira? ---> CaPoAira
# s0 Wh@t i5 CamelStyle? ---> CamelStyle
# Any simple word should match. ---> Any
# I like regular expressions ---> like
str_1 = 'C@n Y0u f1nd CaPoAira?'
str_2 = 's0 Wh@t i5 CamelStyle?'
str_3 = 'Any simple word should match.'
str_4 = 'I like regular expressions'

REGEXP_4 = r'\b[a-zA-Z]{3,}\b'
print(f'for {str_1}:', re.search(REGEXP_4, str_1))
print(f'for {str_2}:', re.search(REGEXP_4, str_2))
print(f'for {str_3}:', re.search(REGEXP_4, str_3))
print(f'for {str_4}:', re.search(REGEXP_4, str_4))
print('\n')

# all those that were numbered of the camps throughout their hosts were 603550. ---> 603550
# What is the meaning of life, the universe and everything? *42* Douglas Adams ---> 42
# Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898. ----> 29
str_1 = 'all those that were numbered of the camps throughout their hosts were 603550.'
str_2 = 'What is the meaning of life, the universe and everything? *42* Douglas Adams'
str_3 = 'Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898.'


REGEXP_5 = r'\d+'
print(f'for {str_1}:', re.search(REGEXP_5, str_1))
print(f'for {str_2}:', re.search(REGEXP_5, str_2))
print(f'for {str_3}:', re.search(REGEXP_5, str_3))
print('\n')


# New York: W. H. Freeman, pp. 347-353, 1991. ---> Freeman
# set out to travel much faster than light ---> travel
# Arise ye, and depart; for this is not your rest... ---> depart
str_1 = 'New York: W. H. Freeman, pp. 347-353, 1991.'
str_2 = 'set out to travel much faster than light'
str_3 = 'Arise ye, and depart; for this is not your rest...'


REGEXP_6 = r'\w{6,}'
print(f'for {str_1}:', re.search(REGEXP_6, str_1))
print(f'for {str_2}:', re.search(REGEXP_6, str_2))
print(f'for {str_3}:', re.search(REGEXP_6, str_3))
print('\n')

# I know that cat can catch a mouse! ---> cat can catch a mouse
# But this mouse is faster than the cat. ---> mouse is faster than the cat
# Mouse Mickey is not a simple mouse. Tom is a dummy cat. ---> mouse. Tom is a dummy cat
str_1 = 'I know that cat can catch a mouse!'
str_2 = 'But this mouse is faster than the cat.'
str_3 = 'Mouse Mickey is not a simple mouse. Tom is a dummy cat.'


REGEXP_7 = r'(mouse|cat)\b.+(mouse|cat)'
print(f'for {str_1}:', re.search(REGEXP_7, str_1))
print(f'for {str_2}:', re.search(REGEXP_7, str_2))
print(f'for {str_3}:', re.search(REGEXP_7, str_3))
print('\n')

# his phone number was 892512366482. ---> 892512366482
# I called +7 999 648-99-86 ans it was right. ---> +7 999 648-99-86
# Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99 ---> 8 915 747-68-99
str_1 = 'his phone number was 892512366482.'
str_2 = 'I called +7 999 648-99-86 ans it was right.'
str_3 = 'Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99'


REGEXP_8 = r'(\+)?\d(\s)?\d{3}(\s?)\d{3}(\s|-)?\d{2}(\s|-)?\d{2}'
print(f'for {str_1}:', re.search(REGEXP_8, str_1))
print(f'for {str_2}:', re.search(REGEXP_8, str_2))
print(f'for {str_3}:', re.search(REGEXP_8, str_3))
print('\n')

