def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]


words = ["дед", "шалаш", "око"]
#google подсказал более рациональный способ через any.Но если как обычно, то можно ввести переменную и цикл, который будет перебирать каждую букву и при совпадении добавлять счетчик,если буквы совпадают, потом попросить принтануть true, если счетчик больше 0


has_palindrome = any(is_palindrome(w) for w in words)

print(f"Хоть одно слово палиндром: {has_palindrome}")
