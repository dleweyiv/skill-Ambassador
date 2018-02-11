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

				# -------------------------------------------------------------------------------

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
				
				# ---------------------------------------------------------------------------------

				total_enrollment_intent = IntentBuilder("TotalEnrollmentIntent"). \
						require("TotalEnrollmentKeyword").build()
				self.register_intent(total_enrollment_intent, self.handle_total_enrollment_intent)
				
				# ---------------------------------------------------------------------------------

				aerospace_engineering_intent = IntentBuilder("AerospaceEngineeringIntent"). \
						require("AerospaceEngineeringKeyword").build()
				self.register_intent(aerospace_engineering_intent, self.handle_aerospace_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				biochemical_engineering_intent = IntentBuilder("BiochemicalEngineeringIntent"). \
						require("BiochemicalEngineeringKeyword").build()
				self.register_intent(biochemical_engineering_intent, self.handle_biochemical_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				bioengineering_engineering_intent = IntentBuilder("BioengineeringEngineeringIntent"). \
						require("BioengineeringEngineeringKeyword").build()
				self.register_intent(bioengineering_engineering_intent, self.handle_bioengineering_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				biomedical_engineering_intent = IntentBuilder("BiomedicalEngineeringIntent"). \
						require("BiomedicalEngineeringKeyword").build()
				self.register_intent(biomedical_engineering_intent, self.handle_biomedical_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				entrepreneurship_engineering_intent = IntentBuilder("EntrepreneurshipEngineeringIntent"). \
						require("EntrepreneurshipEngineeringKeyword").build()
				self.register_intent(entrepreneurship_engineering_intent, self.handle_entrepreneurship_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				mechatronics_engineering_intent = IntentBuilder("MechatronicsEngineeringIntent"). \
						require("MechatronicsEngineeringKeyword").build()
				self.register_intent(mechatronics_engineering_intent, self.handle_mechatronics_engineering_intent)

				# ---------------------------------------------------------------------------------

				sustainability_engineering_intent = IntentBuilder("SustainabilityEngineeringIntent"). \
						require("SustainabilityEngineeringKeyword").build()
				self.register_intent(sustainability_engineering_intent, self.handle_sustainability_engineering_intent)
				
				# ---------------------------------------------------------------------------------

				alumni_network_intent = IntentBuilder("AlumniNetworkIntent"). \
						require("AlumniNetworkKeyword").build()
				self.register_intent(alumni_network_intent, self.handle_alumni_network_intent)
				
				# ---------------------------------------------------------------------------------

				social_housing_intent = IntentBuilder("SocialHousingIntent"). \
						require("SocialHousingKeyword").build()
				self.register_intent(social_housing_intent, self.handle_social_housing_intent)
				
				# ---------------------------------------------------------------------------------

				villanova_basketball_intent = IntentBuilder("VillanovaBasketballIntent"). \
						require("VillanovaBasketballKeyword").build()
				self.register_intent(villanova_basketball_intent, self.handle_villanova_basketball_intent)
				
				# ---------------------------------------------------------------------------------

				villanova_sports_intent = IntentBuilder("VillanovaSportsIntent"). \
						require("VillanovaSportsKeyword").build()
				self.register_intent(villanova_sports_intent, self.handle_villanova_sports_intent)
				
				# ---------------------------------------------------------------------------------

				university_ranking_intent = IntentBuilder("UniversityRankingIntent"). \
						require("UniversityRankingKeyword").build()
				self.register_intent(university_ranking_intent, self.handle_university_ranking_intent)
				
				# ---------------------------------------------------------------------------------

				happy_face_intent = IntentBuilder("HappyFaceIntent"). \
						require("HappyFaceKeyword").build()
				self.register_intent(happy_face_intent, self.handle_happy_face_intent)
				
				# ---------------------------------------------------------------------------------

				sad_face_intent = IntentBuilder("SadFaceIntent"). \
						require("SadFaceKeyword").build()
				self.register_intent(sad_face_intent, self.handle_sad_face_intent)
				
				# ---------------------------------------------------------------------------------

				mad_face_intent = IntentBuilder("MadFaceIntent"). \
						require("MadFaceKeyword").build()
				self.register_intent(mad_face_intent, self.handle_mad_face_intent)

				# ---------------------------------------------------------------------------------

				thinking_face_intent = IntentBuilder("ThinkingFaceIntent"). \
						require("ThinkingFaceKeyword").build()
				self.register_intent(thinking_face_intent, self.handle_thinking_face_intent)
				
				#----------------------------------------------------------------------------------
				
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

				sleeping_intent = IntentBuilder("SleepingIntent"). \
						require("SleepingKeyword").build()
				self.register_intent(sleeping_intent, self.handle_sleeping_intent)
				
				# ---------------------------------------------------------------------------------

				intro_intent = IntentBuilder("IntroIntent"). \
						require("RolleIntroKeyword").build()
				self.register_intent(intro_intent, self.handle_intro_intent)
				
				# ---------------------------------------------------------------------------------

				marcell_intro_intent = IntentBuilder("MarcellIntroIntent"). \
						require("MarcellIntroKeyword").build()
				self.register_intent(marcell_intro_intent, self.handle_marcell_intro_intent)
				
				# ---------------------------------------------------------------------------------

				seafood_platter_intent = IntentBuilder("SeafoodPlatterIntent"). \
						require("SeafoodPlatterKeyword").build()
				self.register_intent(seafood_platter_intent, self.handle_seafood_platter_intent)
				
		def handle_fun_fact_villanova_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("fun.fact.villanova")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO4","On")

		def handle_chemical_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
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
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("computer.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")

		def handle_civil_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
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
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("mechanical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(13)
				except:
					time.sleep(13)

				GPIO.set("GPIO3","Off")

		def handle_electrical_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("electrical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(12)
				except:
					time.sleep(12)

				GPIO.set("GPIO3","Off")

		def handle_water_fountain_directions_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("water.fountain.directions")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(5)
				except:
					time.sleep(5)

				GPIO.set("GPIO3","Off")


		def handle_bathroom_directions_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("bathroom.directions")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(5)
				except:
					time.sleep(5)

				GPIO.set("GPIO3","Off")

		def handle_liberal_arts_synopsis_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("liberal.arts.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(11)
				except:
					time.sleep(11)

				GPIO.set("GPIO3","Off")

		def handle_vsb_synopsis_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("vsb.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(9)
				except:
					time.sleep(9)

				GPIO.set("GPIO3","Off")

		def handle_nursing_synopsis_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("nursing.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(12)
				except:
					time.sleep(12)

				GPIO.set("GPIO3","Off")

		def handle_campus_size_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("campus.size")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(7)
				except:
					time.sleep(7)

				GPIO.set("GPIO3","Off")
				
		def handle_class_size_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("class.size")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(4)
				except:
					time.sleep(4)

				GPIO.set("GPIO3","Off")
				
		def handle_graduation_rate_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("graduation.rate")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(3)
				except:
					time.sleep(3)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_resources_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("engineering.resources")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(11)
				except:
					time.sleep(11)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_service_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("engineering.service")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def handle_engineering_study_abroad_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
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
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("engineering.freshman.curriculum")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(11)
				except:
					time.sleep(11)

				GPIO.set("GPIO3","Off")
			
		def handle_church_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("church")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def handle_total_enrollment_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("total.enrollment")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(5)
				except:
					time.sleep(5)

				GPIO.set("GPIO3","Off")
				
		def handle_aerospace_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("aerospace.engineering")
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
				
		def handle_biochemical_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("biochemical.engineering")
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
		
		def handle_bioengineering_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("bioengineering.engineering")
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
				
		def handle_biomedical_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("biomedical.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def handle_entrepreneurship_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("entrepreneurship.engineering")
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
				
		def handle_mechatronics_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("mechatronics.engineering")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(11)
				except:
					time.sleep(11)

				GPIO.set("GPIO3","Off")
				
		def handle_sustainability_engineering_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("sustainability.engineering")
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
				
		def handle_alumni_network_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("alumni.network")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(11)
				except:
					time.sleep(11)

				GPIO.set("GPIO3","Off")
				
		def handle_social_housing_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("social.housing")
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
		
		def handle_villanova_basketball_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("villanova.basketball")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(13)
				except:
					time.sleep(13)

				GPIO.set("GPIO3","Off")
				
		def handle_villanova_sports_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("villanova.sports")
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
				
		def handle_university_ranking_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("university.ranking")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(9)
				except:
					time.sleep(9)

				GPIO.set("GPIO3","Off")
		
		def handle_happy_face_intent(self, message):
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")
				GPIO.set("GPIO4","On")
				time.sleep(5)
				GPIO.set("GPIO2","Off")
				
		def handle_sad_face_intent(self, message):
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(5)
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","Off")
				GPIO.set("GPIO4","On")
				
		def handle_mad_face_intent(self, message):
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","On")
				time.sleep(5) 									#I put the V eyes here
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","Off")
				
		def handle_thinking_face_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(5)
				GPIO.set("GPIO3","Off")
				GPIO.set("GPIO4","On")
				
		def handle_college_majors_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
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
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
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
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("engineering.synopsis")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def sleeping_synopsis_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","Off")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
		
		def handle_intro_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("rolle.intro")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def handle_marcell_intro_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("marcell.intro")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO3","Off")
				
		def handle_seafood_platter_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("seafood.platter")
				time.sleep(1) 									#I put the V eyes here
				GPIO.set("GPIO4","On")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(6)
				except:
					time.sleep(6)

				GPIO.set("GPIO3","Off")
				
		def stop(self):
				pass

			
def create_skill():
		return AmbassadorSkill()
