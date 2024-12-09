module data
  save

  integer::cas !宣告事件數
  integer,allocatable::dicimal_number(:) !以陣列宣告原始數字
  integer,allocatable::system_10_change_to(:) !以陣列宣告轉換方式
  character(len=16),allocatable::new_system_number(:) !以陣列宣告轉換後結果
  integer::i !宣吿次數
  integer::mes 
  integer::temp !宣告暫存值
  
end module data

!----------------------------------------------------------------------------------------------------------

subroutine sub1 !計算出資料共幾筆
  use data
  implicit none
  cas=0

 
  do !算出次數
     read(10,*,iostat=mes)temp !讀取檔案
     if(mes==0)then
        cas=cas+1
     else
        exit
     end if
  end do
  rewind(10) !將游標移回檔案起始並以陣列方式讀取
  allocate(dicimal_number(1:cas),system_10_change_to(1:cas),new_system_number(1:cas))
  do i=1,cas,1
     read(10,*)dicimal_number(i),system_10_change_to(i)
  end do
end subroutine sub1

!----------------------------------------------------------------------------------------------------------

subroutine sub2 !輸出方式
  use data
  implicit none

  do i=1,cas,1
     if(dicimal_number(i)>65535)then
        new_system_number(i)=' number overflow'
     else if(system_10_change_to(i)==2)then
        call sub2_1
     else if(system_10_change_to(i)==8)then
        call sub2_2
     else if(system_10_change_to(i)==16)then
        call sub2_3
     else
        new_system_number(i)='    wrong system'
     end if
  end do

end subroutine sub2

!----------------------------------------------------------------------------------------------------------

subroutine sub2_1 !十進位轉二進位
  use data 
  implicit none

  character(len=16)::ctemp !由長度為16格的暫存值暫時儲存轉換出來的字串
  integer::remainder !宣告餘數
  integer::ii !由於二進位須由後向前填，所以需要ii進行運算處理
  integer::num !儲存每次計算後的商值

  num=dicimal_number(i)
  ii=16
  ctemp=' '

  do ii=16,1,-1 !因為要由後向前填，所以是由第16格向回填
     remainder=mod(num,2) !進行轉換運算
     num=(num-remainder)/2
     if(remainder==0)then
        ctemp(ii:ii)="0"
     else
        ctemp(ii:ii)="1"
     end if
     if(num==0)exit
  end do
  new_system_number(i)=ctemp
end subroutine sub2_1

!----------------------------------------------------------------------------------------------------------

subroutine sub2_2 !十進位轉八進位
  use data
  implicit none

  character(len=16)::ctemp !由長度為16格的暫存值暫時儲存轉換出來的字串
  integer::remainder !宣告餘數
  integer::ii !由於八進位須由後向前填，所以需要ii進行運算處理
  integer::num !儲存每次計算後的商值

  num=dicimal_number(i)
  ii=16
  ctemp=' '

  do ii=16,1,-1 !因為要由後向前填，所以是由第16格向回填
     remainder=mod(num,8) !進行轉換運算
     num=(num-remainder)/8
     if(remainder==0)then
        ctemp(ii:ii)="0"
     else if(remainder==1)then
        ctemp(ii:ii)="1"
     else if(remainder==2)then
        ctemp(ii:ii)="2"
     else if(remainder==3)then
        ctemp(ii:ii)="3"
     else if(remainder==4)then
        ctemp(ii:ii)="4"
     else if(remainder==5)then
        ctemp(ii:ii)="5"
     else if(remainder==6)then
        ctemp(ii:ii)="6"
     else
        ctemp(ii:ii)="7"
     end if
     if(num==0)exit
  end do
  new_system_number(i)=ctemp
end subroutine sub2_2

!----------------------------------------------------------------------------------------------------------

subroutine sub2_3 !十進位轉十六進位
  use data
  implicit none

  character(len=16)::ctemp !由長度為16格的暫存值暫時儲存轉換出來的字串
  integer::remainder !宣告餘數
  integer::ii !由於十六進位須由後向前填，所以需要ii進行運算處理
  integer::num !儲存每次計算後的商值

  num=dicimal_number(i)
  ii=16
  ctemp=' '

  do ii=16,1,-1 !因為要由後向前填，所以是由第16格向回填
     remainder=mod(num,16) !進行轉換運算
     num=(num-remainder)/16
     if(remainder==0)then
        ctemp(ii:ii)="0"
     else if(remainder==1)then
        ctemp(ii:ii)="1"
     else if(remainder==2)then
        ctemp(ii:ii)="2"
     else if(remainder==3)then
        ctemp(ii:ii)="3"
     else if(remainder==4)then
        ctemp(ii:ii)="4"
     else if(remainder==5)then
        ctemp(ii:ii)="5"
     else if(remainder==6)then
        ctemp(ii:ii)="6"
     else if(remainder==7)then
        ctemp(ii:ii)="7"
     else if(remainder==8)then
        ctemp(ii:ii)="8"
     else if(remainder==9)then
        ctemp(ii:ii)="9"
     else if(remainder==10)then
        ctemp(ii:ii)="A"
     else if(remainder==11)then
        ctemp(ii:ii)="B"
     else if(remainder==12)then
        ctemp(ii:ii)="C"
     else if(remainder==13)then
        ctemp(ii:ii)="D"
     else if(remainder==14)then
        ctemp(ii:ii)="E"
     else
        ctemp(ii:ii)="F"     
     end if
     if(num==0)exit
  end do
  new_system_number(i)=ctemp
end subroutine sub2_3

!----------------------------------------------------------------------------------------------------------

subroutine sub3 !輸出格式和結果
  use data
  implicit none

  write(11,"('case',2x,'dicimal_number',2x,'system_10_change_to',2x,'new_system_number')")

  do i=1,cas,1 !由於new_system_number就為字串，所以不需考慮number overflow或wrong system的格式問題
     write(11,"(2x,I2,2x,I6,14x,I2,16x,A)")i,dicimal_number(i),system_10_change_to(i),new_system_number(i)
  end do
end subroutine sub3

!----------------------------------------------------------------------------------------------------------

program HW6_109612075 !執行主程式
  use data
  implicit none 

  open(10,file="system_change_input.txt",status="old") !開啟輸入和輸出檔
  open(11,file="system_change_output.txt",status="replace")
  
  call sub1 !叫出先前所寫的轉換及格式程式
  call sub2
  call sub3

end program HW6_109612075 !結束
