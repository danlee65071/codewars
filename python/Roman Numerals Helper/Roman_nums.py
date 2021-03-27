class RomanNumerals:
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    @staticmethod
    def to_roman(num):
        rank = {1: 'IVX', 2: 'XLC', 3: 'CDM', 4: 'M'}
        counter_rank = 1
        res = ''
        for digit in str(num)[::-1]:
            if 4 > int(digit) > 0:
                for i in range(int(digit)):
                    res = rank[counter_rank][0] + res
            elif int(digit) == 4:
                res = rank[counter_rank][0] + \
                      rank[counter_rank][1]
            elif int(digit) == 5:
                res = rank[counter_rank][0] + \
                       rank[counter_rank][1] + res
            elif 5 < int(digit) < 9:
                res = rank[counter_rank][1] + res
                for i in range(int(digit) - 5):
                    res += rank[counter_rank][0]
            elif int(digit) == 9:
                res = rank[counter_rank][0] + \
                       rank[counter_rank][2] + res
            counter_rank += 1
        return res

    @staticmethod
    def from_roman(num):
        prev_digit = RomanNumerals.roman_nums[num[-1]]
        res = 0
        for digit in num[::-1]:
            if prev_digit <= RomanNumerals.roman_nums[digit]:
                res += RomanNumerals.roman_nums[digit]
            else:
                res -= RomanNumerals.roman_nums[digit]
            prev_digit = RomanNumerals.roman_nums[digit]
        return res


print(RomanNumerals.from_roman('M'))
print(RomanNumerals.to_roman(19))
print(RomanNumerals.to_roman(4))
print(RomanNumerals.to_roman(2008))
print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(1990))
