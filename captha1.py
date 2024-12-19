import random as r
from captcha.image import ImageCaptcha as i
image = i(width = 280, height = 90) 
a = r.randint(0,9)
b = r.randint(0,9)
c = r.randint(0,9)
d = r.randint(0,9)
e = r.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
f = r.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
l_1 = [str(a),str(b),str(c),str(d),e,f]
r.shuffle(l_1)
j = ""
for i in l_1:
    j+=i
data = image.generate(j)
image.write(j, 'CAPTCHA.png')
print(j)