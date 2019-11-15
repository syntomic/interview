zip_str = '[2|A]'

def unzip(zip_str):
    str_ = zip_str[1:-1]
    if str_ == '':
        return
    left = str_.find('[')
    right = str_.rfind(']')

    if left == -1:
        return str_[2:] * int(str_[0]) 
    else:
        return (str_[2:left] + unzip(zip_str[left+1:right+2]) + str_[right+1:]) * int(str_[0])


print(unzip(zip_str))
    
    