# 載入os套件，處理文件和目錄
import os
import socket
# 載入time、datetime套件，處理時間
import datetime
# 載入shutil套件，處理移動檔案使用
import shutil
import time


# 視窗大小設定
os.system('mode con: cols=120 lines=40')


# 變數宣告
PcName = socket.gethostname() #取得電腦名稱
exePath = os.getcwd() #取得此py檔案執行位置 輸出路徑 紀錄用
dataPath = 'C:\Cable Linker8761\data' #需要移動的資料夾
dataPathList = list(os.walk(dataPath)) #獲得所有資料夾的資訊列表
TargetPath = 'Z:\電測機Data\\'+PcName #複製到此目標資料夾
backupPath = 'C:\8761-Backup' #備份位置



# 主程式
def CopyToCCD():
    dataNum = 0 # 被複製的資料數量
    dataNum2 = 0 # 被移動的資料數量
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #獲取當前時間 計算用
    beforeDate = (datetime.datetime.now()-datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S") #獲取前一小時 判斷用
    LogPath = 'C:\Cable Linker8761\Mobile file for CCD Log - '+now[0:10]+'.txt' #紀錄日誌名稱

    # 寫入記錄檔開頭
    with open(LogPath, 'a') as f:
        f.write('==============================\n')
        f.write('執行日期:'+str(now)+'\n')
        f.write('備份時間 '+str(beforeDate)+' 前的檔案\n')

    print('==============================')
    print('執行日期:'+str(now))
    print('備份時間 '+str(beforeDate)+' 前的檔案')
    os.chdir(dataPathList[0][0]) #進入本級路徑，防止找不到檔案而報錯  

    # 新建資料夾的 CallBack Function
    def NewFile(File):
        #如果沒有資料夾執行建立
        if not os.path.isdir(File):
            print('新建資料夾 : '+File)
            #寫入創建的資料夾名稱
            with open(LogPath, 'a') as f:
                f.write('新建資料夾 : '+File+'\n')
            os.makedirs(File) # 建立資料夾
    
    # 建立多層目錄調用 NewFile()
    NewFile(TargetPath)
    NewFile(backupPath)

    for Item in dataPathList[0][2]: #遍歷這些檔案
        # 變數
        ctime = datetime.datetime.fromtimestamp(os.path.getctime(Item)) #獲取檔案建立時間
        ctimeDel = datetime.datetime.now()-datetime.timedelta(hours=1) #獲取一小時前時間
        strctime = str(ctime)[0:10] # 獲取檔案建立日期後轉為日期的字串

        # print('檔案建立時間'+str(ctime))
        # print('前一小時時間'+str(ctimeDel))

        # 如果檔案時間建立超過一小時以上，複製並移動
        if ctimeDel >= ctime:
            #如果有此資料夾則複製至此
            if os.path.isdir(TargetPath):
                DataName = str(os.path.basename(Item)) #複製檔案的名稱

                # 檔案存在於 dataPath 時才進行複製
                if os.access(dataPath+'\\'+os.path.basename(Item), os.F_OK):
                    #複製檔案至相符資料夾中
                    with open(LogPath, 'a') as f:
                        f.write('檔案 <'+DataName+'> 複製至 '+TargetPath+'\n')
                    print('檔案 <'+DataName+'> 複製至 '+TargetPath)

                    dataNum = dataNum + 1 #統計被複製的資料數量

                    shutil.copy(dataPath+'\\'+os.path.basename(Item),TargetPath) # 複製檔案到上面所新增的資料夾當中

            # 如果檔案在 TargetPath 且也在 dataPath 則移動至 backupPath
            if os.access(dataPath+'\\'+os.path.basename(Item), os.F_OK) & os.access(TargetPath+'\\'+os.path.basename(Item), os.F_OK):
                #如果有此資料夾則移動至此
                if os.path.isdir(backupPath):
                    DataName = str(os.path.basename(Item)) #移動檔案的名稱

                    # 檔案存在於 dataPath 時才進行移動
                    if os.access(dataPath+'\\'+os.path.basename(Item), os.F_OK):
                        #移動檔案至相符資料夾中
                        with open(LogPath, 'a') as f:
                            f.write('檔案 <'+DataName+'> 移動至 '+backupPath+'\n')
                        print('檔案 <'+DataName+'> 移動至 '+backupPath)

                        dataNum2 = dataNum2 + 1 #統計被移動的資料數量

                        shutil.move(dataPath+'\\'+os.path.basename(Item),backupPath+'\\'+os.path.basename(Item)) # 移動檔案到上面所新增的資料夾當中


    # 判斷是否有複製、移動資料，然後寫入記錄檔結尾
    if dataNum == 0 & dataNum2 == 0:
        with open(LogPath, 'a') as f:
            f.write('------- 完成檔案統計 -------\n')
            f.write('無複製、移動任何資料\n')
            f.write('----------------------------\n')
            f.write('==============================\n')
            f.write('\n')
            f.write('\n')
            f.write('\n')
    else:
        with open(LogPath, 'a') as f:
            f.write('------- 完成檔案統計 -------\n')
            f.write('複製數量 : '+str(dataNum)+' 個\n')
            f.write('移動日期 : '+str(dataNum2)+' 個\n')
            f.write('----------------------------\n')
            f.write('==============================\n')
            f.write('\n')
            f.write('\n')
            f.write('\n')
                






CopyToCCD()



# print()
os.system('pause')






