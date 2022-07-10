def chain(*iterables):
    for it in iterables:
        yield from it
    
print( list(chain('hello', ['world','of'], ('tuple','of','values'))))

print()

def sequence(name, start, end):
    print('%s 제네레이터에서 %i 시작'%(name, start))
    yield from range(start, end)
    print('%s 제네레이터에서 %i 종료' %(name, end))
    return end

def main():
    step1 = yield from sequence('first', 0,5)
    step2 = yield from sequence('second', 6, 8)

g = main()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(next(g))
class CustomException(Exception):
    pass

def sequence2(name, start, end):
    value = start
    print('%s 제네레이터에서 %i 시작'%(name, start))
    while value < end:
        try:
            received = yield value
            print('%s 제네레이터 %r 값 수신' %(name, received))
            value += 1
        except CustomException as e:
            print('%s 제네레이터 %s 에러처리' % (name, e))
            received = yield 'ok'
        
    return end

def main2():
    step1 = yield from sequence2('first', 0,5)
    step2 = yield from sequence2('second', 6, 8)

g = main2()
print(next(g))
print(next(g))
g.send('first generator args value ')
g.throw(CustomException('throwable exception throws!!!'))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
g.throw(CustomException('forward Second Generator, throwable exception throws!!!'))
g.close()
print(next(g))



