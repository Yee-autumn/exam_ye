
class Car:
    def __init__(self,color,number):
        self._color=color
        self._number=number

# 模拟C中的析构函数，此处手动调用
    def release(self):
        print(f"车辆{self._number}销毁")

    def display(self):
        print(f"车辆颜色：{self._color},车牌号：{self._number}")


def main():
    car1 =Car("红色",1)
    car2 =Car("蓝色",2)

    car1.display()
    car2.display()

    # 手动模拟析构
    # car1.release()
    car2.release()


if __name__=='__main__':
    main()