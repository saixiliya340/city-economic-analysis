# 中国城市薪资与生活成本分析

## 项目简介
使用 Python (Pandas + Matplotlib) 对 23 个中国城市的薪资、房租、生活开销等数据进行多维度分析。

## 项目结构
`
📂 city-economic-analysis/
├── analysis.py       ← 分析代码（中文注释）
├── city_data.csv     ← 23个城市原始数据
└── output/           ← 5张可视化图表
`

## 分析结果一览

### 1. 各城市平均薪资排行
![薪资排行](https://raw.githubusercontent.com/saixiliya340/city-economic-analysis/main/output/01_%E8%96%AA%E8%B5%84%E6%8E%92%E8%A1%8C.png)

### 2. 各城市租房压力对比
![租房压力](https://raw.githubusercontent.com/saixiliya340/city-economic-analysis/main/output/02_%E7%A7%9F%E6%88%BF%E5%8E%8B%E5%8A%9B%E5%AF%B9%E6%AF%94.png)

### 3. 不同线城市薪资对比
![城市等级](https://raw.githubusercontent.com/saixiliya340/city-economic-analysis/main/output/03_%E5%9F%8E%E5%B8%82%E7%AD%89%E7%BA%A7%E8%96%AA%E8%B5%84%E5%AF%B9%E6%AF%94.png)

### 4. 各城市每月可支配收入对比
![每月结余](https://raw.githubusercontent.com/saixiliya340/city-economic-analysis/main/output/04_%E6%AF%8F%E6%9C%88%E7%BB%93%E4%BD%99%E5%AF%B9%E6%AF%94.png)

### 5. 薪资 vs 房租散点图
![薪资vs房租](https://raw.githubusercontent.com/saixiliya340/city-economic-analysis/main/output/05_%E8%96%AA%E8%B5%84vs%E6%88%BF%E7%A7%9F%E6%95%A3%E7%82%B9%E5%9B%BE.png)

## 如何运行
`ash
pip install pandas matplotlib
python analysis.py
`
