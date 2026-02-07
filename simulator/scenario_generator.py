import time

def run_loop(pipeline, interval=5):
    while True:
        pipeline.step()
        time.sleep(interval)
