# **How-to: Control the thermostat with `my_thermo_stat`**

this guide shows how to determine whether the thermostat should run the heat, the AC, or stay off, using the [my_thermo_stat][functions.my_thermo_stat] function.

## Steps

First step, define the current room temperature (`temp`) and the preferred temperature (`desired_temp`):

```py
temp = 65
desired_temp = 70
```

Second step, call the function with these values:

```py
status = my_thermo_stat(temp, desired_temp)
```

Third step, print the returned value to check what the thermostat should do:

```py
print(status) #Should print out Heat
```

Fourth step, try different values to see how the thermostat responds:

```py
print(my_thermo_stat(80, 70))  # AC
print(my_thermo_stat(72, 70))  # off
```