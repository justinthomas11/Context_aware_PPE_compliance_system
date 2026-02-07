import time

def run_loop(pipeline, steps=20):
    for _ in range(steps):
        pipeline.step()
        time.sleep(0.5)
