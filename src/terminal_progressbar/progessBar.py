import threading
import time


class PrintedProgressBar():
    sym_arr = ['/', u'\u2500', '\\', '|']
    empty = chr(9608)
    full = chr(9617)

    def __init__(self, maximum: int, bar_width: int):
        self.maximum = maximum
        self.bar_width = bar_width
        self.progress = 0
        self.bar = 0
        self.th1 = threading.Thread(target=self.m_print)

    def step(self):
        self.progress += 1
        self.bar = self.bar_width * self.progress // self.maximum

    def m_print(self):

        while True:
            percent = self.progress / self.maximum
            sym = "  " + self.sym_arr[self.progress % 4] + " "
            print(sym + int(self.bar) * self.empty + int(self.bar_width - self.bar) * self.full + f'  {percent:.1%} ',
                  end='\r')
            # print(f'  {percent:.1%} ')
            time.sleep(0.1)
            if self.progress >= self.maximum:
                percent = 1
                print(
                    sym + int(self.bar) * self.empty + int(
                        self.bar_width - self.bar) * self.full + f'  {percent:.0%}  Completed')
                b = (self.bar_width - 9) + 4

                break

    def print_progress(self):
        self.th1.start()


def try_progress_bar():
    n = 1000
    mp = PrintedProgressBar(maximum=n, bar_width=50)
    mp.print_progress()
    for i in range(n + 1):
        time.sleep(0.01)
        mp.step()



try_progress_bar()