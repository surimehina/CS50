def main():
    print("Amount Due: 50")
    is_enough()

def is_enough():
    all_money = []
    while True:
        money = int(input("Insert coin: "))
        temp = 0

        if money > 25:
            money = 0
            money = money - temp

        all_money.append(money)
        sum_money = sum(all_money)
        print("Amount Due: ", sum_money)

        if sum_money >= 50:
            print("Change Own: ", abs(50 - sum_money) + temp)
            break            
# 原测试例似乎存在问题，在投入25之后再投入10，例子中还要投入的钱居然变成40了

main()