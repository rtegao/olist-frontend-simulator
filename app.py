from frontend_simulator.producers.simulate import Simulate
import os

if __name__ == "__main__":
    if 'DOCKER_ENV' in os.environ:
        default_path = 'docker'
    else:
        default_path = 'local'


    simulate_obj = Simulate(chunck_size=10, sleep=1)
    simulate_obj.simulate()
