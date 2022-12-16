# random_pickup

Sample random pickup question, it is easy when you can estimate number of input number of the target ture. 
```
pickup = tf.random.uniform(shape=[ n_random_pickup ], minval=0, maxval=array.shape[0], dtype=tf.int64, seed=10).numpy()
```

## Question ##

Question find matching colors of socks when there are 10 of white color and 10 for black.
```
   [ 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦 ]
   [ 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦 ]
```

## Gnerate input ##

Generate the random number sequences as the question instants and you can change the seed number for next time quiz.
```
random_seed = tf.random.set_seed(1238)
n_objects = 10
n_random_pickup = 3

value = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
input = tf.random.shuffle(
    value, seed=random_seed, name="shuffle"
)
```

## Selection problem ##

Selecting and display
```
n_temp = tf.experimental.numpy.argmax( input, axis=0).numpy()
n_temp = tf.cast( n_temp, dtype=tf.int64 ).numpy()
array = tf.concat( [ input[0:n_temp], input[n_temp + 1:2 * n_objects + 1] ], axis=0 )
array = tf.concat( [ array, [-1] ], axis=0 )
print( 'array: ' + str( array ) )
print( 'array: ' + str( tf.math.count_nonzero( array, dtype=tf.dtypes.int64, ).numpy() ) )
pickup = tf.random.uniform(shape=[ n_random_pickup ], minval=0, maxval=array.shape[0], dtype=tf.int64, seed=10).numpy()
print( 'pickup: ' + str( pickup ) )
for element in pickup :
    print( array[element].numpy() )
```

## Result ##

Result is the input array, 0 as white and -1 is contrast.
```
array: tf.Tensor([ 0  0 -1 -1  0  0 -1 -1 -1 -1  0 -1  0 -1 -1  0  0  0 -1 -1], shape=(20,), dtype=int32)
array: 11
pickup: [19 15  3]
-1
0
-1
```

## Books ##

It is not my book but I think it is kind some some promotions, they added some tips when you reading you talking to librarians of the bookstore, conversation of knowledge desires never wrong in the same pace of good willing .

![Alt text](https://github.com/jkaewprateep/random_pickup/blob/main/03.jpg?raw=true "Title")
![Alt text](https://github.com/jkaewprateep/random_pickup/blob/main/04.jpg?raw=true "Title")
