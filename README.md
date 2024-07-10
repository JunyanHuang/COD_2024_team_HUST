## 2024年 人工智能与自动化学院 《模式识别课程设计》
### 课程设计题目： COD


### 小组成员
- 组长：黄骏言
- 组员：杨兆兴, 周俊诚, 王会博, 罗仰
- 指导老师：胡静


### 项目简介
#### 任务描述：实现静态图像中伪装目标的检测与识别 。


#### 数据集：
- [CAMO](CAMO-V.1.0-CVIU2019)：CAMO包含1250张图片（训练集1000张，测试集250张）。CAMO数据集可以粗略地分为自然伪装和人工伪装两种情况。自然伪装动物包括两栖动物、鸟类、昆虫、哺乳动物、爬行动物和各种环境中的水下动物。自然伪装背景包括水下、沙漠、森林、山和雪等复杂的场景。而人工伪装则包括人体绘画艺术和军事伪装迷彩等。
- CHAMELEON：CHAMELEON仅包含76张图像，手工标注了对象级的真值图（GTs）。这些图像是以“伪装的动物”为关键字，通过谷歌搜索引擎收集的。因为数据集图片数量较少，一般作为测试集。
- [COD-10K](COD10K-v3)：包含10,000张图片(5,066张伪装图片，3,000张背景图片，1,934张非伪装图片)，分为10个超级类，以及78个子类(69伪装，9非伪装)，其中伪装图像3040张作为训练集，2026张作为测试集。这些图像来源于多个摄影学网站,主要是Flickr网站。为了避免选择偏差，还从Flickr上收集了3000张显著图像。为了进一步丰富负样本，又从互联网上选取了1934幅非伪装图像，包括森林、雪、草原、天空、海水等类别的背景场景。最新更新的v3版本除了对象基本的分割标注，还提供了类别标签、实例级别的标注以及coco格式的检测框和分割标注，可以进一步作为检测和识别的数据集。COD-10K下载地址：[https://dengpingfan.github.io/pages/COD.html](https://dengpingfan.github.io/pages/COD.html)

#### 生成数据集
- [imagenet1K_selected](imagenet1K_selected)中包含了ImageNet-1K中所有和COD-10K类别匹配的图片. ImageNet-1K下载地址：[https://www.kaggle.com/c/imagenet-object-localization-challenge/data](https://www.kaggle.com/c/imagenet-object-localization-challenge/data)
- [COD-ImageNet.json](COD-ImageNet.json)中记录ImageNet-1K 和 COD-10K 的类别匹配结果，[imagenet_selection.py](imagenet_selection.py)程序从ImageNet-1K中筛选JPG文件生成[Imagenet1K_selected](imagenet1K_selected)
