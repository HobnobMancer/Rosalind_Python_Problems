# Splice a given string at 4 points, inclusive of given variables
# Given variables: a 62, b 75, c 148, d 154
givenString = "TMKw2vXQr36zvugPHFVw6kBgphFJoLDmVdP2LBF8Qwazliyi83WD7h3vOUfCtnCitharacanthusx2ZA62iKreJpNffrZr4nkq8SguefgJTDwKvDfspWDOjUtSolJomieEpSU7R2kqAQ4AM60hpjdentataMF4u7IwAFxJuDXGu4K8g9sZN"
a = 62
b = 76
c = 148
d = 155

#first splice
firstSplice = givenString[a:b]

#second splice
secondSplice = givenString[c:d]

#Output
print(firstSplice + " " + secondSplice)
