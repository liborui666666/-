import random


def guess_number():
    """
    猜数字游戏主函数
    功能：让用户猜测一个随机生成的数字
    """

    print("=== 猜数字游戏 ===")
    print("请输入数字范围(最小值和最大值)")
    
    # 获取并验证数字范围
    while True:
        try:
            min_num = int(input("请输入最小数字(建议0-1000): "))
            max_num = int(input("请输入最大数字(建议10-1000): "))
            
            # 范围验证
            if min_num < 0 and max_num < 0:
                print("错误：最小数字不能为负数！")
                print("错误：最大数字不能为负数！")
                continue
            elif min_num < 0:
                print("错误：最小数字不能为负数！")
                continue
            elif max_num < 0:
                print("错误：最大数字不能为负数！")
                continue
                
            # 基本验证
            if min_num >= max_num:
                print("错误：最小数字必须小于最大数字！")
                continue
                
            if max_num > 1000:
                print("建议使用0-1000范围内的数字以获得最佳体验！")
                
            if max_num - min_num < 2:
                print("错误：最小和最大数字之间必须至少相差2！")
                continue
                
            break
                
        except ValueError:
            print("请输入有效的整数！")
    
    # 生成随机数
    if max_num - min_num == 2:
        target = min_num + 1
    else:
        target = random.randint(min_num, max_num)
    
    attempts = 0
    print(f"游戏开始！我已经想好了一个{min_num}到{max_num}之间的数字。")
    
    # 游戏主循环
    while True:
        guess_input = input(f"请输入你的猜测[{min_num}-{max_num}](输入q退出): ")
        
        # 退出条件
        if guess_input.lower() == 'q':
            print(f"游戏结束，正确答案是: {target}")
            break
            
        try:
            guess = int(guess_input)
            attempts += 1
            
            # 范围检查
            if guess < min_num or guess > max_num:
                print(f"请输入{min_num}-{max_num}范围内的数字！")
                continue
                
            # 判断猜测结果
            if guess < target:
                print("太小了！")
                min_num = guess + 1
            elif guess > target:
                print("太大了！")
                max_num = guess - 1
            else:
                print(f"恭喜！你在{attempts}次尝试后猜对了！")
                break
                
        except ValueError:
            print("请输入有效的整数！")


if __name__ == "__main__":
    guess_number()