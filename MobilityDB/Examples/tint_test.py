from datetime import datetime, timedelta
from bdateutil.parser import parse
from spans.types import Range
from MobilityDB.TimeTypes import TimestampSet, Period, PeriodSet
from MobilityDB.MainTypes import TInt, TIntInst, TIntI, TIntSeq, TIntS

"""
class floatrange(Range):
	__slots__ = ()
	type = float
"""

print("\nConstructors for TFloatInst")
inst = TIntInst('10@2019-09-08')
print(inst)
inst = TIntInst('10', '2019-09-08')
print(inst)
t = parse('2019-09-08')
inst = TIntInst(10, t)
print(inst)

print("\nConstructors for TIntI")
ti = TIntI('{10@2019-09-08, 20@2019-09-09, 20@2019-09-10}')
print(ti)
ti = TIntI('10@2019-09-08', '20@2019-09-09', '20@2019-09-10')
print(ti)
ti = TIntI(['10@2019-09-08', '20@2019-09-09', '20@2019-09-10'])
print(ti)
t1 = TIntInst('10@2019-09-08')
t2 = TIntInst('20@2019-09-09')
t3 = TIntInst('20@2019-09-10')
ti = TIntI(t1, t2, t3)
print(ti)
ti = TIntI([t1, t2, t3])
print(ti)

print("\nConstructors for TIntSeq")
seq = TIntSeq('[10@2019-09-08, 20@2019-09-09, 20@2019-09-10]')
print(seq)
seq = TIntSeq(['10@2019-09-08', '20@2019-09-09', '20@2019-09-10'])
print(seq)
seq = TIntSeq([t1, t2, t3])
print(seq)
seq = TIntSeq([t1, t2, t3], False, True)
print(seq)

print("\nConstructors for TIntS")
ts = TIntS('{[10@2019-09-08, 20@2019-09-09, 20@2019-09-10],[15@2019-09-11, 30@2019-09-12]}')
print(ts)
ts = TIntS(['[10@2019-09-08, 20@2019-09-09, 20@2019-09-10]', '[15@2019-09-11, 30@2019-09-12]'])
print(ts)
seq1 = TIntSeq('[10@2019-09-08, 20@2019-09-09, 20@2019-09-10]')
seq2 = TIntSeq('[15@2019-09-11, 30@2019-09-12]')
ts = TIntS([seq1, seq2])
print(ts)

print("\n__class__ ")
print(inst.__class__.__name__)
print(ti.__class__.__name__)
print(seq.__class__.__name__)
print(ts.__class__.__name__)

print("\n__bases__ ")
print(inst.__class__.__bases__)
print(ti.__class__.__bases__)
print(seq.__class__.__bases__)
print(ts.__class__.__bases__)

print("\nduration")
print(inst.duration())
print(ti.duration())
print(seq.duration())
print(ts.duration())

print("\ninterpolation")
print(seq.interpolation())
print(ts.interpolation())

print("\ngetValue")
print(inst.getValue())

print("\ngetValues")
print(inst.getValues())
print(ti.getValues())
print(seq.getValues())
print(ts.getValues())

print("\nstartValue")
print(inst.startValue())
print(ti.startValue())
print(seq.startValue())
print(ts.startValue())

print("\nendValue")
print(inst.endValue())
print(ti.endValue())
print(seq.endValue())
print(ts.endValue())

print("\nminValue")
print(inst.minValue())
print(ti.minValue())
print(seq.minValue())
print(ts.minValue())

print("\nmaxValue")
print(inst.maxValue())
print(ti.maxValue())
print(seq.maxValue())
print(ts.maxValue())

print("\nvalueRange")
print(inst.valueRange())
print(ti.valueRange())
print(seq.valueRange())
print(ts.valueRange())

print("\ngetTimestamp")
print(inst.getTimestamp())

print("\ngetTime")
print(inst.getTime())
print(ti.getTime())
print(seq.getTime())
print(ts.getTime())

print("\ntimespan")
print(inst.timespan())
print(ti.timespan())
print(seq.timespan())
print(ts.timespan())

print("\nperiod")
print(inst.period())
print(ti.period())
print(seq.period())
print(ts.period())

print("\nnumInstants")
print(inst.numInstants())
print(ti.numInstants())
print(seq.numInstants())
print(ts.numInstants())

print("\nstartInstant")
print(inst.startInstant())
print(ti.startInstant())
print(seq.startInstant())
print(ts.startInstant())

print("\nendInstant")
print(inst.endInstant())
print(ti.endInstant())
print(seq.endInstant())
print(ts.endInstant())

print("\ninstantN")
print(inst.instantN(1))
print(ti.instantN(1))
print(seq.instantN(1))
print(ts.instantN(1))

print("\ninstants")
print(inst.instants())
print(ti.instants())
print(seq.instants())
print(ts.instants())

print("\nnumTimestamps")
print(inst.numTimestamps())
print(ti.numTimestamps())
print(seq.numTimestamps())
print(ts.numTimestamps())

print("\nstartTimestamp")
print(inst.startTimestamp())
print(ti.startTimestamp())
print(seq.startTimestamp())
print(ts.startTimestamp())

print("\nendTimestamp")
print(inst.endTimestamp())
print(ti.endTimestamp())
print(seq.endTimestamp())
print(ts.endTimestamp())

print("\ntimestampN")
print(inst.timestampN(1))
print(ti.timestampN(1))
print(seq.timestampN(1))
print(ts.timestampN(1))

print("\ntimestamps")
print(inst.timestamps())
print(ti.timestamps())
print(seq.timestamps())
print(ts.timestamps())

print("\nnumSequences")
print(seq.numSequences())
print(ts.numSequences())

print("\nstartSequence")
print(seq.startSequence())
print(ts.startSequence())

print("\nendSequence")
print(seq.endSequence())
print(ts.endSequence())

print("\nsequenceN")
print(seq.sequenceN(1))
print(ts.sequenceN(1))

print("\nsequences")
print(seq.sequences())
print(ts.sequences())

print("\nshift")
print(inst.shift(timedelta(days=1)))
print(ti.shift(timedelta(days=1)))
print(seq.shift(timedelta(days=1)))
print(ts.shift(timedelta(days=1)))

print("\nintersectsTimestamp")
t = datetime.strptime('2019-09-09', '%Y-%m-%d')
print(inst.intersectsTimestamp(t))
print(ti.intersectsTimestamp(t))
print(seq.intersectsTimestamp(t))
print(ts.intersectsTimestamp(t))

print("\nintersectsTimestampset")
tss = TimestampSet('{2019-09-09, 2019-09-10}')
print(inst.intersectsTimestampset(tss))
print(ti.intersectsTimestampset(tss))
print(seq.intersectsTimestampset(tss))
print(ts.intersectsTimestampset(tss))

print("\nintersectsPeriod")
p = Period('2019-09-09', '2019-09-10', True, True)
print(inst.intersectsPeriod(p))
print(ti.intersectsPeriod(p))
print(seq.intersectsPeriod(p))
print(ts.intersectsPeriod(p))

print("\nintersectsPeriodset")
ps = PeriodSet('{[2019-09-09,2019-09-10], [2019-09-11,2019-09-12]}')
print(inst.intersectsPeriodset(ps))
print(ti.intersectsPeriodset(ps))
print(seq.intersectsPeriodset(ps))
print(ts.intersectsPeriodset(ps))

"""
f = TInt('1@2000-01-01')
print(f)
f = TInt('{1@2000-01-01, 1@2000-01-02}')
print(f)
"""
