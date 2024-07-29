# WSSS4LUAD classification dataset

Adapted for multi label classification tasks.

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


