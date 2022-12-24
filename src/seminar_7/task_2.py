# 2) Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
#
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна.
#
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    # Read only by object space-vision available
    # and block reset var (Python way)
    # Толщина по ГОСТ
    @property
    def _thinkness_asphalt(self):
        return 5

    @_thinkness_asphalt.setter
    def _thinkness_asphalt(self, value):
        pass

    @property
    def _need_kg_per_quad_meter(self):
        return 25

    @_need_kg_per_quad_meter.setter
    def _need_kg_per_quad_meter(self, value):
        pass

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_weight_asphalt(self):
        return self._lenght * self._width \
               * self._thinkness_asphalt * self._need_kg_per_quad_meter


if __name__ == '__main__':
    road = Road(20, 5000)

    print(f"Need ton - {road.calc_weight_asphalt() / 1000}")