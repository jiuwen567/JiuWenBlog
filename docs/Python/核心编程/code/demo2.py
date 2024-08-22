def config_name(name):
    def config_msg(msg):
        print(name+':'+msg)
    return config_msg

Alice = config_name('爱丽丝')
Bob = config_name('鲍勃')

Alice('你好，Bob')
Bob('你好呀')