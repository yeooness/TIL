# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
# apple
word = 'apple'
reverse_word= ''

for a in word:
    reverse_word = a + reverse_word
print(reverse_word)