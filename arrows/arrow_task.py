def any_arrows(arrows):    
    goodArrows = []
    badArrows = []

    if arrows:
        print('not empty')
        for item in arrows:
            if 'damaged' not in item:
                goodArrows.append(item)
            else:
                key, badArrow = 'damaged', True
                keyTwo, goodArrow = 'damaged', False
                if keyTwo in item and goodArrow == item[keyTwo]:
                    goodArrows.append(item)
                elif key in item and badArrow == item[key]:
                    badArrows.append(item)


    if goodArrows and badArrows:
        return True
    elif goodArrows:
        return True
    elif badArrows:
        return False
    else:
        return False
