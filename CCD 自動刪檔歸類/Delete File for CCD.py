# 載入os套件，處理文件和目錄
import os
# 載入time、datetime套件，處理時間
import datetime
# 載入shutil套件，處理高級資料夾連同檔案清除 (暫無使用
import shutil


# 變數宣告
dataNum = 0 # 被刪除的資料數量
wd = os.getcwd() #取得此py檔案執行位置 輸出路徑 紀錄用
dirToBeEmptied = str(wd)+'\Data' #需要清空的資料夾
ds = list(os.walk(dirToBeEmptied)) #獲得所有資料夾的資訊列表
days = 90 #過期的天數 預設90天
delta = datetime.timedelta(days) #設定 days 天前的檔案為過期
now = datetime.datetime.now() #獲取當前時間 計算用
nowDate = str(datetime.datetime.now())[0:19] #獲取當前時間的前19位 紀錄用
LogPath = str(wd)+'\Delete File for CCD Log - '+nowDate[0:10]+'.txt' #紀錄日誌名稱

print()

# 寫入記錄檔開頭
with open(LogPath, 'a') as f:
    f.write('==============================\n')
    f.write('執行日期:'+str(nowDate)+'\n')
    f.write('刪除超過 '+str(days)+' 天的檔案\n')
    f.write('刪除的檔案 :\n')



for d in ds: #遍歷該列表
    os.chdir(d[0]) #進入本級路徑，防止找不到檔案而報錯
    if d[2] != []: #如果該路徑下有檔案
        for x in d[2]: #遍歷這些檔案
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #獲取檔案建立時間
            # print(ctime) # DeBug用 檢視檔案建立日期
            if ctime < (now-delta): #若建立於delta天前
                delName = str(os.path.basename(x)) #刪除檔案的名稱
                print('刪除 '+delName)
                #寫入刪除的檔案名稱 (含副檔名) 寫入記錄檔
                with open(LogPath, 'a') as f:
                    f.write(delName+'\n')

                dataNum = dataNum + 1 #統計被刪除的資料數量
                os.remove(x) #則刪掉



# 判斷是否有刪除資料，然後寫入記錄檔結尾
if dataNum == 0:
    with open(LogPath, 'a') as f:
        f.write('------- 過期檔案統計 -------\n')
        f.write('無刪除任何資料\n')
        f.write('----------------------------\n')
        f.write('==============================\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
else:
    with open(LogPath, 'a') as f:
        f.write('------- 過期檔案統計 -------\n')
        f.write('刪除數量 : '+str(dataNum)+' 個\n')
        f.write('刪除日期 : '+str(nowDate)+'\n')
        f.write('----------------------------\n')
        f.write('==============================\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')



print()
print('------- 過期檔案統計 -------')
print('刪除資料數量 : ',dataNum,' 個')
print('----------------------------')
print()
os.system('pause')



# --- OS 操作方法 ---

# os.listdir(dirname)：列出dirname下的目錄和檔案
# os.getcwd()：獲得當前工作目錄
# os.curdir:返回當前目錄（'.')
# os.chdir(dirname):改變工作目錄到dirname
# os.path.isdir(name):判斷name是不是一個目錄，name不是目錄就返回false
# os.path.isfile(name):判斷name是不是一個檔案，不存在name也返回false
# os.path.exists(name):判斷是否存在檔案或目錄name
# os.path.getsize(name):獲得檔案大小，如果name是目錄返回0L
# os.path.abspath(name):獲得絕對路徑
# os.path.normpath(path):規範path字串形式
# os.path.split(name):分割檔名與目錄（事實上，如果你完全使用目錄，它也會將最後一個目錄作為檔名而分離，同時它不會判斷檔案或目錄是否存在）
# os.path.splitext():分離檔名與副檔名
# os.path.join(path,name):連線目錄與檔名或目錄
# os.path.basename(path):返回檔名
# os.path.dirname(path):返回檔案路徑
# os.remove(dir) #dir為要刪除的資料夾或者檔案路徑
# os.rmdir(path) #path要刪除的目錄的路徑。需要說明的是，使用os.rmdir刪除的目錄必須為空目錄，否則函式出錯。
# os.path.getmtime(name) ＃獲取檔案的修改時間
# os.stat(path).st_mtime＃獲取檔案的修改時間
# os.stat(path).st_ctime #獲取檔案修改時間
# os.path.getctime(name)#獲取檔案的建立時間

# 打包命令
# pyinstaller -i "Delete.ico" "Delete File for CCD.py" -n "Delete File for CCD" --onefile