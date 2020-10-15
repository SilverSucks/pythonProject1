import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 4))
x = np.linspace(0, 10, 1000)  # 从0~10 采1000个数，形成一个数组
y = np.sin(x)    # y=sin(x)
z = np.cos(x**2) # z=cos(x)^2
plt.plot(x, y, label="sin(x)", color="red", linewidth=2)
plt.plot(x, z, "b--", label="cos(x^2)")
plt.xlabel("Time(s)") # 设置x轴
plt.ylabel("Volt")    # 设置y轴
plt.title("PyPlot First Example")   # 设置标题
plt.ylim(-1.2, 1.2)
plt.legend()    # 显示图注
plt.savefig('E:\\class\\pycharm_workstation\\picture_location\\first.jpg', dpi=200) # 放在show()之前图片才能正常保存
plt.show()
