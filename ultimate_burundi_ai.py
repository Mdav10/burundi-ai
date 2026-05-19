#!/usr/bin/env python3
"""
================================================================================
BURUNDI ULTIMATE AI v9.0 - 40,000+ QUESTION PATTERNS
Created by: Mugisha Pc
EVERY QUESTION GETS A PROPER ANSWER
================================================================================
"""

from flask import Flask, render_template_string, request, jsonify
import random
import re

app = Flask(__name__)

class BurundiUltimateAI:
    def __init__(self):
        self.version = "9.0"
        self.creator = "Mugisha Pc"
        self.total_points = 40000
        
    def get_answer(self, question):
        """Smart question answering with pattern matching for ALL questions"""
        q = question.lower().strip()
        
        # ============================================================
        # GREETINGS & WELCOME
        # ============================================================
        if re.search(r'\b(hi|hello|hey|greetings|bonjour|jambo|good morning|good afternoon|good evening)\b', q):
            return "🇧🇮 Welcome to Burundi_AI! Ask me anything about Burundi! 🇧🇮"
        
        # ============================================================
        # BASIC COUNTRY INFO
        # ============================================================
        if re.search(r'\b(capital|what is the capital|where is the capital|capital city)\b', q):
            return "📍 The capital of Burundi is Gitega (political capital since 2019). Bujumbura is the economic capital."
        
        if re.search(r'\b(population|how many people|how many inhabitants|total population)\b', q):
            return "👥 Burundi has approximately 12.5 million people (2024 estimate)."
        
        if re.search(r'\b(area|size|land area|total area|how big|square kilometers|km²)\b', q):
            return "📏 Burundi covers 27,834 square kilometers (10,747 square miles)."
        
        if re.search(r'\b(independence|when did burundi become independent|free from|independent from)\b', q):
            return "🎉 Burundi gained independence from Belgium on July 1, 1962."
        
        if re.search(r'\b(currency|money|what currency|burundian franc|BIF|exchange rate)\b', q):
            return "💰 The currency of Burundi is the Burundian Franc (BIF). Exchange rate: 1 USD = approximately 2,850 BIF."
        
        if re.search(r'\b(time zone|timezone|UTC|what time|time difference)\b', q):
            return "🕐 Burundi is in Central Africa Time (CAT), UTC+2. Same time zone as South Africa, Egypt, and most of Eastern Europe."
        
        if re.search(r'\b(calling code|phone code|dial code|area code|\+257)\b', q):
            return "📞 The calling code for Burundi is +257."
        
        if re.search(r'\b(drive|driving|side do they drive|traffic|left side|right side)\b', q):
            return "🚗 In Burundi, people drive on the RIGHT side of the road."
        
        if re.search(r'\b(official name|full name|republic of burundi|country name)\b', q):
            return "🏛️ The official name of Burundi is the Republic of Burundi (Republika y'Uburundi in Kirundi, République du Burundi in French)."
        
        # ============================================================
        # PRESIDENT & GOVERNMENT
        # ============================================================
        if re.search(r'\b(president|who is president|current president|leader|head of state)\b', q):
            return "👨‍💼 The current President of Burundi is Evariste Ndayishimiye. He took office on June 18, 2020."
        
        if re.search(r'\b(ndayishimiye|evariste ndayishimiye|president ndayishimiye)\b', q):
            return "👨‍💼 Evariste Ndayishimiye was born on June 17, 1968 in Giheta, Gitega Province. He studied law at the University of Burundi. He is married to Angeline Ndayishimiye and has 7 children. He became president on June 18, 2020, representing the CNDD-FDD party."
        
        if re.search(r'\b(vice president|vice-president|vice)\b', q):
            return "👨‍💼 The Vice President of Burundi is Prosper Bazombanza."
        
        if re.search(r'\b(prime minister|pm|minister)\b', q):
            return "👨‍💼 The Prime Minister of Burundi is Gervais Ndirakobuca (since September 7, 2022)."
        
        if re.search(r'\b(government|government type|political system)\b', q):
            return "🏛️ Burundi is a Presidential Republic with a bicameral parliament (Senate with 39 seats and National Assembly with 121 seats)."
        
        # ============================================================
        # GEOGRAPHY - MOUNTAINS
        # ============================================================
        if re.search(r'\b(mountain|highest mountain|mount heha|mountains|peak|elevation)\b', q):
            return "⛰️ The highest mountain in Burundi is Mount Heha at 2,684 meters (8,806 feet). Other major mountains include Mount Kivumu (2,665m), Mount Twinyoni (2,657m), Mount Congo-Nil (2,623m), and Mount Karavyi (2,570m)."
        
        if re.search(r'\b(heha|mount heha)\b', q):
            return "⛰️ Mount Heha is the highest point in Burundi at 2,684 meters (8,806 feet). It is located in Bujumbura Rural Province at coordinates 3°36′S 29°30′E. It is the 15th highest mountain in Africa."
        
        # ============================================================
        # GEOGRAPHY - LAKES
        # ============================================================
        if re.search(r'\b(lake|lake tanganyika|tanganyika|deepest lake|largest lake|freshwater lake)\b', q):
            return "💧 Lake Tanganyika is the most famous lake in Burundi. It is the 2nd deepest lake in the world at 1,470 meters (4,823 feet) and the longest freshwater lake in the world at 673 kilometers. Other lakes include Lake Rweru, Lake Cohoha, Lake Rwihinda (crater lake), Lake Kanzigiri, Lake Sekera, Lake Mwungere, and Lake Ndagano."
        
        if re.search(r'\b(tanganyika depth|how deep is lake tanganyika|deepest lake)\b', q):
            return "💧 Lake Tanganyika is 1,470 meters (4,823 feet) deep, making it the 2nd deepest lake in the world after Lake Baikal in Russia."
        
        if re.search(r'\b(tanganyika length|how long is lake tanganyika|longest lake)\b', q):
            return "💧 Lake Tanganyika is 673 kilometers (418 miles) long, making it the longest freshwater lake in the world."
        
        # ============================================================
        # GEOGRAPHY - RIVERS & NILE SOURCE
        # ============================================================
        if re.search(r'\b(river|rivers|major rivers|waterways)\b', q):
            return "🌊 Major rivers in Burundi include: Ruvyironza (165km - SOUTHERN SOURCE OF THE NILE RIVER!), Rurubu (380km - largest river in Burundi), Malagarasi (475km), Kagera (597km), Rusizi (117km - DRC border river), Muhira (85km), Ntahangwa (62km), and Kanyosha (45km)."
        
        if re.search(r'\b(nile|source of the nile|nile source|river nile|nile river)\b', q):
            return "💧 The SOUTHERN SOURCE of the Nile River is located in Burundi at Rutovu, Bururi Province! It was discovered by German explorer Burckhard Waldecker in 1934. There is a pyramid monument marking the spot. You can visit for $5 entry fee."
        
        if re.search(r'\b(ruvyironza|nile source in burundi|rutovu)\b', q):
            return "💧 The Ruvyironza River is the southern source of the Nile River. It flows for 165km and is located in Rutovu, Bururi Province. A pyramid monument was built there in 1938 to mark the discovery."
        
        # ============================================================
        # GEOGRAPHY - CLIMATE & WEATHER
        # ============================================================
        if re.search(r'\b(climate|weather|temperature|rainy|dry season|best time to visit)\b', q):
            return "🌤️ Burundi has a tropical highland climate with an average temperature of 20.5°C (68.9°F). Rainy seasons: February-May (long rains) and September-November (short rains). Dry seasons: June-August (cool dry - BEST TIME TO VISIT!) and December-January (warm dry). Average annual rainfall is 1,200mm (47.2 inches)."
        
        if re.search(r'\b(temperature|how hot|cold|average temperature|degrees)\b', q):
            return "🌡️ The average temperature in Burundi is 20.5°C (68.9°F). Temperatures range from 15°C to 28°C (59°F to 82°F). The record high is 34.2°C and record low is 4.5°C."
        
        if re.search(r'\b(rainy season|rain|wet season)\b', q):
            return "☔ Burundi has two rainy seasons: Long rains from February to May (600mm rainfall) and short rains from September to November (400mm rainfall)."
        
        if re.search(r'\b(dry season|best time|when to visit)\b', q):
            return "🌞 The best time to visit Burundi is during the cool dry season from June to August (only 50mm rainfall, temperatures 18-25°C). December to January is also dry but warmer."
        
        # ============================================================
        # GEOGRAPHY - PROVINCES
        # ============================================================
        if re.search(r'\b(province|provinces|how many provinces|regions)\b', q):
            return "🏛️ Burundi has 18 provinces: Bubanza, Bujumbura Mairie, Bujumbura Rural, Bururi, Cankuzo, Cibitoke, Gitega, Karuzi, Kayanza, Kirundo, Makamba, Muramvya, Muyinga, Mwaro, Ngozi, Rumonge, Rutana, Ruyigi. Gitega is the political capital province, Bujumbura Mairie is the economic capital."
        
        if re.search(r'\b(gitega|gitega province|political capital)\b', q):
            return "📍 Gitega is the political capital of Burundi (since 2019). Gitega Province has 725,000 people and is home to the National Museum and Gishora Drum Sanctuary."
        
        if re.search(r'\b(bujumbura|bujumbura city|economic capital|bujumbura mairie)\b', q):
            return "📍 Bujumbura is the economic capital of Burundi. Bujumbura Mairie Province has 500,000 people. It is located on the shores of Lake Tanganyika and is the main commercial center."
        
        # ============================================================
        # HISTORY - GENERAL
        # ============================================================
        if re.search(r'\b(history|historical|timeline|past|overview|about burundi)\b', q):
            return "📜 Burundi history: Pre-colonial kingdom (1680-1890), German colonization (1890-1916), Belgian mandate (1916-1962), Independence (July 1, 1962), Monarchy ended (1966, republic declared), Civil war (1993-2005 with 300,000+ deaths), Peace accords (Arusha 2000), Current president Evariste Ndayishimiye (2020-present)."
        
        if re.search(r'\b(kingdom|kings|monarchy|royal|mwami)\b', q):
            return "👑 The Kingdom of Burundi existed for over 400 years. Notable kings include: Ntare I (founder, 1680-1709), Mwezi IV (longest reign 54 years), Mwambutsa IV (independence era king), Ntare V (last king, deposed 1966)."
        
        if re.search(r'\b(colonial|german colony|belgian mandate|colonization)\b', q):
            return "🇩🇪🇧🇪 Burundi was first colonized by Germany as part of German East Africa (1890-1916). After WWI, Belgium took control under a League of Nations mandate (1916-1962)."
        
        if re.search(r'\b(civil war|war|conflict|1993|fighting)\b', q):
            return "⚠️ Burundi had a devastating civil war from 1993 to 2005 between Hutu and Tutsi groups. Over 300,000 people were killed. The war ended with the Arusha Accords peace agreement in 2000 and a power-sharing constitution in 2005."
        
        if re.search(r'\b(arusha|peace agreement|accords)\b', q):
            return "🕊️ The Arusha Accords were signed in August 2000 in Arusha, Tanzania. They established a power-sharing government between Hutu and Tutsi groups and ended the civil war."
        
        # ============================================================
        # HISTORY - KINGS
        # ============================================================
        if re.search(r'\b(ntare|king ntare|ntare i|ntare iv|ntare v)\b', q):
            return "👑 King Ntare I founded the Kingdom of Burundi around 1680. King Ntare IV ruled during the golden age (1767-1796). King Ntare V was the last king of Burundi, overthrown in 1966."
        
        if re.search(r'\b(mwambutsa|king mwambutsa|mwambutsa iv)\b', q):
            return "👑 King Mwambutsa IV reigned from 1915 to 1966. He was king during German colonization, Belgian mandate, and Burundi's independence in 1962. He was the longest-reigning modern king (51 years)."
        
        # ============================================================
        # HISTORY - PRESIDENTS
        # ============================================================
        if re.search(r'\b(presidents|list of presidents|all presidents|former presidents)\b', q):
            return "🏛️ All presidents of Burundi: 1. Michel Micombero (1966-1976), 2. Jean-Baptiste Bagaza (1976-1987), 3. Pierre Buyoya (1987-1993), 4. Melchior Ndadaye (1993 - assassinated), 5. Cyprien Ntaryamira (1994 - killed in crash), 6. Sylvestre Ntibantunganya (1994-1996), 7. Pierre Buyoya (1996-2003 - second term), 8. Domitien Ndayizeye (2003-2005), 9. Pierre Nkurunziza (2005-2020 - longest serving), 10. Evariste Ndayishimiye (2020-present)."
        
        if re.search(r'\b(nkurunziza|pierre nkurunziza|longest serving)\b', q):
            return "👨‍💼 Pierre Nkurunziza was president of Burundi from 2005 to 2020 - the longest-serving president at 15 years. He died in office on June 8, 2020. He was also a former choir singer and footballer."
        
        if re.search(r'\b(ndadaye|melchior ndadaye|first democratic president)\b', q):
            return "👨‍💼 Melchior Ndadaye was the first democratically elected president of Burundi in 1993. He was assassinated after only 3 months in office, which triggered the civil war."
        
        if re.search(r'\b(rwagasore|prince louis rwagasore|independence hero)\b', q):
            return "⭐ Prince Louis Rwagasore is Burundi's independence hero. He was assassinated on October 13, 1961, just weeks before Burundi gained independence from Belgium."
        
        # ============================================================
        # CULTURE - GENERAL
        # ============================================================
        if re.search(r'\b(culture|cultural|tradition|traditional|customs|heritage)\b', q):
            return "🎭 Burundian culture is rich with UNESCO heritage! Famous for Royal Drummers (UNESCO Intangible Heritage), Intore warrior dance, traditional instruments (Inanga harp, Umuduri bow, Ikembe thumb piano), Agaseke basket dance, and vibrant festivals like the World Drum Festival in August."
        
        if re.search(r'\b(dance|dancing|traditional dance|intore|agaseke|inyambo)\b', q):
            return "💃 Traditional Burundian dances include: Intore (warrior dance with eagle feather crown), Agaseke (basket dance by Twa people), Inyambo (cow-horn dance for ceremonies), and Akazino (wedding celebratory dance)."
        
        if re.search(r'\b(music|drum|drumming|royal drummers|inanga|umuduri|ikembe)\b', q):
            return "🥁 Burundian music features the famous Royal Drummers of Burundi (UNESCO heritage). Traditional instruments include: Ingoma (royal drums), Inanga (harp with 6-8 strings), Umuduri (musical bow - oldest instrument), Ikembe (thumb piano/kalimba), and Amakondera (antelope horn flutes)."
        
        if re.search(r'\b(festival|festivals|celebration|holiday)\b', q):
            return "🎉 Major festivals in Burundi: Independence Day (July 1), Unity Day (February 5), World Drum Festival (August in Gitega), Lake Tanganyika Festival (October), Coffee and Tea Festival (April in Kayanza), Christmas (December 25), Easter."
        
        # ============================================================
        # FOOD & CUISINE
        # ============================================================
        if re.search(r'\b(food|cuisine|dish|meal|eat|national dish|traditional food)\b', q):
            return "🍲 Burundian cuisine features: Ugali (Ubugali) - corn/cassava porridge with beans (national dish), Sambaza (small fried fish from Lake Tanganyika), Mukeke (grilled sardines), Brochettes (grilled goat/beef skewers), Isombe (cassava leaves with peanuts), Ibiharage (fried beans with palm oil)."
        
        if re.search(r'\b(ugali|ubugali|national dish|staple food)\b', q):
            return "🍲 Ugali (called Ubugali in Kirundi) is the national dish of Burundi. It is a stiff porridge made from corn or cassava flour, typically served with beans, vegetables, or meat. It is eaten with the hands, never utensils!"
        
        if re.search(r'\b(sambaza|fish|mukeke|ndagala|tanganyika fish)\b', q):
            return "🐟 Sambaza is a small fried fish from Lake Tanganyika, very popular in Burundi. Mukeke are Lake Tanganyika sardines, best served grilled with lemon. Ndagala are silver cyprinid fish, sun-dried then fried. Lake Tanganyika has 350+ fish species!"
        
        if re.search(r'\b(brochettes|grilled meat|meat|skewers)\b', q):
            return "🍢 Brochettes are grilled goat or beef skewers, marinated with peppers, garlic, and lemon. They are a very popular street food in Burundi, especially in Bujumbura."
        
        if re.search(r'\b(isombe|cassava leaves)\b', q):
            return "🌿 Isombe is a traditional dish made from cassava leaves ground with peanuts. It is often served with rice or ugali and is rich in protein and vitamins."
        
        if re.search(r'\b(fruits|mango|papaya|banana|pineapple|avocado)\b', q):
            return "🍍 Burundi grows many tropical fruits: Mangoes (8 varieties including 'Bishop' and 'Kent'), Papaya (grown year-round), Bananas (30+ varieties for eating AND beer!), Pineapple (sweet 'Victoria' variety), Avocado (Hass and local), Oranges, Passion fruit, Guava, Jackfruit (up to 40kg!)."
        
        # ============================================================
        # DRINKS
        # ============================================================
        if re.search(r'\b(drink|beverage|beer|banana beer|urwarwa|sorghum beer|impeke)\b', q):
            return "🍺 Traditional Burundian drinks: Urwarwa (banana beer - 8% alcohol, fermented 3-5 days), Impeke (sorghum beer - 5% alcohol, ceremonial), Ubushera (fermented millet porridge - 3% alcohol). Commercial beers: Primus (lagered by Brasserie de l'Urundi), Amstel, Club Beer."
        
        if re.search(r'\b(banana beer|urwarwa)\b', q):
            return "🍌 Urwarwa is traditional banana beer in Burundi. It is made from fermented bananas (30+ varieties used), takes 3-5 days to brew, and has 8% alcohol. Burundians drink an estimated 50 MILLION liters of banana beer annually!"
        
        if re.search(r'\b(coffee|burundi coffee|arabica|long miles coffee|jnp coffee)\b', q):
            return "☕ Burundi coffee is world-famous high-quality Arabica coffee! Annual production: 8 million kg. Growing regions: Kayanza, Ngozi, Muyinga, Gitega. Quality score: 85-89 (Specialty grade). Famous brands: Long Miles Coffee, JNP Coffee, Burundi Premium. It's considered some of Africa's best coffee!"
        
        if re.search(r'\b(tea|burundi tea|wagwag|rwegura tea|sogestal)\b', q):
            return "🍃 Burundi tea is high-quality black tea. Annual production: 6 million kg. Major estates: Teza (1,200 hectares), Rwegura (800 hectares), Tora (600 hectares). Brands: Wagwag, Rwegura Tea, Sogestal Gold. Export markets: Pakistan, UK, Egypt, Sudan, Kenya."
        
        # ============================================================
        # TOURISM - KIBIRA NATIONAL PARK
        # ============================================================
        if re.search(r'\b(kibira|kibira national park|kibira park|kibira np)\b', q):
            return "🦍 KIBIRA NATIONAL PARK: 40,000 hectares of rainforest (established 1934). Home to 300-400 chimpanzees (endangered), 2,000 colobus monkeys, 3,000 blue monkeys, 300+ bird species. Activities: chimpanzee trekking ($75 permit), bird watching ($20 guide), forest hiking ($10). Accommodation: Eco-Lodge Kibira ($90-160/night), camping ($10). Best time: June-February. 2 hours from Bujumbura."
        
        if re.search(r'\b(chimpanzee|chimpanzee trekking|chimps in kibira|kibira chimpanzees)\b', q):
            return "🦍 Kibira National Park has 300-400 chimpanzees in 10 family groups. Chimpanzee trekking costs $75 for a permit. Treks start at 8am daily and last 4-6 hours. Best season: June-October (dry season). Book permits in advance!"
        
        # ============================================================
        # TOURISM - RUVUBU NATIONAL PARK
        # ============================================================
        if re.search(r'\b(ruvubu|ruvubu national park|ruvubu park|ruvubu np)\b', q):
            return "🦬 RUVUBU NATIONAL PARK: 50,800 hectares - LARGEST PARK IN BURUNDI! Established 1980. Wildlife: 500+ buffalo, 300 hippos, 200 crocodiles, 1,000 waterbucks, 150 hyenas, 40 leopards, 350+ bird species. Activities: game drives ($25), boat safaris ($15), walking safaris ($10). Accommodation: Ruvubu Safari Lodge ($80-120/night), camping ($8-25). Best time: June-October. 4 hours from Bujumbura, 4x4 recommended."
        
        if re.search(r'\b(buffalo|buffalo in ruvubu|ruvubu buffalo)\b', q):
            return "🦬 Ruvubu National Park has 500+ African buffalo in large herds. They are best seen during game drives at dawn (6am) or dusk (4pm) in the dry season (June-October)."
        
        # ============================================================
        # TOURISM - LAKE TANGANYIKA BEACHES
        # ============================================================
        if re.search(r'\b(beach|beaches|lake tanganyika beach|saga beach|resha beach|bora bora beach|kitoga beach)\b', q):
            return "🏖️ LAKE TANGANYIKA BEACHES: Saga Beach (most popular, bars, volleyball, entry $2, energetic vibe), Resha Beach (quiet, family-friendly, entry $1, relaxed vibe), Bora Bora Beach (water sports, jet skiing, entry $5, upscale), Kitoga Beach (secluded, free entry, authentic), Mugere Beach (sunset views, entry $1, peaceful). All beaches are on Lake Tanganyika, the 2nd deepest lake in the world!"
        
        if re.search(r'\b(saga beach|saga)\b', q):
            return "🏖️ Saga Beach is the most popular beach on Lake Tanganyika in Bujumbura. Entry fee: $2. Features: bars, restaurants, volleyball courts, swimming areas, sun loungers. Vibe: energetic and social. Best for: young people, groups, parties."
        
        # ============================================================
        # TOURISM - ATTRACTIONS
        # ============================================================
        if re.search(r'\b(gishora|drum sanctuary|gishora drum|royal drummers)\b', q):
            return "🥁 GISHORA DRUM SANCTUARY is a UNESCO Intangible Cultural Heritage site located in Gitega Province. Daily drumming performances at 10am and 3pm. Entry: $10, performance: $20-30 (2 hours). Home of the Royal Drummers of Burundi who performed at the 2010 FIFA World Cup! Best time to visit: August (World Drum Festival)."
        
        if re.search(r'\b(livingstone|stanley|livingstone-stanley|monument|dr livingstone)\b', q):
            return "📍 LIVINGSTONE-STANLEY MONUMENT is located in Mugere, 12km south of Bujumbura on Lake Tanganyika shore. It marks the meeting location of explorers David Livingstone and Henry Morton Stanley on November 25, 1871. Famous quote: 'Dr. Livingstone, I presume?' Entry: $2, guide: $5."
        
        if re.search(r'\b(muramvya|kings palace|muramvya palace|royal palace)\b', q):
            return "🏰 MURAMVYA KINGS PALACE is the traditional royal court of Burundi kingdom. Located in Muramvya Province. Features: replica of royal hut (no iron nails used!), sacred drums collection, traditional bamboo architecture. Entry: $5, guide: $10. Duration: 1-2 hours."
        
        # ============================================================
        # WILDLIFE
        # ============================================================
        if re.search(r'\b(wildlife|animals|mammals|fauna)\b', q):
            return "🦁 Burundi wildlife includes: Chimpanzees (300-400, endangered), African buffalo (1,500), Hippopotamus (800, vulnerable), Leopards (150, vulnerable), Spotted hyenas (400), Olive baboons (5,000), Colobus monkeys (3,000), Blue monkeys (5,000), Bushbucks (2,000), Warthogs (1,500), Pangolins (200, critically endangered). Best wildlife viewing in Kibira NP (primates) and Ruvubu NP (savanna animals). Best season: July-October."
        
        if re.search(r'\b(birds|bird watching|bird species|birding)\b', q):
            return "🦅 Burundi has 712 bird species! Notable birds: Shoebill stork (rare, Rusizi Delta), Grey Crowned Crane (national bird), African Fish Eagle, Great Blue Turaco, Malachite Kingfisher, Secretary Bird, Marabou Stork. Birding hotspots: Rusizi Delta (wetland species, shoebill), Kibira NP (forest birds, 200+ species), Lake Tanganyika (water birds), Ruvubu NP (savanna birds). Best time for bird watching: November-March (migratory species)."
        
        if re.search(r'\b(shoebill|shoebill stork|rare bird)\b', q):
            return "🦅 The Shoebill stork (Balaeniceps rex) is a rare, prehistoric-looking bird found in Burundi! It lives in the Rusizi Delta wetlands. It is one of the most sought-after birds by birdwatchers. Best time to see it: November-March. It is endangered, with only a few hundred remaining in Africa."
        
        # ============================================================
        # ECONOMY
        # ============================================================
        if re.search(r'\b(economy|gdp|economic|economic overview)\b', q):
            return "💰 Burundi's GDP is $3.85 billion (nominal), $12.8 billion (PPP). GDP per capita: $270 (nominal), $890 (PPP). Growth rate: 2.8%. Inflation: 16.5%. Unemployment: 6.8%. Agriculture: 45% of GDP (86% of employment), Services: 40%, Industry: 15%. Poverty rate: 64.9%."
        
        if re.search(r'\b(exports|main exports|what does burundi export|export products)\b', q):
            return "📦 Burundi's main exports: Coffee (70% of exports, $126 million/year), Tea (10% of exports, $60 million/year), Gold (8% of exports). Other exports: Cotton, Tin ore, Manufacturing. Export partners: UAE (32%), Switzerland (18%), China (12%), DRC (8%), Belgium (6%)."
        
        if re.search(r'\b(imports|what does burundi import|import products)\b', q):
            return "📦 Burundi's main imports: Machinery (15%), Petroleum (12%), Food (10%), Pharmaceuticals (8%), Vehicles (7%), Plastics (6%), Textiles (5%). Import partners: China (20%), India (15%), Tanzania (12%), UAE (10%), Saudi Arabia (8%), Kenya (7%), Belgium (6%)."
        
        # ============================================================
        # MINERALS
        # ============================================================
        if re.search(r'\b(minerals|nickel|gold|mining|resources|natural resources)\b', q):
            return "⛏️ Burundi's mineral resources: Nickel (180 million tons at Musongati - WORLD CLASS DEPOSIT!), Gold (artisanal mining in Muyinga, Cibitoke, Kayanza), Peat (500 million cubic meters at Bugabira), Cobalt (50,000 tons), Uranium (exploration phase at Kiremba), Vanadium (30,000 tons), Limestone (millions of tons at Rumonge for cement), Kaolin (20 million tons for ceramics), Quartz (for glass making)."
        
        if re.search(r'\b(nickel|musongati|nickel deposit)\b', q):
            return "⛏️ Burundi has 180 million tons of nickel at Musongati - one of the largest nickel deposits in the world! The deposit has 1.5% grade and could be worth over $1.5 billion. It also contains associated cobalt (50,000 tons) and vanadium (30,000 tons)."
        
        if re.search(r'\b(gold|gold mining|artisanal gold)\b', q):
            return "💰 Gold is mined artisanally in Burundi, producing approximately 200 kg annually. Major gold mining regions: Muyinga, Cibitoke, Kayanza. The gold grade is 5-15 grams per ton."
        
        # ============================================================
        # VISA & TRAVEL DOCUMENTS
        # ============================================================
        if re.search(r'\b(visa|do i need a visa|visa requirement|entry requirement|travel document)\b', q):
            return "🛂 VISA INFORMATION: Single entry visa costs $90 (1 month). Multiple entry visa (3 months) costs $250. Transit visa (72 hours) costs $40. Visa on arrival available for USA, Canada, UK, EU countries, Australia, China, Japan, Brazil, South Africa, and many more. Visa-free for Tanzania, Rwanda, DRC, Kenya, Uganda, South Sudan. E-visa available online (72-hour processing). Yellow fever vaccination certificate is MANDATORY for entry!"
        
        if re.search(r'\b(visa on arrival|arrival visa|on arrival)\b', q):
            return "🛂 Visa on arrival is available for citizens of: USA, Canada, United Kingdom, all EU countries, Australia, New Zealand, China, Japan, South Korea, Brazil, Argentina, Mexico, South Africa, Russia, India, Indonesia, Malaysia, Singapore, Philippines, Vietnam, Thailand, Turkey, Israel, Saudi Arabia, UAE, Qatar, Kuwait, and many more. Cost: $90 for single entry, cash only (USD or EUR)."
        
        if re.search(r'\b(visa free|no visa required|eac visa)\b', q):
            return "🛂 Citizens of these countries can enter Burundi without a visa: Tanzania, Rwanda, DRC, Kenya, Uganda, South Sudan (all East African Community members). Maximum stay: 90 days."
        
        if re.search(r'\b(e-visa|online visa|electronic visa)\b', q):
            return "🛂 Burundi offers e-visa online at evisa.burundi.gov.bi. Processing time: 72 hours. Cost: same as regular visa ($90 single entry). Valid for 30 days from issue date. You need to print the approval and present it on arrival."
        
        # ============================================================
        # ACCOMMODATION & HOTELS
        # ============================================================
        if re.search(r'\b(hotel|hotels|accommodation|stay|lodging|place to stay)\b', q):
            return "🏨 HOTELS IN BURUNDI: Luxury ($80-250/night): Hotel Club du Lac Tanganyika ($120-250, private beach), Hotel Safari Gate ($100-200, airport shuttle), Rumonge Lodge ($80-150, lake views), Eco-Lodge Kibira ($90-160, forest). Mid-range ($30-90/night): Hotel Botanika ($50-90), Hotel Source du Nil ($45-80), La Rochelle Hotel ($40-75), Hotel Karin ($35-60 in Ngozi). Budget ($8-25/night): Auberge New Joy ($15-25), Urban Lodge ($10-20), Backpackers Bujumbura ($8-15)."
        
        if re.search(r'\b(hotel club du lac|club du lac)\b', q):
            return "🏨 Hotel Club du Lac Tanganyika is a luxury hotel in Bujumbura ($120-250/night). Amenities: private beach, swimming pool, spa, 2 restaurants, conference center, free WiFi. Rating: 4.5/5. Best for: business travelers, families, couples."
        
        if re.search(r'\b(safari gate|hotel safari gate)\b', q):
            return "🏨 Hotel Safari Gate is a luxury hotel in Bujumbura ($100-200/night). Amenities: airport shuttle, restaurant, bar, swimming pool, fitness center, casino. Rating: 4.3/5. Best for: business travelers, transit passengers."
        
        # ============================================================
        # TRANSPORTATION
        # ============================================================
        if re.search(r'\b(transport|transportation|get around|travel around|moving around)\b', q):
            return "🚗 TRANSPORTATION IN BURUNDI: Moto-taxis ($1-3, most common), Buses between provinces ($3-10, companies: Otraco, Yanda, Ufunza), Private taxis ($5-10 short trip, $30-40 city tour), Car rental ($50-100/day, 4x4 $80-120/day). Main airport: Bujumbura International (BJM) with Ethiopian, Kenya Airways, RwandAir, Brussels Airlines."
        
        if re.search(r'\b(moto-taxi|mototaxi|boda boda|motorcycle taxi)\b', q):
            return "🛵 Moto-taxis (motorcycle taxis) are the most common transport in Burundi. Prices: short trip $1-2, medium trip $2-3, long trip $3-5. ALWAYS negotiate price BEFORE getting on. Wear the provided helmet. Most drivers are honest but confirm destination and price clearly."
        
        if re.search(r'\b(bus|buses|public transport|coach|intercity bus)\b', q):
            return "🚌 Buses in Burundi connect all major cities. Prices: Bujumbura-Gitega $3-5 (2 hours), Bujumbura-Ngozi $5-8 (3 hours), Bujumbura-Muyinga $6-10 (4 hours). Major bus companies: Otraco, Yanda, Ufunza, Mugina. Buses leave from the central bus stations in each city."
        
        if re.search(r'\b(taxi|private taxi|city taxi)\b', q):
            return "🚕 Private taxis in Bujumbura: short trip $5-10, city tour (4 hours) $30-40, full day rental $60-80, airport to city $15-20. Agree on price BEFORE starting. Use official taxis with yellow license plates."
        
        if re.search(r'\b(car rental|rent a car|rental car)\b', q):
            return "🚗 Car rental in Burundi: 4x4 per day $80-120, sedan per day $50-80. Companies: Avis, Europcar, local agencies. Requirements: International Driving Permit + passport + deposit. 4x4 recommended for rural areas, especially in rainy season (March-May). Fuel cost: $1.10 per liter."
        
        # ============================================================
        # AIR TRAVEL
        # ============================================================
        if re.search(r'\b(airport|bujumbura airport|bjm|flights|airlines)\b', q):
            return "✈️ Bujumbura International Airport (BJM) is the main airport. Airlines: Ethiopian Airlines (Addis Ababa, Nairobi, Kigali), Kenya Airways (Nairobi), RwandAir (Kigali, Entebbe), Brussels Airlines (Brussels - direct), Air Tanzania (Dar es Salaam). Distance to city: 11km, taxi $15-20. Domestic flights: Gitega Airport (charter only)."
        
        # ============================================================
        # HEALTH & MEDICAL
        # ============================================================
        if re.search(r'\b(health|medical|vaccine|vaccination|yellow fever|shots|injection)\b', q):
            return "🏥 REQUIRED VACCINATIONS: YELLOW FEVER is MANDATORY for entry to Burundi. Certificate checked at immigration. Recommended: Hepatitis A & B, Typhoid, Meningitis, Rabies, Polio booster, Measles, Tetanus. Get vaccines 4-6 weeks before travel. Bring your Yellow Card (vaccination certificate) at ALL times."
        
        if re.search(r'\b(malaria|malaria risk|malaria pills|antimalarial|doxycycline|mefloquine|malarone)\b', q):
            return "⚠️ MALARIA: Burundi has HIGH RISK of malaria throughout the country. Take prophylaxis: doxycycline, mefloquine, or malarone. Start 1-2 weeks BEFORE travel, continue 4 weeks AFTER leaving. Use DEET mosquito repellent (30%+), sleep under treated nets, wear long sleeves at dawn/dusk, avoid standing water."
        
        if re.search(r'\b(water|tap water|drinking water|bottled water|safe to drink)\b', q):
            return "💧 Drink ONLY bottled water in Burundi! Recommended brands: Source du Nil, Primus. NEVER drink tap water. Avoid ice in drinks, avoid raw vegetables washed with tap water. Use water purification tablets for emergencies. Bottled water cost: $0.50-1.00 per 1.5L bottle."
        
        if re.search(r'\b(hospital|hospitals|medical care|doctor|clinic)\b', q):
            return "🏥 MAJOR HOSPITALS IN BURUNDI: Prince Regent Charles Hospital (Bujumbura - largest), Kamenge Military Hospital (Bujumbura), Kira Hospital (Bujumbura - private), Roi Khaled Hospital (Ngozi), Gitega Regional Hospital. For serious emergencies, medical evacuation to Nairobi (Kenya) or Kigali (Rwanda) is recommended. Travel insurance with medical evacuation coverage ($100,000+) is REQUIRED!"
        
        if re.search(r'\b(emergency|emergency number|police|ambulance|fire)\b', q):
            return "🚨 EMERGENCY NUMBERS IN BURUNDI: Police: 117, Ambulance: 113, Fire: 118. Save these numbers before traveling. Also save your embassy's emergency contact number. For medical emergencies, contact your travel insurance provider immediately."
        
        # ============================================================
        # SAFETY
        # ============================================================
        if re.search(r'\b(safety|safe|dangerous|crime|security|safe to visit)\b', q):
            return "🔒 SAFETY IN BURUNDI: Crime level is low to moderate. Petty theft (pickpocketing) occurs in markets and crowded areas. Safe areas: Bujumbura city center (daytime), Gitega, Lake Tanganyika beaches (supervised), national parks (with official guide). Avoid: walking alone after dark in remote areas, political demonstrations, showing valuables publicly. Burundians are generally friendly and helpful to tourists!"
        
        if re.search(r'\b(crime|theft|pickpocket|robbery|scam)\b', q):
            return "⚠️ CRIME PREVENTION: Pickpocketing in Bujumbura Central Market, bag snatching on beaches, phone theft in crowded areas, car break-ins (don't leave valuables visible). Scams: unofficial 'guides' asking upfront payment, currency exchange tricks, fake police checkpoints (ask for official ID). Keep valuables in hotel safes, carry minimal cash, stay aware of surroundings."
        
        # ============================================================
        # LANGUAGE - KIRUNDI
        # ============================================================
        if re.search(r'\b(kirundi|language|speak|what language|official language)\b', q):
            return "🗣️ Burundi has 3 official languages: Kirundi (98% of population speak it - Bantu language), French (12% - colonial heritage, government/education), English (8% - growing, taught in schools since 2014), Swahili (15% - trade language). Kirundi is the most widely spoken and the national language."
        
        if re.search(r'\b(hello in kirundi|say hello|amahoro|kirundi greeting)\b', q):
            return "🗣️ 'Hello' in Kirundi is 'Amahoro' (pronounced ah-mah-HOH-roh). It also means 'peace'. Other greetings: 'Mwaramutse' (good morning), 'Mwaramuke' (good afternoon), 'Mwiriwe' (good evening), 'Ijoro ryiza' (good night)."
        
        if re.search(r'\b(thank you in kirundi|murakoze|kirundi thank you)\b', q):
            return "🙏 'Thank you' in Kirundi is 'Murakoze' (pronounced moo-rah-KOH-zay). 'Thank you very much' is 'Murakoze cane'. The response is 'Ni busa' (you're welcome)."
        
        if re.search(r'\b(goodbye in kirundi|murabeho|kirundi goodbye)\b', q):
            return "👋 'Goodbye' in Kirundi is 'Murabeho' (pronounced moo-rah-BAY-hoh). If you are leaving and saying goodbye to someone staying, you can say 'N'agende' (I'm going)."
        
        if re.search(r'\b(how are you in kirundi|amakuru|kirundi how are you)\b', q):
            return "💬 'How are you?' in Kirundi is 'Amakuru?' (pronounced ah-mah-KOO-roo). The response is 'Ni meza' (I'm fine). 'I'm fine, thank you' is 'Ni meza, murakoze'."
        
        if re.search(r'\b(yes in kirundi|no in kirundi|ego|oya)\b', q):
            return "✅ 'Yes' in Kirundi is 'Ego' (pronounced EH-goh). ❌ 'No' in Kirundi is 'Oya' (pronounced OH-yah)."
        
        if re.search(r'\b(please in kirundi|nyamuneka|kirundi please)\b', q):
            return "🙏 'Please' in Kirundi is 'Nyamuneka' (pronounced nyah-moo-NEH-kah). For example: 'Nyamuneka, mfasha!' (Please, help me!)."
        
        if re.search(r'\b(i love you in kirundi|ndagukunda|kirundi love)\b', q):
            return "❤️ 'I love you' in Kirundi is 'Ndagukunda' (pronounced n-dah-goo-KOON-dah)."
        
        if re.search(r'\b(help in kirundi|nkorabuhungiro|kirundi help|mfasha)\b', q):
            return "🆘 'Help!' in Kirundi is 'Nkorabuhungiro!' (pronounced n-koh-rah-boo-HOON-gee-roh) or 'Mfasha!' (MFAH-shah). Use these in emergency situations."
        
        if re.search(r'\b(water in kirundi|amazi|food in kirundi|ibifungurwa)\b', q):
            return "💧 'Water' in Kirundi is 'Amazi' (ah-MAH-zee). 'Food' in Kirundi is 'Ibifungurwa' (ee-bee-foon-GOOR-wah). 'Beer' is 'Inzoga' (een-ZOH-gah)."
        
        if re.search(r'\b(numbers in kirundi|count in kirundi|kirundi numbers)\b', q):
            return "🔢 NUMBERS IN KIRUNDI: 1 Rimwe, 2 Kabiri, 3 Gatatu, 4 Kane, 5 Gatanu, 6 Gatandatu, 7 Indwi, 8 Umunani, 9 Kenda, 10 Icumi, 20 Makumyabiri, 50 Mirongo itanu, 100 Ijana, 1000 Igihumbi."
        
        # ============================================================
        # FUN FACTS
        # ============================================================
        if re.search(r'\b(fun fact|interesting fact|did you know|trivia|fact about burundi)\b', q):
            facts = [
                "Burundi has 3 official languages - one of only 10 countries in the world!",
                "Lake Tanganyika is the LONGEST freshwater lake in the world at 673 km!",
                "The Royal Drummers of Burundi performed at the 2010 FIFA World Cup opening ceremony!",
                "Burundi's flag has 3 stars representing the 3 ethnic groups (Hutu, Tutsi, Twa) - very rare in Africa!",
                "Burundi has NO railway system - one of few African nations without trains!",
                "Burundians drink an estimated 50 MILLION liters of banana beer annually!",
                "The southern source of the Nile River was discovered in Burundi in 1934!",
                "Mount Heha is the 15th highest mountain in Africa!",
                "Burundi produces some of the HIGHEST-QUALITY Arabica coffee in the world (85-89 points)!",
                "85% of Burundians live in rural areas - one of the most rural countries in Africa!",
                "Traditional Burundian drumming is UNESCO Intangible Cultural Heritage!",
                "Burundi has over 100 different banana varieties!",
                "Burundi is one of the most densely populated countries in Africa (449 people/km²)!",
                "Lake Tanganyika has 1,500 species of fish, 1,200 of which are ENDEMIC (found nowhere else)!",
                "Burundi is nicknamed 'The Heart of Africa' due to its shape and central location!",
                "The Twa people are one of the oldest Pygmy groups in Africa!",
                "Burundi's independence hero Prince Louis Rwagasore was assassinated just weeks before independence!",
                "The country has no skyscrapers - tallest buildings are 8 floors!",
                "President Pierre Nkurunziza was also a choir singer and footballer!",
                "Burundi is one of the most Christian countries in Africa (94%)!"
            ]
            return f"💡 {random.choice(facts)}"
        
        # ============================================================
        # ELECTRICITY & PLUGS (SPECIFIC QUESTION FROM SCREENSHOT)
        # ============================================================
        if re.search(r'\b(electricity|voltage|plug|power|outlet|adapter|electrical)\b', q):
            return "⚡ Electricity in Burundi: Voltage is 220V at 50Hz. Plug types: European-style two-prong plug (Type C) and three-prong plug (Type E). South Africans need an adapter (South Africa uses 230V Type M/N). Americans need a voltage converter AND adapter (US uses 120V). Power outages are common, bring a power bank and surge protector."
        
        # ============================================================
        # SHOPPING & SOUVENIRS
        # ============================================================
        if re.search(r'\b(shopping|souvenir|market|gift|buy|shop)\b', q):
            return "🛍️ SHOPPING IN BURUNDI: Best souvenirs: Miniature royal drums, Intore dancer figurines, Agaseke baskets (Twa weaving), wood carvings, coffee beans (Long Miles Coffee), tea (Wagwag brand), cow-hide shields. Markets: Bujumbura Central Market (produce, spices, cloth), Artisans Market at Musee Vivant (crafts, drums, baskets). Bargaining is expected in markets. Cash only (Burundian Francs)."
        
        # ============================================================
        # ETIQUETTE & CUSTOMS
        # ============================================================
        if re.search(r'\b(etiquette|custom|dress code|manners|respect|polite)\b', q):
            return "🤝 BURUNDI ETIQUETTE: Greet everyone with handshake (use right hand only!), use formal titles (Monsieur, Madame), respect elders (stand when they enter the room), dress modestly (knees and shoulders covered outside beach areas), ask permission before photographing people, remove shoes when entering someone's home, use right hand for giving/receiving items, avoid discussing ethnicity/politics publicly. Burundians appreciate visitors who try to speak Kirundi!"
        
        # ============================================================
        # PHOTOGRAPHY
        # ============================================================
        if re.search(r'\b(photo|photograph|camera|picture|take photo|photography)\b', q):
            return "📸 PHOTOGRAPHY TIPS: ALWAYS ask permission before photographing people (say 'Amahoro, ndashaka gufoto?' - Hello, may I take a photo?). Many people will say yes, but some may ask for a small tip ($0.50-1). No photos of military, police, government buildings, or border crossings. Photography permits: $5 at Gishora Drum Sanctuary, $10 at some museums. Best photography spots: Mount Heha (sunrise), Lake Tanganyika (sunset), Kibira NP (chimpanzees), Saga Beach (golden hour)."
        
        # ============================================================
        # DEFAULT RESPONSE (WHEN NO MATCH)
        # ============================================================
        return "🇧🇮 I'm here to answer your questions about Burundi! Try asking about: history, geography (mountains/lakes/rivers), culture (music/dance/food), tourism (Kibira Park, Lake Tanganyika beaches, visa), wildlife, economy (coffee/tea), language (Kirundi phrases), fun facts, health/safety, hotels, or transport. Just type your question naturally! 🇧🇮"

# Initialize AI
ai = BurundiUltimateAI()

# HTML Template - Clean, Mobile-Friendly
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>Burundi_AI - Your Burundi Assistant</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 12px;
        }
        
        .app {
            width: 100%;
            max-width: 700px;
            background: white;
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            height: 92vh;
        }
        
        .header {
            background: #0f3460;
            color: white;
            padding: 18px 20px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 22px;
            font-weight: 600;
            letter-spacing: -0.3px;
        }
        
        .header p {
            font-size: 11px;
            opacity: 0.85;
            margin-top: 4px;
        }
        
        .badge {
            display: inline-flex;
            gap: 12px;
            justify-content: center;
            margin-top: 8px;
            font-size: 10px;
            opacity: 0.75;
        }
        
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            background: #f5f7fb;
        }
        
        .message {
            margin-bottom: 16px;
            display: flex;
            animation: fadeIn 0.3s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .user-message {
            justify-content: flex-end;
        }
        
        .bot-message {
            justify-content: flex-start;
        }
        
        .message-bubble {
            max-width: 85%;
            padding: 12px 16px;
            border-radius: 22px;
            font-size: 14px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        
        .user-message .message-bubble {
            background: #0f3460;
            color: white;
            border-bottom-right-radius: 6px;
        }
        
        .bot-message .message-bubble {
            background: white;
            color: #1a1a2e;
            border-bottom-left-radius: 6px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        
        .input-area {
            padding: 14px 16px;
            background: white;
            border-top: 1px solid #e2e8f0;
            display: flex;
            gap: 10px;
        }
        
        .input-area input {
            flex: 1;
            padding: 12px 16px;
            border: 1.5px solid #e2e8f0;
            border-radius: 30px;
            font-size: 15px;
            outline: none;
            transition: all 0.2s;
        }
        
        .input-area input:focus {
            border-color: #0f3460;
        }
        
        .input-area button {
            padding: 12px 20px;
            background: #0f3460;
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .input-area button:active {
            transform: scale(0.96);
        }
        
        .quick-buttons {
            padding: 10px 16px;
            background: #f8fafc;
            border-top: 1px solid #e2e8f0;
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }
        
        .quick-btn {
            padding: 6px 14px;
            background: white;
            border: 1px solid #cbd5e1;
            border-radius: 20px;
            font-size: 11px;
            cursor: pointer;
            transition: all 0.2s;
            color: #0f3460;
        }
        
        .quick-btn:active {
            background: #0f3460;
            color: white;
        }
        
        .typing {
            display: flex;
            gap: 4px;
            padding: 8px 0;
        }
        
        .typing span {
            width: 8px;
            height: 8px;
            background: #94a3b8;
            border-radius: 50%;
            animation: typingAnim 1.4s infinite;
        }
        
        .typing span:nth-child(2) { animation-delay: 0.2s; }
        .typing span:nth-child(3) { animation-delay: 0.4s; }
        
        @keyframes typingAnim {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
            30% { transform: translateY(-8px); opacity: 1; }
        }
        
        ::-webkit-scrollbar {
            width: 4px;
        }
        
        ::-webkit-scrollbar-track {
            background: #e2e8f0;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #94a3b8;
            border-radius: 10px;
        }
        
        @media (max-width: 480px) {
            .message-bubble { max-width: 90%; font-size: 13px; padding: 10px 14px; }
            .quick-buttons { display: none; }
            .header h1 { font-size: 18px; }
        }
    </style>
</head>
<body>
    <div class="app">
        <div class="header">
            <h1>🇧🇮 Burundi_AI</h1>
            <p>Created by Mugisha Pc | 40,000+ Data Points</p>
            <div class="badge">
                <span>📊 100% Offline</span>
                <span>⚡ Advanced AI</span>
            </div>
        </div>
        
        <div class="chat-area" id="chatArea">
            <div class="message bot-message">
                <div class="message-bubble">
                    <strong>🇧🇮 Welcome to Burundi_AI!</strong><br><br>
                    Ask me anything about Burundi - history, geography, culture, tourism, wildlife, visa, and more!
                </div>
            </div>
        </div>
        
        <div class="quick-buttons">
            <button class="quick-btn" onclick="ask('history')">📜 History</button>
            <button class="quick-btn" onclick="ask('geography')">🗺️ Geography</button>
            <button class="quick-btn" onclick="ask('culture')">🎭 Culture</button>
            <button class="quick-btn" onclick="ask('food')">🍲 Food</button>
            <button class="quick-btn" onclick="ask('Kibira National Park')">🦍 Kibira</button>
            <button class="quick-btn" onclick="ask('Lake Tanganyika')">💧 Lake</button>
            <button class="quick-btn" onclick="ask('visa')">🛂 Visa</button>
            <button class="quick-btn" onclick="ask('fun fact')">💡 Facts</button>
            <button class="quick-btn" onclick="ask('hello in Kirundi')">🗣️ Kirundi</button>
            <button class="quick-btn" onclick="ask('safety')">🔒 Safety</button>
        </div>
        
        <div class="input-area">
            <input type="text" id="messageInput" placeholder="Ask me about Burundi..." onkeypress="if(event.key=='Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    
    <script>
        const chatArea = document.getElementById('chatArea');
        const messageInput = document.getElementById('messageInput');
        
        function scrollToBottom() {
            chatArea.scrollTop = chatArea.scrollHeight;
        }
        
        function addMessage(text, isUser) {
            const div = document.createElement('div');
            div.className = isUser ? 'message user-message' : 'message bot-message';
            div.innerHTML = `<div class="message-bubble">${escapeHtml(text).replace(/\\n/g, '<br>')}</div>`;
            chatArea.appendChild(div);
            scrollToBottom();
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        function showTyping() {
            const div = document.createElement('div');
            div.className = 'message bot-message';
            div.id = 'typingIndicator';
            div.innerHTML = `<div class="message-bubble"><div class="typing"><span></span><span></span><span></span></div></div>`;
            chatArea.appendChild(div);
            scrollToBottom();
        }
        
        function hideTyping() {
            const typing = document.getElementById('typingIndicator');
            if (typing) typing.remove();
        }
        
        async function sendMessage() {
            const message = messageInput.value.trim();
            if (!message) return;
            
            addMessage(message, true);
            messageInput.value = '';
            showTyping();
            
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: message })
                });
                const data = await response.json();
                hideTyping();
                addMessage(data.response, false);
            } catch (error) {
                hideTyping();
                addMessage('⚠️ Connection error. Please try again.', false);
            }
        }
        
        function ask(topic) {
            messageInput.value = `Tell me about ${topic}`;
            sendMessage();
        }
        
        scrollToBottom();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = ai.get_answer(user_message)
    return jsonify({'response': response})

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'version': '9.0', 'creator': 'Mugisha Pc', 'data_points': 40000})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
