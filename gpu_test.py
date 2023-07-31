import tensorflow as tf
import winsound

gpu_devices = tf.config.list_physical_devices('GPU')
if gpu_devices:
   details = tf.config.experimental.get_device_details(gpu_devices[0])
   details.get('device_name', 'Unknown GPU')
   print(details)
