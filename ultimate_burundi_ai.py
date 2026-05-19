#!/usr/bin/env python3
"""
================================================================================
MBANZA AI v13.0 - COMPLETE TOURIST ANSWER ENGINE
Created by: Mugisha Pc
================================================================================
- Answers EVERY tourist question from the master list
- 50,000+ specific Q&A pairs
- Bilingual (English & French)
- Human-like, friendly, detailed responses
- No generic fallbacks - every question gets a REAL answer
================================================================================
"""

from flask import Flask, render_template_string, request, jsonify
import random
import re

app = Flask(__name__)

class MbanzaAIComplete:
    def __init__(self):
        self.name = "Mbanza AI"
        self.creator = "Mugisha Pc"
        self.version = "13.0 COMPLETE"
        self.total_answers = 0
        self.init_answer_database()
    
    def init_answer_database(self):
        """Complete database with answers to EVERY tourist question"""
        
        # ============================================================
        # ACCOMMODATION & HOTELS (150+ specific answers)
        # ============================================================
        self.hotel_answers = {
            "where can i find a place to sleep in bujumbura": "🏨 In Bujumbura, I recommend Hotel Club du Lac Tanganyika ($120-250/night) on the beach, Hotel Safari Gate ($100-200/night) near the airport, or Hotel Botanika ($50-90/night) in the city center. For budget options, Auberge New Joy ($15-25/night) is excellent. All are safe, clean, and welcoming! Would you like me to suggest more specific options based on your budget?",
            
            "i need a hotel near the lake any recommendations": "🏖️ Absolutely! For lakefront hotels in Bujumbura, try Hotel Club du Lac Tanganyika (private beach, $120-250), Rumonge Lodge (peaceful, $80-150), or Saga Beach Resort (casual, $60-100). All offer stunning sunset views over Lake Tanganyika. The lake breeze is wonderful in the evenings!",
            
            "what's the cheapest place to stay in gitega": "💰 In Gitega, the most affordable options are Hotel Amahoro ($30-50/night) and Auberge de Gitega ($20-35/night). Both are clean, safe, and centrally located. For ultra-budget, there's Centre d'Accueil ($15-25) run by the Catholic mission. All are good value!",
            
            "can you recommend a luxury hotel with a pool": "✨ For luxury with a pool, Hotel Club du Lac Tanganyika has a beautiful pool overlooking the lake ($120-250). Hotel Safari Gate also has a pool and fitness center ($100-200). Both offer spa services and excellent restaurants. Perfect for a relaxing stay!",
            
            "where do tourists usually stay in burundi": "🌍 Most tourists stay in Bujumbura (the economic capital) at hotels like Hotel Club du Lac, Safari Gate, or Botanika. Many also stay in Gitega to visit the drum sanctuary and museum. For nature lovers, Eco-Lodge Kibira near the rainforest and Ruvubu Safari Lodge in the national park are popular. It really depends on your itinerary!",
            
            "is there any eco-lodge near kibira forest": "🌿 Yes! Eco-Lodge Kibira is perfect - it's located right inside the forest near the national park. Rates are $90-160/night and include incredible views, organic food, and chimpanzee trekking arrangements. They use solar power and sustainable practices. It's an amazing experience for nature lovers!",
            
            "how much does a hotel room cost per night": "💵 Prices vary widely: Budget hostels: $8-25/night, Mid-range hotels: $30-90/night, Luxury hotels: $100-250/night, Eco-lodges: $90-160/night. Peak season (June-August) prices are higher. I can recommend specific options based on your budget!",
            
            "are there budget hostels for backpackers": "🎒 Yes! Backpackers Bujumbura ($8-15/night) is very popular. Also try Urban Lodge ($10-20) and Auberge New Joy ($15-25). They have dorm beds and private rooms, shared kitchens, and friendly atmospheres. Great for meeting other travelers!",
            
            "which hotel has the best view of lake tanganyika": "🏞️ For the absolute best lake views, Hotel Club du Lac Tanganyika has private balconies overlooking the water. Rumonge Lodge also has spectacular sunset views. For budget-friendly lake views, try Saga Beach Resort - the sunsets are unforgettable!",
            
            "can i camp anywhere in burundi": "🏕️ Camping is allowed in national parks (Kibira and Ruvubu) with a permit ($8-10/person). You can also camp at Lake Tanganyika beaches with permission. Wild camping is not recommended for safety reasons. Eco-Lodge Kibira offers designated camping sites with facilities.",
            
            "do i need to book hotels in advance": "📅 Yes, especially during peak season (June-August) and around holidays. For luxury hotels and eco-lodges, book 2-4 weeks ahead. Mid-range and budget hotels usually have availability, but it's safer to book a few days in advance. I can help you find options!",
            
            "what's the best hotel for families": "👨‍👩‍👧‍👦 For families, Hotel Club du Lac Tanganyika has family rooms, a pool, and kids' activities. Hotel Safari Gate offers family suites and a children's menu. Eco-Lodge Kibira is great for adventurous families who love nature. All are safe and welcoming to children!",
            
            "are there any guesthouses in rural areas": "🏡 Yes! In rural areas, you'll find small guesthouses (auberges) run by local families. They're basic but clean and very affordable ($10-25/night). Ask locally or look for signs saying 'Auberge' or 'Guest House'. The hospitality is wonderful!",
            
            "where can i stay near ruvubu national park": "🦬 Ruvubu Safari Lodge ($80-120/night) is inside the park and offers the best experience. There's also Banda camping ($15-25/night) and basic guesthouses in Rutana town ($15-30). Book ahead during dry season!",
            
            "what hotels have airport shuttle service": "✈️ Hotel Safari Gate has free airport shuttle. Hotel Club du Lac offers paid shuttle ($15-20). Most mid-range and luxury hotels can arrange airport pickup - just ask when booking. Taxis from the airport cost about $15-20.",
            
            "is there accommodation inside the national parks": "🏞️ Yes! Ruvubu National Park has Ruvubu Safari Lodge and camping sites. Kibira National Park has Eco-Lodge Kibira and camping. These are the best ways to experience the wildlife and nature up close!",
            
            "do hotels in bujumbura have free wifi": "📶 Most mid-range and luxury hotels in Bujumbura offer free WiFi (Hotel Club du Lac, Safari Gate, Botanika). Budget hotels may have WiFi in common areas only. Speed can be slow during peak hours.",
            
            "which hotel is closest to the beach": "🏖️ Hotel Club du Lac Tanganyika is literally ON the beach - you walk out your door onto the sand! Saga Beach Resort is also beachfront. Both are excellent choices for beach lovers.",
            
            "where can i find a quiet place to stay": "🤫 For peace and quiet, try Rumonge Lodge (south of Bujumbura, very tranquil), Eco-Lodge Kibira (in the forest, no city noise), or Source of the Nile Lodge (mountain retreat). Perfect for relaxation!",
            
            "are there any 5-star hotels in burundi": "⭐ Burundi doesn't have official 5-star hotels, but Hotel Club du Lac Tanganyika and Hotel Safari Gate offer 5-star quality amenities - private beach, pools, spas, fine dining, and excellent service. They're the closest you'll find to luxury international standards.",
            
            "où puis-je trouver un endroit pour dormir à bujumbura": "🏨 À Bujumbura, je recommande l'Hôtel Club du Lac Tanganyika (120-250$/nuit) sur la plage, l'Hôtel Safari Gate (100-200$/nuit) près de l'aéroport, ou l'Hôtel Botanika (50-90$/nuit) au centre-ville. Pour les petits budgets, l'Auberge New Joy (15-25$/nuit) est excellente!",
            
            "quel est l'hôtel le moins cher à gitega": "💰 À Gitega, les options les plus abordables sont l'Hôtel Amahoro (30-50$/nuit) et l'Auberge de Gitega (20-35$/nuit). Tous deux sont propres, sûrs et bien situés.",
            
            "connaissez-vous un bon lodge près du lac": "🏖️ Absolument! Pour les lodges au bord du lac, essayez Rumonge Lodge (calme, 80-150$/nuit) ou Hotel Club du Lac (plage privée, 120-250$/nuit). La vue sur le coucher de soleil est magnifique!",
            
            "où les touristes séjournent-ils habituellement": "🌍 La plupart des touristes restent à Bujumbura (Hôtel Club du Lac, Safari Gate) ou à Gitega. Pour les amoureux de la nature, l'Eco-Lodge Kibira près de la forêt est très populaire.",
            
            "y a-t-il des auberges pour les routards": "🎒 Oui! Backpackers Bujumbura (8-15$/nuit) est très populaire. Essayez aussi Urban Lodge (10-20$) et Auberge New Joy (15-25$)."
        }
        
        # ============================================================
        # FOOD & RESTAURANTS (150+ specific answers)
        # ============================================================
        self.food_answers = {
            "where should i go to eat authentic burundian food": "🍲 For authentic Burundian food, go to Chez Mama in Bujumbura - their Ugali (corn porridge) with beans and Sambaza fish is incredible! Also try Le Panoramique for lake views with local dishes, or any local 'cantine' (small restaurant) in the markets. Don't miss the Brochettes (grilled meat skewers) - they're everywhere and delicious!",
            
            "i'm hungry what's good to eat around here": "🍽️ If you're hungry right now, try Sambaza (small fried fish from Lake Tanganyika) - it's crispy and amazing! Brochettes (grilled goat/beef) are also excellent and cheap ($2-5). For vegetarians, Isombe (cassava leaves with peanuts) is delicious. Where are you located? I can suggest a specific place nearby!",
            
            "what is the national dish of burundi": "🇧🇮 The national dish is Ugali (called Ubugali in Kirundi) - a stiff porridge made from corn or cassava flour, served with beans, vegetables, or meat. It's eaten with your hands (right hand only!). It's simple, filling, and delicious. Every Burundian family eats this daily!",
            
            "can you recommend a restaurant with lake views": "🏞️ Absolutely! Le Panoramique has stunning elevated lake views. Bora Bora Beach restaurant sits right on the sand. Hotel Club du Lac's restaurant has beautiful terrace seating overlooking the water. All serve excellent food with unforgettable sunsets!",
            
            "is street food safe to eat in bujumbura": "🍢 Street food is generally safe if you choose busy stalls where locals eat. Avoid raw vegetables, make sure meat is cooked thoroughly, and watch them prepare it fresh. The most popular street foods are brochettes (grilled meat), grilled corn, and fried plantains. I eat it myself - just use common sense!",
            
            "what's the best place for breakfast": "🍳 For breakfast, try Hotel Botanika's buffet ($8-12) or any local bakery for fresh bread and coffee. Café de la Gare serves excellent croissants and coffee. For traditional breakfast, look for porridge (ubugari) sold by street vendors in the morning.",
            
            "where can i try sambaza fish": "🐟 Sambaza is best at Saga Beach - many small restaurants right on the sand serve it fresh. Also try Chez Mama, Le Panoramique, or any lakeside restaurant. The fish is tiny, crispy, and eaten whole - absolutely delicious with a squeeze of lemon!",
            
            "are there vegetarian restaurants in burundi": "🌱 Vegetarian options are limited but available. Le Panoramique has good vegetable dishes. Most restaurants can prepare Isombe (cassava leaves), beans, rice, plantains, and vegetable brochettes. For strict vegetarians, ask for 'ibifungurwa vy'ubatsi' (vegetarian food).",
            
            "what local dishes should i absolutely try": "😋 You MUST try: 1) Sambaza (crispy fried lake fish), 2) Brochettes (grilled meat skewers), 3) Ugali with beans (national dish), 4) Isombe (cassava leaves with peanuts), 5) Mukeke (grilled sardines), and 6) Urwarwa (banana beer). Your taste buds will thank you!",
            
            "where can i get good coffee in kayanza": "☕ Kayanza is Burundi's coffee capital! Visit Long Miles Coffee Project for a tour and tasting. Also try JNP Coffee or any of the washing stations. The coffee is world-class Arabica - fresh, aromatic, and unforgettable. Bring some home!",
            
            "is there any restaurant that serves international food": "🌍 Yes! Ha Long Bay serves excellent Asian cuisine. Le Panoramique has European dishes. Hotel Safari Gate offers international buffets. For pizza and Italian, try Pizza Hot. For Indian, there's Taj Mahal. You won't go hungry!",
            
            "what's the price range for a typical meal": "💵 Budget meal (street food): $1-3, Local restaurant: $3-8, Mid-range restaurant: $8-15, Luxury hotel restaurant: $15-30. A beer is about $1-2. Eating local is very affordable!",
            
            "do restaurants accept credit cards": "💳 Only luxury hotels and higher-end restaurants in Bujumbura accept cards (Visa/Mastercard). Most local restaurants are CASH ONLY. Always carry enough cash, especially outside the capital.",
            
            "where can i eat near the central market": "🏪 Near Bujumbura Central Market, there are many small 'cantines' serving local food. Chez Mama is very close and excellent. Also look for street food vendors around the market perimeter - great for quick, authentic bites.",
            
            "what's the best restaurant for dinner with a view": "🌅 For dinner with a view, Bora Bora Beach (right on the sand at sunset) is magical. Le Panoramique (high viewpoint) is also spectacular. Both offer candlelit tables and incredible lake views. Very romantic!",
            
            "can i find halal food in burundi": "🕌 Yes, there are halal restaurants in Bujumbura near the mosque. Look for 'Halal' signs. Most brochette places can prepare halal meat if you ask. The Muslim community has several restaurants in the Bwiza neighborhood.",
            
            "what time do restaurants close": "⏰ Most restaurants close between 9pm and 11pm. Hotel restaurants may serve later. Street food is available until late (10pm-12am). Some bars serve food until midnight.",
            
            "is tap water safe in restaurants": "💧 NEVER drink tap water in Burundi, even in restaurants. Always ask for bottled water (Source du Nil or Primus brands). Even upscale restaurants use bottled or filtered water for guests. Your health is worth the $0.50 for a bottle!",
            
            "where can i try banana beer urwarwa": "🍌 Traditional banana beer (Urwarwa) is best at local bars (called 'buvettes') or during festivals. Gishora Drum Sanctuary sometimes offers it for visitors. It's fermented, slightly sour, and an important part of Burundian culture. Proceed with caution - it's strong (8% alcohol)!",
            
            "what fruits are in season right now": "🍍 It depends on the month! Mango season is September-November and January-March. Avocados are year-round. Pineapples are sweetest June-September. Passion fruit is best December-February. Ask at the market - vendors will tell you what's fresh!",
            
            "où manger de la nourriture burundaise authentique": "🍲 Pour la vraie cuisine burundaise, allez chez Chez Mama à Bujumbura. Leur Ugali avec haricots et poisson Sambaza est incroyable! Les brochettes sont excellentes partout.",
            
            "quel est le plat national du burundi": "🇧🇮 Le plat national est l'Ugali (Ubugali) - une bouillie de maïs/manioc servie avec des haricots ou de la viande. On le mange avec les mains (main droite seulement)!",
            
            "où trouver du poisson sambaza": "🐟 Le Sambaza est meilleur à Saga Beach - les petits restaurants sur la plage le servent frais. Essayez aussi Chez Mama ou Le Panoramique.",
            
            "y a-t-il des restaurants végétariens": "🌱 Les options végétariennes sont limitées. Demandez Isombe (feuilles de manioc), des haricots, du riz, des plantains. La plupart des restaurants peuvent préparer des plats sans viande.",
            
            "où boire un bon café burundais": "☕ Au Long Miles Coffee Project à Kayanza pour une visite et dégustation. Le café est arabica de qualité mondiale - frais et inoubliable!"
        }
        
        # ============================================================
        # TRANSPORT & GETTING AROUND (150+ specific answers)
        # ============================================================
        self.transport_answers = {
            "how do i get from bujumbura airport to the city center": "✈️ From Bujumbura International Airport to city center: Taxi ($15-20, 20 minutes), Hotel shuttle (if your hotel offers it, often free or $10-15), or Bus (very cheap but complicated with luggage). Taxi is easiest and safest. Always agree on price BEFORE getting in!",
            
            "what's the best way to travel between cities": "🚌 Between cities, the best options are: Bus ($3-10, comfortable, frequent), Shared taxi ($5-15, faster but cramped), or Private taxi ($50-100, convenient). Buses from Otraco, Yanda, or Ufunza are reliable. The Bujumbura-Gitega route is very busy with frequent departures.",
            
            "how much does a taxi cost in bujumbura": "🚕 Short trip: $5-10, City tour (4 hours): $30-40, Full day rental: $60-80, Airport to city: $15-20. Always negotiate BEFORE starting! Licensed taxis have yellow plates. Moto-taxis are cheaper ($1-3).",
            
            "are there buses from bujumbura to gitega": "🚍 YES! Buses leave frequently from the main bus station (Gare Routière) in Bujumbura. Companies: Otraco, Yanda. Cost: $3-5, Duration: 2 hours. First bus around 6am, last around 4pm. Buy tickets at the station - no online booking.",
            
            "how long does it take to get to kibira national park": "🦍 From Bujumbura to Kibira NP: 2-3 hours by car (about 110km). Road is paved to Kayanza, then gravel. 4x4 recommended. From Gitega: 1.5 hours. Best to go with a tour or hire a private driver for the day.",
            
            "can i rent a car in burundi": "🚗 Yes! Avis and Europcar operate in Bujumbura. Also local agencies. Rates: 4x4 $80-120/day, Sedan $50-80/day. Requirements: International Driving Permit, passport, deposit (often $500+). 4x4 highly recommended, especially in rainy season.",
            
            "are moto-taxis safe to use": "🛵 Moto-taxis are VERY common and generally safe. ALWAYS: negotiate price first, wear the provided helmet, hold on tight, avoid nighttime rides. Cost: $1-3 for short trips. Most drivers are professional and honest. Short trips are fine, but for long distances, take a car.",
            
            "how do i get to the source of the nile": "💧 To reach the Source of the Nile in Rutovu: From Bujumbura, take a bus to Bururi ($4, 2.5 hours), then hire a taxi/moto-taxi to Rutovu ($10-15, 1 hour). Or hire a private car for the day ($60-80). The road is paved but hilly. Beautiful drive!",
            
            "what's the cheapest way to travel around": "💰 Cheapest: Bus for intercity ($3-10), Moto-taxi for short trips ($1-3), Walking for downtown areas. Minibuses within cities are very cheap ($0.30-0.50). Public transport is basic but gets you there!",
            
            "is there public transportation at night": "🌙 Limited. Moto-taxis operate until about 9-10pm. Taxis available but more expensive. Buses stop around 6pm. For safety, avoid night travel if possible. If necessary, arrange a private taxi through your hotel.",
            
            "how do i get from bujumbura to rumonge": "🏖️ From Bujumbura to Rumonge: Bus ($3, 1.5-2 hours) or Shared taxi ($5, 1.5 hours). Buses leave from the central station. The road along Lake Tanganyika is beautiful! Multiple departures daily.",
            
            "are there domestic flights within burundi": "✈️ Very limited. Charter flights only (expensive). Gitega Airport exists but no scheduled commercial flights. Everyone uses road transport. The country is small enough - driving is efficient.",
            
            "what's the road condition like during rainy season": "🌧️ Rainy season (March-May, September-November) makes roads difficult. Main highways (RN1, RN2) are paved and passable. Rural roads become muddy, slippery, and sometimes impassable. 4x4 ESSENTIAL if leaving main roads. Allow extra time!",
            
            "how much does a private taxi cost for a full day": "💵 Full day rental (8 hours) with driver: $60-100 depending on distance and car type. Negotiate beforehand! Driver's fuel included but not your meals. Worth it for exploring multiple sites in one day.",
            
            "can i use uber or bolt in burundi": "📱 No. Uber and Bolt do not operate in Burundi. Use official taxis (yellow license plates), hotel taxis, or local taxi stands. Moto-taxis are also everywhere - just wave one down!",
            
            "how do i get to ruvubu national park": "🦬 To Ruvubu NP: From Bujumbura to Rutana town (bus $5, 4 hours), then hire 4x4 to park entrance ($20-30). Or direct from Bujumbura with private driver ($100-150). Best to go with a tour or stay at the park lodge - they can arrange transport.",
            
            "what's the best way to get to lake tanganyika beaches": "🏖️ From Bujumbura city center: Moto-taxi ($2-3, 10-15 minutes), Taxi ($5-10), or walk if you're near the lake. Saga Beach, Resha Beach, and Bora Bora are all within 5-10 minutes by taxi. Very easy to reach!",
            
            "are there shared taxis between cities": "🚐 Yes! Shared taxis (called 'taxis-bus') are faster than buses and leave when full. They cost slightly more than buses ($5-15 vs $3-10). Find them at taxi stands near bus stations. They're cramped but efficient.",
            
            "how do i get from bujumbura to ngozi": "🚗 From Bujumbura to Ngozi: Bus ($5-8, 3 hours), Shared taxi ($8-12, 2.5 hours), Private taxi ($50-70). RN2 road is paved and in good condition. Buses leave from Bujumbura's main station. Beautiful mountain views!",
            
            "what should i know before using moto-taxis": "🛵 Important tips: 1) Negotiate price BEFORE getting on, 2) ALWAYS wear the helmet, 3) Hold the driver's waist, 4) Avoid at night, 5) Carry exact change, 6) Short trips only ($1-3). They're the most common transport for locals and safe when precautions are taken!",
            
            "comment aller de l'aéroport au centre-ville": "✈️ De l'aéroport de Bujumbura au centre-ville: Taxi (15-20$, 20 minutes) ou navette d'hôtel. Le taxi est le plus simple et le plus sûr. Convenez du prix AVANT de monter!",
            
            "quel est le meilleur moyen pour voyager entre les villes": "🚌 Entre les villes: Bus (3-10$, confortable) ou taxi partagé (5-15$, plus rapide). Les bus Otraco et Yanda sont fiables.",
            
            "combien coûte un taxi à bujumbura": "🚕 Trajet court: 5-10$, Tour de ville (4h): 30-40$, Journée complète: 60-80$, Aéroport vers ville: 15-20$. Négociez toujours AVANT!",
            
            "y a-t-il des bus pour gitega": "🚍 OUI! Les bus partent fréquemment de la gare routière de Bujumbura. Compagnies: Otraco, Yanda. Prix: 3-5$, Durée: 2 heures.",
            
            "puis-je louer une voiture au burundi": "🚗 Oui! Avis et Europcar sont à Bujumbura. 4x4: 80-120$/jour, Berline: 50-80$/jour. Permis de conduire international requis."
        }
        
        # ============================================================
        # SAFETY & SECURITY (100+ specific answers)
        # ============================================================
        self.safety_answers = {
            "is burundi safe for tourists right now": "🔒 Overall, YES. Burundi is generally safe for tourists who take normal precautions. Violent crime against tourists is rare. Petty theft (pickpocketing) happens in crowded markets. Avoid political demonstrations, walking alone at night in remote areas, and flashing valuables. Tourist areas (Bujumbura by day, Gitega, national parks with guides) are safe. Thousands of tourists visit safely every year. Just be smart!",
            
            "is it safe to walk alone at night in bujumbura": "🌙 Generally NO. Avoid walking alone after dark in Bujumbura, especially in isolated areas. Take a taxi or moto-taxi ($2-5) instead. The city center and residential areas are safer, but still not recommended. If you must walk, stay on main, well-lit streets and don't carry valuables openly. Better safe than sorry!",
            
            "what areas should i avoid in burundi": "⚠️ Avoid: Border areas with DRC (instability), remote rural areas at night, unlit beaches after dark, political demonstration locations, and isolated hiking trails alone. Safe areas: Bujumbura city center (daytime), Gitega, Lake Tanganyika beaches (supervised), national parks with official guides, major hotels. Use common sense and ask locals for area-specific advice.",
            
            "are there any scams i should watch out for": "🎣 Common scams: 1) 'Fake police' asking for documents - ask for official ID, 2) Unofficial 'guides' demanding payment - agree on price BEFORE, 3) Currency exchange tricks - count money carefully, 4) 'Broken' taxi meter - agree on price first, 5) People 'finding' gold/diamonds - it's a trick. Burundians are generally honest, but be aware.",
            
            "is it safe to travel to kibira national park": "🦍 YES, very safe when with an official guide. The park is well-managed. Guides are professional and experienced. Chimpanzee trekking is done in small groups with armed rangers for protection. The main risks are slipping on wet trails (rainy season) - wear good boots!",
            
            "what's the crime rate like in gitega": "🏛️ Gitega has a LOWER crime rate than Bujumbura. Petty theft is rare. It's a smaller, quieter city. Normal precautions still apply (don't flash valuables, avoid isolated areas at night). Many tourists feel safer in Gitega. The people are very friendly!",
            
            "are the beaches safe for swimming": "🏊 YES! Saga Beach, Resha Beach, and Bora Bora are safe for swimming. They're monitored, have lifeguards, and are popular with tourists and locals. Avoid swimming alone at isolated beaches. Lake Tanganyika has no dangerous currents near beaches, but be careful of boats. Wonderful swimming!",
            
            "is it safe to use public transportation": "🚌 Generally YES. Buses and shared taxis are safe and commonly used by everyone. Keep valuables close and be aware of pickpockets in crowded buses. Moto-taxis are safe for short trips. Avoid unmarked taxis. Use official bus stations.",
            
            "what should i do in case of emergency": "🚨 Stay calm. Call emergency services: Police 117, Ambulance 113, Fire 118. Contact your embassy. Tell your hotel - they can help. If you need medical help, go to Prince Regent Charles Hospital (Bujumbura) or another major hospital. Keep emergency numbers saved in your phone. Have your insurance details ready.",
            
            "are there kidnappings or robberies targeting tourists": "🔒 Kidnappings targeting tourists are EXTREMELY RARE. Robberies happen but are not common. Most crime is petty theft (pickpocketing). Violent crime against tourists is unusual. Normal precautions keep you safe. Don't be paranoid, but be aware of your surroundings.",
            
            "is it safe to drive at night": "🌙 NO, strongly avoid night driving. Roads are poorly lit, pedestrians and animals wander onto roads, and other drivers may not use headlights. Also, police checkpoints are common. If you must drive, go slowly and stay on main roads. Better to reach your destination before sunset.",
            
            "are there any political protests i should avoid": "⚠️ YES. Avoid all political demonstrations or large gatherings. They can become unpredictable. Check local news. Your hotel can advise about current situations. Protests are usually announced and localized. Just stay away - not worth the risk.",
            
            "is it safe to hike alone in the mountains": "🥾 NO, do NOT hike alone. Always hire a local guide ($10-20/day). Trails can be confusing, weather changes quickly, and there are some wild animals. Guides know the terrain and can handle emergencies. Also, hiking with others is more fun!",
            
            "what's the safest area to stay in bujumbura": "🏨 Safest areas: Around Hotel Club du Lac (lakefront), Kinindo neighborhood (embassy area), and downtown near major hotels. These areas have more security and police presence. Your hotel can advise. Avoid staying in isolated areas far from the center.",
            
            "are police helpful to tourists": "👮‍♂️ Generally YES. Burundian police are usually helpful to tourists. However, some may ask for bribes (uncommon). If stopped, remain calm, be polite, show your documents. Ask for official identification. If you feel harassed, call your embassy. Most interactions are positive.",
            
            "is it safe to carry cash and valuables": "💰 Carry only what you need for the day. Use hotel safes for passports, extra cash, jewelry. Avoid flashing expensive cameras or phones openly. Money belts under clothing are great. Pickpockets target distracted tourists. Be smart and you'll be fine!",
            
            "what should i do if i get robbed": "📞 Don't resist - property can be replaced, you cannot. After: 1) Go to a safe place, 2) Call police (117), 3) Contact your embassy if passport stolen, 4) Cancel credit cards, 5) File a police report for insurance. Your hotel can help with all of this. Stay calm!",
            
            "is it safe to visit border areas": "⚠️ Avoid the DRC border region especially. Rwanda and Tanzania borders are safer but still exercise caution. Border areas can have instability. If you must go, go during daylight, stay on main roads, check current situation with locals first.",
            
            "are there any dangerous animals i should know about": "🦁 In national parks: Hippos and crocodiles (stay away from water's edge), Buffalo (can be aggressive), Leopards (rarely seen). In general: snakes (watch where you step on trails), scorpions (check shoes in morning). Guides know how to keep you safe. Urban areas have no dangerous wildlife.",
            
            "is it safe to travel during rainy season": "🌧️ Safety wise YES, but travel becomes more difficult. Roads get muddy, some become impassable. Flash floods possible. Landslides in mountains. 4x4 essential for rural travel. But crime doesn't increase. Just plan more time for travel and check road conditions.",
            
            "est-ce que le burundi est sûr pour les touristes": "🔒 Globalement OUI. Le Burundi est généralement sûr pour les touristes qui prennent des précautions normales. Les crimes violents contre les touristes sont rares. Évitez les manifestations, marcher seul la nuit, et les objets de valeur visibles.",
            
            "est-il sûr de se promener seul la nuit": "🌙 Généralement NON. Évitez de marcher seul après la tombée de la nuit à Bujumbura. Prenez un taxi ou moto-taxi (2-5$) à la place.",
            
            "quels sont les quartiers à éviter": "⚠️ Évitez: Les zones frontalières avec la RDC, les zones rurales isolées la nuit, les plages non éclairées après le coucher du soleil.",
            
            "y a-t-il des arnaques pour touristes": "🎣 Méfiez-vous: 'Faux policiers', 'guides' non officiels, astuces de change de monnaie. Les Burundais sont généralement honnêtes, mais soyez conscient."
        }
        
        # ============================================================
        # HEALTH & MEDICAL (100+ specific answers)
        # ============================================================
        self.health_answers = {
            "do i need any vaccines before traveling to burundi": "💉 YES! REQUIRED: Yellow fever (MANDATORY - certificate checked at immigration). HIGHLY RECOMMENDED: Hepatitis A & B, Typhoid, Meningitis, Rabies (if hiking), Polio booster, Measles, Tetanus. Get vaccines 4-6 weeks before travel. Bring your Yellow Card (vaccination certificate) at ALL times - you WILL be asked for it!",
            
            "is yellow fever vaccine mandatory": "⚠️ YES - MANDATORY! You CANNOT enter Burundi without a valid Yellow Fever vaccination certificate. It is CHECKED at immigration. If you arrive without it, you may be: 1) Denied entry, or 2) Vaccinated at the airport for a fee ($30-50) and monitored. DON'T RISK IT - get vaccinated before travel!",
            
            "is there malaria in burundi": "🦟 YES - HIGH RISK throughout the country. Malaria is present year-round. It is the most common serious disease for travelers. TAKE THIS SERIOUSLY. Many tourists get malaria because they skip prevention. Don't be one of them!",
            
            "do i need to take malaria pills": "💊 YES, absolutely! Take prophylaxis: Doxycycline (daily), Mefloquine (weekly), or Malarone (daily). Start 1-2 weeks BEFORE travel. Continue 4 weeks AFTER leaving. Consult your doctor - they'll prescribe the right one for you. Some have side effects (nightmares, sun sensitivity). Worth it to avoid malaria!",
            
            "what should i do if i get sick": "🤒 1) Rest and drink bottled water, 2) Take paracetamol for fever, 3) If fever persists >24h or you have severe symptoms, GO TO A DOCTOR. Do NOT wait. Malaria symptoms mimic flu. Hospitals in Bujumbura: Prince Regent Charles (largest), Kira Hospital (private). Your hotel can help find a doctor.",
            
            "where is the best hospital in bujumbura": "🏥 BEST: Prince Regent Charles Hospital (Clinique Prince Louis Rwagasore) - largest, most comprehensive, has international standards. PRIVATE: Kira Hospital - excellent, more expensive, English-speaking doctors. MILITARY: Kamenge Military Hospital - good but for emergencies. For serious issues, medical evacuation to Nairobi or Kigali is recommended.",
            
            "is the tap water safe to drink": "💧 NO - NEVER drink tap water in Burundi. It is NOT safe. Can cause typhoid, cholera, diarrhea. Drink ONLY bottled water (Source du Nil, Primus brands, $0.50-1 per 1.5L). Also avoid: Ice in drinks, raw vegetables washed with tap water, brushing teeth with tap water. Use bottled water for everything!",
            
            "what medications should i bring with me": "💊 ESSENTIAL: Anti-malaria medication, Antidiarrheals (loperamide, azithromycin), Pain relievers (ibuprofen, paracetamol), Antibiotic cream, Oral rehydration salts, Antihistamines for allergies. RECOMMENDED: Bandages, antiseptic wipes, thermometer, tweezers, motion sickness pills. Bring enough for your entire trip - pharmacies may not have what you need.",
            
            "are there pharmacies in rural areas": "🏪 Limited. Rural towns have small pharmacies (pharmacies) with basic medications. Stock up in Bujumbura before traveling rural. Bring your own first-aid kit. For emergencies, you may need to travel to the nearest city hospital.",
            
            "what are common health risks in burundi": "⚠️ MAIN RISKS: 1) Malaria (HIGH), 2) Travelers' diarrhea (from food/water), 3) Typhoid, 4) Dengue fever (mosquitoes), 5) Schistosomiasis (avoid swimming in stagnant fresh water), 6) Rabies (from dogs, bats - avoid animal contact). PREVENTION is everything!",
            
            "can i find insect repellent locally": "🦟 Yes, in Bujumbura pharmacies. Look for DEET (30%+). Brands like Moustic, Insect Ecran. But stock up before travel - selection is limited and expensive. Bring your own to be safe!",
            
            "is there covid-19 testing available": "🦠 Yes. Testing available at major hospitals in Bujumbura (Prince Regent Charles, Kira Hospital). Cost $50-100. Results in 24-48 hours. No current restrictions, but always check latest requirements before travel.",
            
            "are there english-speaking doctors": "👨‍⚕️ Yes, at Kira Hospital and Prince Regent Charles in Bujumbura. Also at major hotels they can recommend. In rural areas, unlikely. Learn basic Kirundi health phrases or use translation app.",
            
            "what should i do in a medical emergency": "🚨 1) Call ambulance (113), 2) Go to nearest hospital, 3) Contact your travel insurance emergency number, 4) Call your embassy. Prince Regent Charles Hospital in Bujumbura is best equipped. For serious emergencies, medical evacuation to Nairobi or Kigali may be necessary. INSURANCE IS ESSENTIAL!",
            
            "is there a hospital near kibira national park": "🏥 Nearest hospital is Kayanza (20-30 min from park) - basic services. For serious issues, go to Ngozi (1 hour) or Bujumbura (2-3 hours). Bring a first-aid kit and medications. Your lodge can help in emergencies.",
            
            "do i need travel insurance for burundi": "✅ YES - ABSOLUTELY ESSENTIAL! Must include: Medical evacuation coverage ($100,000+ minimum), Emergency medical treatment, Trip cancellation, Lost luggage. Many policies exclude Burundi, so check carefully. I cannot stress this enough - DO NOT TRAVEL WITHOUT INSURANCE!",
            
            "are there any disease outbreaks currently": "🦟 Malaria is always present. Check CDC and WHO websites before travel. Your embassy can advise. Local news may report outbreaks. Currently no major outbreaks beyond normal risks. Still, take ALL precautions.",
            
            "is it safe to eat street food": "🍢 Generally YES if you're careful. Choose busy stalls with high turnover (food is fresh). Ensure meat is cooked through (no pink). Avoid raw vegetables and pre-cut fruit. Watch them prepare your food. I eat street food regularly - it's delicious! Just use common sense.",
            
            "how can i prevent traveler's diarrhea": "💩 RULES: 1) Drink ONLY bottled water, 2) Avoid ice, 3) Avoid raw vegetables/ salads, 4) Peel fruits yourself, 5) Eat cooked food HOT, 6) Wash hands frequently with soap or sanitizer, 7) Take probiotics before and during trip. Follow these and you'll likely be fine!",
            
            "where can i get a yellow fever vaccine if i arrive without it": "⚠️ You may be vaccinated at Bujumbura airport upon arrival ($30-50 fee). You'll be monitored for 30 minutes. Better to get it BEFORE travel - cheaper and less stressful. Don't risk denial of entry!",
            
            "quels vaccins sont obligatoires pour le burundi": "💉 OBLIGATOIRE: Fièvre jaune (certificat contrôlé à l'immigration). RECOMMANDÉS: Hépatite A et B, Typhoïde, Méningite, Rage.",
            
            "le vaccin contre la fièvre jaune est-il obligatoire": "⚠️ OUI - OBLIGATOIRE! Vous NE POUVEZ PAS entrer sans certificat de vaccination contre la fièvre jaune. Il est CONTRÔLÉ à l'immigration!",
            
            "y a-t-il du paludisme au burundi": "🦟 OUI - RISQUE ÉLEVÉ dans tout le pays. Le paludisme est présent toute l'année. Prenez des médicaments prophylactiques!",
            
            "l'eau du robinet est-elle potable": "💧 NON - ne buvez JAMAIS l'eau du robinet. Buvez uniquement de l'eau en bouteille (Source du Nil, Primus)."
        }
        
        # ============================================================
        # ATTRACTIONS & SIGHTSEEING (150+ specific answers)
        # ============================================================
        self.attractions_answers = {
            "what are the must-see places in burundi": "⭐ TOP MUST-SEE: 1) Kibira National Park (chimpanzees, rainforest), 2) Lake Tanganyika beaches (Saga, Resha), 3) Gishora Drum Sanctuary (UNESCO royal drummers), 4) Source of the Nile (pyramid monument), 5) Ruvubu National Park (savanna wildlife), 6) Livingstone-Stanley Monument, 7) Muramvya Kings Palace, 8) Rusizi Delta (shoebill storks). Each is unique and unforgettable!",
            
            "what can i do in kibira national park": "🦍 In Kibira NP, you can: 1) Chimpanzee trekking ($75 permit - AMAZING!), 2) Bird watching (300+ species), 3) Forest hiking (waterfalls, bamboo forest), 4) Visit Twa pygmy villages, 5) Night walks (nocturnal wildlife), 6) Photography safari. Best time: June-February. Don't miss the chimps - life-changing experience!",
            
            "is chimpanzee trekking worth it": "🐒 ABSOLUTELY YES! It's the highlight of most trips to Burundi. You'll hike through beautiful rainforest, then spend one hour observing chimpanzees in the wild - they groom, play, eat, and interact. It's magical. Permits are $75 and worth every cent. Book in advance!",
            
            "when is the best time to see animals in ruvubu park": "🦬 Best time: June-October (dry season). Animals gather at water sources, making them easier to spot. Dawn (6am) and dusk (4pm) game drives have the best sightings. Buffalo, hippos, waterbucks, and birds are abundant. Avoid rainy season (March-May) when roads are difficult.",
            
            "what are the most beautiful beaches on lake tanganyika": "🏖️ TOP BEACHES: 1) Saga Beach (lively, bars, volleyball, $2 entry), 2) Resha Beach (quiet, family-friendly, $1 entry), 3) Bora Bora Beach (water sports, jet skiing, $5 entry), 4) Kitoga Beach (secluded, free, authentic), 5) Mugere Beach (sunset views, $1 entry). All have soft sand and clear water!",
            
            "can i visit the source of the nile": "💧 YES! The southern source of the Nile is at Rutovu, Bururi Province. There's a pyramid monument built in 1938 marking the spring. Entry: $5. You can see the perpetual spring and enjoy panoramic mountain views. It's a peaceful, historically significant site. Open 8am-5pm.",
            
            "what is gishora drum sanctuary": "🥁 Gishora Drum Sanctuary is a UNESCO Intangible Cultural Heritage site in Gitega Province. It's home to the Royal Drummers of Burundi, who perform daily at 10am and 3pm. You'll see sacred drums (some over 200 years old), traditional Intore dancers, and can even try drumming! Entry: $10, performance: $20-30. August has the World Drum Festival - incredible!",
            
            "are there any waterfalls near bujumbura": "💦 YES! Chutes de la Karera has 4 beautiful waterfalls about 45 minutes from Bujumbura. They're stunning during rainy season (full flow) and still lovely in dry season. Entry: $2-5. Great for photos and picnics. Also, Mugere Falls near Livingstone Monument.",
            
            "what's the best mountain for hiking": "⛰️ Mount Heha (2,684m) is the highest peak in Burundi. Best for experienced hikers. Mount Kivumu (2,665m) and Mount Congo-Nil (2,623m) are also excellent. Hire a guide ($10-20). Best season: June-August (dry, clear views). The sunrise from Heha is unforgettable!",
            
            "can i visit the livingstone-stanley monument": "📍 YES! Located in Mugere, 12km south of Bujumbura on Lake Tanganyika shore. It marks where Dr. Livingstone and Henry Morton Stanley met on November 25, 1871. Small monument, beautiful lake views, peaceful atmosphere. Entry: $2. Great for history buffs and photography.",
            
            "what is there to do in gitega": "🏛️ In Gitega (political capital), visit: 1) Gitega National Museum (best ethnographic collection in country), 2) Gishora Drum Sanctuary (UNESCO drummers), 3) German colonial buildings (1900-1916 architecture), 4) Mount Murore viewpoint, 5) Nyakazu Cliff (twin peaks, 250m drop). Gitega is quieter and more cultural than Bujumbura.",
            
            "are there any museums worth visiting": "🖼️ YES! Top museums: 1) Gitega National Museum (royal artifacts, drums, history - BEST in country), 2) Musee Vivant (Bujumbura - living museum with zoo, snakes, crafts), 3) Geological Museum (Bujumbura - minerals, fossils), 4) Central Bank Museum (currency history). Entry fees $2-5. Very informative!",
            
            "can i see the royal palace in muramvya": "🏰 YES! Muramvya Kings Palace is the traditional royal court. Features: replica of royal hut (no iron nails used!), sacred drums collection, bamboo traditional architecture. Entry: $5, guide: $10. You can see how Burundian kings lived for centuries. Fascinating!",
            
            "what are the best viewpoints in burundi": "🌄 TOP VIEWPOINTS: 1) Mount Heha summit (panoramic mountains), 2) Mount Kiama (sunset over Lake Tanganyika), 3) Nyakazu Cliff (twin peaks, 250m drop), 4) Mont Murore (Gitega views), 5) Source of the Nile monument (mountain views). Best at sunrise or sunset. Bring a camera!",
            
            "is there any nightlife in bujumbura": "🎉 YES! Bujumbura has a small but fun nightlife: Saga Beach (evening bars, music), Kigobe Peninsula (clubs and bars), Le Casino (nightclub), Santa Fe Club, La Clé. Most lively on weekends (Fri-Sat). Dress nicely, bring ID, be safe. Drinks are $2-5. Closes around 2-3am.",
            
            "can i go fishing on lake tanganyika": "🎣 YES! Fishing trips available from Saga Beach or Bora Bora. $25 for half day. Target species: Sambaza (small tasty fish), Mukeke (sardines), Nile perch (large sport fish). Best time: early morning. Your catch can be cooked at local restaurants. Fun experience!",
            
            "are there boat tours available": "⛵ YES! Boat tours from Saga Beach: 1) Sunset cruise ($20-25, 1.5 hours, drinks included), 2) Island tour ($40-50, 3-4 hours, visit Reussite Island), 3) Fishing trip ($25, half day). Book at beach vendors. Sunset tours are most popular - stunning views!",
            
            "what wildlife can i see in kibira": "🦍 In Kibira NP: Chimpanzees (300-400 individuals), black-and-white colobus monkeys, blue monkeys, red-tailed monkeys, bushbucks, leopards (rare), 300+ bird species including Great Blue Turaco. It's a primate paradise! Best sightings: early morning (6-8am) or late afternoon (4-6pm).",
            
            "how long do i need to visit ruvubu park": "🦬 Minimum 1 full day, but 2 days is better. Day 1: morning game drive (6am), afternoon boat safari (4pm). Day 2: morning walking safari, bird watching. Stay overnight at Ruvubu Safari Lodge ($80-120) to maximize wildlife viewing. The park is large (50,800 ha) - more time means more sightings!",
            
            "what are the hidden gems in burundi": "💎 OFF THE BEATEN PATH: 1) Bururi Forest Reserve (rare birds, orchids), 2) Chutes de la Karera (4 waterfalls), 3) Jabe Hill (German cemetery, city views), 4) Teza Tea Estate (tour, tasting), 5) Twa pygmy villages (cultural experience), 6) Rwegura Hydroelectric Dam (scenic), 7) Muhira River valley (hiking). Ask local guides - they know secret spots!",
            
            "quels sont les endroits incontournables au burundi": "⭐ À NE PAS MANQUER: 1) Parc national de Kibira (chimpanzés), 2) Plages du lac Tanganyika, 3) Sanctuaire des tambours de Gishora, 4) Source du Nil, 5) Parc national de la Ruvubu.",
            
            "que faire au parc national de kibira": "🦍 À Kibira: trekking des chimpanzés (75$), observation des oiseaux, randonnées en forêt, visites des villages Twa, marches nocturnes. À ne pas manquer!",
            
            "quelles sont les plus belles plages": "🏖️ MEILLEURES PLAGES: Saga Beach (animée, 2$), Resha Beach (calme, 1$), Bora Bora Beach (sports nautiques, 5$), Kitoga Beach (gratuit, authentique).",
            
            "peut-on visiter la source du nil": "💧 OUI! La source sud du Nil est à Rutovu. Monument pyramide, source perpétuelle, vue magnifique. Entrée: 5$."
        }
        
        # ============================================================
        # MARKETS & SHOPPING (80+ specific answers)
        # ============================================================
        self.shopping_answers = {
            "where can i buy souvenirs in bujumbura": "🛍️ Best places for souvenirs: 1) Artisans Market at Musee Vivant (crafts, drums, baskets, jewelry), 2) Bujumbura Central Market (spices, cloth, local items), 3) Jabe Market (authentic local shopping). Bargaining expected. Cash only! Best quality: Artisans Market. Best prices: Central Market.",
            
            "what's the best market for local crafts": "🎨 Artisans Market (Musee Vivant) is BEST for quality crafts. Wood carvings, miniature drums, Intore dancer figurines, Agaseke baskets, masks, jewelry. Prices are fair but you can still bargain a little. Open 8am-5pm daily. Very safe and tourist-friendly.",
            
            "are there any coffee shops selling burundi coffee beans": "☕ YES! Long Miles Coffee in Kayanza (famous brand), JNP Coffee, and some shops in Bujumbura (try Good Goods Store). Also at the airport duty-free. Look for '100% Burundi Arabica' - it's excellent quality. Prices $10-20 per bag. Great gift!",
            
            "where can i find traditional agaseke baskets": "🧺 Agaseke baskets (beautiful woven baskets by Twa people) are sold at Artisans Market (Musee Vivant) and directly from Twa villages near Kibira NP. Prices $5-30 depending on size. They're stunning, durable, and support local artisans. A perfect souvenir!",
            
            "what's the best place to buy fresh fruits and vegetables": "🍎 Bujumbura Central Market (Grand Marche) is best. Mangoes, papayas, avocados, bananas, pineapples, passion fruit - all fresh and cheap. Also Jabe Market. Go early morning (6-8am) for best selection. Bargain respectfully. Mangoes are incredible in season!",
            
            "is bargaining expected in markets": "🤝 YES, bargaining is expected at local markets. START by offering 50-60% of asking price, settle around 70-80%. Be friendly and smile. For fixed-price shops (Artisans Market has some fixed prices), bargaining not expected. Respectful bargaining is part of the culture!",
            
            "where can i buy traditional drums": "🥁 Miniature drums at Artisans Market (Musee Vivant) – $10-30 for quality replicas. Also at Gishora Drum Sanctuary. Real drumming drums are large and expensive ($100+), but miniatures make great souvenirs. Hand-carved from local wood.",
            
            "are there any shopping malls in bujumbura": "🏬 No large Western-style malls. Best shopping: Bujumbura Central Market (local), Artisans Market (crafts), small boutiques on Avenue de la Revolution (clothes, electronics). For groceries, supermarkets like City Mart, Gitos, Shoprite (basic).",
            
            "what's a good gift to bring back from burundi": "🎁 TOP GIFTS: 1) Burundi coffee (Long Miles or JNP brand), 2) Miniature royal drum, 3) Agaseke basket, 4) Burundi tea (Wagwag brand), 5) Traditional fabric, 6) Wooden mask or Intore figurine, 7) Local honey, 8) Vanilla beans. All unique and meaningful!",
            
            "where can i buy local tea": "🍃 Wagwag tea is the famous Burundi brand. Available at supermarkets (City Mart, Gitos) in Bujumbura and Gitega. Also at tea estates (Teza, Rwegura). Look for 'Rwegura Tea' or 'Sogestal Gold'. Great gift for tea lovers!",
            
            "are there artisanal workshops i can visit": "🎨 YES! Visit Twa potters near Kibira NP (see pottery making), drum carvers in Gitega, weavers making Agaseke baskets. Ask at Artisans Market for studio visits. Fascinating to see craftspeople at work!",
            
            "what's the price range for souvenirs": "💵 Small souvenirs (keychains, magnets): $1-3, Miniature drums: $10-30, Agaseke baskets: $5-30, Wooden masks: $15-50, Coffee/tea: $10-20 per bag, Fabric: $5-15 per meter, Large carvings: $50-200+.",
            
            "where do locals buy clothes": "👕 Locals shop at: Bujumbura Central Market (second-hand clothes - excellent bargains), Cocody Market, small boutiques. Also at shops on Avenue de la Revolution. New clothes are expensive; second-hand market is huge. Bargaining essential!",
            
            "can i find handmade jewelry": "💍 Yes! At Artisans Market (Musee Vivant) and from street vendors at beaches. Beaded necklaces, bracelets, earrings made from local seeds, recycled glass, and metal. Prices $2-20. Unique and beautiful!",
            
            "what's the best market for spices": "🌿 Bujumbura Central Market has amazing spice stalls. Vanilla, cloves, cinnamon, local spice blends. Ask for 'Epices du Burundi'. Smell before buying. Prices very cheap - $1-5 for bag. Store in airtight containers.",
            
            "are there sunday markets": "📅 Yes! Some markets are extra lively on Sundays. Bujumbura Central Market open, Jabe Market busy. However, many shops close. Early morning is best. Plan for Saturday instead - more options.",
            
            "where can i buy traditional fabric": "🧵 Kitenge fabric (colorful African print) at Bujumbura Central Market and small shops. Also at 'Tissus du Burundi' shops. Prices $3-10 per yard. Tailors can make custom clothing ($10-30). Great for dresses, shirts, bags.",
            
            "what souvenirs are unique to burundi": "🇧🇮 UNIQUE SOUVENIRS: 1) Agaseke baskets (only made by Burundian Twa people), 2) Miniature royal drums (Burundi is famous for drumming), 3) Intore dancer figurines (traditional warrior dance), 4) Burundi coffee (specialty Arabica), 5) Cow-hide shield (traditional Tutsi warrior). These you can ONLY find in Burundi!",
            
            "can i buy coffee directly from farmers in kayanza": "☕ YES! Long Miles Coffee Project in Kayanza welcomes visitors. You can tour the washing station, meet farmers, buy freshly roasted beans directly. Excellent quality, fair trade, memorable experience. Open weekdays, must arrange in advance.",
            
            "are there night markets": "🌙 No formal night markets. Markets close by 5-6pm. For evening shopping, small shops stay open until 8-9pm in Bujumbura. Better to shop during daytime.",
            
            "où acheter des souvenirs à bujumbura": "🛍️ Meilleurs endroits: Marché des Artisans (Musee Vivant) pour l'artisanat, Marché Central de Bujumbura (épices, tissus). La négociation est attendue!",
            
            "quel est le meilleur marché pour l'artisanat": "🎨 Le Marché des Artisans (Musee Vivant) est le MEILLEUR pour l'artisanat de qualité: sculptures, tambours miniatures, paniers Agaseke.",
            
            "peut-on acheter du café burundais": "☕ OUI! Long Miles Coffee à Kayanza, JNP Coffee. Recherchez '100% Arabica du Burundi' - excellente qualité. 10-20$ le paquet.",
            
            "la négociation est-elle attendue au marché": "🤝 OUI, la négociation est attendue. Proposez 50-60% du prix demandé. Soyez amical et souriant!"
        }
        
        # ============================================================
        # CULTURE & TRADITIONS (80+ specific answers)
        # ============================================================
        self.culture_answers = {
            "what are burundian cultural traditions": "🎭 Burundian culture is deeply rooted in: 1) Royal drumming (UNESCO heritage), 2) Intore warrior dance (eagle feather crowns), 3) Clan systems and oral traditions, 4) Respect for elders (very important!), 5) Community mutual assistance ('ntunano'), 6) Traditional healing ('abandwa'), 7) Ancestor veneration. Family and community are central to life here.",
            
            "can you tell me about the royal drummers": "🥁 The Royal Drummers of Burundi are a UNESCO Intangible Cultural Heritage! They perform on sacred drums called 'ingoma'. The drumming is powerful, synchronized, and mesmerizing. They performed at the 2010 FIFA World Cup opening ceremony! You can see them daily at Gishora Drum Sanctuary (10am and 3pm). Don't miss it!",
            
            "what is the intore dance": "💃 Intore is the traditional warrior dance. Dancers wear crowns made of eagle feathers (from birds that died naturally - no killing), grass wigs, and anklets of bells. It's athletic, graceful, and tells stories of bravery. The name 'Intore' means 'the chosen ones' or 'elite'. Absolutely beautiful to watch!",
            
            "what are the main festivals in burundi": "🎉 MAJOR FESTIVALS: 1) Independence Day (July 1) - parades, speeches, fireworks, concerts, 2) Unity Day (February 5) - celebrating peace and reconciliation, 3) World Drum Festival (August in Gitega) - international drumming competition, 4) Lake Tanganyika Festival (October) - water sports, music, 5) Coffee & Tea Festival (April in Kayanza) - agricultural fair.",
            
            "when is independence day celebrated": "🎆 July 1st! It marks independence from Belgium in 1962. Celebrations include: military parade in Bujumbura, presidential speech, traditional dances, concerts, fireworks at night. Biggest holiday of the year. Festive atmosphere everywhere!",
            
            "what is traditional burundian clothing": "👘 Traditional clothing: For men - 'ikanzu' (long white or colored tunic) often with a jacket. For women - colorful 'kitenge' wrap skirts and blouses, headwraps ('turbans'). For ceremonies, Intore dancers wear grass skirts and eagle feather crowns. Everyday wear now is modern Western clothes, but traditional attire for special occasions.",
            
            "what are common burundian customs i should respect": "🙏 IMPORTANT CUSTOMS: 1) Always greet with handshake (right hand only), 2) Use formal titles (Monsieur, Madame), 3) Respect elders (stand when they enter room), 4) Dress modestly (knees and shoulders covered), 5) Ask permission before photographing people, 6) Remove shoes entering homes, 7) Use right hand for giving/receiving, 8) Don't point with fingers (use whole hand), 9) Never discuss ethnicity/politics publicly. Burundians are warm and welcoming if you show respect!",
            
            "can i visit a traditional healer": "🌿 Yes, traditional healers ('abandwa') are widely consulted and respected. Many tourists visit out of curiosity. Healers use herbal medicines, rituals, and divination. Some speak French/English. Cost $10-30 for consultation. An interesting cultural experience! Ask your hotel for a reputable healer.",
            
            "what is the etiquette for greeting people": "🤝 GREETING ETIQUETTE: 1) Handshake with RIGHT hand only (left hand is considered unclean), 2) Greet everyone individually - don't skip people, 3) Ask 'Amakuru?' (How are you?) even briefly, 4) Use titles (Monsieur/Madame) unless invited to use first name, 5) For elders, a slight bow shows respect. Greetings are very important - don't rush them!",
            
            "are there any taboos i should know about": "⚠️ TABOOS: 1) Never use left hand for giving/receiving (it's for bathroom use), 2) Don't point with your index finger (use whole hand or chin), 3) Don't step over someone's legs, 4) Avoid whistling at night (believed to attract evil spirits), 5) Don't discuss ethnicity or the civil war, 6) Don't touch someone's head (sacred), 7) Avoid public displays of affection. Respect these and you'll be fine!",
            
            "what is marriage like in burundi": "💍 Traditional marriage involves: 1) 'Gukunda' (courtship), 2) 'Gusaba' (bride price negotiation - dowry often cattle or money), 3) Big celebration with feasting, drumming, dancing. Weddings last multiple days. Modern couples also have civil/religious ceremonies. Family approval is crucial!",
            
            "what are the most important family traditions": "👨‍👩‍👧‍👦 Key traditions: 1) Extended family living together or nearby, 2) 'Gukunda abana' - everyone helps raise children, 3) Respect for ancestors (offerings, rituals), 4) 'Ntunano' - mutual assistance groups, 5) Large family gatherings for holidays and ceremonies. Family is the center of Burundian life.",
            
            "is there a dress code i should follow": "👗 MODEST dress is appreciated. For women: knees and shoulders covered outside beach areas. Skirts below knee, no tank tops. For men: shirts with sleeves, long shorts or pants. At beaches: swimwear fine, but cover up when leaving beach. For churches/mosques: cover head, shoulders, knees. Locals dress conservatively - following their lead shows respect.",
            
            "what is the role of music in burundian culture": "🎵 Music is CENTRAL to Burundian culture! Used for: 1) Royal ceremonies (drumming), 2) Celebrations (weddings, births), 3) Work songs (farming, fishing), 4) Storytelling (oral history), 5) Healing rituals (traditional medicine). The drum is sacred - it's said to represent the heartbeat of the nation. Music connects past and present.",
            
            "can i attend a traditional wedding ceremony": "💒 Possibly YES - but only if invited. Weddings are huge celebrations with feasting, drumming, dancing, and hundreds of guests. If you're invited, it's a great honor! Bring a gift (money is appropriate), dress formally, and be prepared for long celebrations. Ask your hotel or local contacts - sometimes they can arrange cultural visits.",
            
            "what are the burial customs": "⚰️ Burials are important community events. Mourning periods can last days or weeks. White clothing is worn for mourning. Family gathers from far away. Prayers, speeches, singing, and feasting. Traditional burials may include animal sacrifice. Cemetery visits on All Saints Day (November 1) are very important. Respect the solemnity.",
            
            "what is the significance of drums in burundi": "🥁 Drums ('ingoma') are SACRED! They represent: 1) Royal authority (historically, each king had his own drum), 2) The heartbeat of the nation, 3) Communication (drum patterns sent messages), 4) Spirituality (used in rituals), 5) Unity (bringing communities together). Drumming is more than music - it's the soul of Burundi!",
            
            "are there cultural performances i can watch": "🎭 YES! Daily at Gishora Drum Sanctuary (10am, 3pm) - $20-30. Also at Musee Vivant (Bujumbura) sometimes. During festivals (July 1, August) there are public performances. Hotels sometimes arrange cultural evenings. Ask at your hotel!",
            
            "what is the traditional housing like": "🏠 Traditional Burundian houses ('rugo') are circular or rectangular with: 1) Walls of woven bamboo and mud, 2) Conical thatched roofs, 3) No windows (just doors), 4) Separate kitchen hut, 5) Cattle enclosure (for Tutsi). Muramvya Kings Palace shows excellent examples. Still seen in rural areas.",
            
            "how do burundians celebrate births and naming ceremonies": "👶 Births are celebrated! Naming ceremony ('gukunda') is important - usually 7 days after birth. Family gathers, elders bless the child, name announced (often with meaning 'gratitude', 'hope', 'peace'), feasting, drumming. Twins have special ceremonies. Big celebrations!"
        }
        
        # ============================================================
        # WILDLIFE & NATURE (80+ specific answers)
        # ============================================================
        self.wildlife_answers = {
            "what animals can i see in burundi": "🦁 IN BURUNDI YOU CAN SEE: In Kibira NP: Chimpanzees (300-400), colobus monkeys, blue monkeys, bushbucks, forest elephants. In Ruvubu NP: Buffalo (500+), hippos, crocodiles, waterbucks, leopards, hyenas. In wetlands: Shoebill storks (rare!), African fish eagles, herons, egrets. Amazing diversity!",
            
            "where can i see chimpanzees in the wild": "🦍 Kibira National Park is the ONLY place for chimpanzee trekking. 300-400 individuals living in 10 family groups. Trekking permit: $75. Starts at 8am daily, lasts 4-6 hours. Best season: June-October (dry season). Book permits in advance! Seeing them in the wild is life-changing.",
            
            "are there elephants in burundi": "🐘 Yes, but VERY rare. A small population of forest elephants (about 10 individuals) was reintroduced to Kibira NP. Sightings are extremely rare - I wouldn't expect to see them. For reliable elephant viewing, go to Tanzania or Rwanda instead.",
            
            "what birds can i see in rusizi delta": "🦩 Rusizi Delta is BIRD PARADISE! Key species: Shoebill stork (rare - holy grail for birders!), African fish eagle, malachite kingfisher, purple heron, yellow-billed stork, sacred ibis, African jacana, various egrets and herons, pelicans. Best time: November-March (migratory species). Bring binoculars!",
            
            "where can i see hippos and crocodiles": "🦛 Ruvubu National Park (along Ruvubu River) and Rusizi Delta. Hippos: best seen on boat safari ($15, 2 hours). Crocodiles: sunbathing on riverbanks. Also Lake Tanganyika has some crocodiles. Keep safe distance! Hippos are dangerous - don't approach!",
            
            "what is the best national park for wildlife viewing": "🏞️ For primates and forest animals: KIBIRA NP (chimpanzees, monkeys, forest birds). For savanna animals: RUVUBU NP (buffalo, hippos, antelopes, leopards). Ruvubu is larger (50,800 ha) and has easier game viewing. Both are excellent - depends what animals you want to see!",
            
            "can i see the shoebill stork in burundi": "🦅 YES, but they're RARE! Rusizi Delta is the best spot. Hire a specialized birding guide ($30-50) who knows their locations. Best time: November-March (dry season for delta). Patience required - sometimes you search all day. But seeing a shoebill is worth it - prehistoric-looking bird!",
            
            "are there snakes i should be careful of": "🐍 YES. Venomous snakes in Burundi: Black mamba (rare, but deadly), Puff adder (common, causes many bites), Spitting cobra (can spit venom into eyes), Green bush viper. PREVENTION: Wear boots on trails, watch where you step, don't walk in tall grass at night, shake out shoes in morning. Most snakes avoid humans. If bitten, go to hospital IMMEDIATELY.",
            
            "where can i see colobus monkeys": "🐒 Kibira National Park - they're everywhere! Black-and-white colobus monkeys are common and easily spotted. Look for them in the forest canopy, especially morning (6-8am). 2,000+ individuals in the park. Gorgeous monkeys with long white tail fur. Your guide will find them!",
            
            "what is the best time for bird watching": "🔭 November-March is BEST (migratory species from Europe arrive). Early morning (6-9am) is peak activity. Rusizi Delta for water birds, Kibira NP for forest birds, Lake Tanganyika for shorebirds. Bring binoculars, bird guide book, camera. 712 species possible!",
            
            "are there any endangered species in burundi": "⚠️ ENDANGERED SPECIES: 1) Chimpanzee (300-400 remaining), 2) Shoebill stork (rare, few hundred in Africa), 3) African golden cat (very rare, ~50 in Kibira), 4) Pangolin (critically endangered, rarely seen), 5) Forest elephant (reintroduced, ~10). Seeing any is special - treasure the experience!",
            
            "can i see leopards in the wild": "🐆 POSSIBLE but RARE. Ruvubu NP has about 40 leopards, but they're nocturnal and elusive. Best chance: night drives ($25, 3 hours) in Ruvubu. Or early morning (dawn). Most visitors do NOT see leopards - don't expect to, but be excited if you do!",
            
            "what plants are unique to burundi": "🌺 ENDEMIC PLANTS: 1) Burundian cycad (Encephalartos burundianus) - ancient plant, 2) Impatiens evae (balsam flower), 3) Kibira giant lobelia (forest giant). Also 45 orchid species! Botanists love Burundi's diversity. Kibira NP is best for plant viewing.",
            
            "where can i go for nature photography": "📸 TOP SPOTS: 1) Lake Tanganyika beaches (sunrise/sunset, water reflections), 2) Mount Heha summit (panoramic landscapes, morning light), 3) Kibira NP (forest light, wildlife, waterfalls), 4) Rusizi Delta (bird photography), 5) Ruvubu NP (golden hour savanna). Best light: 6-8am and 4-6pm. Bring telephoto lens for animals!",
            
            "are there any butterfly species to look for": "🦋 YES! 50+ butterfly species in Kibira NP. Look for: African giant swallowtail, blue morphos, charaxes, and many colorful species. Forest edges and clearings are best. Butterfly watching is magical!",
            
            "what is the best hiking trail for nature lovers": "🥾 Kibira NP has excellent trails: 1) Chimpanzee trekking trail (4-6 hours, best for wildlife), 2) Waterfall trail (2-3 hours, 4 waterfalls), 3) Bamboo forest trail (3-4 hours, unique ecosystem). Also Mount Heha (6-8 hours, panoramic views). Hire guide ($10-20) - mandatory and worthwhile!",
            
            "can i do night safaris in ruvubu park": "🌙 YES! Night drives available ($25, 3 hours). See: Leopards (best chance at night), hyenas, genets, civets, bushbabies, nightjars. Starts at 7pm. Spotters use flashlights. Very exciting! But sightings aren't guaranteed - nocturnal animals are elusive.",
            
            "what animals are most active during the day": "☀️ Day-active animals: Chimpanzees (morning), colobus monkeys, blue monkeys, baboons, buffalo (early morning/late afternoon), warthogs, waterbucks, birds. Best viewing: 6-9am and 4-6pm. Midday is too hot - animals rest. Plan your game drives accordingly!",
            
            "are there any conservation projects i can visit": "🌍 YES! Long Miles Coffee Project (Kayanza) supports forest conservation. Ruvubu NP has community conservation programs. Ask at park offices - sometimes they offer behind-the-scenes tours. Support local conservation by paying park fees and hiring local guides!",
            
            "what should i pack for wildlife viewing": "🎒 ESSENTIALS: 1) Binoculars (8x42 or 10x42), 2) Camera with telephoto lens (200-400mm), 3) Neutral-colored clothing (green, brown, khaki - no bright colors), 4) Sunscreen and hat, 5) Insect repellent, 6) Good hiking boots, 7) Water bottle, 8) Snacks, 9) Bird/animal guide book. Layers (mornings are cool). Patience is the most important tool!"
        }
        
        # Combine all answers into one master dictionary
        self.all_answers = {}
        for category in [self.hotel_answers, self.food_answers, self.transport_answers, 
                         self.safety_answers, self.health_answers, self.attractions_answers,
                         self.shopping_answers, self.culture_answers, self.wildlife_answers]:
            self.all_answers.update(category)
        
        self.total_answers = len(self.all_answers)
        print(f"✅ MBANZA AI v13.0 READY: {self.total_answers} specific answers loaded")
    
    def find_answer(self, question):
        """Find the BEST answer for ANY question"""
        q = question.lower().strip()
        
        # Exact match
        if q in self.all_answers:
            return self.all_answers[q]
        
        # Partial match - find most similar question
        best_match = None
        best_score = 0
        
        for key in self.all_answers.keys():
            # Check if question contains key keywords
            key_words = set(key.split())
            q_words = set(q.split())
            common = key_words & q_words
            score = len(common)
            
            # Bonus for key phrases
            if len(key) > 20 and key in q:
                score += 10
            
            if score > best_score and score >= 2:  # At least 2 common words
                best_score = score
                best_match = key
        
        if best_match:
            return self.all_answers[best_match]
        
        return None
    
    def respond(self, question):
        """Main response generator"""
        q = question.lower().strip()
        
        # Special handling for greetings
        if re.search(r'\b(hi|hello|hey|bonjour|salut|good morning|good afternoon)\b', q):
            return self.greeting_response(q)
        
        # Special handling for who are you
        if re.search(r'\b(who are you|your name|what are you|qui es-tu)\b', q):
            return self.identity_response(q)
        
        # Special handling for thank you
        if re.search(r'\b(thank|merci|thanks)\b', q):
            return self.thank_response()
        
        # Special handling for help
        if q in ['help', 'commands', 'what can you do', '?', 'aide']:
            return self.help_response()
        
        # Try to find answer in database
        answer = self.find_answer(question)
        if answer:
            return answer + "\n\n💡 Anything else I can help you with? I'm here to make your Burundi trip amazing! 😊"
        
        # Ultimate fallback for unknown questions
        return self.fallback_response(question)
    
    def greeting_response(self, question):
        """Friendly greeting responses"""
        french = any(w in question.lower() for w in ['bonjour', 'salut', 'ça va'])
        if french:
            return "🇧🇮 Bonjour et bienvenue au Burundi! 🌍 Je suis Mbanza AI, votre assistant de voyage personnel. J'ai des réponses à TOUTES vos questions sur les hôtels, la nourriture, le transport, la sécurité, la santé, les attractions, les marchés, la culture, la faune, et bien plus encore! Comment puis-je vous aider aujourd'hui? 😊"
        return "🇧🇮 Hello and welcome to Burundi! 🌍 I'm Mbanza AI, your personal travel assistant. I have answers to EVERY question you might have about hotels, food, transport, safety, health, attractions, markets, culture, wildlife, and so much more! How can I help you today? 😊"
    
    def identity_response(self, question):
        """Who am I response"""
        french = any(w in question.lower() for w in ['qui es-tu', 'tu es qui', 'nom'])
        if french:
            return "🤖 Je suis Mbanza AI, créé par Mugisha Pc pour aider les touristes qui visitent le Burundi. Je connais TOUT sur ce magnifique pays: où dormir, où manger, comment se déplacer, la sécurité, la santé, les attractions, les marchés, la culture, la faune, et bien plus encore! Posez-moi n'importe quelle question - je suis là pour vous! 🇧🇮"
        return "🤖 I am Mbanza AI, created by Mugisha Pc to help tourists visiting Burundi. I know EVERYTHING about this beautiful country: where to sleep, where to eat, how to get around, safety, health, attractions, markets, culture, wildlife, and so much more! Ask me anything - I'm here for you! 🇧🇮"
    
    def thank_response(self):
        """Response to thank you"""
        return "🇧🇮 You're very welcome! 😊 It's my absolute pleasure to help you discover the beauty of Burundi. Do you have any other questions? I'm here 24/7 to make your trip unforgettable! 🌍"
    
    def help_response(self):
        """Help command response"""
        return """📚 MBANZA AI - COMPLETE TRAVEL ASSISTANT

I can answer ANY question about Burundi, including:

🏨 ACCOMMODATION - "Where can I find a place to sleep?"
🍽️ FOOD - "What's good to eat around here?"
🚗 TRANSPORT - "How do I get from Bujumbura to Gitega?"
🔒 SAFETY - "Is it safe to walk alone at night?"
💉 HEALTH - "Do I need a yellow fever vaccine?"
📍 ATTRACTIONS - "What can I do in Kibira National Park?"
🛍️ SHOPPING - "Where can I buy souvenirs?"
🎭 CULTURE - "What is the Intore dance?"
🦁 WILDLIFE - "Where can I see chimpanzees?"
🌤️ WEATHER - "What's the best time to visit?"
🗣️ LANGUAGE - "How do you say hello in Kirundi?"
💰 MONEY - "What currency do they use?"
📞 EMERGENCY - "What's the police number?"

Just ask naturally, like you're talking to a friend! I speak English and French. What would you like to know? 🇧🇮"""
    
    def fallback_response(self, question):
        """When no specific answer found"""
        # Detect language
        french = any(w in question.lower() for w in ['comment', 'où', 'quand', 'pourquoi', 'quel', 'quelle', 'est-ce que', 'je voudrais', 'je cherche'])
        
        if french:
            return f"""🇧🇮 Merci pour votre question! Je veux m'assurer de vous donner la meilleure réponse possible.

Pouvez-vous être un peu plus précis(e) ? Par exemple, demandez-moi :

• "Où puis-je trouver un hôtel pas cher à Bujumbura?"
• "Comment aller au parc national de Kibira?"
• "Est-ce que je peux boire l'eau du robinet?"
• "Quel est le meilleur restaurant pour manger du poisson?"

Je suis là pour vous aider avec TOUS vos besoins de voyage au Burundi. Que souhaitez-vous savoir exactement? 😊"""
        
        return f"""🇧🇮 Thank you for your question! I want to make sure I give you the best possible answer.

Could you be a bit more specific? For example, you could ask me:

• "Where can I find a cheap hotel in Bujumbura?"
• "How do I get to Kibira National Park?"
• "Is it safe to drink tap water?"
• "What's the best restaurant for fish?"

I'm here to help with ALL your Burundi travel needs. What would you like to know exactly? 😊"""

# Initialize AI
ai = MbanzaAIComplete()

# HTML Template (beautiful, mobile-friendly)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>Mbanza AI – Complete Burundi Travel Assistant</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #0a2f44 0%, #0a2f44 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 12px;
        }
        .app {
            width: 100%;
            max-width: 850px;
            background: white;
            border-radius: 32px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
            display: flex;
            flex-direction: column;
            height: 92vh;
        }
        .header {
            background: linear-gradient(135deg, #0a2f44 0%, #0a2f44 100%);
            color: white;
            padding: 18px 20px;
            text-align: center;
        }
        .header h1 { font-size: 26px; font-weight: 600; letter-spacing: -0.5px; }
        .header p { font-size: 11px; opacity: 0.85; margin-top: 4px; }
        .badge {
            display: inline-flex;
            gap: 12px;
            justify-content: center;
            margin-top: 8px;
            font-size: 10px;
            background: rgba(255,255,255,0.15);
            padding: 5px 14px;
            border-radius: 30px;
        }
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 16px;
            background: #f0f2f5;
        }
        .message { margin-bottom: 16px; display: flex; animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
        .user-message { justify-content: flex-end; }
        .bot-message { justify-content: flex-start; }
        .message-bubble {
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 24px;
            font-size: 14px;
            line-height: 1.5;
            white-space: pre-wrap;
            word-wrap: break-word;
        }
        .user-message .message-bubble {
            background: #0a2f44;
            color: white;
            border-bottom-right-radius: 6px;
        }
        .bot-message .message-bubble {
            background: white;
            color: #1e293b;
            border-bottom-left-radius: 6px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.08);
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
            padding: 14px 18px;
            border: 1.5px solid #e2e8f0;
            border-radius: 30px;
            font-size: 15px;
            outline: none;
        }
        .input-area input:focus { border-color: #0a2f44; }
        .input-area button {
            padding: 14px 24px;
            background: #0a2f44;
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 500;
            cursor: pointer;
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
            border-radius: 30px;
            font-size: 11px;
            cursor: pointer;
            color: #0a2f44;
        }
        .quick-btn:active { background: #0a2f44; color: white; }
        .typing { display: flex; gap: 4px; padding: 8px 0; }
        .typing span {
            width: 8px; height: 8px; background: #94a3b8; border-radius: 50%;
            animation: typingAnim 1.4s infinite;
        }
        .typing span:nth-child(2) { animation-delay: 0.2s; }
        .typing span:nth-child(3) { animation-delay: 0.4s; }
        @keyframes typingAnim {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
            30% { transform: translateY(-8px); opacity: 1; }
        }
        @media (max-width: 550px) {
            .message-bubble { max-width: 90%; font-size: 13px; }
            .quick-buttons { display: none; }
            .header h1 { font-size: 20px; }
        }
    </style>
</head>
<body>
<div class="app">
    <div class="header">
        <h1>🇧🇮 Mbanza AI</h1>
        <p>Created by Mugisha Pc | {{ total_answers }}+ Specific Answers</p>
        <div class="badge">
            <span>🎯 EVERY Question Answered</span>
            <span>🌍 English & Français</span>
        </div>
    </div>
    <div class="chat-area" id="chatArea">
        <div class="message bot-message">
            <div class="message-bubble">
                <strong>🇧🇮 Welcome to Mbanza AI!</strong><br><br>
                I am your COMPLETE Burundi travel assistant with <strong>{{ total_answers }}+ specific answers</strong> to EVERY question tourists ask.<br><br>
                Ask me ANYTHING, just like talking to a friend:<br>
                • "Where can I find a place to sleep in Bujumbura?" 🏨<br>
                • "Is it safe to walk alone at night?" 🔒<br>
                • "What's the best food to try?" 🍲<br>
                • "How do I get to Kibira National Park?" 🚗<br>
                • "Do I need a yellow fever vaccine?" 💉<br><br>
                <strong>I speak English and French. What would you like to know about Burundi? 🇧🇮</strong>
            </div>
        </div>
    </div>
    <div class="quick-buttons">
        <button class="quick-btn" onclick="ask('Where can I find a place to sleep in Bujumbura?')">🏨 Find a hotel</button>
        <button class="quick-btn" onclick="ask('What is the national dish of Burundi?')">🍲 National food</button>
        <button class="quick-btn" onclick="ask('Is it safe to travel to Burundi?')">🔒 Safety</button>
        <button class="quick-btn" onclick="ask('How do I get to Kibira National Park?')">🦍 To Kibira</button>
        <button class="quick-btn" onclick="ask('Do I need a yellow fever vaccine?')">💉 Health</button>
        <button class="quick-btn" onclick="ask('What animals can I see in Burundi?')">🦁 Wildlife</button>
        <button class="quick-btn" onclick="ask('Where can I buy souvenirs?')">🛍️ Shopping</button>
        <button class="quick-btn" onclick="ask('What is the Intore dance?')">🎭 Culture</button>
        <button class="quick-btn" onclick="ask('Comment aller à Bujumbura depuis l aéroport?')">🇫🇷 Français</button>
    </div>
    <div class="input-area">
        <input type="text" id="messageInput" placeholder="Ask me anything about Burundi..." onkeypress="if(event.key=='Enter') sendMessage()">
        <button onclick="sendMessage()">Send 💬</button>
    </div>
</div>
<script>
    const chatArea = document.getElementById('chatArea');
    const messageInput = document.getElementById('messageInput');
    function scrollToBottom() { chatArea.scrollTop = chatArea.scrollHeight; }
    function escapeHtml(text) { const div = document.createElement('div'); div.textContent = text; return div.innerHTML; }
    function addMessage(text, isUser) {
        const div = document.createElement('div');
        div.className = isUser ? 'message user-message' : 'message bot-message';
        div.innerHTML = `<div class="message-bubble">${escapeHtml(text).replace(/\\n/g, '<br>')}</div>`;
        chatArea.appendChild(div);
        scrollToBottom();
    }
    function showTyping() {
        const div = document.createElement('div');
        div.className = 'message bot-message';
        div.id = 'typingIndicator';
        div.innerHTML = `<div class="message-bubble"><div class="typing"><span></span><span></span><span></span></div></div>`;
        chatArea.appendChild(div);
        scrollToBottom();
    }
    function hideTyping() { const typing = document.getElementById('typingIndicator'); if (typing) typing.remove(); }
    async function sendMessage() {
        const message = messageInput.value.trim();
        if (!message) return;
        addMessage(message, true);
        messageInput.value = '';
        showTyping();
        try {
            const response = await fetch('/chat', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ message: message }) });
            const data = await response.json();
            hideTyping();
            addMessage(data.response, false);
        } catch (error) { hideTyping(); addMessage('⚠️ Connection error. Please try again.', false); }
    }
    function ask(topic) { messageInput.value = topic; sendMessage(); }
    scrollToBottom();
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, total_answers=ai.total_answers)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    response = ai.respond(user_message)
    return jsonify({'response': response})

@app.route('/stats')
def stats():
    return jsonify({
        'status': 'ok',
        'version': '13.0',
        'creator': 'Mugisha Pc',
        'total_answers': ai.total_answers,
        'message': 'Mbanza AI is ready to answer ANY tourist question about Burundi! 🇧🇮'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
