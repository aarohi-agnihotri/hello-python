
## Exponential Backoff

**Exponential Backoff** is a strategy used when something **fails**, like:
- internet request fails
- server not responding
- API call fails

Instead of retrying immediately every second, you **wait longer and longer** between each retry:

```
Retry 1 → wait 1 second
Retry 2 → wait 2 seconds
Retry 3 → wait 4 seconds
Retry 4 → wait 8 seconds
Retry 5 → wait 16 seconds
→ stop after 5 retries
```

Each wait time is **double** the previous one, that's why it's called **exponential**.

**Why not retry immediately?**
- if server is overloaded, hitting it again and again makes it worse
- giving it more time helps it recover

**Real world example:**
- your phone can't connect to wifi → tries after 1s, then 2s, then 4s... instead of trying every second!

## Code Explanation

### `import time`
- `time` is a built-in Python module
- gives access to time-related functions
- needs to be imported before using

### `time.sleep()`
- pauses the program for given seconds
- `time.sleep(1)` → pauses for 1 second
- `time.sleep(2)` → pauses for 2 seconds

---

### How the program works:

| Attempt | Wait Time | After `*= 2` |
|---------|-----------|--------------|
| 0       | 1 sec     | 2            |
| 1       | 2 sec     | 4            |
| 2       | 4 sec     | 8            |
| 3       | 8 sec     | 16           |
| 4       | 16 sec    | 32           |

- `wait_time *= 2` → doubles wait time each attempt
- `attempts += 1` → counts each retry
- loop stops when `attempts == 5` (max_retries)

### Why `while` and not `for`?
- `while` is preferred here because in real world
the retry count can be dynamic, not always fixed at 5
