### 18번 줄

```python
    if -1 < time_arr[ni][nj] < time: # 이미 저장된 시간이 현재 시간보다 작으면, 고려할 필요x
        break
```
![image](https://github.com/user-attachments/assets/011d0bfe-2dbe-4823-9e9d-d6797a9007c9)

---

### 20번 줄

```python
    if -1 < time_arr[ni][nj]: # 이미 저장된 시간이 현재 시간보다 크거나 같으면, 같은 방향 다음 칸 검사
        continue
```
![image](https://github.com/user-attachments/assets/e537e2a4-4888-4ea4-b0dc-82b497a5b7fb)

- 다음 턴 진행될 때, 값이 증가하기 때문

![image](https://github.com/user-attachments/assets/fceee306-5c99-473f-9bfb-5f78f42d7a08)