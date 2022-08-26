1) Stwórz klasę Tank (zbiornik).
Zbiornik posiada następujące atrybuty: nazwę oraz pojemność.
Należy stworzyć następujące operacje:
pourWater(volume) - ale w zbiorniku nie może być więcej wody niż pojemność
pourOutWater(volume) - ale nie można odlać więcej wody niż jest dostępne w zbiorniku
transferWater(from, volume) - przelewa wodę ze zbiornika "from" do naszego (pod warunkiem, że przelewanie jest możliwe)
Dodatkowo stworzyć metody, które pozwalają:
Znaleźć zbiornik, w którym jest najwięcej wody
Znaleźć zbiornik, który jest najbardziej zapełniony
Znaleźć wszystkie puste zbiorniki
2) Każda operacja na zbiorniku jest rejestrowana.
Dla każdej operacji pamiętamy: datę i czas jej wykonania, jej nazwę, zbiornik, na którym była ona wykonana oraz ilość wody, jaka była brana pod uwagę oraz to, czy operacja się powiodła czy nie.

Należy zaimplementować taką funkcjonalność oraz dodatkowo stworzyć metody, które:
Pozwalają znaleźć zbiornik, na którym było najwięcej operacji zakończonych niepowodzeniem
Pozwalają znaleźć zbiornik, w którym było najwięcej operacji danego typu (typ podajemy jako argument metody)

3) To co zaimplementowaliśmy powyżej to demo "Event Sourcingu" - na czym ono polega?
Zaimplementuj metodę checkState(volumeName), która pozwoli określić, czy stan wody jest spójny z tym, co mamy na liście historii operacja dla danego zbiornika. 