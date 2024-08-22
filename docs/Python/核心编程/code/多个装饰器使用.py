def Choice(flag):
    def label(func):
        def inner():
            if flag == 'p':
                return '<p>'+func()+'</p>'
            else:
                return '<div>'+func()+'</div>'
        return inner
    return label
@Choice('div')
def content():
    return "人生苦短，我用python"
res = content()
print(res)