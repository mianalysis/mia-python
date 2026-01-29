from __future__ import annotations
from jpype import JImplements, JOverride # type: ignore
from weakref import WeakKeyDictionary

from src.objects.measurement import Measurement

_wrapper_cache: WeakKeyDictionary[Measurement, MeasurementWrapper] = WeakKeyDictionary()

@JImplements('io.github.mianalysis.mia.object.measurements.MeasurementI')
class MeasurementWrapper:
    def __init__(self, name: str, value: float):
        self._measurement: Measurement = Measurement(name, value)
        
    def setPythonMeasurement(self, measurement: Measurement):
        self._measurement = measurement
        
    def getPythonMeasurement(self) -> Measurement:
        return self._measurement
    
    @JOverride
    def duplicate(self) -> MeasurementWrapper:
        return wrapMeasurement(self._measurement.duplicate())

    @JOverride
    def getName(self) -> str:
        return self._measurement.getName()
    
    @JOverride
    def getValue(self) -> float:
        return self._measurement.getValue()
    
    @JOverride
    def setValue(self, value: float):
        self._measurement.setValue(value)


@JImplements('io.github.mianalysis.mia.object.measurements.MeasurementFactoryI')
class MeasurementFactoryWrapper:
    
    @JOverride
    def getName(self) -> str:
        return "Python measurement factory"
    
    @JOverride
    def duplicate(self) -> MeasurementFactoryWrapper:
        return MeasurementFactoryWrapper()

    @JOverride
    def createMeasurement(self, name: str, value: float) -> MeasurementWrapper:
        return MeasurementWrapper(name, value)


def wrapMeasurement(measurement: Measurement) -> MeasurementWrapper:
    try:
        return _wrapper_cache[measurement]
    except:        
        measurement_wrapper: MeasurementWrapper = MeasurementWrapper("",0)
        measurement_wrapper.setPythonMeasurement(measurement)
        _wrapper_cache[measurement]  = measurement_wrapper
    
        return measurement_wrapper
