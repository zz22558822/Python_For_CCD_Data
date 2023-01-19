# 載入os套件，處理文件和目錄
import os
# 載入time、datetime套件，處理時間
import datetime
# 載入shutil套件，處理移動檔案使用
import shutil

# 變數宣告
dataNum = 0 # 被移動的資料數量
fileNum = 0 # 新建資料夾數量
wd = os.getcwd() #取得此py檔案執行位置 輸出路徑 紀錄用
dirToBeEmptied = str(wd)+'\Data' #需要移動的資料夾
ds = list(os.walk(dirToBeEmptied)) #獲得所有資料夾的資訊列表
now = datetime.datetime.now() #獲取當前時間 計算用
nowDate = str(datetime.datetime.now())[0:19] #獲取當前時間的前19位 紀錄用
LogPath = str(wd)+'\Classify File for CCD Log - '+nowDate[0:10]+'.txt' #紀錄日誌名稱




for d in ds: #遍歷該列表
    print('---1.'+d[0]+'---')
    os.chdir(d[0]) #進入本級路徑，防止找不到檔案而報錯
    if d[2] != []: #如果該路徑下有檔案
        for x in d[2]: #遍歷這些檔案
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #獲取檔案建立時間
            strctime = str(ctime)[0:10] # 獲取檔案建立日期後轉為日期的字串

            # 更改判定位置到 Data之下
            # os.chdir(dirToBeEmptied)

            # 如果沒有資料夾執行建立
            if not os.path.isdir(strctime):
                fileNum = fileNum + 1 #統計新增的資料夾數量
                os.mkdir(strctime) # 建立資料夾
            

            os.chdir(dirToBeEmptied+'\\'+strctime)
            # 如果有資料夾就檢查是否檔案已在資料夾內
            if os.path.lexists(x):
                print('Yes')












            # #如果有此資料夾則移動至此
            # if os.path.isdir(strctime):
            #     xx = str(dirToBeEmptied+'\\'+os.path.basename(x))#移動檔案的絕對路徑
            #     delName = str(os.path.basename(x)) #移動檔案的名稱
            #     dataNum = dataNum + 1 #統計被移動的資料數量
            #     shutil.move(os.path.basename(x),strctime) # 移動檔案到上面所新增的資料夾當中
