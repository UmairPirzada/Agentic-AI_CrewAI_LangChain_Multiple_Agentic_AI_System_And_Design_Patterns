from langgraph.func import entrypoint, task





@task
def task1():
    print("Task 1")
    return "Task 1 Executed"


@task
def task2():
    print("Task 2")    
    return T"ask 2 Executed"
    
    
@entrypoint
def run_flow(input:str):
    print("Running Simple Workflow", input)

    task1_output = task1().result()
    task2_output = task2().result()

    return f"Workflow executed successfully with outputs: {task1_output} and {task2_output}"

    

def     

