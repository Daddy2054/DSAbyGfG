def func(n):
    if n>4000:
        return
    print(n)
    func(n*2)
    print(n)

func(1000)