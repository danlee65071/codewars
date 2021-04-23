def justify(text, width):
    words = text.split()
    lines = []
    my_sum = 0
    ind = 0
    ind_start = 0
    while ind < len(words):
        my_sum += len(words[ind]) + 1
        if my_sum - 1 == width:
            lines.append([words[i] for i in range(ind_start, ind + 1)])
            ind_start = ind + 1
            my_sum = 0
        elif my_sum - 1 > width:
            ind -= 1
            my_sum = 0
            lines.append([words[i] for i in range(ind_start, ind + 1)])
            ind_start = ind + 1
        elif ind == len(words) - 1:
            lines.append([words[i] for i in range(ind_start, ind + 1)])
        ind += 1
    for line_ind, line in enumerate(lines):
        if len(line) == 1:
            buf_space = [0]
        else:
            sum_words_len = sum([len(x) for x in line])
            min_space = (width - sum_words_len) // (len(line) - 1)
            add_space_steps = width - sum_words_len - min_space * (len(line) - 1)
            if line_ind == len(lines) - 1:
                buf_space = [1 for i in range(len(line) - 1)]
                add_space_steps = 0
            else:
                buf_space = [min_space for i in range(len(line) - 1)]
            for i in range(add_space_steps):
                buf_space[i] = buf_space[i] + 1
        for ind in range(0, len(line) - 1):
            line[ind] = line[ind] + ' ' * buf_space[ind]
        lines[line_ind] = ''.join(line)
    return '\n'.join(lines)

#print(justify("1234567", 7))
print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 30))
