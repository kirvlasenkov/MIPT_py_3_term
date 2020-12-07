### Приведу отличия на примере определений:
**Процесс** — экземпляр программы во время выполнения, независимый объект, имеющий свои собственные системные рецурсы, такие как:
- Образ машинного кода
- область памяти, вместе с IO данными процесса, стеком вызовов и кучей для динамически создаваемых данных
- дескрипторы операционной системы, а также состояние процесса

При этом он выполняется в отдельном адресном пространстве, то еть напрямую не может получить доступ к работе другого процесса, а только через межпроцессорные взаимодействия (например, файлы, каналы связи между компами).

**Поток** -наименьшая единица обработки, исполнение которой может быть назначено ядром операционной системы. Фактически, потоки создаются внутри отдельного процесса, также имея доступ ко всем системным ресурсам своего процесса. Каждый поток обладет собственным набором регистров и собственным стеком вызова, но доступ к ним имеют и другие потоки. При этом есть некоторые особенности работы потоков:
- одно ядро процессора в один момент может исполнять только один поток
- потоки одного процесса могут исполняться физически одновременно (на разных ядрах)
- не имеет смысла порождать потоков больше, чем  ядер