import os

def print_console(text, newline = False):
    if newline:
        text = "\n" + text + "\n"
    print (text)
    
def get_datetime():
    import datetime
    return datetime.datetime.now()

def extend_list(x,y):
    x.extend(y)
    return x;

def unique_word_string(text):
    ulist = []
    [ulist.append(x) for x in text.split(" ") if x not in ulist]
    return ' '.join(ulist)

def remove_word_by_list(text, listWord):
    return ' '.join([x for x in text.split(" ") if x not in listWord])

def rescale(value, limitMinMax,baseMinMax=[0,1]):
    return ((limitMinMax[1] - limitMinMax[0]) * (value - baseMinMax[0]) / (baseMinMax[1] - baseMinMax[0])) + limitMinMax[0];

def remove_accents(txt, codif='utf-8'):
    from unicodedata import normalize, combining
    test = normalize('NFKD', txt.decode(codif,'ignore')).encode('ASCII','ignore')
    return test

    #nfkd_form = normalize('NFKD', txt.decode(codif))
    #tratado =  u"".join([c for c in nfkd_form if not combining(c)])
    #return tratado.encode('ASCII',errors='ignore')

def only_letters_numbers_ascii(raw_html):
    import string
    make_trans=string.maketrans('','')
    dif_chars = make_trans.translate(make_trans, string.digits + string.ascii_letters + " ")
    raw_html = str(raw_html)
    if  raw_html is not None and len(raw_html) > 0:
        cleantext = remove_accents(raw_html)
        cleantext = cleantext.translate(make_trans,dif_chars)
        return cleantext
    else:
        return ''


def to_str_with_encoding(text):
    return text.encode('utf-8') if type(text) in [str,unicode] else str(text)

def remove_new_line(text):
    return text.replace('\r', ' ').replace('\n', ' ')

import datetime
def date_to_string(date = None):
    date = get_datetime() if date is None else date
    return date.strftime("%Y%m%d%H%M%S")

def string_to_date(date):
    return datetime.datetime.strptime(date,"%Y%m%d%H%M%S")


def get_files_in_dir(path):
    return [get_file_info(path, filename = x) for x in os.listdir(path)]

def get_file_info(path, filename = None):
    if filename is None:
        return os.path.basename(path), get_file_modification_date(path)
    else:
        return filename,  get_file_modification_date(path + filename)

def get_file_modification_date(path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(path))

def create_zip_from_list(zip_path, files_path, is_python_files = False):
    import zipfile
    zip = zipfile.PyZipFile(zip_path, mode='w') if is_python_files else zipfile.ZipFile(zip_path, mode='w')
    method_write = zip.writepy if is_python_files else zip.write
    
    if type(files_path) is list:
        for file_path in list_file_path:
            method_write(file_path)
    else:
        method_write(files_path)
    zip.close()   

def get_kafka_cnn_str(bootstrap_servers, bootstrap_port):
    return bootstrap_servers + ":" + bootstrap_port 
