b = int(input("nhập số nguyên dương n: "))
if b < 0:
    print("phải nhập số nguyên dương!")
else:
    daonguoc = 0
    goc = b
    while b > 0:
        phandu = b % 10
        daonguoc = daonguoc * 10 + phandu
        b = b // 10
    print(f"số đảo ngược của n = {goc} -> {daonguoc}")
        
