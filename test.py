# -*- coding: utf-8 -*-

from pyltp import Segmentor

PATH = '/Users/mac/Documents/ITP/ltp-models/ltp_data/'
EXAMPLE_TXT = '巴蒂尔长传球给大姚'

# 还有很对添加外部字典或者是model的方法，详见文档。
def spilt_words_with_extra():
    CWS_PATH = PATH + 'cws.model'
    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon(CWS_PATH, PATH + 'extra_data.txt')  # 加载模型
    words = segmentor.segment(EXAMPLE_TXT)
    print '\t'.join(words)
    segmentor.release()

def consumer():
    from pyltp import CustomizedSegmentor
    CWS_PATH = PATH + 'cws.model'
    customized_segmentor = CustomizedSegmentor()  # 初始化实例
    customized_segmentor.load(CWS_PATH, '/Users/mac/Documents/ITP/ltp-master/tools/train/extra')  # 加载模型
    words = customized_segmentor.segment(EXAMPLE_TXT)
    print '\t'.join(words)
    customized_segmentor.release()

consumer()