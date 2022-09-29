import comp348_a3_q5


if __name__ == '__main__':
    shapes = []
    SHAPE_NAME = "shape"
    CIRCLE_NAME = "circle"
    ELLIPSE_NAME = "ellipse"
    RHOMBUS_NAME = "rhombus"

    fo = open("input.txt", "r")
    reader = fo.readline()

    while reader:
        reader_split = reader.split()
        reader_count = len(reader_split)
        error = False

        if reader == "\n":
            reader = fo.readline()

        elif reader_split[0].lower() == SHAPE_NAME and reader_count == 1:
            shape = comp348_a3_q5.Shape()
            shapes.append(shape)
            print(shape)

        elif reader_split[0].lower() == CIRCLE_NAME and reader_count == 2 and reader_split[1].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Circle(int(reader_split[1]))
            shapes.append(shape)
            if not reader_split[1].isnumeric():
                error = True
                print("Error: Invalid " + shape.__class__.__name__)
            print(shape)

        elif reader_split[0].lower() == ELLIPSE_NAME and reader_count == 3 and reader_split[1].lstrip('-').isnumeric() and reader_split[2].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Ellipse(int(reader_split[1]), int(reader_split[2]))
            shapes.append(shape)
            if not (reader_split[1].isnumeric() and reader_split[2].isnumeric()):
                error = True
                print("Error: Invalid " + shape.__class__.__name__)
            print(shape)
            if not error:
                print("linear eccentricity: " + str(shape.eccentricity()))

        elif reader_split[0].lower() == RHOMBUS_NAME and reader_count == 3 and reader_split[1].lstrip('-').isnumeric() and reader_split[2].lstrip('-').isnumeric():
            shape = comp348_a3_q5.Rhombus(int(reader_split[1]), int(reader_split[2]))
            shapes.append(shape)
            if not (reader_split[1].isnumeric() and reader_split[2].isnumeric()):
                error = True
                print("Error: Invalid " + shape.__class__.__name__)
            print(shape)
            if not error:
                print("in-radius: " + str(shape.inradius()))

        else:
            print("UNKNOWN ERROR")
            fo.close()
            exit(-1)

        reader = fo.readline()
    fo.close()
