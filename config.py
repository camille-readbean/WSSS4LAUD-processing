from pathlib import Path
import logging

data_dir = Path('.') 
train_data_dir = data_dir / '1.training'
val_data_dir = data_dir / '2.validation'
val_img_data_dir = val_data_dir / 'img'
test_data_dir = data_dir / '3.testing'
test_img_data_dir = test_data_dir / 'img'
processed_dir_path = Path('WSSSLAUD-processed/')



logger = logging.getLogger('WSSS4LAUD')

logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('processing.log')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s %(name)s %(levelname)s ] %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)