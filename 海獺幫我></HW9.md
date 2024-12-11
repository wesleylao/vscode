• Design a class named lineseg to describe a 2D line segment: 

• lineseg ( x1 = 0, y1 = 0, x2 = 0, y2 = 0) 

• (x1, y1) indicates the start point of a line segment;

• (x2, y2) indicates the terminal point of a line segment. 

• lineseg.sumsq() returns the sum of square differences by 

$$
(x_{2}-x_{1})^2+(y_{2}-y_{1})^2+(z_{2}-z_{1})^2
$$

• lineseg.length() returns the length of a line segment by 
$$
\sqrt{(x_{2}-x_{1})^2+(y_{2}-y_{1})^2+(z_{2}-z_{1})^2}
$$

• An object of lineseg can be multiplied by a float number. 

 Your lineseg must satisfy the following test [code](https://e3p.nycu.edu.tw/mod/folder/view.php?id=63608 "code"):

  

line = lineseg (1., 2., 4., 6.) 

print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length()) 

line *= 2.0 

print(line.x1, line.y1, line.x2, line.y2, line.sumsq(), line.length())

  

 The results will be: 

1.0, 2.0, 4.0, 6.0, 25.0, 5.0 

1.0, 2.0, 8.0, 12.0, 149.0, 12.2066 

• Notice that the error must be in ±0.001.

  

Design a class lineseg3 inherited from lineseg to describe a 3D line segment. 

• lineseg3 ( x1 = 0, y1 = 0 , z1 = 0, x2 = 0, y2 = 0, z2 = 0) 

• (x1, y1, z1) indicates the start point of a line segment; 

• (x2, y2, z2) indicates the terminal point of a line segment. 

• lineseg3.sumsq() returns the sum of square differences by
$$
(x_{2}-x_{1})^2+(y_{2}-y_{1})^2+(z_{2}-z_{1})^2
$$

• lineseg3.length() returns the length of a line segment by 
$$
\sqrt{(x_{2}-x_{1})^2+(y_{2}-y_{1})^2+(z_{2}-z_{1})^2}
$$
  
• An object of lineseg3 can be multiplied by a float number.

  

Your lineseg3 must satisfy the following test [code](https://e3p.nycu.edu.tw/mod/folder/view.php?id=63608 "code"): 

line = lineseg3 (1., 2., 3., -1., -2., -3.)

print(line.x1, line.y1, line.z1,  line.x2, line.y2, line.z2, line.sumsq(), line.length())

line *= 2.0 

print(line.x1, line.y1,  line.z1, line.x2, line.y2, line.z2 , line.sumsq(), line.length())

  

• The results will be:

1.0, 2.0, 3.0, -1.0, -2.0, -3.0, 56.0, 7.483 

1.0, 2.0, 3.0, -2.0, -4.0, -6.0, 126.0, 11.225 

• Notice that the error must be in ±0.001. 

  

請 follow template 寫出 兩個 class lineseg, lineseg3 並上傳至 E3

class 需要能呼叫 .sumsq(), .length() 並且執行 *= 動作 請確認舉例都能執行正確

請注意 lineseg3 需要以**繼承 lineseg 的方式完成**，若不是用繼承會扣分

兩個 class **把握 reusing 的概念**，重複概念的程式若出現會被扣分

ex: .sumsq() 算出來的值沒有用到 .length() 而是直接重算一遍

資料格式都是浮點數

注意 template (lineseg, x1, y1, z1….) 參數/函數名稱，若參數名稱與 template 不同會斟酌扣分

 助教會輸入其他測資來測試同學的程式能否處理正常的輸入值，

 助教是直接在程式內修改參數指派的值 因此不用幫助教寫input() 也不用考慮助教會怎麼輸入參數的值

 不用考慮不合法的輸入(例如字串、無解的狀況)

**檔名格式: 學號_HW9.py**

 用 colab 同學可以從 [檔案] -> [下載] -> [下載 .py] 儲存 .py 檔案)

 給分標準:

 Correctness: 20% (程式執行正確)

 Structure: 80% (若程式執行失敗 or 測資 fail 仍會有的基本分, )

 (lineseg3 not using inherit - 10 points, 重複概念程式 -5)

 Deadline: 2024.12.23 23:55

 遲交一周，score * 0.9

 遲交一個月以內，score * 0.8

 學期結束前繳交，score * 0.6