from LabelTool import *

import sys, os, glob
import json, csv

from PyQt5.QtWidgets import QFileDialog, QApplication, QInputDialog
from PyQt5.QtCore import QAbstractTableModel, Qt

import pandas as pd
import re

current_tsv_file_path = ""
df_template_set = pd.DataFrame()
to_show_template_set = pd.DataFrame()
uniqueTemplateList = []
col = ['Term', 'Label', 'Count']
labeled_df = pd.DataFrame(columns=col)
data = ""
my_itr = 0
total_len, counter = 0, 0
CONSTANT_TEXT_RANGE = 0
CONSTANT_FILE_NAME = 'template'
labels_list = ['ACT', 'RSL', 'KOB']
folders_list = ['Labeled_Terms', 'Reports', 'Templates_sets', 'TSV_training_set']


def addLabel():
    global labels_list
    text, input = QInputDialog.getText(mainWindow, "Add Label", "New Label:")
    if input:
        classes_df = pd.DataFrame(columns=['Classes'])
        labels_list.append(text)
        for i in labels_list:
            classes_df = classes_df.append(pd.Series(i, index=['Classes']), ignore_index=True)
        classes_df.to_csv('labels.tsv', sep='\t', index=False, header=True)
        classes_df = pd.read_csv(os.path.join(os.getcwd(), 'labels.tsv'), sep='\t')
        ui.comboBox_Classes.clear()
        ui.comboBox_Classes.addItems(classes_df['Classes'].to_list())

def copyJSONtoTemplateSetFolder(filepath):
    global data, df_template_set, my_itr, current_tsv_file_path, counter, total_len, uniqueTemplateList
    const_temp_set_fname = "Template_Set_"
    const_train_set_fname = "Training_Set_"
    const_file_number = str(1).zfill(4)

    json_fname = filepath.split('/')[-1]
    file_name = json_fname.split('.')[0]

    current_tsv_file_path = file_name
    is_file_exist = False
    list_of_files = os.listdir('Templates_sets')
    # print(list_of_files)
    for k, v in enumerate(list_of_files):
        temp_fname = v.split('.')[0]
        if temp_fname == file_name:
            is_file_exist = True
            break
    if is_file_exist:
        # print("".join([const_train_set_fname, file_name.split("_")[-1]])+'.tsv')
        df_template_set = pd.read_csv(os.path.join(os.getcwd(),'TSV_training_set',"".join([const_train_set_fname, file_name.split("_")[-1]])+'.tsv'), sep='\t')
        model = pandasModel(labeled_df)
        ui.tv_LabeledTerms.setModel(model)
        current_tsv_file_path = "".join([const_train_set_fname, file_name.split("_")[-1]])
        # ui.progressBar.setVisible(False)
        ui.lt_TempSetFileName.setText("".join([const_temp_set_fname, file_name.split("_")[-1]])+'.json')
        ui.lt_TrainingSetFileName.setText("".join([const_train_set_fname, file_name.split("_")[-1]])+'.tsv')
    else:
        with open(filepath, 'r') as f:
            data = json.load(f)
        # loading JSON file to Templates Set folder
        if list_of_files:
            latest_file = max(glob.glob(os.path.join(os.getcwd(), "TSV_training_set", "*.tsv")), key=os.path.getctime)
            latest_file_number = int(os.path.split(latest_file)[-1].split('.')[0].split('_')[-1])
            const_file_number = latest_file_number + 1

        with open(f'Templates_sets/{"".join([const_temp_set_fname,str(const_file_number).zfill(4)])}.json', 'w') as wfile:
            json.dump(data, wfile)
        ui.progressBar.setVisible(True)
        ui.progressBar.setMaximum(len(data))
    # preparing TSV file and loading it to TSV Training Set folder
        values_list = []
        check_list = ['', ' ']
        t='O'
        p = re.compile(r"([=\\:. ])")
        for i in range(len(data)):
            if isinstance(data[i], dict):
                vals = data[i]['template']
                if vals != "":
                    local_list = [[i, t] for i in re.split(p, vals) if i not in check_list]
                    local_list.append(['\n', None])
                    values_list.append(local_list)
                ui.progressBar.setValue(i)
        ui.lt_TempSetFileName.setText("".join([const_temp_set_fname,str(const_file_number).zfill(4)])+'.json')
        ui.lt_TrainingSetFileName.setText("".join([const_train_set_fname,str(const_file_number).zfill(4)])+'.tsv')

        df_template_set = pd.concat([pd.DataFrame(v, columns=['text','tags']) for v in values_list], ignore_index=True)
        df_template_set.to_csv(os.path.join(os.getcwd(), f'TSV_training_set/{"".join([const_train_set_fname,str(const_file_number).zfill(4)])}.tsv'), index=False, header=True, sep='\t')
        current_tsv_file_path = "".join([const_train_set_fname,str(const_file_number).zfill(4)])
        if list_of_files:
            autoLabeling()
        ui.progressBar.setValue(len(data))

        model = pandasModel(labeled_df)
        ui.tv_LabeledTerms.setModel(model)
        # time.sleep(1)
        ui.progressBar.setVisible(False)
    msg = ""
    for k,v in df_template_set['text'].items():
        if v == '\n':
            my_itr = k+1
            break
        if k == 0:
            msg = v
            continue
        msg = " ".join([msg,v])
    with open(filepath, 'r') as f:
        data = json.load(f)
        for temp_i in range(len(data)):
            temp_text = data[temp_i]['template']
            if temp_text != "":
                if not uniqueTemplateList:
                    uniqueTemplateList.append(temp_text)
                else:
                    if not temp_text in uniqueTemplateList:
                        uniqueTemplateList.append(temp_text)
        total_len = len(uniqueTemplateList)
    ui.textEdit_TemplateContext.setPlainText(msg)
    ui.lt_CountDownJSONContext.setText(f'{counter+1} out of {total_len}')
    ui.btnLabel.setDisabled(False)
    ui.btnReport.setDisabled(False)
    ui.btnNext.setDisabled(False)
    ui.btnAddLabel.setDisabled(False)
#-------------------------------------------------------------------------------------------------------------------------
def loadJSON():
    global uniqueTemplateList, counter
    cur_dir = os.path.join(os.getcwd(),'Templates_sets')
    # print("The path ", cur_dir)
    fname = QFileDialog.getOpenFileName(parent=QtWidgets.QDialog(), directory=cur_dir, caption='Choose JSON template to label', filter='JSON files (*.json);;TSV files (*.tsv)')
    if fname[0]:
        uniqueTemplateList = []
        counter = 0
        copyJSONtoTemplateSetFolder(fname[0])

def autoLabeling():
    global df_template_set, labeled_df
    the_list = df_template_set['text'].tolist()
    the_terms = []
    for i in labeled_df['Term'].tolist():
        the_terms.append(i.split(" "))
    ind = 0
    for terms_key, terms_val in enumerate(the_terms):
        temp_counter = 0
        indexes = []
        for temp_k, temp_v in enumerate(the_list):
            if the_list[temp_k:temp_k + len(terms_val)] == terms_val:
                temp_counter += 1
                indexes.append((temp_k, temp_k + len(terms_val)))
        labeled_df['Count'][ind] = labeled_df['Count'][ind] + temp_counter
        # print(indexes)
        for k in indexes:
            ct = 0
            for i in range(k[0], k[1]):
                if len(terms_val) > 1:
                    if ct == 0:
                        df_template_set['tags'][i] = "-".join(['B',labeled_df['Label'][ind]])
                        ct += 1
                    else:
                        df_template_set['tags'][i] = "-".join(['I',labeled_df['Label'][ind]])
                else:
                    if df_template_set['tags'][i] == 'O':
                        df_template_set['tags'][i] = "-".join(['S',labeled_df['Label'][ind]])
        ind += 1
    saveFunc()
#------------------------------------------------------------------------------------------------------------------
def labelIt():
    global labeled_df
    if not ui.lineEdit_Terms.text().strip():
        return
    class_type = str(ui.comboBox_Classes.currentText())
    the_terms_list = ui.lineEdit_Terms.text().strip().split(" ")
    bi_struct = []

    if len(the_terms_list) == 1:
        cls_lb = "-".join(['S',class_type])
        bi_struct.append(cls_lb)
    else:
        for k,v in enumerate(the_terms_list):
            if k == 0:
                cls_lb = "-".join(['B', class_type])
                bi_struct.append(cls_lb)
            else:
                cls_lb = "-".join(['I', class_type])
                bi_struct.append(cls_lb)

    text_list = df_template_set['text'].tolist()
    tags_list = df_template_set['tags'].tolist()
    indexes = []
    temr_counter = 0
    for k,v in enumerate(text_list):
        if text_list[k:k+len(the_terms_list)] == the_terms_list:
            # print(f"The tag: {tags_list[k:k+len(the_terms_list)][0]}")
            if len(the_terms_list) == 1 and tags_list[k:k+len(the_terms_list)][0] != 'O':
                continue
            else:
                temr_counter += 1
                indexes.append((k,k+len(the_terms_list)))
    if not indexes:
        # print('RETURNED')
        return

    label = bi_struct[0].split("-")[-1]
    labeled_list = []
    labeled_list.append(" ".join(the_terms_list))
    labeled_list.append(label)
    labeled_list.append(temr_counter)
    if is_file_empty(os.path.join(os.getcwd(), "Labeled_Terms","label_terms.tsv")):
        # Save into Labeled Terms: Term | Label | Count
        labeled_df = labeled_df.append(pd.Series(labeled_list, index=col), ignore_index=True)
        labeled_df.to_csv('Labeled_Terms/label_terms.tsv', sep='\t', index=False)
    else:
        if not the_terms_list in [item.split(" ") for item in labeled_df['Term'].to_list()]:
            labeled_df = labeled_df.append(pd.Series(labeled_list, index=col), ignore_index=True)

    for k in indexes:
        ct = 0
        for i in range(k[0], k[1]):
            df_template_set['tags'][i] = bi_struct[ct]
            ct += 1
    model = pandasModel(labeled_df)
    ui.tv_LabeledTerms.setModel(model)
    saveFunc()

def is_file_empty(file_path):
    global labeled_df
    # Check if file exist and it is empty
    if not os.path.exists(file_path):
        labeled_df.to_csv('Labeled_Terms/label_terms.tsv', sep='\t', index=False)
    return os.stat(file_path).st_size <= 18

def saveFunc():
    df_template_set.to_csv(os.path.join(os.getcwd(), "TSV_training_set", current_tsv_file_path)+'.tsv', sep='\t', index=False)
    labeled_df.to_csv('Labeled_Terms/label_terms.tsv', sep='\t', index=False)
    # print(f'{current_tsv_file_path}')
    print('SAVED!!!')

def nextTemplate():
    global counter
    # print(len(uniqueTemplateList))
    if ui.le_temp_num.text().strip() and ui.le_temp_num.text().strip().isdigit():
        counter = int(ui.le_temp_num.text().strip()) - 1
        ui.le_temp_num.setText('')
    else:
        counter += 1
    msg = uniqueTemplateList[counter]
    ui.textEdit_TemplateContext.setPlainText(msg)
    ui.lt_CountDownJSONContext.setText(f'{counter+1} out of {total_len}')
    if counter > 0:
        ui.btnPrev.setEnabled(True)
    if counter >= total_len-1:
        ui.btnNext.setDisabled(True)

def prevTemplate():
    global counter
    # print(len(uniqueTemplateList))
    counter -= 1
    msg = uniqueTemplateList[counter]
    ui.textEdit_TemplateContext.setPlainText(msg)
    ui.lt_CountDownJSONContext.setText(f'{counter+1} out of {total_len}')
    if counter <= 0:
        ui.btnPrev.setDisabled(True)
    if counter < total_len:
        ui.btnNext.setEnabled(True)

def funcReport():
    # print(labeled_df.head())
    import datetime
    now = datetime.datetime.now()
    postfix = now.strftime("%Y-%m-%d_%H-%M-%S")
    report_fname = "_".join(["Report",postfix])
    the_path = os.path.join(os.getcwd(),'Reports',report_fname)
    labeled_df.to_json(f'{the_path}.json', orient='records')
    ui.lt_LabeledTermsReportFileName.setText(f'{report_fname}.json')

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

app = QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
mainWindow.show()

for i in folders_list:
    if not os.path.exists(i):
        os.makedirs(i)

if os.path.exists('Labeled_Terms/label_terms.tsv'):
    labeled_df = pd.read_csv('Labeled_Terms/label_terms.tsv', sep='\t')
    # labeled_df = pd.read_csv('Labeled_Terms/label_terms.tsv', converters={'Term': eval}, sep='\t')
# print(labeled_df.head())

if not os.path.exists('labels.tsv'):
    classes_df = pd.DataFrame(columns=['Classes'])
    for i in labels_list:
        classes_df = classes_df.append(pd.Series(i, index=['Classes']), ignore_index=True)
    classes_df.to_csv('labels.tsv', sep='\t', index=False, header=True)
    ui.comboBox_Classes.addItems(classes_df['Classes'].to_list())
else:
    classes_df = pd.read_csv(os.path.join(os.getcwd(), 'labels.tsv'), sep='\t')
    labels_list = classes_df['Classes'].to_list()
    ui.comboBox_Classes.addItems(classes_df['Classes'].to_list())

ui.btnPrev.setDisabled(True)
ui.btnLabel.setDisabled(True)
ui.btnReport.setDisabled(True)
ui.btnNext.setDisabled(True)
ui.btnAddLabel.setDisabled(True)
ui.progressBar.setVisible(False)

ui.btnAddLabel.clicked.connect(addLabel)
ui.btnLoad.clicked.connect(loadJSON)
ui.btnLabel.clicked.connect(labelIt)
ui.btnNext.clicked.connect(nextTemplate)
ui.btnPrev.clicked.connect(prevTemplate)
ui.btnReport.clicked.connect(funcReport)

sys.exit(app.exec_())