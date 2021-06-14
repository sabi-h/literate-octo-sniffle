
def predict(current_balance: float, regular_income: float, predict_months: int) -> list:
    total_income = regular_income * predict_months
    spendings = total_income * 0.7
    return int(current_balance + total_income - spendings)


if __name__ == "__main__":
    print(
        f"Current Balance: £500", 
        f"Regular Income: £500",
        f"Predicted Balance (1 month): £{predict(500, 500, 1)}",
        sep='\n',
        end='\n\n'
    )
    print(
        f"Current Balance: £500", 
        f"Regular Income: £500",
        f"Predicted Balance (3 month): £{predict(500, 500, 3)}",
        sep='\n',
        end='\n\n'
    )
    print(
        f"Current Balance: £500", 
        f"Regular Income: £500",
        f"Predicted Balance (6 month): £{predict(500, 500, 6)}",
        sep='\n',
        end='\n\n'
    )
