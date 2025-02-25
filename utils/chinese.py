CHINESE_DIGITS = {'一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, 
                      '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100}


def chinese_to_number(text):

    def convert(chinese_num):
        if chinese_num in CHINESE_DIGITS:
            return CHINESE_DIGITS[chinese_num]
        
        if "百" in chinese_num:
            parts = chinese_num.split("百")
            left = CHINESE_DIGITS.get(parts[0], 1)
            right = convert(parts[1]) if parts[1] else 0
            return left * 100 + right
        
        if "十" in chinese_num:
            parts = chinese_num.split("十")
            left = CHINESE_DIGITS.get(parts[0], 1) if parts[0] else 1 
            right = CHINESE_DIGITS.get(parts[1], 0) if parts[1] else 0
            return left * 10 + right

        return sum(CHINESE_DIGITS[c] for c in chinese_num) 

    return convert(text)


if __name__ == "__main__":
    # test_text = "三十二"
    # test_text = "三百一十六"
    test_text = "两"
    print(chinese_to_number(test_text))


