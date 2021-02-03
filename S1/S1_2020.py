N = int(input())

obs = {}
obs_arr = []

for i in range(N):
    line = input()
    x = line.index(" ")
    t = int(line[:x]) #time
    p = int(line[x:]) #pos
    obs[t] = p
    obs_arr.append(t)

obs_arr.sort()

speed = 0.0

for i in range(len(obs_arr)):
    if i == N - 1:
        continue
    t_diff = obs_arr[i+1] - obs_arr[i]
    p_diff = abs(obs[obs_arr[i+1]] - obs[obs_arr[i]])
    if p_diff / t_diff > speed:
        speed = p_diff / t_diff

print(speed)

    



    