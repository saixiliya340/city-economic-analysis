import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

# 使用非交互式后端（服务器环境不需要显示窗口）
matplotlib.use('Agg')
 
# 设置中文字体（让图表里的中文能正常显示）
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'PingFang SC']
matplotlib.rcParams['axes.unicode_minus'] = False

# ===== 第1步：读取数据 =====
df = pd.read_csv('city_data.csv', encoding='utf-8-sig')

print('='*50)
print('中国城市薪资与生活成本分析')
print('='*50)

# ===== 第2步：预览数据 =====
print('\n前5行数据：')
print(df.head())
print(f'\n共 {df.shape[0]} 个城市，{df.shape[1]} 个维度')

# ===== 第3步：基本统计 =====
print('\n薪资&开销统计：')
stats = df[['avg_salary', 'total_expense', 'disposable_income']].describe().round(0)
print(stats)

# ===== 第4步：关键发现 =====
print('\n关键发现：')
highest = df.loc[df['avg_salary'].idxmax()]
print(f'① 平均薪资最高：{highest["city"]}（{int(highest["avg_salary"])}元/月）')

df['rent_ratio'] = (df['rent_1br'] / df['avg_salary'] * 100).round(1)
best_rent = df.loc[df['rent_ratio'].idxmin()]
print(f'② 租房压力最小：{best_rent["city"]}（房租只占工资{best_rent["rent_ratio"]}%）')

df['disposable_income'] = df['avg_salary'] - df['total_expense']
best_save = df.loc[df['disposable_income'].idxmax()]
print(f'③ 月结余最多：{best_save["city"]}（每月剩{int(best_save["disposable_income"])}元）')

# ===== 第5步：画图 =====
os.makedirs('output', exist_ok=True)

# 图1：薪资排行
plt.figure(figsize=(12, 6))
sorted_df = df.sort_values('avg_salary', ascending=True)
colors = ['#ff6b6b' if c in ['一线'] else '#ffd93d' if c in ['新一线'] else '#6bcb77' if c in ['二线'] else '#4d96ff' if c in ['三线'] else '#a8a8a8' for c in sorted_df['tier']]
bars = plt.barh(sorted_df['city'], sorted_df['avg_salary'], color=colors)
plt.xlabel('平均月薪（元）')
plt.title('中国各城市平均薪资排行')
plt.grid(axis='x', alpha=0.3)
for bar, val in zip(bars, sorted_df['avg_salary']):
    plt.text(val + 200, bar.get_y() + bar.get_height()/2, f'{int(val)}', va='center', fontsize=8)
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#ff6b6b', label='一线城市'),
    Patch(facecolor='#ffd93d', label='新一线城市'),
    Patch(facecolor='#6bcb77', label='二线城市'),
    Patch(facecolor='#4d96ff', label='三线城市'),
    Patch(facecolor='#a8a8a8', label='县城'),
]
plt.legend(handles=legend_elements, loc='lower right')
plt.tight_layout()
plt.savefig('output/01_薪资排行.png', dpi=150)
plt.close()
print('图1：薪资排行 → output/01_薪资排行.png')

# 图2：租房压力
plt.figure(figsize=(12, 6))
sorted_rent = df.sort_values('rent_ratio', ascending=True)
colors2 = ['#ff6b6b' if c in ['一线'] else '#ffd93d' if c in ['新一线'] else '#6bcb77' if c in ['二线'] else '#4d96ff' for c in sorted_rent['tier']]
bars2 = plt.barh(sorted_rent['city'], sorted_rent['rent_ratio'], color=colors2)
plt.xlabel('房租占工资比例（%）')
plt.title('各城市租房压力对比')
plt.grid(axis='x', alpha=0.3)
for bar, val in zip(bars2, sorted_rent['rent_ratio']):
    plt.text(val + 0.3, bar.get_y() + bar.get_height()/2, f'{val}%', va='center', fontsize=8)
plt.legend(handles=legend_elements, loc='lower right')
plt.tight_layout()
plt.savefig('output/02_租房压力对比.png', dpi=150)
plt.close()
print('图2：租房压力 → output/02_租房压力对比.png')

# 图3：城市等级对比
plt.figure(figsize=(10, 6))
tier_order = ['一线', '新一线', '二线', '三线', '县城']
tier_data = df.groupby('tier')['avg_salary'].agg(['mean', 'min', 'max']).round(0)
tier_data = tier_data.reindex(tier_order)
x = range(len(tier_order))
plt.bar(x, tier_data['mean'], yerr=[tier_data['mean'] - tier_data['min'], tier_data['max'] - tier_data['mean']],
        capsize=5, color=['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#a8a8a8'])
plt.xticks(x, tier_order)
plt.ylabel('平均月薪（元）')
plt.title('不同线城市平均薪资对比')
for i, v in enumerate(tier_data['mean']):
    plt.text(i, v + 300, f'{int(v)}元', ha='center', fontsize=10)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('output/03_城市等级薪资对比.png', dpi=150)
plt.close()
print('图3：城市等级对比 → output/03_城市等级薪资对比.png')

# 图4：每月结余
plt.figure(figsize=(12, 6))
sorted_save = df.sort_values('disposable_income', ascending=True)
bars4 = plt.barh(sorted_save['city'], sorted_save['disposable_income'],
                  color=['#2ecc71' if v > 8000 else '#f1c40f' if v > 6000 else '#e74c3c' for v in sorted_save['disposable_income']])
plt.xlabel('每月结余（元）')
plt.title('各城市每月可支配收入（薪资 - 基本开销）')
plt.grid(axis='x', alpha=0.3)
for bar, val in zip(bars4, sorted_save['disposable_income']):
    plt.text(val + 100, bar.get_y() + bar.get_height()/2, f'{int(val)}元', va='center', fontsize=8)
plt.tight_layout()
plt.savefig('output/04_每月结余对比.png', dpi=150)
plt.close()
print('图4：每月结余 → output/04_每月结余对比.png')

# 图5：散点图 薪资vs房租
plt.figure(figsize=(10, 8))
tier_colors = {'一线': '#ff6b6b', '新一线': '#ffd93d', '二线': '#6bcb77', '三线': '#4d96ff', '县城': '#a8a8a8'}
for tier in tier_order:
    subset = df[df['tier'] == tier]
    if len(subset) > 0:
        plt.scatter(subset['avg_salary'], subset['rent_1br'],
                    c=tier_colors[tier], label=tier, s=100, alpha=0.7)
        for _, row in subset.iterrows():
            plt.annotate(row['city'], (row['avg_salary'], row['rent_1br']),
                        fontsize=7, alpha=0.8, xytext=(5, 5), textcoords='offset points')
plt.xlabel('平均月薪（元）')
plt.ylabel('一居室月租（元）')
plt.title('薪资 vs 房租：各城市宜居性分析')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('output/05_薪资vs房租散点图.png', dpi=150)
plt.close()
print('图5：散点图 → output/05_薪资vs房租散点图.png')

print()
print('完成！5张图表已保存到 output/ 文件夹')
print('面试可以说："我用 Python 分析了23个城市的薪资与生活成本数据"')
