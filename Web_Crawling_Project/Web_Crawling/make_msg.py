
def make_msg(df, col):
    msg = []
    if col == "단어":
        msg.append("=================================\n")
        msg.append("{} : {}\n".format(col, df[col]))
        msg.append("------------------------------------\n")
    elif col == '뜻':
        msg.append(" {} :\n".format(col))
        for ls in df[col]:
            msg.append("  {}\n".format(ls))
        msg.append("------------------------------------\n")
    elif col == '문법':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")
    elif col == '문장예시':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")    
    elif col == '반의어':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n") 
    elif col == '복합어・숙어':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")   
    elif col == '유의어':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")
    elif col == '테마 단어':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")
    elif col == '파생어':
        if df[col] == -1:
            pass
        else:
            msg.append(" {} :\n".format(col))
            for ls in df[col]:
                msg.append("  {}\n".format(ls))
            msg.append("------------------------------------\n")
    return "".join(msg)
