# 1) update() :-

ep_1={123:34,127:44,157:57}
ep_2={222:22,233:34,277:55}
print("Before update() :-")
print(ep_1)
print(ep_2)
ep_1.update({157:73})
ep_2.update(ep_1)
print("After update() method :-")
print(ep_1)
print(ep_2)

# 2) clear() :-

ep_1={123:34,127:44,157:57}
print("Before clear() :-")
print(ep_1)
ep_1.clear()
print("After clear() :-")
print(ep_1)


# 3) pop() :-

ep_1={123:34,127:44,157:57}
print("Before pop() :-")
print(ep_1)
print("After pop() :-")
ep_1.pop(127)
print(ep_1)


# 4) popitem() :-

ep_1={123:34,127:44,157:57}
print("Before popitem() :-")
print(ep_1)
print("After popitem() :-")
ep_1.popitem()
print(ep_1)

# 5) del :-

ep_1={123:34,127:44,157:57}
ep_2={222:22,233:34,277:55}
print("Before using del :-")
print(ep_1)
print(ep_2)
print("After using del :-")
del ep_1[127]
del ep_2
print(ep_1)
# print(ep_2) #  NameError: name 'ep_2' is not defined. Did you mean: 'ep_1'?