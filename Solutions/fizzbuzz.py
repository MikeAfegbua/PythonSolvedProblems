def fizz_buzz(number):
    answer = ''
    if number % 3 == 0:
        answer = 'Fizz'
        if number % 5 == 0:
            answer = answer + 'Buzz'

        return answer
    else:
        return number


val = int(input('enter: '))
print(fizz_buzz(val))
