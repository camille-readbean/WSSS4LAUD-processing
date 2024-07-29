# WSSS4LUAD classification dataset

Adapted for multi label classification tasks.  
  
https://wsss4luad.grand-challenge.org/WSSS4LUAD/  


`annotations.csv`:  
```csv
npy_filepath,label,original_size,new_size,original_file_path,split
"train/1217322-39328-15772-[1, 1, 0].npy",tumor:True|stroma:True|normal:False,"(187, 224)","(187, 224)","1.training/1217322-39328-15772-[1, 1, 0].png",train
val/10.npy,tumor:True|stroma:True|normal:False,"(228, 293)","(228, 293)",2.validation/img/10.png,val
test/00.npy,tumor:True|stroma:True|normal:False,"(225, 301)","(225, 301)",3.testing/img/00.png,test
```

```
:~/ruibin_datasets/WSSS4LAUD-processing$ find 1.training/ -type f | wc -l
10093
:~/ruibin_datasets/WSSS4LAUD-processing$ find 2.validation/img -type f | wc -l
40
:~/ruibin_datasets/WSSS4LAUD-processing$ find 3.testing/img -type f | wc -l
80
```

8314 different resolutions

```
[2024-07-29 16:37:22,699 WSSS4LAUD INFO ] 8314
[2024-07-29 16:37:22,700 WSSS4LAUD INFO ] max: (5606, 2850) min: (150, 156)
[2024-07-29 16:37:22,700 WSSS4LAUD INFO ] min W: 150, max W: 5606
[2024-07-29 16:37:22,700 WSSS4LAUD INFO ] min H: 150, max H: 4371
[2024-07-29 16:37:22,707 WSSS4LAUD INFO ] Index(['npy_filepath', 'label', 'original_size', 'new_size',
       'original_file_path', 'split'],
      dtype='object')
[2024-07-29 16:37:22,707 WSSS4LAUD INFO ] npy_filepath               train/1217322-39328-15772-[1, 1, 0].npy
label                          tumor:True|stroma:True|normal:False
original_size                                           (187, 224)
new_size                                                (187, 224)
original_file_path    1.training/1217322-39328-15772-[1, 1, 0].png
split                                                        train
Name: 0, dtype: object
[2024-07-29 16:37:22,709 WSSS4LAUD INFO ] npy_filepath                                  test/40.npy
label                 tumor:True|stroma:True|normal:False
original_size                                  (434, 432)
new_size                                       (434, 432)
original_file_path                   3.testing/img/40.png
split                                                test
Name: 10210, dtype: object
```



## Citations

[1] Han, Chu, et al. "Multi-layer pseudo-supervision for histopathology tissue semantic segmentation using patch-level classification labels." Medical Image Analysis (2022): 102487.
```latex
    @article{Han2022Multilayer,
      title = {Multi-Layer Pseudo-Supervision for Histopathology Tissue Semantic Segmentation using Patch-level Classification Labels},
      journal = {Medical Image Analysis},
      pages = {102487},
      year = {2022},
      issn = {1361-8415},
      author = {Chu Han and Jiatai Lin and Jinhai Mai and Yi Wang and Qingling Zhang and Bingchao Zhao and Xin Chen and Xipeng Pan and Zhenwei Shi and Zeyan Xu and Su Yao and Lixu Yan and Huan Lin and Xiaomei Huang and Changhong Liang and Guoqiang Han and Zaiyi Liu}
    }
```

[2] Han, Chu, et al. (2022).  WSSS4LUAD: Grand Challenge on Weakly-supervised Tissue Semantic Segmentation for Lung Adenocarcinoma. (https://arxiv.org/abs/2204.06455)
```latex
    @inproceedings{han2022wsss4luad,
      author = {Han, Chu and Pan, Xipeng and Yan, Lixu and Lin, Huan and Li, Bingbing and Yao, Su and Lv, Shanshan and Shi, Zhenwei and Mai, Jinhai and Lin, Jiatai and Zhao, Bingchao and Xu, Zeyan and Wang, Zhizhen and Wang, Yumeng and Zhang, Yuan and Wang, Huihui and Zhu, Chao and Lin, Chunhui and Mao, Lijian and Wu, Min and Duan, Luwen and Zhu, Jingsong and Hu, Dong and Fang, Zijie and Chen, Yang and Zhang, Yongbing and Li, Yi and Zou, Yiwen and Yu, Yiduo and Li, Xiaomeng and Li, Haiming and Cui, Yanfen and Han, Guoqiang and Xu, Yan and Xu, Jun and Yang, Huihua and Li, Chunming and Liu, Zhenbing and Lu, Cheng and Chen, Xin and Liang, Changhong and Zhang, Qingling and Liu, Zaiyi},
      title = {WSSS4LUAD: Grand Challenge on Weakly-supervised Tissue Semantic Segmentation for Lung Adenocarcinoma},
      publisher = {arXiv},
      year = {2022}
    }
```