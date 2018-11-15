# 记录所有的名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("-" * 50)
    print("欢迎使用【名片管理系统】")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("-" * 50)


def new_card():
    """新增名片"""
    print("您当前在使用：新增名片")

    # 1.提示用户输入名片详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2.使用信息建立一个名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}

    # 3.将名片字典添加到列表中
    card_list.append(card_dict)
    print(card_list)

    # 4.提示添加成功
    print("添加 %s 的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("您当前在使用：显示所有名片")

    # 判读是否存在记录，如没有提升用户
    if len(card_list) == 0:
        print("当前没有任何记录，请使用新增功能添加！")

        #返回到调用处，结束函数
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")

    # 打印分割线
    print("=" * 50)

    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """搜索名片"""
    print("您当前在使用：搜索名片")

    #1.提示用户输入搜索姓名
    find_name = input("请输入要查询的姓名：")

    #2.遍历，查询，
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

            # 针对找到的名片记录执行修改和删除操作
            deal_card(card_dict)
            break
    else:
        print("抱歉，没有找到 %s " % find_name)


def deal_card(find_dict):
    """处理函数
    :param find_dict: 查找到的名片
    """
    action_str = input("请输入对名片的操作 "
                       "1.修改 2.删除 0.返回上级：")

    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功！")
    elif action_str == "2":
        card_list.remove(find_dict)
        print("删除名片成功！")


def input_card_info(dict_value, tip_message):
    """修改时
    :param dict_value:字典原有值
    :param tip_message:提示的文字
    :return:如果输入了内容，则返回内容，否则返回原有值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)

    # 2.针对用户输入进行判断，如果输入则返回结果
    if len(result_str) > 0:
        return  result_str

    # 3.如果没有输入值，则返回字典原有值
    else:
        return dict_value
