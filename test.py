from progress.bar import ChargingBar
import time

lengthofsong = 100
bar = FillingSquaresBar('progress |', suffix='| songlength', max = lengthofsong)
for i in range(lengthofsong):
    time.sleep(0.1)
    # Do some work
    bar.next()
bar.finish()
