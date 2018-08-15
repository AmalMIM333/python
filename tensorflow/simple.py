import tensorflow as tf
print ("This program take your first and second exam grade in 3 subjects and display the average ")
print("Enter your grades for subject 1")
print("1st exam")
f1 = int(input())
print("2nd exam")
s1 = int(input())

print("Enter your grades for subject 2")
print("1st exam")
f2 = int(input())
print("2nd exam")
s2 = int(input())

print("Enter your grades for subject 3")
print("1st exam")
f3 = int(input())
print("2nd exam")
s3 = int(input())

f = tf.constant([f1/2,f2/2,f3/2])
s = tf.constant([s1/2,s2/2,s3/2])

result = tf.add(f,s)

sess = tf.Session()
print(sess.run(result))
sess.close()

