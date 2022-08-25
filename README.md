# 基于CNN和EEMD的脑电信号麻醉深度预测
复现论文：[Depth of anesthesia prediction via EEG signals using convolutionalneural network and ensemble empirical mode decomposition](https://bura.brunel.ac.uk/handle/2438/22883)

此论文思想是通过EEMD将脑电信号进行分解，选取前4个分解结果，通过STFT（短时傅里叶变换）生成频谱图并拼合在一起。然后通过CNN进行分类。

由于作者没有给出他自己的网络的具体参数，故此项目只是按照他的思想进行复现。

>eemd1.py   是原始脑电信号数据处理成频谱图的代码  
>eemd2.py  
>resize.py  是图片转换成128x128大小的代码  
>main.py    是CNN分类识别训练部分，使用的框架是paddlepaddle  
>data 内数据是麻醉深度脑电信号数据，源链接：https://figshare.com/articles/dataset/EEG_and_BIS_raw_data/5589841/1

百度AI Studio项目链接：https://aistudio.baidu.com/aistudio/projectdetail/4450917
