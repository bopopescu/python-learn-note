'''

判断密码强弱等级程序，要求输入密码，输出密码的等级（建议使用正则表达式和非正则表达式两种写法，并比较性能差异）：
	a.	very weak ---- 纯字母 or 数字 or 特殊字符（长度为4~8）
	b.	weak ---- 字母+数字 or 特殊字符+数字 or 字母+特殊字符 （字母并非大小写混合，长度为4~8）
	c.	medium ---- 大小写字母混合+数字 or 大小写字母混合+特殊字符（长度为4~8）
	d.	strong ---- 大小写字母混合+数字+特殊字符（长度为4~8）
	e.	very strong ---- 大小写字母混合+数字+特殊字符（长度为8～32）
	f.	invalid ---- 匹配不了以上规则的则为无效密码

'''
import re


number_set = set([n for n in range(48, 58)])
lower_letter_set = set([n for n in range(97, 123)])
upper_letter_set = set([n for n in range(65, 91)])
special_letter_set = set([n for n in range(33, 47)] + [n for n in range(58, 65)])


def judge_pass(password):
    # number,lower_letter, upper_letter, special
    default_res = [False] * 4
    ascii_string = [ord(s) for s in password]
    ascii_string_length = len(ascii_string)
    ascii_string_set =set(ascii_string)
    default_res[0] = judge_number(ascii_string_set) 
    default_res[1] = judge_lower_letter(ascii_string_set) 
    default_res[2] = judge_upper_letter(ascii_string_set) 
    default_res[3] = judge_special_letter(ascii_string_set) 

    if 4 <= len(ascii_string) <= 8:
        if default_res.count(False) == 0:
            return "strong"
        elif default_res.count(False) == 1 and (default_res[0] is False or \
                                                default_res[3] is False):
            return "medium"
        elif default_res.count(False) == 2 and (default_res[1] is False or \
                                               default_res[2] is False):
            return "weak"
        elif default_res.count(False) == 3:
            return "very weak"

    elif 8 < ascii_string_length <= 32 and default_res.count(False) == 0:
        return "very strong"
    else:
        return "invalid"


def judge_number(string_set):
    return bool(number_set & string_set)

def judge_lower_letter(string_set):
    return bool(lower_letter_set & string_set)

def judge_upper_letter(string_set):
    return bool(upper_letter_set & string_set)

def judge_special_letter(string_set):
    return bool(special_letter_set & string_set)

def judge_pass_with_re(password):
    default_res = [False] * 4
    default_res[0] = re_judge_number(password) 
    default_res[1] = re_judge_lower_letter(password) 
    default_res[2] = re_judge_upper_letter(password) 
    default_res[3] = re_judge_special_letter(password) 
    print(default_res)
    print("-----> ", password)
    if 4 <= len(password) <= 8:
        if default_res.count(False) == 0:
            return "strong"
        elif default_res.count(False) == 1 and (default_res[0] is False or \
                                                default_res[3] is False):
            return "medium"
        elif default_res.count(False) == 2 and (default_res[1] is False or \
                                               default_res[2] is False):
            return "weak"
        elif default_res.count(False) == 3:
            return "very weak"

    elif 8 < len(password) <= 32 and default_res.count(False) == 0:
        return "very strong"
    else:
        return "invalid"

def re_judge_number(string):
    return bool("".join(re.findall("\d*", string)))

def re_judge_lower_letter(string):
    return bool("".join(re.findall("[a-z]*", string)))

def re_judge_upper_letter(string):
    return bool("".join(re.findall("[A-Z]*", string)))

def re_judge_special_letter(string):
    return bool("".join(re.findall("\W*", string)))
