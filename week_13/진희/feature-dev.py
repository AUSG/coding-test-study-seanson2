def solution(progresses, speeds):
    answer = []
    while (len(progresses) != 0):
        comp_job_count = 0
        i = 0
        while (i < (len(progresses))):
            progresses[i] = progresses[i]+speeds[i]
            if (i == 0 and progresses[i] >= 100):
                progresses.pop(0)
                speeds.pop(0)
                comp_job_count = comp_job_count + 1
                i = 0
            else:
                i = i+1

        if (comp_job_count > 0):
            answer.append(comp_job_count)
    return answer


progresses = [93, 30, 55, 23, 56, 44]
speeds = [1, 30, 5, 1, 20, 50]
print(solution(progresses, speeds))
