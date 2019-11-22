from .actions import Text


def formatted_text(capitalisation, spacing, t):
    if capitalisation == 0:
        capitalisation = 5
    if spacing == 0 and capitalisation == 3:
        spacing = 1

    if capitalisation == 6:
        t = "".join(t.split(" "))
        t = t.lower()
        punc = "@1/4#9?5%,."
        result = []
        for i in range(len(t)):
            if i%2==0:
                result.append(punc[(i/2)%len(punc)])
            if i%3==0:
                result.append(t[i].upper())
            else:
                result.append(t[i])
        t = "".join(result)
    elif capitalisation != 0:
        if capitalisation == 1:
            t = t.upper()
        elif capitalisation == 2:
            t = t.title()
        elif capitalisation == 3:
            if len(t) > 1:
                t = t.title()
                t = t[0].lower() + t[1:]
            else:
                t = t[0].lower()
        elif capitalisation == 4:
            t = t.capitalize()
        elif capitalisation == 5:
            t = t.lower()
    if spacing != 0:
        if spacing == 1:
            t = "".join(t.split(" "))
        elif spacing == 2:
            t = "-".join(t.split(" "))
        elif spacing == 3:
            t = "_".join(t.split(" "))
        elif spacing == 4:
            t = ".".join(t.split(" "))
        elif spacing == 5:
            t = "/".join(t.split(" "))
        elif spacing == 6:
            t = "\\".join(t.split(" "))
        elif spacing == 7:
            t = ", ".join(t.split(" "))
    return t

def master_format_text(capitalisation, spacing, text):
    Text(formatted_text(capitalisation, spacing, text)).execute()