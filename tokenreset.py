from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('*67@hjyjhk',120)
    return s.dumps({'user':rollno}).decode('utf-8')
