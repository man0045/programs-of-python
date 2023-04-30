def get_fraction(value, idx):
    arr=[4,5,2,0]
    idx_value = arr[idx]
    value/idx_value
if __name__ =='__main__':
    value = 54
    idx = 5
    try:
        result = get_fraction(value, idx)
        print("fraction is ", result)
    except IndexError:
        print("idx of {} is out of range". format(idx))
    except ZeroDivisionError:
        print("arr[{}] is 0 . hence , can't divide by zero".format(idx))
    except Exception as ex:
        print(ex)
        print("Not sure what happened so not safe to continue , \ app will be interrupted")
        raise ex