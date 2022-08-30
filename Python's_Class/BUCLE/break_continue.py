def run():
    for  contador in range(1000):
        if contador % 2 != 0:           # Usage of the word continue to pass a few numbers.
            continue
        print(contador)


    #  for i in range(10000):
    #      print(i)
    #      if i == 5678:                    #Usage of the word break to stop the cycle
    #          break


    # text= input('Type a text')
    # for letter in text:
    #     if letter == 'o':
    #         break
    #     print(letter)


if __name__ == '__main__':
    run()