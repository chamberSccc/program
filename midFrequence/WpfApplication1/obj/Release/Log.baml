   M S B A M L   `   `   `  ����   midFrequence    midFrequence.Log   W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     -     � Title$  运行记录��$	��700��$
��1150�� � ShowInTaskbar .   � WindowStartupLocation$ CenterScreen=� � 
ResizeMode$ NoResize=�.���  � RowDefinitions �� �� $
��auto �.+��� -   $��tabControl1��$��Stretch=�$��3q�$��Stretch=�$��18(�.@��� -   $��tabItem1��$��系统运行记录��.��� .+�&   System.Windows.Controls.DataGrid  -   $��dataGridSyslog��$��Stretch=�$��5q�$��Stretch=�   CanUserResizeColumns .     AutoGenerateColumns .     CanUserResizeRows .     
IsReadOnly . ���� 	   Columns	 4  .System.Windows.Controls.DataGridTemplateColumn  ,  &System.Windows.Controls.DataGridColumn
   Width5  /System.Windows.Controls.DataGridLengthConverter$	
 120    Header$ 记录日期��   CellTemplate �� .R��� $��Center=�����  �� Path$ LOGDATE� �� StringFormat$ 
yyyy-MM-dd��  $	
 120 $ 记录时间�� �� .R��� $��Center=����� $ LOGTIME�$ HH:mm:ss��  $	
 160 $ 操作状态�� �� .R��� $��Center=����� $ OPERATE�  $	
 200 $ 备注�� �� .R��� $��Center=����� $ REMARK�  $	
 100 $ 操作�� �� .R��� -   $��删除���� -   $��tabItem2��$��发射机工作记录��.��� .+�  -   $��dataGridOptlog��$��Stretch=�$��5q�$��Stretch=� .   .   .   . $��12(����� 	   $
 80 $ 记录日期�� �� .R��� $��Center=����� $ LOGDATE�$ 
yyyy-MM-dd��  $
 80 $ 记录时间�� �� .R��� $��Center=����� $ LOGTIME�$ HH:mm:ss��  $
 60 $ 入射功率�� �� .R��� $��Center=����� $ RS�  $
 60 $ 反射功率�� �� .R��� $��Center=����� $ FS�  $
 60 $ 	主电流�� �� .R��� $��Center=����� $	 ZDL�  $
 60 $ 	主电压�� �� .R��� $��Center=����� $	 ZDY�  $
 70 $ 天线驻波比�� �� .R��� $��Center=����� $ TXZBB�  $
 70 $ 带通驻波比�� �� .R��� $��Center=����� $ DTZBB�  $
 60 $ 	调幅度�� �� .R��� $��Center=����� $	 TFD�  $
 60 $
 +22V�� �� .R��� $��Center=����� $
 Z22V�  $
 60 $
 -22V�� �� .R��� $��Center=����� $
 F22V�  $
 60 $	 +8V�� �� .R��� $��Center=����� $	 Z8V�  $
 60 $	 -8V�� �� .R��� $��Center=����� $	 F8V�  $
 60 $ 射频推动�� �� .R��� $��Center=����� $
 SPTD�  $
 70 $ 射频高字节�� �� .R��� $��Center=����� $	 SPG�  $
 70 $ 射频低字节�� �� .R��� $��Center=����� $	 SPD�  $
 60 $ 操作�� �� .R��� -   $��删除���� $��1�� �� Orientation$ 
Horizontal=�$��Center=�$��Center=�.+��� -	   $��lblCount��$��--- 共0条记录 ---��$��Stretch=�$��10q�$��Stretch=�$��Center=�$��Center=�$��16(�(  "System.Windows.Controls.DatePicker  -
   $��datePicker1��$��Center=�$��Center=�$��Stretch=�$��10q�$��Stretch=�$��18(��� -   $��btnFind��$��查找��$��30,10,30,10q�$��Stretch=�$��10q�$��Stretch=�$��18(��� -   $��btnClose��$��关闭��$��30,10,30,10q�$��Stretch=�$��10q�$��Stretch=�$��18(� �� IsCancel . 