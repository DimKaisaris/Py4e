text = "X-DSPAM-Confidence:    0.8475"
x=text.find('0')
y=text[x:]
z=float(y)
print(z)
