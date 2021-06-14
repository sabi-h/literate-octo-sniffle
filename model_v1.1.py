
def predict(current_balance: float, regular_income: float, predict_months: int) -> list:
    total_income = regular_income * predict_months
    spendings = total_income * 0.7
    return int(current_balance + total_income - spendings)


if __name__ == "__main__":
    print(predict(500, 500, 1))
    print(predict(500, 500, 3))
    print(predict(500, 500, 6))
