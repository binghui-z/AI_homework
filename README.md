# AI_homework

本项目集成了GA,ACO,PSO三种路劲规划算法，并通过GUI进行交互操作，最终通过可视化进行分析
<div align=center>
<img src="/figure/gui.png" />
</div>


## 使用说明
1. 输入文件的路径，该路径包含预定义的城市坐标；（确定/更换）
2. 输入每个算法要迭代的次数；（确定/清空）

## 测试
迭代次数统一设置为500
<div align=center>
<img src="/figure/result.png" />
</div>

## 打包为exe
1. pyinstaller -F visual.py
2. pyinstaller visual.spec

注：
- a.单个py文件 https://blog.csdn.net/yql_617540298/article/details/112441159
- b.多个py文件相互依赖https://blog.csdn.net/weixin_43502949/article/details/101057825,&& https://blog.csdn.net/qq_45193872/article/details/123563085


## reference
1. 感谢 https://github.com/kellenf/TSP_collection 提供了算法思路;
2. 感谢 https://github.com/WHU-gentle/AI-RomaniaProblem 提供了GUI思路;
3. 感谢 https://github.com/425776024/TSP-GA-py 提供了问题的应用场景;