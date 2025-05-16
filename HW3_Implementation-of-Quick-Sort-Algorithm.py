# -*- coding: utf-8 -*-
"""
Created on Thu May 15 13:14:30 2025

@author: coco5
"""

data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41] #待處理的資料

def quicksort(array, start, end): #自定義函式-大小排序
    if start >= end: #若陣列剩餘 0、1個元素，則跳出遞迴
        return

    pivot_index = start  # 基準值索引
    pivot_value = array[pivot_index]  # 基準值
    left = start + 1  # 從陣列的左邊開始
    right = end  # 從陣列的右邊開始

    while left <= right: #若左邊的數值全部大於右邊時代表已經分類好了左右兩邊的數值，跳出迴圈
        while left <= right and array[left] <= pivot_value: #當右邊的數值大於左邊的數值且基準值大於左邊數值
            left += 1 #左邊index加一
        while left <= right and array[right] >= pivot_value:
            right -= 1 #右邊index加一
        if left < right: #若右邊大於左邊時，兩者互換
            array[left], array[right] = array[right], array[left]
            print("交換", array)

    array[start], array[right] = array[right], array[start] 
    print("交換", array)
    
    quicksort(array, start, right - 1) #依照上面的步驟排序序列的左邊
    quicksort(array, right + 1, end) #依照上面的步驟排序序列的右邊

def main():
    print("排列前：", data)
    quicksort(data, 0, len(data) - 1)
    print("排列前：", data)
    print("排序後結果:", data)
    
if __name__ == "__main__":
    main()