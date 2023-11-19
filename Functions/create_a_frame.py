def frame(text, char):
    if ',' in text:
        text = text.split()
        h = len(text)
        w = 0
        lines = ''
        for t in text:
            if len(t) > w:
                w = len(t)
                lines += t
        w = len(w) * '*'
        returning_list = f'{w, end='\n'}, okay'
        
        return 
