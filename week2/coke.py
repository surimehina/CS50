def main():
    print("Amount Due: 50")
    all_money = []
    while sum(all_money) < 50:
        money = int(input("Insert coin: "))
        if money in [5, 10, 25]:
            all_money.append(money)
        print("Amount Due: ", sum(all_money))
    print("Change Owed: ", sum(all_money) - 50)
        


main()