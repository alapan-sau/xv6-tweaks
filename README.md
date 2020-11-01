# xv6-tweaks

## System calls

### waitx()

#### Synonsis
```c
int waitx(int* wtime, int*rtime)
```
#### Description
The two arguments are pointers to integers to which waitx will assign the total number of clock ticks during which process was waiting and the total number of clock ticks when the process was running.
#### Return values
It returns the 0 on success, and -1 on failure.

### set_priority()

#### Synopsis
```c
int set_priority(int new_priority, int pid)
```
#### Description
The system-call sets the priority of a process `pid` to `new_priority` between 0 to 100. In case the priority of the process increases (the value is lower than before), then rescheduling should be done immediately (for PBS scheduler).

#### Return values
It returns the `old_priority` on success, and -1 on failure.

### ps()

#### Synopsis
```c
void ps()
```

#### Description
This system call lists some basic information about all the active processes as explained.
- `Priority` - ​Current priority of the process (defined as per the need of schedulers below)
- `State` - ​Current state of the process
- `r-time` - ​Total time for which the process ran on CPU till now (use a
suitable unit of time)
- `w-time` - ​Time for which the process has been waiting (reset this to 0
whenever the process gets to run on CPU or if a change in the queue takes place (in the case of MLFQ scheduler))
- `n_run` - ​Number of times the process was picked by the scheduler
- `cur_q` - ​Current queue (check task 2 part C)
- `q{i}` ​- Number of ticks the process has received at each of the 5 queues.

## Schedulers

### FCFS
Implemented with a non-preemptive policy that selects the process with the lowest creation time. The chosen process runs until it no longer needs CPU time.

### Round Robin
This is the default scheduler implemented in the xv6. It picks a process and runs it for one time quanta(1 clock tick). All processes are priority-neutral to the scheduler.

### Priority Based Scheduler(PBS)
Each process has a priority associated with it between `0` to `100`  (`60 by default`).The scheduler selects the process with the highest priority for execution. In case two or more processes have the same priority, selection is done in a round-robin fashion. The scheduler also has a time quantum of 1 clock tick. After every clock tick, it checks for arrival of any process with higher priority.

### Multilevel Feedback Queue(MLFQ)
There are five priority queues, with the highest priority being number as 0 and the bottom queue with the lowest priority as 4.
The time-quantum for priority 0 is 1 timer tick. The time-quantum for priority 1 is 2 timer ticks; for priority 2, it is 4 timer ticks; for priority 3, it is 8 timer ticks; for priority 4, it is 16 timer ticks.<br>
On the initiation of a process, it is pushed to the end of the highest priority queue.<br>
If the process uses the complete time slice assigned for its current priority queue, it is preempted and ​inserted at the end of the next lower level queue. If a process voluntarily relinquishes control of the CPU, it leaves the queuing network, and when the process becomes ready again after the I/O, it is​ ​inserted at the tail of the same queue, from which it is relinquished earlier​.<br>
`NOTE : A process might exploit this by intentionally relinquising the control of CPU just before the last tick`
<br><br>
A round-robin scheduler should be used for processes at the lowest priority queue.<br>
To prevent `starvation`, we implement `aging` by limiting the waiting time for 10,20,30 and 40 clock ticks in q0, q1, q3, q4 respectively.

### Comparision


