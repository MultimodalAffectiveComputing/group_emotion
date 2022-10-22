# -*- coding: utf-8 -*-
import task1
import task2
import task3
import task4
import platform
import time


def emotion_analysis(filename):
    for i in range(0, 10):
        filename = f'E:\\爬虫任务\\3月任务\\三胎政策数据.csv'
        print('系统:', platform.system())
        T1 = time.perf_counter()
        task1.cluster_density(filename)
        task2.evaluates_senti(filename)
        task3.cluster_trust(filename)
        task4.group_emotion(filename)
        T2 = time.perf_counter()
        print('程序运行时间:%s秒' % (T2 - T1))
        print(f'文件{i}完成')


if __name__ == '__main__':
    # filename = input('请输入待处理的文件：')
    filename = 'test.xlsx'
    emotion_analysis(filename)
