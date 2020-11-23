Фактически этот модуль при выполнении программы создает копии интерпретатора **Python** вместе со всей программой и параллельно каждый процесс вычисляет, что должен вычислять
. На чуть более подкапотном уровне это можно реализовать при помощи `os.fork`, и далее по PID организовывать, что должен делать дочерний, а что родительский процессы.

Память между процессами никак не делится, так как создаются полностью автономные копии родительского процесса. 