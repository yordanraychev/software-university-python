pool_volume = int(input())
flow_first_pipe = int(input())
flow_second_pipe = int(input())
hours = float(input())

volume_first_pipe = flow_first_pipe * hours
volume_second_pipe = flow_second_pipe * hours
total_volume = volume_first_pipe + volume_second_pipe
percentage_full = total_volume * 100 / pool_volume
overflow = total_volume - pool_volume

if total_volume <= pool_volume:
    print(f"The pool is {percentage_full:.2f}% full. "
          f"Pipe 1: {(volume_first_pipe * 100 / total_volume):.2f}%. "
          f"Pipe 2: {(volume_second_pipe * 100 / total_volume):.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {overflow:.2f} liters.")
