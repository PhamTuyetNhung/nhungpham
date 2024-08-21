# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:05:30 2024

@author:Phạm Tuyết Nhung-23707091
"""
s="Đại học Quốc gia, Khu phố 6, P.Linh Trung, Q.Thủ Đức, Tp.HCM"
s1=s.replace(" P. ","").replace(" Q. ","").replace(" Tp. ","").split(",")
for i in s1:
    print(i)
