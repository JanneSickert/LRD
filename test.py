import main as m

if __name__ == "__main__":
    local_a_a, local_a_b = 0.6869166, 76.89601688
    s = f"f(x) = {local_a_b} + x * {local_a_a}"
    m.start_lrs()
    from_system = m.create_formula()
    print("test: ", s)
    print("main: ", from_system)
    if from_system == s:
        print("test ok!")
    else:
        print("test faild!")