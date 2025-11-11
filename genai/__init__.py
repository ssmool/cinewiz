from rembg import remove
from PIL import Image
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from transformers import pipeline
from nltk.corpus import genesis
from transformers import pipeline
from skimage import io
from skimage.feature import hog
from skimage.measure import regionprops, label
import nltk
import requests
import time
import qrcode
import cv2
import numpy as np

_buff_lang = 'en'
_buff_glob = 'null_file'
_buff_glob_lib_inri = 'null'
_buff_glob_lib = 'null'
_buff_glob_rag_coll = {"file":"null","rag_file":"null","pos_x":0.0,"pos_y":0.0,"file_type":"null","content":"null","layer_type":"null"}
_buff_glob_rag_coll_arr = []
_buff_glob_rag_coll_txt = {"file":"null","keywords":"null","file_type:":-1,"inri_corpus":"null","pos_x":-1,"pos_y":-1,"font-ttf-format":"null"}
_buff_glob_rag_coll_txt_att = []

def set_start_first_use_config():
	_buff_www_cv2_load = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
	_buff_class = []
	with open("coco.names", "r") as _buff_f_cc_name_coll:
		_buff_class = [_buff_l_prg.strip() for _buff_l_prg in _buff_f_cc_name_coll.readlines()]
	_buff_dw_name = _buff_www_cv2_load.getLayerNames()
	_buff_w_dw = [_buff_dw_name[_buff_l_prg_eq - 1] for _buff_l_prg_eq in _buff_www_cv2.getUnconnectedOutLayers()]

def set_init(_buff_glob_file):
	_buff_glob = _buf_glob_file

def set_lang(_buff_lang_flag):
	_buff_lang = _buf_lang_flag

def add_read_lib_inri_uri(_buff_uri):
	_buff_glob_lib_inri += _buff_uri

def add_read_lib(_buff_uri):
	_buff_glob_lib += _buff_uri

def set_picture(image_file,_flag_rmbg):
	fl_in = image_file
	_w = image_file + "_rag_0x_sx_nbx0.png"
	with open(fl_in, "rb") as _fl:
		_buff = _fl.read()
	if(_flag_rmbg == 0):
		_fl_out = _buff
	if(_flag_rmbg == 1):
		_fl_out = set_picture_remove_bg(_buff)
	with open(fl_out, "wb") as _fl_buff:
	    	_w.write(_fl_buff)
	_buff_glob_rag_coll_x = {"file":_w,"rag_file":"rembg={str(_flag_rmbg)}","pos_x":0,"pos_y":0,"file_type":"local-image:{ext-type}","content":keywords,"layer_type":"rag_fill_add"}
	_buff_yolo_arr = get_yolo_config(__fl_buff)
	_buff_yolo_arr_l = ','.join(_buff_yolo_arr)
	_t_content = f"_buff_glob_rag_coll_x['content']*0x00*:{_buff_yolo_arr_l}"
	_buff_glob_rag_coll_x_tx = {"content":_t_content}
	_buff_glob_rag_coll_x.update(_buff_glob_rag_coll_x_tx)
	_buff_glob_rag_coll_arr.append(_buf_glob_rag_coll_x)
	return _w

def set_picture_remove_bg(_buff):
	_fl_out = remove(_buff)
	return _fl_out

def set_board(siz_x,siz_y,color_rgb):
	_c_arr = color_rgb.split(',')
	_buff_glob = Image.new("RGB", (siz_x,siz_y), color = (_c_arr[0],_c_arr[1],_c_arr[2]))
	_buff_glob.save(_buff_glob)

def set_text(file_name,txt,pos_x,pos_y,format, text_color_rgb, _c_att_font_ttf, _c_att_font_ttf_size):
	_c_att_font_cfg = _c_att_font_ttf + ";" + _c_att_font_ttf_size
	_buff_glob_temp = Image.open(_buff_glob)
	_c_w = ImageDraw.Draw(_buff_glob_temp)
	_c_txt = str(txt)
	try:
		font = ImageFont.truetype( _c_att_font_ttf, _c_att_font_ttf_size)
	except IOError:
		font = ImageFont.load_default()
	_c_att = format.split(',')
	_c_pos = (pox_x, pos_y)
	_c_arr = text_color_rgb.split(',')
	_c_txt_rgb = (_c_arr[0], _c_arr[1], _c_arr[2])
	#_c_w.text(_c_pos, _c_att[0], _c_txt, fill=_c_txt_rgb, font=font, _c_att[1])
	_c_w.text(_c_pos, _c_att[0], _c_txt, fill=_c_txt_rgb, font=font)
	buff_glob_temp.save(_buff_glob)
	_buff_glob_rag_coll_txt_x = {"file":file_name,"keywords":file_name,"file_type:":"text","inri_corpus":"false","pos_x":pox_x,"pos_y":pox_y,"font-ttf-format":_c_att_font_cfg}
	set_inri_corpus_text_add_lib(_buff_glob_rag_coll_txt_x)

def set_text_inri(file_name, keywords, glob_lang):
	glob_lang_en = set_glob_lang(glob_lang, keywords)
	_dbas = genesis.words(glob_lang_en)
	_dbas_txt = nltk.Text(_dbas)
	_dbas_txt_coll = [_dbas_txt.generate(length=800),_dbas_txt.generate(length=400),_dbas_txt.generate(length=200),	_dbas_txt.generate(length=100),_dbas_txt.generate(length=80),_dbas_txt.generate(length=40),_dbas_txt.generate(length=20)]
	_buff_glob_rag_coll_txt_x = {"file":file_name,"keywords":keyword,"file_type:":"text_arr_inri_corpus","inri_corpus":_dbas_txt_coll,"pos_x":0,"pos_y":0,"font-ttf-format":"null"}
	set_inri_corpus_text_add_lib(_buff_glob_rag_coll_txt_x)
	return _dbas_txt_coll

def set_inri_corpus_text_add_lib(_buff):
	_buff_glob_rag_coll_txt_att.append[_buff]

def get_inri_corpus_text_lib(_file_name):
	for _buff in _buff_glob_rag_coll_txt_att:
		_buff_k = _buff.get("file")
		if(_buff_k == _file_name):
			return _buff

def set_glob_lang(glob_lang_cod, _dbas_txt):
	_cfg_glob_lang = pipeline("translation", model="Helsinki-NLP/opus-mt-{_buff_lang}-{glob_lang_cod}")
	_txt_glob_lang = _dbas_txt
	_tot_txt_glob_lang = translator(_txt_glob_lang)[0]['translation_text']
	return _tot_txt_glob_lang

def get_yolo_config(_buff_glob_fl):
	_buff_fl = cv2.imread(_buff_glob_fl)
	_p_h, _p_w, _p_c = _buff_fl.shape
	_buff_tx = cv2.dnn.blobFromImage(_buff_fl, 0.00392, (416, 416), swapRB=True, crop=False)
	net.setInput(_buff_tx)
	_buff_cc = net.forward(output_layers)

def get_yolo_detect_tags(_buff_cc):
	_buff_tag_kpi = []
	_buff_sx = []
	_buff_gx = []
	for _buff_rnd_x in _buff_cc:
		for _buff_cf in _buff_cc:
			_buff_p_fl = _buff_cf_in[5:]
			_buff_tag_kpi_z = np.argmax(_buff_p_fl)
			_buff_sx_z = _buff_p_fl[_buff_tag_kpi]
			if _buff_sx_z > 0.5:
				_pos_c_x = int(_buff_cf[0] * width)
				_pos_c_y = int(_buff_cf[1] * height)
				_pos_w = int(detection[2] * width)
				_pos_h = int(_buff_cf[3] * height)
				_pos_x = int(_pos_c_x - _pos_w / 2)
				_pos_y = int(_pos_c_y - _pos_h / 2)
				_buff_gx.append([_pos_x, _pos_y, _pos_w, _pos_h])
				_buff_sx.append(float(_buff_sx_z))
				_buff_tag_kpi.append(_buff_tag_kpi_z)
	return _buff_tag_kpi

def search_image(key_words, _buff_glob_lib_flag, pos_x, pos_y,flag_rmbg=0):
	_fl_conn = webdriver.Chrome()
	_buff_uri_lib = _buff_glob_lib.split(';')
	_fl_conn.get(_buf_uri_lib[_buf_glob_lib_flag])
	for _bit in range(1):
		_fl_conn.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
		time.sleep(2)
	_fl_dw = _fl_conn.find_elements(By.CSS_SELECTOR, 'img[alt]')
	for _bit_dw in _fl_dw:
		print(_bit_dw.get_attribute('src'))
		_fl_dw_w = _bit_dw.get_attribute('src')
	_fl_conn.quit()
	_fl_www = requests.get(_fl_dw_w)
	_fl_data_bit = BytesIO(_fl_www.content)
	_buff_glob_fl_data_bit = Image.Open(_fl_data_bit)
	#analise tags by image like objects and colors - detect RGB points and fill images_collection add dictionary
	#to doing now 12:23 24/07/2025 + 10 minutes
	#next task
	#await to doing
	#doing at: 12:31 24/07/2025
	#await to done
	_buff_blog_tx = keywords.replace(' ','_').replace('-','_').replace('+','_')
	_buff_blog_tx += _buf_glob
	_buff_w = set_picture(_buff_blog_tx,flag_rmbg)
	_buff_glob_fl.paste(_buff_w, (0,0))
	_buff_glob_rag_coll_x = {"file":_buff_w,"rag_file":_fl_www,"pos_x":pos_x,"pos_y":pos_y,"file_type":"download-image:{ext-type}","content":keywords,"layer_type":"rag_fill_add"}
	_buff_yolo_arr = get_yolo_config(_buff_glob_fl)
	_buff_yolo_arr_l = ','.join(_buff_yolo_arr)
	_t_content = f"{_buff_glob_rag_coll_x['content']}*0x00*:{_buff_yolo_arr_l}"
	_buff_glob_rag_coll_x_tx = {"content":_t_content}
	_buff_glob_rag_coll_x.update(_buff_glob_rag_coll_x_tx)
	set_file_lib(_buff_data_file)
	return _buff_w

def set_file_lib(_buff_data_file):
		_buff_glob_rag_coll_arr.append(_buf_data_file)

def get_file_lib_name(_file_name):
	for _buff in _buff_glob_rag_coll_arr:
		_buff_k_tx = {"file":_file_name}
		_buff_k = _buff.get(_buff_k_tx)
		if(_buff_k == _file_name):
			return _buff

def set_data_text_lib(_buff_data_text):
	_buff_search_data_text_rag_coll_arr.append(_buff_data_text)

def get_text_lib_name(_file_name):
	for _buff in _buff_search_data_text_rag_coll_arr:
		_buff_k_tx = {"file":_file_name}
		_buff_k = _buff.get(_buff_k_tx)
		if(_buff_k == _file_name):
			return _buff

def search_data(key_words,_buff_uri_index):
	try:
		_www_conn_tx = _buff_uri_index
		_www_conn = requests.get(_www_conn_tx)
		_www_conn.raise_for_status()
		_www = BeautifulSoup(response.text, 'html.parser')
		_txt = _www.get_text()
		if _m.lower() in _txt.lower():
			_buff_txt = f"{_txt.lower()}"
			_buff = {"file":_buff_uri_index,"rag_file":_buff_txt,"pos_x":0,"pos_y":0,"file_type":"search_data_uri:{ext-type}","content":keywords,"layer_type":"rag_fill_add"}
			set_data_text_lib(_buff)
			return _buff_txt
		else:
			#_uri = _buf_data_uri[_buff_uri_index++]
			_uri = _buff_uri_index
			return search_data(key_words,_uri)
	except requests.exceptions.RequestException as e:
		return f"404 - {url}: {e}"

def set_background(type,key_words,_buff_glob_fl,_buff_flag_smx):
	if(type == 0):
		fl_r = Image.open(_buff_glob_fl)
	if(type == 1):
		_buff_flag_smx = 0
		for _buff_flag_arr in _buff_glob_lib:
			fl_r = search_image(key_words, _buff_flag_smx, 0, 0)
	_fl_r = _fl_r.convert("RGB")
	_buff = _fl_r.getdata()
	_buff_coll = []
	for _pass in _buff:
		if _pass[0] in list(range(190, 256)):
			_buff_coll.append((255, 204, 100))
		else:
			_buff_coll.append(_pass)
	#_fl_r.putdata(_buff_coll)
	#_fl_r.save(_buff_glob)
	#add to image lib
	#to do at 14:46 24/07/2025 + 10 min
	_buff_glob_rag_coll_x = {"file":_buff_coll,"rag_file":str(type),"pos_x":0,"pos_y":0,"file_type":"{str(type)}:{ext-type}","content":key_words,"layer_type":"rag_fill_add_background"}
	_buff_yolo_arr = get_yolo_config(_buff_glob_fl)
	_buff_yolo_arr_l = ','.join(_buff_yolo_arr)
	_t_content = f"_buff_glob_rag_coll_x['content']*0x00*:{_buff_yolo_arr_l}"
	_buff_glob_rag_coll_x_tx = {"content":_t_content}
	_buff_glob_rag_coll_x.update(_buff_glob_rag_coll_x_tx)
	set_file_lib(_buff_glob_rag_coll_x)

def set_comix(_buff_glob_data):
	_buf_glob_data_comix = Image.open(_buff_glob)
	_buf_glob_data_comix_x = _buf_glob_data_comix.quantize(colors=64)
	_buf_glob_data_comix_x.save(_buff_glob_data)

def set_qrcode(url):
	_uri = url
	_buff_qr_x = qrcode.QRCode(version=1, box_size=10, border=4,)
	_buff_qr_x.add_data(_uri)
	_buff_qr_x.make(fit=True)
	_w = _buff_qr_x.make_image(fill_color="black", back_color="white").convert("RGBA")
	return _w

def add_qrcode(_w, pos_x, pos_y):
	try:
		_fl_qr_w = Image.open(_buff_glob).convert("RGBA")
	except FileNotFoundError:
		print("Background image not found. Skipping pasting.")
	if _fl_qr_w:
		qr_w, qr_h = _w.size
		bg_w, bg_h = _fl_qr_w.size
		pos = (pos_x, pos_y)
		_buff_glob_mx = _buf_glob.split()[-1]
		_fl_qr_w.paste(_w, pos, _buff_glob_mx)
		_fl_qr_w.save(_buff_glob)
	else:
		_fl_qr_w.save(_buff_glob)

def set_sign(author,email):
	_author_sign = author + ":" + email
	set_text(_author_sign,10,10,'LEFT')
