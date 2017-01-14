# -*- coding:utf8 -*-

# ITP 默认显示每个IP 200次/秒。
import urllib

url_get_base = "http://api.ltp-cloud.com/analysis/"
# 读API，除去结尾的\n符号。
my_api = open('my_api').readline()[:-1]
dafault_txt = '我是中国人。'


def split(str_txt = dafault_txt):
    print '- '* 20, 'ws 分词', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'ws',
        'format': 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 如果get_entity_list是False，那么则返回所有内容，反之则仅返回 命名实体列表
def ner(get_entity_list = False, str_txt=dafault_txt):
    print '- '* 20, '命名实体识别', '- ' * 20
    if get_entity_list:
        args = {
            'api_key': my_api,
            'text': str_txt,
            'pattern': 'ner',
            'format': 'plain',
            'only_ner' : 'true'
        }
    else:
        args = {
            'api_key': my_api,
            'text': '我是中国人。',
            'pattern': 'ner',
            'format': 'plain'
        }

    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 依存句法分析
def dependency(str_txt=dafault_txt):
    print '- ' * 20, '句法分析 dp', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'dp',
        'format': 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 语义依存分析
def semantic_dependency(str_txt=dafault_txt):
    print '- ' * 20, '语义依存分析 sdp', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'sdp',
        'format': 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 语义角色标注
def role_tag(str_txt=dafault_txt):
    print '- ' * 20, '语义角色标注 srl', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'srl',
        'format': 'plain'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 对文本进行全部任务的分析，返回xml
# 具体每个节点标签的含义 见：http://www.ltp-cloud.com/document/
def show_all_xml(str_txt=dafault_txt):
    print '- ' * 20, 'show all via xml', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'all',
        'format': 'xml'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 对文本进行全部任务的分析，json
# 通过添加has_key=false字段可以掉键值名
def show_all_json(str_txt=dafault_txt):
    print '- ' * 20, 'show all via json', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'all',
        'format': 'json'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content


# 对文本进行全部任务的分析，用table表示出来
def show_conll(str_txt=dafault_txt):
    print '- ' * 20, 'show all via table', '- ' * 20
    args = {
        'api_key': my_api,
        'text': str_txt,
        'pattern': 'all',
        'format': 'conll'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args))  # POST method
    content = result.read().strip()
    print content

if __name__ == '__main__':
    # split()
    # ner(True)
    # dependency()
    # semantic_dependency()
    # role_tag()
    # show_all_xml()
    # show_all_json()
    show_conll()
