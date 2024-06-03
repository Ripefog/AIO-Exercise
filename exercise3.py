import random
import math

def exercise3():
    # Nhap so luong input tu user
    num_samples = input("Input number of samples (integer number) which are generated: ")

    # Kiem tra xem num_samples co hop le hay khong
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)

    # Nhap ten ham loss tu user
    loss_name = input("Input loss name (MAE, MSE, RMSE): ").strip().upper()

    total_loss = 0

    for i in range(num_samples):
        pred = random.uniform(0, 10)
        target = random.uniform(0, 10)

        if loss_name == "MAE":
            loss = abs(pred - target)
        elif loss_name == "MSE":
            loss = (pred - target) ** 2
        elif loss_name == "RMSE":
            loss = (pred - target) ** 2
        else:
            print(f"{loss_name} is not supported")
            return
        
        total_loss += loss
        
        print(f"loss name: {loss_name}, sample: {i}, pred: {pred}, target: {target}, loss: {loss}")
    
    if loss_name == "RMSE":
        final_loss = math.sqrt(total_loss / num_samples)
        print(f"final RMSE: {final_loss}")
    else:
        final_loss = total_loss / num_samples
        print(f"final {loss_name}: {final_loss}")


exercise3()