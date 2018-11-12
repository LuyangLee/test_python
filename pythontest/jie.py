import jieba

seg_list = jieba.cut("没有什么能够阻挡")
print("/".join(seg_list))

seg_list2 = jieba.cut_for_search("")