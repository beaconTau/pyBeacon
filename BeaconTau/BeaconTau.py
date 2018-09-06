from _BeaconTau import * # This imports the c++ defined code from BeaconTau.cpp
import matplotlib.pyplot as plt
import os

class EventAnalyzer():
    """
    Do some useful things with the raw Event and Header classes defined in BeaconTau.cpp
    The magic of pybind11 only gets us so far: it's hard to extend the same c++ classes in python.
    Inheritance is also pain to implement (it's difficult and would be inefficient to copy data to the derived class).
    So instead this we have this EventAnalyzer class that has event and header members, and does useful things with them.
    """

    def __init__(self, header, event):
        if header.event_number != event.event_number:
            raise ValueError('Mismatched header and event!')
        self.header = header
        self.event = event

    def __repr__(self):
        return '<BeaconTau.EventAnalyzer for event ' + str(self.event.event_number) + '>'

    def plot(self, n_rows = 2, show = False):
        for board in self.event.data:
            n_cols = int(len(board)/n_rows)
            fig, axes = plt.subplots(n_rows, n_cols, sharey = True)
            for channel, waveform in enumerate(board):
                axes.flat[channel].plot(waveform[:self.event.buffer_length])
                axes.flat[channel].set_title('Channel' + str(channel+1))
        plt.suptitle('Event ' + str(self.event.event_number))



class DataDirectory():
    """
    High level interface to the BEACON data directory structures.
    Allows iteration over runs.

    First looks in an optional data_dir string.
    If one is not provided, then it looks for a BEACON_DATA_DIR environment variable.
    If there isn't one it looks in the current directory.
    If it doesn't find any run subfolders in any of those places, it gives up.
    """
    def __init__(self, data_dir = None):

        self.data_dir = data_dir

        if self.data_dir == None:
            try:
                self.data_dir = os.environ['BEACON_DATA_DIR']
                print('Found ' + self.data_dir + ' from BEACON_DATA_DIR')
            except:
                print('No BEACON_DATA_DIR environment variable, setting to current directory')
                self.data_dir = os.getcwd()

        self.run_dirs = [d for d in os.listdir(self.data_dir) if 'run' in d]

        if len(self.run_dirs) == 0:
            raise ValueError("Couldn't find any runs under " + self.data_dir)

        self.runs = sorted([int(x.strip('run')) for x in self.run_dirs])
        self._i =  0

    def __repr__(self):
        return '<BeaconTau.DataDirectory containing runs' + str(self.runs) + '>'

    def __iter__(self):
        return self

    def __next__(self):
        if self._i < len(self.runs):
            self._i += 1 # For next call to __next__
            return RunReader(self.runs[self._i - 1], self.data_dir)
        else:
            raise StopIteration

    def run(self, run_number):
        run_index = -1
        try:
            run_index = self.runs.index(run_number)
        except:
            raise ValueError('No run ' +  str(run_number) + ' in ' + self.data_dir + ', available runs are ' + str(self.runs))

        return RunReader(run_number, self.data_dir)

def main():
    d = DataDirectory()

    for r in d:
        a = EventAnalyzer(r.headers[0],  r.events[0])
        a.plot(show = True)
    plt.show()
    return 0;

    r = RunReader(99, '../../data')

    evs = [h.event_number for h in r.headers]
    rot = [st.readout_time for st in r.statuses]
    threshs = [st.trigger_thresholds for st in r.statuses]
    threshs2 = list(map(list, zip(*threshs)))
    plt.xlabel('Time (seconds)')
    plt.ylabel('Threshold (???)')
    plt.title('BEACON Thresholds')
    for channel, t in enumerate(threshs2, 1):
        plt.plot(rot, t, label = 'Channel' + str(channel))
    plt.legend()

    plt.show()

if __name__ == '__main__':
    main()
