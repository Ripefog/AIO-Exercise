
def evaluate(tp, fp, fn):
    # Kiem tra xem tp, fp, fn co phai la so nguyen khong
    if type(tp) is not int:
        print("tp must be int")
        return
    if type(fp) is not int:
        print("fp must be int")
        return
    if type(fn) is not int:
        print("fn must be int")
        return
    
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    
    # Tinh f1_score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)

    print(f"precision is {precision}")
    print(f"recall is {recall}")
    print(f"f1-score is {f1_score}")

