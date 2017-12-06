# Copyright 2017 David Lewis
# This file is part of the Villanova tour guide mrcroft skill
from os.path import dirname

import mycroft.util
import time
import requests
import json
import threading
import sys
from os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import GPIO

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'dlew'

LOGGER = getLogger(__name__)

class AmbassadorSkill(MycroftSkill):
		def __init__(self):
				super(AmbassadorSkill, self).__init__(name="AmbassadorSkill")

		def initialize(self):
				fun_fact_villanova_intent = IntentBuilder("FunFactVillanovaIntent"). \
						require("FunFactVillanovaKeyword").build()
				self.register_intent(fun_fact_villanova_intent, self.handle_fun_fact_villanova_intent)

				# ---------------------------------------------------------------------------------

				college_majors_intent = IntentBuilder("CollegeMajorsIntent"). \
						require("CollegeMajorsKeyword").build()
				self.register_intent(college_majors_intent, self.handle_college_majors_intent)

				# ---------------------------------------------------------------------------------

				college_minors_intent = IntentBuilder("CollegeMinorsIntent"). \
						require("CollegeMinorsKeyword").build()
				self.register_intent(college_minors_intent, self.handle_college_minors_intent)

				# ---------------------------------------------------------------------------------

				engineering_synopsis_intent = IntentBuilder("EngineeringSynopsisIntent"). \
						require("EngineeringSynopsisKeyword").build()
				self.register_intent(engineering_synopsis_intent, self.handle_engineering_synopsis_intent)

				# ---------------------------------------------------------------------------------

				chemical_engineering_intent = IntentBuilder("ChemicalEngineeringIntent"). \
						require("ChemicalEngineeringKeyword").build()
				self.register_intent(chemical_engineering_intent, self.handle_chemical_engineering_intent)

				# ---------------------------------------------------------------------------------

				computer_engineering_intent = IntentBuilder("ComputerEngineeringIntent"). \
						require("ComputerEngineeringKeyword").build()
				self.register_intent(computer_engineering_intent, self.handle_computer_engineering_intent)

				# ---------------------------------------------------------------------------------

				civil_engineering_intent = IntentBuilder("CivilEngineeringIntent"). \
						require("CivilEngineeringKeyword").build()
				self.register_intent(civil_engineering_intent, self.handle_civil_engineering_intent)

				# ---------------------------------------------------------------------------------

				mechanical_engineering_intent = IntentBuilder("MechanicalEngineeringIntent"). \
						require("MechanicalEngineeringKeyword").build()
				self.register_intent(mechanical_engineering_intent, self.handle_mechanical_engineering_intent)

				# ---------------------------------------------------------------------------------

				electrical_engineering_intent = IntentBuilder("ElectricalEngineeringIntent"). \
						require("ElectricalEngineeringKeyword").build()
				self.register_intent(electrical_engineering_intent, self.handle_electrical_engineering_intent)

				# ---------------------------------------------------------------------------------

				water_fountain_directions_intent = IntentBuilder("WaterFountainDirectionsIntent"). \
						require("WaterFountainDirectionsKeyword").build()
				self.register_intent(water_fountain_directions_intent, self.handle_water_fountain_directions_intent)

				# ---------------------------------------------------------------------------------

				bathroom_directions_intent = IntentBuilder("BathroomDirectionsIntent"). \
						require("BathroomDirectionsKeyword").build()
				self.register_intent(bathroom_directions_intent, self.handle_bathroom_directions_intent)

				# ---------------------------------------------------------------------------------

				liberal_arts_synopsis_intent = IntentBuilder("LiberalArtsSynopsisIntent"). \
						require("LiberalArtsSynopsisKeyword").build()
				self.register_intent(liberal_arts_synopsis_intent, self.handle_liberal_arts_synopsis_intent)

				# ---------------------------------------------------------------------------------

				vsb_synopsis_intent = IntentBuilder("VSBSynopsisIntent"). \
						require("VSBSynopsisKeyword").build()
				self.register_intent(vsb_synopsis_intent, self.handle_vsb_synopsis_intent)

				# ---------------------------------------------------------------------------------

				nursing_synopsis_intent = IntentBuilder("NursingSynopsisIntent"). \
						require("NursingSynopsisKeyword").build()
				self.register_intent(nursing_synopsis_intent, self.handle_nursing_synopsis_intent)
				
				# ---------------------------------------------------------------------------------
				
				campus_size_intent = IntentBuilder("CampusSizeIntent"). \
						require("CampusSizeKeyword").build()
				self.register_intent(campus_size_intent, self.handle_campus_size_intent)
				
				# ---------------------------------------------------------------------------------
				
				class_size_intent = IntentBuilder("ClassSizeIntent"). \
						require("ClassSizeKeyword").build()
				self.register_intent(class_size_intent, self.handle_class_size_intent)
				
				# ---------------------------------------------------------------------------------

				graduation_rate_intent = IntentBuilder("GraduationRateIntent"). \
						require("GraduationRateKeyword").build()
				self.register_intent(graduation_rate_intent, self.handle_graduation_rate_intent)
				
				# ---------------------------------------------------------------------------------

				engineering_resources_intent = IntentBuilder("EngineeringResourcesIntent"). \
						require("EngineeringResourcesKeyword").build()
				self.register_intent(engineering_resources_intent, self.handle_engineering_resources_intent)

				# ---------------------------------------------------------------------------------

				engineering_service_intent = IntentBuilder("EngineeringServiceIntent"). \
						require("EngineeringServiceKeyword").build()
				self.register_intent(engineering_service_intent, self.handle_engineering_service_intent)

				# ---------------------------------------------------------------------------------

				engineering_study_abroad_intent = IntentBuilder("EngineeringStudyAbroadIntent"). \
						require("EngineeringStudyAbroadKeyword").build()
				self.register_intent(engineering_study_abroad_intent, self.handle_engineering_study_abroad_intent)

				# ---------------------------------------------------------------------------------

				engineering_freshman_curriculum_intent = IntentBuilder("EngineeringFreshmanCurriculumIntent"). \
						require("EngineeringFreshmanCurriculumKeyword").build()
				self.register_intent(engineering_freshman_curriculum_intent, self.handle_engineering_freshman_curriculum_intent)
				
				# ---------------------------------------------------------------------------------

				church_intent = IntentBuilder("ChurchIntent"). \
						require("ChurchKeyword").build()
				self.register_intent(church_intent, self.handle_church_intent)

		def handle_fun_fact_villanova_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("fun.fact.villanova")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(5)
				except:
					time.sleep(5)

				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO4","On")

		def handle_college_majors_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("college.majors")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_college_minors_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("college.minors")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_engineering_synopsis_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_chemical_engineering_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("chemical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_computer_engineering_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("computer.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_civil_engineering_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("civil.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_mechanical_engineering_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("mechanical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_electrical_engineering_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("electrical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_water_fountain_directions_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("water.fountain.directions")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")


		def handle_bathroom_directions_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("bathroom.directions")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_liberal_arts_synopsis_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("liberal.arts.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_vsb_synopsis_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("vsb.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_nursing_synopsis_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("nursing.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")

		def handle_campus_size_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("campus.size")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_class_size_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("class.size")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_graduation_rate_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("graduation.rate")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_resources_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.resources")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_service_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.service")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_study_abroad_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.study.abroad")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_freshman_curriculum_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("engineering.freshman.curriculum")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
			
		def handle_church_intent(self, message):
				GPIO.set("GPIO1","Off")
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				self.speak_dialog("church")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(8)
				except:
					time.sleep(8)

				GPIO.set("GPIO3","Off")
		
		def stop(self):
				pass

def create_skill():
		return AmbassadorSkill()
