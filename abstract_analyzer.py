import re

# 示例文章列表
articles = """
<ul class="literature-list">
    <li>
        %0 Journal Article
        %A 刘芷君
        %+ 贵阳学院;
        %T 基于色彩心理学的花境营造浅析
        %J 现代园艺
        %D 2024
        %V 47
        %N 16
        %K 园林;花境;色彩;色彩心理学
        %X 色彩设计在花境设计中为重要内容之一，色彩刺激人们的视觉与情感，给人们提供丰富的观感。基于色彩心理学，分析探索不同色彩构成的花境对人心理产生的影响，并根据色彩理论，提出花境设计的应用建议，旨在科学配置花境设计，营造色彩协调、对人身心具有健康作用的花境，为建设绿色城市景观提供参考。
        %P 118-120+123
        %@ 1006-4958
        %L 36-1287/S
        %U https://link.cnki.net/doi/10.14051/j.cnki.xdyy.2024.16.040
        %R 10.14051/j.cnki.xdyy.2024.16.040
        %W CNKI
    </li>
    <!-- 更多的条目 -->
</ul>
"""

# 提取标题、关键词和摘要的正则表达式
title_pattern = r"%T (.+?)\n"
keywords_pattern = r"%K (.+?)\n"
abstract_pattern = r"%X (.+?)\n"

# 提取文章信息
titles = re.findall(title_pattern, articles)
keywords = re.findall(keywords_pattern, articles)
abstracts = re.findall(abstract_pattern, articles)

# 显示提取的信息
for title, keywords, abstract in zip(titles, keywords, abstracts):
    print("标题:", title[0])
    print("关键词:", keywords[0])
    print("摘要:", abstract[0])
    print("---")
