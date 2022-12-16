import tensorflow as tf

# Question find matching colors of socks when there are 10 of white color and 10 for black.
# [ 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦, 🧦 ]
# [ 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦 ], [ 🧦, 🧦, 🧦 ]

random_seed = tf.random.set_seed(1238)

n_objects = 10
n_random_pickup = 3

value = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
input = tf.random.shuffle(
    value, seed=random_seed, name="shuffle"
)

	
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
