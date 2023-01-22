def up(some_str):
    """
    Переводит в верхний регистр
    """
    return some_str.upper()


def up_title(some_str):
    """
    Переводит первые буквы в верхний регистр
    """
    new_list = []
    for i in some_str.split():
        new_list.append(i.title())
    return ' '.join(new_list)