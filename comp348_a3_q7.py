import comp348_a3_q5


if __name__ == '__main__':
    shapes = []
    count_dict = {}
    SHAPE_NAME = "shape"
    CIRCLE_NAME = "circle"
    ELLIPSE_NAME = "ellipse"
    RHOMBUS_NAME = "rhombus"

    def doesExist():
        global exists
        global shape_exists
        for k in count_dict:
            if k == reader_split[0].lower() and not k == SHAPE_NAME:
                exists = True
            elif k == SHAPE_NAME:
                shape_exists = True

        if exists:
            count_dict[reader_split[0].lower()] += 1
            count_dict[SHAPE_NAME] += 1
        else:
            if not reader_split[0].lower() == SHAPE_NAME:
                count_dict[reader_split[0].lower()] = 1
            if shape_exists:
                count_dict[SHAPE_NAME] += 1
            else:
                count_dict[SHAPE_NAME] = 1

    fo = open("input.txt", "r")
    reader = fo.readline()

    while reader:
        reader_split = reader.split()
        reader_count = len(reader_split)
        shape_exists = False
        exists = False

        if reader == "\n":
            reader = fo.readline()

        elif reader_split[0].lower() == SHAPE_NAME and reader_count == 1:
            shape = comp348_a3_q5.Shape()
            shapes.append(shape)

            doesExist()

        elif reader_split[0].lower() == CIRCLE_NAME and reader_count == 2 and reader_split[1].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Circle(int(reader_split[1]))
            shapes.append(shape)

            doesExist()

        elif reader_split[0].lower() == ELLIPSE_NAME and reader_count == 3 and reader_split[1].lstrip('-').isnumeric() and reader_split[2].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Ellipse(int(reader_split[1]), int(reader_split[2]))
            shapes.append(shape)

            doesExist()

        elif reader_split[0].lower() == RHOMBUS_NAME and reader_count == 3 and reader_split[1].lstrip('-').isnumeric() and reader_split[2].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Rhombus(int(reader_split[1]), int(reader_split[2]))
            shapes.append(shape)

            doesExist()

        else:
            print("UNKNOWN ERROR")
            fo.close()
            exit(-1)

        reader = fo.readline()
    fo.close()

    sorted_count_dict = dict(sorted(count_dict.items()))  # Sort by key
    # sorted_count_dict = dict(sorted(count_dict.items(), key=lambda item: item[1]))  # Sort by value

    for key in sorted_count_dict:
        if not key == SHAPE_NAME:
            if key == RHOMBUS_NAME:
                print(key.capitalize() + "(es): " + str(sorted_count_dict[key]))
            else:
                print(key.capitalize() + "(s): " + str(sorted_count_dict[key]))
    print("--")
    if SHAPE_NAME in sorted_count_dict:
        print(SHAPE_NAME.capitalize() + "(s): " + str(sorted_count_dict[SHAPE_NAME]))
