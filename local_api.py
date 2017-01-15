# -*- coding: utf-8 -*-

from pyltp import SentenceSplitter
from pyltp import Segmentor
from pyltp import NamedEntityRecognizer
from pyltp import Postagger
from pyltp import Parser
from pyltp import SementicRoleLabeller


# 需要在网上下载model 网址：http://ltp.readthedocs.io/zh_CN/latest/install.html
# 在百度云里获得。用最新的ltp_data，否则可能不能用。
PATH = '/Users/mac/Documents/ITP/ltp-models/ltp_data/'
EXAMPLE_TXT = '甲烷（CH4）分子去掉一个氢原子后剩余部分（· CH3）含有未成对的价电子，称甲基或甲基游离基，也包括单原子的游离基（· Cl）'


def split_sentence():
    sents = SentenceSplitter.split('元芳你怎么看？我就趴窗口上看呗！')  # 分句
    print '\n'.join(sents)


def split_words():
    CWS_PATH = PATH + 'cws.model'
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(CWS_PATH)  # 加载模型
    words = segmentor.segment(EXAMPLE_TXT)  # 分词
    print '\t'.join(words)
    segmentor.release()  # 释放模型


# 还有很对添加外部字典或者是model的方法，详见文档。
def spilt_words_with_extra():
    CWS_PATH = PATH + 'cws.model'
    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon(CWS_PATH, PATH + 'extra.txt')  # 加载模型
    words = segmentor.segment(EXAMPLE_TXT)
    print '\t'.join(words)
    segmentor.release()


# 添加词性, 和实体识别 等等。
def pos_and_ner():
    postagger = Postagger()  # 初始化实例
    postagger.load(PATH+'pos.model')  # 加载模型
    words = ['元芳', '你', '怎么', '看']
    postags = postagger.postag(words)  # 词性标注，这里传入的要是个数组
    print '\t'.join(postags)
    postagger.release()  # 释放模型

    print '- ' * 20 + 'ner ' + '- ' * 20
    NER_PATH = PATH + 'ner.model'
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(NER_PATH)  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    print '\t'.join(netags)
    recognizer.release()

    print '- ' * 20 + ' 依存句法分析 parse ' + '- ' * 20
    parser = Parser()  # 初始化实例
    parser.load(PATH+'parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
    parser.release()  # 释放模型

    print '- ' * 20 + ' 语义角色标注 RoleLabeller ' + '- ' * 20
    labeller = SementicRoleLabeller()  # 初始化实例
    labeller.load(PATH+'srl')  # 加载模型
    roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
    for role in roles:
        print role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])
    labeller.release()  # 释放模型


# split_words()
# spilt_words_with_extra()
pos_and_ner()