# объявление функции
def is_one_away(word1, word2):
    """
    Принимает в качестве аргументов два слова word1 и word2 и возвращает значение True,
    если слова имеют одинаковую длину и отличаются ровно в одном символе и False в противном случае.
    :return:
    """
    mismatches = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                mismatches += 1

        return mismatches == 1

    return False


print(is_one_away(input(), input()))