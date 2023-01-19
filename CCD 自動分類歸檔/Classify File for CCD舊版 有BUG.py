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


print()



# 寫入記錄檔開頭
with open(LogPath, 'a') as f:
    f.write('==============================\n')
    f.write('執行日期:'+str(nowDate)+'\n')


for d in ds: #遍歷該列表
    os.chdir(d[0]) #進入本級路徑，防止找不到檔案而報錯
    if d[2] != []: #如果該路徑下有檔案
        for x in d[2]: #遍歷這些檔案
            ctime = datetime.datetime.fromtimestamp(os.path.getctime(x)) #獲取檔案建立時間
            strctime = str(ctime)[0:10] # 獲取檔案建立日期後轉為日期的字串
            # print(ctime) # DeBug用 檢視檔案建立日期
            # print(strctime) # DeBug用 檢視檔案建立日期


            # ☆★☆★☆這邊有問題待檢修，目錄會一直往下加☆★☆★☆

            # 更改判定位置到 Data之下
            os.chdir(dirToBeEmptied)




            #如果沒有資料夾執行建立
            if not os.path.isdir(strctime):
                print('新建資料夾 : '+strctime)
                #寫入創建的資料夾名稱
                with open(LogPath, 'a') as f:
                    f.write('新建資料夾 : '+strctime+'\n')
                fileNum = fileNum + 1 #統計新增的資料夾數量
                os.mkdir(strctime) # 建立資料夾

            #如果有此資料夾則移動至此
            if os.path.isdir(strctime):

                xx = str(dirToBeEmptied+'\\'+os.path.basename(x))#移動檔案的絕對路徑
                delName = str(os.path.basename(x)) #移動檔案的名稱

                # if os.path.isfile(xx):
                #     print('路徑存在檔案 XX 。 路徑存在檔案 XX 。')

                print('檔案 <'+delName+'> 移動至 '+strctime)

                #移動檔案至相符資料夾中
                with open(LogPath, 'a') as f:
                    f.write('檔案 <'+delName+'> 移動至 '+strctime+'\n')

                dataNum = dataNum + 1 #統計被移動的資料數量

                


                # ☆★☆★☆這邊有問題待檢修，目錄會一直往下加☆★☆★☆
                if os.access(x, os.F_OK):
                    print(os.access(x, os.F_OK))
                    print('檔案存在')
                    shutil.move(os.path.basename(x),strctime) # 移動檔案到上面所新增的資料夾當中
                else:
                    print(x)
                    print(os.access(x, os.F_OK))
                    print('檔案不存在')
                    


                
                    







# 判斷是否有移動資料，然後寫入記錄檔結尾
if dataNum == 0:
    with open(LogPath, 'a') as f:
        f.write('------- 移動檔案統計 -------\n')
        f.write('無移動任何資料\n')
        f.write('----------------------------\n')
        f.write('==============================\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')
else:
    with open(LogPath, 'a') as f:
        f.write('------- 移動檔案統計 -------\n')
        f.write('新資料夾 : '+str(fileNum)+' 個\n')    
        f.write('移動數量 : '+str(dataNum)+' 個\n')
        f.write('----------------------------\n')
        f.write('==============================\n')
        f.write('\n')
        f.write('\n')
        f.write('\n')


print()
print('------- 移動檔案統計 -------')
print('新建資料夾數量 : ',fileNum,' 個')
print('移動檔案的數量 : ',dataNum,' 個')
print('----------------------------')
print()
os.system('pause')
