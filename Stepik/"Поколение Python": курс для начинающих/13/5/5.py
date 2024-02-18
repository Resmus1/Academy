# https://stepik.org/lesson/334150/step/6?unit=317559
def is_one_away(word1, word2):
    """
    Принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
    если слова имеют одинаковую длину и отличаются ровно в одном символе и False в противном случае.
    :return:
    """
    cnt = 0
    if len(word1) != len(word2) or word1 == word2:
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
            if cnt > 1:
                return False
    return True


print(is_one_away(input(), input()))
