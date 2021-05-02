#!/usr/bin/env python3

# create a person class and then a patient class that will inherit it
class Person:
  def __init__(self, fname, lname, gender, age):
    self.fname = fname
    self.lname = lname
    self.gender = gender
    self.age = age

  def fullname(self):
    return '{} {}'.format(self.fname, self.lname)


  # class method as alternative constructor
  @classmethod
  def from_string(cls, pe_str):
    fname, lname, gender, age = pe_str.split('-') 
    return cls(fname, lname, gender, age)
  
# class inheritance 
class Patient(Person):
  def __init__(self, fname, lname, gender, age, ID, weight, height, btemp, s_bp, d_bp, pulse, cdict):
    super().__init__(fname, lname, gender, age) # single inheritance
    Patient.ID = ID
    Patient.height = height
    Patient.weight = weight
    Patient.btemp = btemp
    Patient.s_bp = s_bp
    Patient.d_bp = d_bp
    Patient.pulse = pulse
    Patient.cdict = {}
  
  @property
  def BMI(self):
    calc = self.weight / (self.height)**2
    if calc < 18.5:
      s = ' - Underweight'
    elif calc < 24.9:
      s = ' - Normal Weight'
    elif calc < 29.9:
      s = '- Pre-obesity'
    elif calc < 34.9:
      s = ' - Obesity class I'
    elif calc < 39.9:
      s = ' - Obesity class II'
    else:
      s = ' - Obesity class III'
    return 'BMI: ' + str(round(calc,2)) + s

  @property
  def btemp_classification(self):
    if self.btemp < 35:
      s = ' - Hypothermia'
    elif self.btemp < 37.6:
      s = ' - Normal Body Temperature'
    elif self.btemp < 38.3:
      s = ' - Fever/Hypethermia'
    else:
      s = ' - Hyperpyrexia'
    return 'Body Temp: ' + str(round(self.btemp,2)) + s
    
  @property
  def bp_classification(self):
    if self.s_bp < 120 and self.d_bp < 80:
      s = ' - Normal Blood Pressuure'
    elif self.s_dp < 129 and self.d_bp < 80:
      s = ' - Elevated Blood Pressure'
    elif self._bp < 139 and self.d_bp < 89:
      s = ' - High Blood Pressure (Hypertension) - Stage 1'
    elif self.s_bp < 180 and self.d_bp < 120:
      s = ' - High Blood Pressure (Hypertension) - Stage 2'
    else:
      s = ' - High Blood Pressure (Hypertension) - Stage 3'
    return 'Systolic Blood Pressure: ' + str(round(self.s_bp,2)) + ', Dystolic Blood Pressure: ' + str(round(self.d_bp,2)) + s

    
  # overloading operators
  def __repr__(self):
    return "Patient('{}', '{}', {})".format(self.fname, self.lname, self.age)

  def __str__(self):
    return '{} - {}'.format(self.fullname(), self.ID)

# class instantiation
p1 = Person('John', 'Doe', 'male', 45)
# print(p1.fullname())

p2 = Patient(p1.fname, p1.lname, p1.gender, p1.age, 907895390, 70, 1.85, 37, 119, 75, 70, {})
print(p2) # finally calls __str__
# print(p2.ID)
print(' ' + p2.BMI)
print(' ' + p2.btemp_classification)
print(' ' + p2.bp_classification)
print(' Pulse: ' + str(p2.pulse) + ' BPM')

# parsing input - we can use to parse CSV 
print()
pe_str = 'Simran-Moolchandaney-female-20'
new_pe = Person.from_string(pe_str)
print(new_pe.fullname())

