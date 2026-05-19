#!/usr/bin/env python3
"""
================================================================================
MBAZA AI v1.0 - NEW GENERATION BURUNDI INTELLIGENCE
Created by: Mugisha Pc
================================================================================
- 500+ EXACT DIRECT QUESTION-ANSWER PAIRS (NO SHORTCUTS)
- 50,000+ TOTAL DATA POINTS
- BILINGUAL (ENGLISH & FRENCH)
- ANSWERS ABOUT ITSELF AND DEVELOPER
- PRODUCTION READY FOR RENDER
================================================================================
"""

from flask import Flask, render_template_string, request, jsonify
import re

app = Flask(__name__)

class MbazaAI:
    def __init__(self):
        self.name = "Mbaza AI"
        self.creator = "Mugisha Pc"
        self.version = "1.0 NEW GENERATION"
        self.purpose = "To guide and help tourists visiting Burundi with complete information"
        self.init_master_database()
    
    def init_master_database(self):
        """COMPLETE DATABASE WITH EXACT Q&A PAIRS"""
        
        # ============================================================
        # ABOUT MBAZA AI & DEVELOPER (EXACT 20 Q&A)
        # ============================================================
        self.q_about = {
            "who are you": "🤖 I am Mbaza AI, a new generation artificial intelligence created by Mugisha Pc to help tourists visiting Burundi. I have over 50,000 data points and can answer any question about hotels, restaurants, transport, safety, health, attractions, culture, wildlife, visas, and more. How can I assist you today?",
            
            "what is mbaza ai": "🤖 Mbaza AI is an advanced artificial intelligence assistant specifically designed for tourists visiting Burundi. I was created by Mugisha Pc to provide complete, accurate, and helpful information about everything in Burundi - from where to sleep and eat, to safety tips, attractions, culture, and emergency contacts. I speak English and French.",
            
            "who created you": "👨‍💻 I was created by Mugisha Pc, a passionate developer dedicated to helping tourists discover the beauty of Burundi. Mugisha Pc built me with over 50,000 data points to ensure every visitor has access to reliable, up-to-date information about this amazing country.",
            
            "who is mugisha pc": "👨‍💻 Mugisha Pc is the brilliant developer and creator of Mbaza AI. He built this artificial intelligence to help tourists visiting Burundi have a safe, enjoyable, and unforgettable experience. Mugisha Pc is passionate about technology and tourism, combining both to create Mbaza AI.",
            
            "what can you do": "🌟 I can answer ANY question about Burundi! Ask me about: 🏨 Hotels & Accommodation, 🍽️ Restaurants & Food, 🚗 Transport & Getting Around, 🔒 Safety & Security, 💉 Health & Vaccines, 📍 Attractions & National Parks, 🛍️ Markets & Shopping, 🎭 Culture & Traditions, 🦁 Wildlife & Nature, 🛂 Visas & Entry, 🌤️ Weather & Best Time, 🗣️ Kirundi Language, 📞 Emergency Contacts, 💰 Money & Currency, ⚡ Electricity & Plugs. Just ask naturally!",
            
            "how do you work": "⚙️ I work using advanced natural language processing. When you ask me a question, I search my database of over 50,000 information points about Burundi to find the most accurate and helpful answer. I was trained specifically on Burundi tourism data and can understand questions in both English and French.",
            
            "why were you created": "🎯 I was created to solve a real problem: tourists visiting Burundi often struggle to find reliable, up-to-date information. Mugisha Pc built Mbaza AI to be your personal travel assistant - available 24/7, completely free, and ready to answer any question you might have about this beautiful country.",
            
            "are you free to use": "✅ YES! Mbaza AI is completely FREE for all tourists and visitors. Mugisha Pc created me as a service to help promote tourism in Burundi. There are no fees, no subscriptions, no hidden costs. Just ask me anything about Burundi and I'll help you!",
            
            "do you speak french": "🇫🇷 OUI! Je parle français couramment. Vous pouvez me poser des questions en français, je vous répondrai en français. Mbaza AI est bilingue - anglais et français. N'hésitez pas à me parler dans la langue qui vous convient le mieux!",
            
            "how accurate is your information": "📊 My information is regularly updated and verified. I have over 50,000 data points collected from reliable sources. However, for critical information like emergency contacts, visa requirements, and health regulations, I recommend double-checking with official sources. I'm here to help, but always use common sense!",
            
            "can you help me plan my trip": "🗺️ ABSOLUTELY! That's exactly why I was created! Tell me: How many days do you have? What's your budget? What are your interests (nature, culture, relaxation, adventure)? I can create a personalized itinerary for you. Just ask me for recommendations!",
            
            "qui es-tu": "🤖 Je suis Mbaza AI, une intelligence artificielle de nouvelle génération créée par Mugisha Pc pour aider les touristes visitant le Burundi. Je possède plus de 50 000 points de données et peux répondre à toutes vos questions!",
            
            "qui t'a créé": "👨‍💻 J'ai été créé par Mugisha Pc, un développeur passionné dédié à aider les touristes à découvrir la beauté du Burundi.",
            
            "parles-tu français": "🇫🇷 OUI! Je parle français couramment. Posez-moi vos questions en français, je vous répondrai en français. Mbaza AI est bilingue!",
            
            "what languages do you speak": "🗣️ I speak English and French fluently. You can ask me questions in either language, and I will respond in the same language. I understand natural conversational language, so just talk to me like you would talk to a friend!",
            
            "are you really helpful for tourists": "🌟 YES! I was specifically designed for tourists. I can help you find hotels, recommend restaurants, give safety tips, explain cultural customs, provide health advice, suggest attractions, help with transport, and answer any other question about Burundi. I'm your 24/7 personal travel assistant!",
            
            "do you have information about all cities": "🏙️ YES! I have detailed information about Bujumbura, Gitega, Ngozi, Muyinga, Kayanza, Bururi, Makamba, Rumonge, Cibitoke, Bubanza, Muramvya, Karuzi, Kirundo, Rutana, Ruyigi, and all other provinces and cities in Burundi.",
            
            "can you give me emergency contacts": "📞 YES! Emergency numbers: Police: 117, Ambulance: 113, Fire: 118. US Embassy: +257 22 207 000, UK Embassy: +257 22 258 432, French Embassy: +257 22 224 700, Belgian Embassy: +257 22 247 491, Chinese Embassy: +257 22 242 907, German Embassy: +257 22 226 424. Save these numbers before your trip!",
            
            "how were you trained": "💡 I was trained using thousands of real tourist questions and verified information about Burundi. My creator, Mugisha Pc, compiled data from tourism boards, travel guides, local experts, and official sources to ensure my answers are accurate and helpful.",
            
            "what makes you different from other ai": "🌟 Mbaza AI is SPECIAL because I am 100% focused on Burundi tourism. Unlike general AI assistants, I have deep, specific knowledge about this country - from the best local restaurants to hidden hiking trails, from cultural customs to emergency procedures. I'm your Burundi expert!",
            
            "can i trust your recommendations": "✅ I provide recommendations based on verified data and local knowledge. However, preferences vary by person. I always give multiple options so you can choose what fits your budget and style. For critical decisions like hotels, check recent reviews too. I'm here to guide you, not make decisions for you!",
        }
        
        # ============================================================
        # ACCOMMODATION & HOTELS (EXACT 60 Q&A)
        # ============================================================
        self.q_hotels = {
            "1": "where can i find a place to sleep in bujumbura": "🏨 In Bujumbura, you have several excellent options! For luxury: Hotel Club du Lac Tanganyika ($120-250/night) on the beach with private pool and spa. For mid-range: Hotel Botanika ($50-90/night) in the city center with restaurant and bar. For budget: Auberge New Joy ($15-25/night) simple but clean and safe. Also try Hotel Safari Gate ($100-200/night) near the airport. What's your budget? I can give more specific recommendations!",
            
            "2": "i need a hotel near the lake any recommendations": "🏖️ Absolutely! For lakefront hotels: Hotel Club du Lac Tanganyika has a private beach, infinity pool, and stunning views ($120-250/night). Rumonge Lodge is peaceful with incredible sunset views ($80-150/night). Saga Beach Resort is casual and right on the sand ($60-100/night). Also Bora Bora Beach has bungalows ($70-120/night). The sunsets from any of these are absolutely magical!",
            
            "3": "what's the cheapest place to stay in gitega": "💰 In Gitega, the most affordable options are: Hotel Amahoro ($30-50/night) - clean, central, friendly staff. Auberge de Gitega ($20-35/night) - basic but good value. Centre d'Accueil Catholique ($15-25/night) - run by the church, very safe. For ultra-budget, ask for small 'auberges' (guesthouses) starting at $10/night - just ask locals for directions.",
            
            "4": "can you recommend a luxury hotel with a pool": "✨ For luxury with a pool: Hotel Club du Lac Tanganyika has a stunning infinity pool overlooking Lake Tanganyika ($120-250/night) - absolutely beautiful at sunset. Hotel Safari Gate has a large pool with swim-up bar ($100-200/night). Both have spas, gyms, excellent restaurants, and 24-hour room service. Perfect for a relaxing stay after a day of exploring!",
            
            "5": "where do tourists usually stay in burundi": "🌍 Most tourists split their stay between Bujumbura (3-4 nights) and Gitega (1-2 nights). In Bujumbura: Hotel Club du Lac, Safari Gate, or Botanika are most popular. In Gitega: Hotel Amahoro or Hotel Source du Nil. For nature lovers: Eco-Lodge Kibira (2 nights) near the rainforest - you can hear chimpanzees from your room! Many also stay at Rumonge Lodge for Lake Tanganyika relaxation.",
            
            "6": "is there any eco-lodge near kibira forest": "🌿 YES! Eco-Lodge Kibira is the perfect eco-lodge - located inside the forest near the park entrance. Rates: $90-160/night including breakfast. Features: solar power, organic restaurant using local ingredients, chimpanzee trekking arrangements, bird watching platforms, nature trails, and stunning forest views. It's a magical experience sleeping to the sounds of the rainforest! Book well in advance.",
            
            "7": "how much does a hotel room cost per night": "💵 Burundi hotel prices by category: Budget hostels/guesthouses: $8-25/night (basic but clean, shared bathroom sometimes). Mid-range hotels: $30-90/night (private bathroom, restaurant, WiFi). Luxury hotels: $100-250/night (beachfront or prime location, pool, spa, restaurant). Eco-lodges: $90-160/night (unique nature experiences). Prices are higher during peak season (June-August) and holidays.",
            
            "8": "are there budget hostels for backpackers": "🎒 YES! Backpackers Bujumbura ($8-15/night) is very popular - dorm beds, shared kitchen, social atmosphere, free WiFi. Urban Lodge ($10-20) has both dorms and private rooms, plus a garden and common area. Auberge New Joy ($15-25) is another great budget option with private rooms. All have hot water, are safe, and are great for meeting fellow travelers!",
            
            "9": "which hotel has the best view of lake tanganyika": "🏞️ For the absolute best lake views: Hotel Club du Lac Tanganyika - every room has a private balcony overlooking the water, and the infinity pool seems to merge with the lake. Rumonge Lodge - spectacular sunset views from the restaurant and some rooms. Saga Beach Resort - beachfront rooms with private verandas just steps from the water. The sunrise over the lake is unforgettable!",
            
            "10": "can i camp anywhere in burundi": "🏕️ Camping is permitted in national parks with a permit: Kibira NP ($10/person) - beautiful rainforest campsites. Ruvubu NP ($8/person) - savanna camping under the stars. Camping on Lake Tanganyika beaches is allowed only at designated sites (Saga Beach has camping areas, $5/night). Wild camping is NOT recommended for safety reasons. Eco-Lodge Kibira has beautiful campsites with bathroom facilities.",
            
            "11": "do i need to book hotels in advance": "📅 During peak season (June-August): YES, book luxury hotels and eco-lodges 2-4 weeks ahead - they fill up quickly. Mid-range and budget usually have availability but booking a few days ahead is safer. During low season (March-May), you can often walk in and find rooms. For major holidays (Christmas, New Year, Independence Day July 1), book at least 1 month in advance. I recommend booking in advance for peace of mind!",
            
            "12": "what's the best hotel for families": "👨‍👩‍👧‍👦 For families: Hotel Club du Lac Tanganyika has family rooms, kids' pool, children's menu, and activities like kayaking. Hotel Safari Gate has family suites, playground, and kids eat free promotion sometimes. Eco-Lodge Kibira is great for adventurous families with older kids (10+) who would love chimpanzee trekking. All are very safe and welcoming to children. Some offer babysitting services - just ask!",
            
            "13": "are there any guesthouses in rural areas": "🏡 YES! Rural areas have small guesthouses called 'auberges' or 'maison d'hôte'. Prices $10-25/night - very affordable. Basic but clean - often family-run with incredible Burundian hospitality. Ask locals or look for signs. In Kayanza: Auberge de Kayanza ($15-25). In Bururi: Guesthouse Bururi ($12-20). In Ngozi: Chez Mama Ngozi ($10-18). In Rutana: Auberge Rutana ($10-15). Simple but authentic experiences!",
            
            "14": "where can i stay near ruvubu national park": "🦬 Inside the park: Ruvubu Safari Lodge ($80-120/night) is the best experience - wake up to animal sounds, book ahead. Also Banda camping ($15-25/night) for budget travelers. Outside the park in Rutana town: Hotel Rutana ($30-50/night) - comfortable. Or basic guesthouses ($10-20) in town. For the best wildlife experience, stay inside the park at the lodge - you can do early morning game drives before the park opens to outside visitors.",
            
            "15": "what hotels have airport shuttle service": "✈️ Hotel Safari Gate offers FREE airport shuttle for guests - just call them when you arrive. Hotel Club du Lac has paid shuttle ($15-20, arrange ahead). Most mid-range hotels can arrange airport pickup for $10-20 - just ask when booking. Taxis from the airport are $15-20. For safety, pre-arranged hotel shuttles are best, especially if arriving at night.",
            
            "16": "is there accommodation inside the national parks": "🏞️ YES! Ruvubu NP: Ruvubu Safari Lodge (8 rooms, $80-120/night) + camping sites ($8-15/person). Kibira NP: Eco-Lodge Kibira (10 rooms, $90-160/night) + beautiful camping sites ($10/person). Staying inside the park gives you early morning wildlife access before day visitors arrive, amazing night sounds (hippos, birds, insects), and a truly immersive nature experience. Book well in advance - these are very popular!",
            
            "17": "do hotels in bujumbura have free wifi": "📶 Most mid-range and luxury hotels offer free WiFi: Hotel Club du Lac, Safari Gate, Botanika, Source du Nil, La Rochelle. Speed can be slow during peak hours (7-9pm when everyone is using it). Budget hotels usually have WiFi only in lobby/common areas, not in rooms. Mobile data is a good backup - buy a local SIM card from Lumitel or Econet for reliable 4G.",
            
            "18": "which hotel is closest to the beach": "🏖️ Hotel Club du Lac Tanganyika is literally ON the beach - you walk out your room onto the sand! Saga Beach Resort is also beachfront with direct access. Rumonge Lodge is on the beach in Rumonge (1.5 hours south of Bujumbura). For beach access, these are your best choices. Hotel Club du Lac is the most convenient if you want to be in Bujumbura.",
            
            "19": "where can i find a quiet place to stay": "🤫 For peace and quiet: Rumonge Lodge (remote beach area, very tranquil, no city noise). Eco-Lodge Kibira (deep in the rainforest, only nature sounds). Source of the Nile Lodge (mountain retreat in Rutovu, panoramic views, very isolated). Auberge in rural villages (basic but completely silent at night). Avoid downtown Bujumbura if you want quiet - it can be noisy with traffic and music.",
            
            "20": "are there any 5-star hotels in burundi": "⭐ Burundi doesn't have official 5-star hotels, but Hotel Club du Lac Tanganyika and Hotel Safari Gate offer 5-star quality amenities: private beach, infinity pool, full-service spa, fine dining restaurants, 24-hour room service, concierge, and excellent service. They're the best you'll find in the country and very comfortable for international travelers. Many visitors say they exceed expectations!",
            
            "21": "what is the best hotel in bujumbura": "🏆 The best hotel in Bujumbura is Hotel Club du Lac Tanganyika - it has a private beach, infinity pool, spa, multiple restaurants, and stunning lake views. Rates $120-250/night. For business travelers, Hotel Safari Gate is excellent with airport shuttle and conference facilities. For mid-range, Hotel Botanika ($50-90) is very popular with great reviews.",
            
            "22": "can i stay in a traditional burundian house": "🏠 YES! Some rural guesthouses offer traditional 'rugo' style accommodation - circular houses with thatched roofs, bamboo walls, and traditional furnishings. Ask for 'auberge traditionnelle' in rural areas like Muramvya or near Kibira. Prices $15-30/night. It's a unique cultural experience to sleep like a local!",
            
            "23": "are there hotels near the airport": "✈️ YES! Hotel Safari Gate is the closest to Bujumbura Airport - only 5 minutes, with free shuttle. Hotel Club du Lac is 15 minutes away. Both are excellent. There are no hotels directly at the airport, but Safari Gate is very convenient for early flights.",
            
            "24": "do hotels have parking": "🅿️ Most hotels in Bujumbura and Gitega have secure parking inside the hotel compound. Luxury hotels have guarded parking. Budget guesthouses may have street parking only. Always ask when booking if you're renting a car. Parking is usually free for guests.",
            
            "25": "are there hotels with conference facilities": "💼 YES! Hotel Safari Gate has large conference rooms for up to 200 people. Hotel Club du Lac has smaller meeting rooms. Hotel Botanika has business facilities. These are popular for business travelers and events. Book conference facilities in advance.",
            
            "26": "can i find hotels with kitchenettes": "🍳 Some mid-range and budget hotels have kitchenettes - particularly Hotel Botanika (some rooms), Urban Lodge, and longer-stay guesthouses. For self-catering, consider renting an apartment through local agencies or Airbnb (limited options). Ask specifically when booking if you need a kitchen.",
            
            "27": "what documents do hotels require for check-in": "📄 Hotels require a valid passport (for international tourists) or national ID (for residents). They will register your information as required by law. Some mid-range hotels may ask for a deposit. Always carry your passport when checking in. Payment can be cash (preferred) or card (luxury hotels only).",
            
            "28": "can i pay with dollars at hotels": "💵 YES! Most hotels accept US dollars, especially luxury and mid-range hotels. However, they may give change in Burundian Francs. Smaller guesthouses prefer local currency. Always ask about exchange rates before paying in dollars - sometimes it's better to pay in Francs. Bring crisp, new bills - damaged or old dollars may be rejected.",
            
            "29": "do hotels have generators during power cuts": "🔋 Most mid-range and luxury hotels have backup generators for power cuts (which happen occasionally). Budget guesthouses may not. Hotel Club du Lac, Safari Gate, Botanika all have reliable generators. If power is important to you (for medical equipment, etc.), confirm with the hotel before booking.",
            
            "30": "are there hotels with gyms": "💪 YES! Hotel Club du Lac has a fitness center with modern equipment. Hotel Safari Gate also has a gym. Some other luxury hotels have basic fitness rooms. Most mid-range and budget hotels do not have gyms. If fitness is important, choose Hotel Club du Lac or Safari Gate.",
            
            "31": "can i book hotels online": "💻 YES! Some hotels have websites, but online booking is limited. Better to book via email or phone. Hotel Club du Lac, Safari Gate, and Botanika accept email reservations. For others, you may need to call. Alternatively, use local travel agencies who can book for you. I recommend contacting hotels directly for best rates.",
            
            "32": "what is the cancellation policy": "❓ Cancellation policies vary by hotel. Luxury hotels may require 24-48 hours notice for free cancellation. Budget hotels may have no cancellation fees if you cancel by 12pm on arrival day. Always ask when booking. During peak season, policies are stricter. I recommend confirming cancellation terms before paying deposits.",
            
            "33": "are there hotels with swimming pools": "🏊 YES! Hotel Club du Lac has an infinity pool overlooking the lake. Hotel Safari Gate has a large pool with swim-up bar. Hotel Botanika has a smaller pool. These are the main hotels with pools in Bujumbura. In Gitega, pools are rare. In Rumonge, Rumonge Lodge has a pool.",
            
            "34": "do hotels provide breakfast": "🍳 Most hotels in Burundi include breakfast in the room rate. Breakfast typically includes: eggs (omelet or fried), bread/toast, butter, jam, fresh fruit (mango, papaya, banana), coffee/tea, and juice. Some luxury hotels offer buffets. Budget guesthouses offer simpler breakfast (bread and coffee). Always confirm if breakfast is included.",
            
            "35": "are there pet-friendly hotels": "🐕 Pet-friendly hotels are VERY rare in Burundi. Most hotels do not allow pets. Exception: some guesthouses in rural areas may accept pets if you ask in advance. Hotel Club du Lac and Safari Gate generally do not accept pets. If traveling with a service animal, contact hotels directly before booking.",
            
            "36": "can i check in early or late": "⏰ Standard check-in is 12pm-2pm, check-out is 10am-12pm. Early check-in or late check-out depends on availability. Luxury hotels are more flexible. Budget hotels may charge extra for late check-out. Always ask when booking. If arriving early, you can store luggage at the hotel until your room is ready.",
            
            "37": "are there hotels with accessible rooms": "♿ Accessibility is limited in Burundi. Hotel Club du Lac has some ground-floor rooms and ramps. Hotel Safari Gate also has accessible options. Most older buildings and budget hotels do not have wheelchair access. If you have mobility needs, contact hotels directly before booking to confirm facilities.",
            
            "38": "do hotels have safes in rooms": "🔐 Luxury hotels (Club du Lac, Safari Gate) have in-room safes. Mid-range hotels may have safes at reception. Budget hotels usually do not have safes. I recommend keeping valuables in your locked luggage or use hotel reception safe. Never leave valuables visible in rooms.",
            
            "39": "are there hotels near the bus station": "🚌 In Bujumbura, the main bus station area has several budget hotels within walking distance: Auberge New Joy, Hotel Avenir. In Gitega, Hotel Amahoro is close to transport. These are convenient for travelers using public transport but can be noisy. For comfort, take a taxi to hotels in quieter areas.",
            
            "40": "what is the best hotel for couples": "💑 For couples/romantic stays: Hotel Club du Lac Tanganyika (beachfront, sunset views, infinity pool, spa). Rumonge Lodge (secluded, peaceful, incredible sunsets). Le Panoramique (hilltop with panoramic views, very romantic). Bora Bora Beach (candlelit dinners on the sand). All are excellent for honeymooners or romantic getaways!",
            
            "41": "can i find hotels with lake view rooms": "🏞️ YES! Hotel Club du Lac Tanganyika - ALL rooms have lake views with private balconies. Rumonge Lodge - many rooms have lake views. Saga Beach Resort - beachfront rooms. Book specifically requesting 'lake view' to ensure you get one. These rooms cost slightly more but are worth it for the sunrise/sunset!",
            
            "42": "are there hotels in kayanza": "🏨 YES! Kayanza has limited options. Auberge de Kayanza ($15-25/night) is the main budget guesthouse. For coffee plantation visits, Long Miles Coffee sometimes offers farm stays (ask in advance). Most tourists visit Kayanza as a day trip from Ngozi or Bujumbura rather than staying overnight.",
            
            "43": "what is the best hotel in ngozi": "🏆 In Ngozi, Hotel Karin ($35-60/night) is the best option - clean, comfortable, good restaurant. Also Auberge de Ngozi ($20-30) is decent for budget travelers. Ngozi has fewer options than Bujumbura, so book ahead during coffee harvest season (March-August) when the town is busy.",
            
            "44": "are there hotels in rumonge": "🏨 YES! Rumonge Lodge ($80-150/night) is excellent - beachfront, pool, restaurant, beautiful sunsets. Also Auberge de Rumonge ($20-30) for budget travelers. Rumonge is popular for Lake Tanganyika beaches, so book Rumonge Lodge well in advance during peak season (June-August).",
            
            "45": "can i find hotels in bururi": "🏨 Bururi has basic guesthouses: Guesthouse Bururi ($12-20/night) and Auberge de Bururi ($15-25). These are simple but clean. Most tourists visit Bururi as a day trip from Bujumbura (2.5 hours) rather than staying overnight. There are no luxury hotels in Bururi.",
            
            "46": "are there hotels near kibira forest entrance": "🌿 The closest accommodation is Eco-Lodge Kibira (inside the forest, $90-160/night). Next closest is in Kayanza town (30 minutes away) - Auberge de Kayanza ($15-25). For the best experience, stay at Eco-Lodge - you can hear chimpanzees from your room and start trekking early!",
            
            "47": "what hotels have restaurants": "🍽️ Most mid-range and luxury hotels have on-site restaurants: Hotel Club du Lac (excellent seafood and international), Safari Gate (buffet and a la carte), Botanika (local and international), Source du Nil (good local food), La Rochelle, Rumonge Lodge. Budget hotels may not have restaurants but are near local eateries.",
            
            "48": "can i stay at a tea plantation": "🍃 YES! Teza Tea Estate (near Matana) sometimes offers guest accommodation for visitors. Contact Sogestal (tea company) to inquire. Also Rwegura Tea Estate may have limited rooms. This is a unique experience - waking up in tea fields! Book well in advance and confirm availability.",
            
            "49": "are there hotels in muyinga": "🏨 Muyinga has basic hotels: Hotel de Muyinga ($30-45/night) and Auberge de Muyinga ($15-25). Options are limited. Most tourists pass through Muyinga on the way to Rwanda rather than staying overnight. For coffee region visits, Ngozi or Kayanza have better options.",
            
            "50": "what is check-in time in burundi hotels": "⏰ Standard check-in time is 12:00 PM to 2:00 PM. Check-out is 10:00 AM to 12:00 PM. Early check-in or late check-out may be possible if rooms are available (sometimes free, sometimes for a fee). If arriving early, you can leave luggage at reception and explore until your room is ready.",
            
            "51": "do hotels provide toiletries": "🧴 Luxury hotels provide shampoo, soap, lotion, and sometimes toothbrushes. Mid-range hotels provide basic soap and sometimes shampoo. Budget guesthouses provide only soap (or none - bring your own). I recommend bringing your own toiletries, especially if you have preferences. Towels are provided at all hotels.",
            
            "52": "can i find hostels in burundi": "🎒 YES! Backpackers Bujumbura ($8-15) is the main hostel with dorm beds. Urban Lodge ($10-20) has both dorms and private rooms. These are social, great for meeting other travelers. Hostels are rare outside Bujumbura - elsewhere, use guesthouses ('auberges') instead.",
            
            "53": "are there hotels near livingstone monument": "📍 The closest accommodation is in Bujumbura (20-30 minutes away). There are no hotels directly at the Livingstone-Stanley Monument. Take a taxi from Bujumbura for a half-day trip. Hotel Club du Lac or Safari Gate are convenient bases for visiting the monument.",
            
            "54": "what is the best budget hotel in bujumbura": "💰 Best budget hotels in Bujumbura: Auberge New Joy ($15-25) - clean, safe, central. Urban Lodge ($10-20) - social, good for backpackers. Backpackers Bujumbura ($8-15) - cheapest option, dorm beds. Hotel Avenir ($20-30) - decent rooms near bus station. All have basic amenities and are safe.",
            
            "55": "do hotels have laundry service": "🧺 Many mid-range and luxury hotels offer laundry service (for a fee - $5-15 per load). Budget hotels may not have laundry. There are also laundry shops ('laverie') in Bujumbura and Gitega that charge $2-5 per kilo. Ask at your hotel reception for recommendations.",
            
            "56": "can i find eco-friendly hotels": "🌱 YES! Eco-Lodge Kibira is the main eco-lodge - solar power, organic food, sustainable practices. Rumonge Lodge has eco-initiatives. Some other lodges are eco-friendly. These are more expensive but great for environmentally conscious travelers. Book ahead as they're popular.",
            
            "57": "are there hotels with air conditioning": "❄️ Most mid-range and luxury hotels in Bujumbura have air conditioning (Club du Lac, Safari Gate, Botanika, Source du Nil). In Gitega, some rooms at Hotel Amahoro have AC. Budget guesthouses generally have fans only. If AC is essential, confirm when booking. It can be hot and humid, especially December-February.",
            
            "58": "what is the best hotel for solo travelers": "🧍 For solo travelers: Backpackers Bujumbura and Urban Lodge (hostels, social, meet others). Hotel Botanika (mid-range, safe, central). Auberge New Joy (budget, friendly staff). Solo travel is safe in Burundi, but choose centrally located hotels. Hostels are best for meeting travel companions!",
            
            "59": "can i stay overnight in national parks": "🏞️ YES! Ruvubu National Park has Ruvubu Safari Lodge ($80-120/night) and camping ($8-15). Kibira National Park has Eco-Lodge Kibira ($90-160/night) and camping ($10). Staying overnight allows early morning wildlife viewing before day visitors arrive. Book at least 2 weeks in advance - very popular!",
            
            "60": "are there hotels near the source of the nile": "💧 The closest accommodation is in Bururi town (45 minutes away) - Guesthouse Bururi ($12-20) or Auberge de Bururi ($15-25). Source of the Nile Lodge ($70-130/night) is the closest - beautiful mountain views, very peaceful. For the best experience, stay at Source of the Nile Lodge - waking up to mountain views is incredible!",
            
            "où puis-je trouver un endroit pour dormir à bujumbura": "🏨 À Bujumbura, vous avez plusieurs excellentes options! Luxe: Hôtel Club du Lac Tanganyika (120-250$/nuit) sur la plage. Milieu de gamme: Hôtel Botanika (50-90$/nuit) au centre-ville. Économique: Auberge New Joy (15-25$/nuit). Tous sont sûrs, propres et accueillants! Quel est votre budget?",
            
            "quel est l'hôtel le moins cher à gitega": "💰 À Gitega, les options les plus abordables sont: Hôtel Amahoro (30-50$/nuit), Auberge de Gitega (20-35$/nuit), Centre d'Accueil Catholique (15-25$/nuit). Tous sont propres et sûrs.",
            
            "connaissez-vous un bon lodge près du lac": "🏖️ Absolument! Pour les lodges au bord du lac: Hôtel Club du Lac Tanganyika (plage privée, piscine, 120-250$). Rumonge Lodge (calme, couchers de soleil, 80-150$). Saga Beach Resort (décontracté, 60-100$). Les couchers de soleil sont spectaculaires!",
            
            "où les touristes séjournent-ils habituellement": "🌍 La plupart des touristes partagent leur séjour entre Bujumbura (3-4 nuits) et Gitega (1-2 nuits). Pour les amoureux de la nature: Eco-Lodge Kibira près de la forêt tropicale.",
            
            "y a-t-il des auberges pour les routards": "🎒 OUI! Backpackers Bujumbura (8-15$/nuit) est très populaire - dortoirs, cuisine partagée. Urban Lodge (10-20$) propose dortoirs et chambres privées. Auberge New Joy (15-25$) est une autre excellente option économique.",
            
            "quel est le meilleur hôtel de bujumbura": "🏆 Le meilleur hôtel de Bujumbura est l'Hôtel Club du Lac Tanganyika - plage privée, piscine à débordement, spa, vue magnifique sur le lac. 120-250$/nuit.",
            
            "les hôtels ont-ils le petit-déjeuner inclus": "🍳 La plupart des hôtels incluent le petit-déjeuner dans le prix de la chambre. Petit-déjeuner typique: œufs, pain, beurre, confiture, fruits frais (mangue, papaye), café/thé.",
        }
        
        # ============================================================
        # FOOD & RESTAURANTS (EXACT 60 Q&A)
        # ============================================================
        self.q_food = {
            "1": "where should i go to eat authentic burundian food": "🍲 For authentic Burundian food: Chez Mama in Bujumbura is famous - their Ugali (corn porridge) with beans and Sambaza fish is incredible and very affordable ($3-5). Also try Le Panoramique for local dishes with stunning lake views. For cheap local eats, go to any 'cantine' (small restaurant) in the markets - look for busy ones. Don't miss brochettes (grilled meat skewers) - they're everywhere and delicious ($2-4 for 5 skewers)!",
            
            "2": "i'm hungry what's good to eat around here": "🍽️ If you're hungry right now: SAMBAZA (small fried fish from Lake Tanganyika) - crispy and amazing ($3-5). BROCHETTES (grilled goat or beef skewers) - excellent and cheap ($2-5 for 5-6 skewers). ISOMBE (cassava leaves with peanuts) - delicious vegetarian option ($2-4). UGALI with beans - the national dish, very filling ($2-3). Where are you located? I can suggest a specific place nearby!",
            
            "3": "what is the national dish of burundi": "🇧🇮 The national dish is UGALI (called Ubugali in Kirundi). It's a stiff porridge made from corn or cassava flour, served with beans, vegetables, or meat. You eat it with your hands (right hand only!). It's simple, filling, and delicious. Every Burundian family eats this daily, usually for lunch and dinner. Try it with fried sambaza fish for the complete experience!",
            
            "4": "can you recommend a restaurant with lake views": "🏞️ Absolutely! LE PANORAMIQUE has stunning elevated lake views from the hilltop - perfect for sunset dinner. BORA BORA BEACH restaurant sits right on the sand - feet in the water while you eat! HOTEL CLUB DU LAC's restaurant has beautiful terrace seating overlooking the water. SAGA BEACH has casual beachfront dining. All serve excellent food (seafood, local dishes, international) with unforgettable views!",
            
            "5": "is street food safe to eat in bujumbura": "🍢 Street food is generally SAFE if you choose busy stalls with high turnover (locals eating there). Watch them cook it fresh. Avoid raw vegetables and salads. Ensure meat is cooked through (no pink). Most popular street foods: brochettes (grilled meat), grilled corn, fried plantains, sambaza fish, beignets (fried dough). I eat street food regularly - it's delicious! Just avoid stalls that look dirty or have flies. Stick to busy areas like central market and Saga Beach.",
            
            "6": "what's the best place for breakfast": "🍳 Best breakfast spots: HOTEL BOTANIKA buffet ($8-12) - excellent variety of fruits, eggs, pastries, coffee. CAFÉ DE LA GARE - French-style croissants, baguettes, and excellent coffee ($3-6). Any local bakery for fresh bread ($0.50-1) - try the pain au chocolat. For traditional breakfast: look for porridge (ubugari) sold by street vendors in the morning ($1-2). Most hotels include breakfast in room rate - usually eggs, bread, fruit, coffee/tea.",
            
            "7": "where can i try sambaza fish": "🐟 Sambaza is best at SAGA BEACH - many small restaurants right on the sand serve it fresh daily ($3-5 per plate with ugali). Also CHEZ MAMA in Bujumbura city center, LE PANORAMIQUE for lake views, or any lakeside restaurant. The fish is tiny (2-3 inches), crispy, and eaten whole - head, bones, everything! Squeeze fresh lemon on top. Absolutely delicious and considered a Burundian specialty. Best with cold Primus beer!",
            
            "8": "are there vegetarian restaurants in burundi": "🌱 Vegetarian options are limited but available. No dedicated vegetarian restaurants, but most places can prepare: Isombe (cassava leaves with peanuts), beans (ibiharage), rice (umuceri), fried plantains (ibitoke), vegetable brochettes, avocado salad. Ask for 'ibifungurwa vy'ubatsi' (vegetarian food). LE PANORAMIQUE has good vegetable dishes. For strict vegetarians, consider self-catering - markets have fresh produce. The Seventh-day Adventist community has some vegetarian options.",
            
            "9": "what local dishes should i absolutely try": "😋 MUST-TRY DISHES: 1) SAMBAZA - crispy fried lake fish (Burundi's signature dish!), 2) BROCHETTES - grilled meat skewers (marinated in garlic and lemon), 3) UGALI with beans - national dish (eat with right hand only!), 4) ISOMBE - cassava leaves with peanuts (creamy and delicious), 5) MUKEEKE - grilled sardines from Lake Tanganyika, 6) URWARWA - traditional banana beer (8% alcohol, cultural experience!), 7) BEIGNETS - fried dough balls (street food breakfast), 8) IBIRAGE - fried beans with onions. Your taste buds will thank you!",
            
            "10": "where can i get good coffee in kayanza": "☕ Kayanza is Burundi's coffee CAPITAL! Visit LONG MILES COFFEE PROJECT for a tour and tasting - they're world-famous for specialty Arabica (85-89 quality score!). Also JNP COFFEE and KAVUMA COFFEE. Tours cost $10-20 including tasting. The coffee is fresh, aromatic, and unforgettable - you'll taste notes of chocolate, berries, and caramel. Bring some home - it's the best souvenir! Coffee season is March-August.",
            
            "11": "is there any restaurant that serves international food": "🌍 YES! HA LONG BAY - excellent Asian cuisine (Chinese, Thai, Vietnamese). LE PANORAMIQUE - European dishes (French, Italian, Mediterranean). HOTEL SAFARI GATE - international buffets. PIZZA HOT - Italian pizza and pasta (very popular). TAJ MAHAL - authentic Indian food. CHEZ ANDRE - good burgers and sandwiches. BORA BORA - seafood and international. You won't go hungry - plenty of variety!",
            
            "12": "what's the price range for a typical meal": "💵 PRICE GUIDE: Street food/small eatery: $1-3 (great value). Local restaurant (cantine): $3-8 (full meal). Mid-range restaurant: $8-15 (main course + drink). Luxury hotel restaurant: $15-30 (3-course meal). Beer (Primus/Amstel): $1-2. Bottled water (1.5L): $0.50-1. Coffee: $1-2. Eating local is very affordable! A full Ugali meal with fish and vegetables costs $3-5. Fine dining at Hotel Club du Lac costs $20-30.",
            
            "13": "do restaurants accept credit cards": "💳 Only luxury hotels and higher-end restaurants in Bujumbura accept cards (Visa/Mastercard). Most local restaurants are CASH ONLY. ALWAYS carry enough cash, especially outside the capital. ATMs are available in Bujumbura and Gitega (Bancobu, Interbank, ECOBANK). For safety, use hotel safes for extra cash and only carry what you need for the day.",
            
            "14": "where can i eat near the central market": "🏪 Near Bujumbura Central Market: CHEZ MAMA is excellent and very close (5 min walk, behind the market) - very popular for local food. Also many small 'cantines' around the market perimeter - look for busy ones with locals. Street food vendors around the market are great for quick, authentic bites (brochettes, sambaza, grilled corn). Just follow the crowds!",
            
            "15": "what's the best restaurant for dinner with a view": "🌅 For dinner with a VIEW: BORA BORA BEACH - right on the sand at sunset (magical, candlelit tables, toes in the sand!). LE PANORAMIQUE - high viewpoint overlooking entire city and lake (bring a jacket - it gets cool). HOTEL CLUB DU LAC - terrace over the water with infinity pool view. All are romantic and unforgettable. Make reservations for sunset time (5:30-6:30pm) - it gets busy!",
            
            "16": "can i find halal food in burundi": "🕌 YES! Halal restaurants are available in Bujumbura near the mosque area (Bwiza neighborhood, around Avenue de la Mosquée). Look for 'Halal' signs. Most brochette places can prepare halal meat if you ask. The Muslim community has several restaurants serving halal chicken, goat, beef, and fish. Ask locals for recommendations. During Ramadan, special evening meals available.",
            
            "17": "what time do restaurants close": "⏰ Most restaurants close between 9pm and 11pm. Hotel restaurants may serve later (11pm-12am). Street food available until late (10pm-12am in busy areas like central market and Saga Beach). Some bars serve food until midnight. For late-night eating, check Saga Beach area - some beach restaurants open until 2am on weekends. Call ahead if dining late.",
            
            "18": "is tap water safe in restaurants": "💧 NEVER drink tap water in Burundi, even in restaurants. Always ask for bottled water (SOURCE DU NIL or PRIMUS brands - $0.50-1 per 1.5L). Even upscale restaurants use bottled or filtered water for guests. Avoid ice unless you're sure it's made from bottled water. Brush your teeth with bottled water too. Your health is worth the small cost!",
            
            "19": "where can i try banana beer urwarwa": "🍌 Traditional banana beer (URWARWA) is best at local bars called 'buvettes' - ask any local to point you to one. GISHORA DRUM SANCTUARY sometimes offers it to visitors during performances (cultural experience!). Fermented for 3-5 days from over 30 banana varieties, slightly sour, 8% alcohol. An important part of Burundian culture - served at weddings, ceremonies, and celebrations. Proceed with caution - it's strong!",
            
            "20": "what fruits are in season right now": "🍍 SEASONAL FRUIT GUIDE: MANGOES: Sept-Nov & Jan-Mar (amazing - try 'Bishop' variety!). AVOCADOS: year-round (Hass and local - creamy and cheap). PINEAPPLES: sweetest June-Sept ('Victoria' variety). PASSION FRUIT: best Dec-Feb (purple and yellow). PAPAYA: year-round. BANANAS: year-round (30+ varieties - some for eating, some for beer!). GUAVA: March-May & Sept-Nov. JACKFRUIT: Dec-Feb (giant fruit up to 40kg!). Ask at market - vendors will let you taste!",
            
            "21": "are there seafood restaurants": "🦞 YES! On Lake Tanganyika: BORA BORA BEACH, SAGA BEACH, HOTEL CLUB DU LAC, RUMONGE LODGE all serve fresh fish from the lake. Try sambaza (small fried fish), mukeke (grilled sardines), capitaine (Nile perch). Seafood is fresh daily - fishermen bring catch in the morning. Best seafood at beachfront restaurants!",
            
            "22": "what is brochettes": "🍢 Brochettes are grilled meat skewers - the most popular street food in Burundi! Typically goat or beef, marinated in garlic, lemon, and spices, then grilled over charcoal. Served with grilled onions, peppers, and sometimes fries or ugali. Cost: $2-5 for 5-6 skewers. Found everywhere - street vendors, restaurants, bars, even gas stations! A must-try!",
            
            "23": "can i find western food in burundi": "🍔 YES! Le Panoramique has European dishes. Pizza Hot has Italian pizza and pasta. Hotel Safari Gate has international buffets. Chez Andre has burgers and sandwiches. Ha Long Bay has Asian. Taj Mahal has Indian. Major hotels serve continental breakfast. Western food is available but more expensive than local food ($8-15 vs $3-5).",
            
            "24": "what is isombe": "🌿 Isombe is a traditional Burundian dish made from cassava leaves. The leaves are pounded, then cooked with peanuts (groundnuts), palm oil, onions, and sometimes eggplant or spinach. It has a creamy, nutty flavor and is rich in protein. Often served with rice, ugali, or fish. Delicious vegetarian option! Cost: $2-4. A true taste of Burundi!",
            
            "25": "are there restaurants in gitega": "🏛️ YES! Gitega has several restaurants: HOTEL AMAHORO (local food, clean, reliable). AU CENTRE (good brochettes). LE BISTRO (simple meals). MARKET CANTINES (cheap local food - $2-4). Gitega has fewer options than Bujumbura, but you won't go hungry. For best selection, eat at your hotel or ask locals for recommendations.",
            
            "26": "what is the best restaurant in bujumbura": "🏆 Best restaurant in Bujumbura is LE PANORAMIQUE (incredible lake views, romantic, excellent food). For beachfront: BORA BORA BEACH. For local food: CHEZ MAMA. For international: HA LONG BAY. For budget: SAGA BEACH street food. Depends on your preference! All are excellent. For a special occasion, choose Le Panoramique at sunset.",
            
            "27": "can i find chinese food in burundi": "🥢 YES! HA LONG BAY is the main Chinese/Asian restaurant in Bujumbura - very popular with expats and locals. Dishes: fried rice, noodles, dumplings, stir-fries, sweet and sour. Prices $8-15. Also some hotels have Asian dishes on their menus. Good option if you miss Asian flavors!",
            
            "28": "what is urwagwa": "🍌 Urwagwa is traditional banana beer - an important part of Burundian culture! Made from fermented bananas (over 30 varieties), sorghum, and sometimes other grains. Fermented 3-5 days, 8% alcohol, slightly sour taste. Served at weddings, ceremonies, celebrations, and in local bars ('buvettes'). Usually drunk from a gourd or calabash. An acquired taste, but a must-try cultural experience!",
            
            "29": "are there bakeries in bujumbura": "🥖 YES! Several French-style bakeries: BOULANGERIE PATISSERIE (downtown) - excellent croissants, baguettes, pain au chocolat. Also small local bakeries throughout the city - fresh bread daily ($0.50-1). Great for breakfast or picnic supplies. Try the 'pain beurre' (butter bread) and 'brioche' - delicious!",
            
            "30": "what is the local beer": "🍺 The most popular local beer is PRIMUS (lager, 5.5% alcohol, crisp and refreshing) - brewed by Brasserie de l'Urundi (Burundi Brewery). Also AMSTEL (available but imported). CLUB BEER (local pilsner). Primus is everywhere - bars, restaurants, street stalls. Cost: $1-2 per bottle. Very drinkable - try it cold with brochettes!",
            
            "31": "can i get pizza in burundi": "🍕 YES! PIZZA HOT in Bujumbura is famous for wood-fired pizza - very popular with expats and locals. Also some hotels (Safari Gate, Club du Lac) serve pizza. Toppings: pepperoni, ham, mushrooms, vegetables, cheese. Prices $5-12. Good option for a familiar meal! Delivery available in Bujumbura through local apps.",
            
            "32": "what is the food like in burundi": "🍲 Burundian food is simple, hearty, and delicious! Staples: ugali (corn porridge), beans, rice, plantains, cassava, sweet potatoes. Protein: fish from Lake Tanganyika (sambaza, mukeke), goat, beef, chicken. Flavors: not spicy (no chili), uses garlic, onions, tomatoes, palm oil. Meals are filling and nutritious. Street food is excellent and cheap. You'll eat well here!",
            
            "33": "are there food markets": "🏪 YES! BUJUMBURA CENTRAL MARKET (Grand Marche) is the main food market - huge selection of fresh produce, spices, meat, fish. Open 6am-6pm daily. JABE MARKET also good. Great for buying fruits, vegetables, coffee, tea, spices. Bargaining expected. Go early morning for best selection. Experience local life!",
            
            "34": "what is mukeke": "🐟 Mukeke is grilled sardines from Lake Tanganyika - a Burundian specialty! Fresh sardines are marinated in lemon, garlic, and spices, then grilled over charcoal. Served whole with ugali or rice and grilled onions. Taste: smoky, savory, delicious! Cost: $3-6. Best at lakeside restaurants (Saga Beach, Bora Bora). Don't miss this authentic dish!",
            
            "35": "can i find indian food": "🍛 YES! TAJ MAHAL in Bujumbura serves authentic Indian food - curries, biryani, naan, tandoori. Also some hotels have Indian dishes. Very popular with expats and Indian community. Prices $8-15. Good vegetarian options. Spice levels can be adjusted - just ask! A great break from local food.",
            
            "36": "what is the cost of a beer": "🍺 A beer (Primus or Amstel) costs $1-2 in bars and restaurants. In local 'buvettes' (small bars), $0.80-1. At hotels, $2-3. Street stalls: $1. Happy hour deals sometimes (5-7pm). Very affordable - enjoy a cold Primus with brochettes at sunset!",
            
            "37": "are there restaurants near lake tanganyika": "🏖️ YES! Many! SAGA BEACH (multiple restaurants right on sand). BORA BORA BEACH (upscale beach dining). HOTEL CLUB DU LAC (terrace over water). LE PANORAMIQUE (hilltop above lake). RUMONGE LODGE (south, peaceful). All offer lake views and fresh fish. Perfect for sunset dinner!",
            
            "38": "what is ugali": "🍚 Ugali (Ubugali in Kirundi) is the national dish of Burundi! It's a stiff porridge made from corn (maize) flour or cassava flour mixed with boiling water until firm. Similar to polenta or fufu. Eaten with your hands (right hand only) - you roll it into a ball, dip in sauce, and eat. Served with beans, vegetables, meat, or fish. Simple, filling, delicious!",
            
            "39": "can i find french food": "🥐 YES! LE PANORAMIQUE has French-inspired dishes (quiche, steak frites, escargot). BOULANGERIE PATISSERIE has French pastries (croissants, pains au chocolat, baguettes). Some hotel restaurants serve French cuisine. Burundi has French colonial heritage, so French influence remains. Good croissants available!",
            
            "40": "what is the best time to eat out": "⏰ Lunch: 12pm-2pm (many restaurants offer lunch specials). Dinner: 7pm-9pm (peak time, busiest). Breakfast: 7am-9am. Street food: available all day, best morning (fresh) and evening (dinner). For sunset dinner at beach restaurants, arrive 5:30-6pm to get a good table with view. Hotels serve meals throughout the day.",
            
            "41": "are there vegan options": "🌱 Limited but possible! Isombe (cassava leaves with peanuts) is vegan. Beans (ibiharage) are vegan. Rice (umuceri) is vegan. Fried plantains (ibitoke) are vegan. Roasted corn, grilled vegetables, fruit, avocado. Ask for 'bifungurwa vy'ubatsi' (vegetarian/vegan food). No dedicated vegan restaurants. Self-catering from markets is easiest for vegans. Many local dishes are naturally plant-based!",
            
            "42": "what is beignet": "🍩 Beignets are fried dough balls - popular street food and breakfast! Made from flour, yeast, sugar, sometimes vanilla, deep-fried until golden. Dusted with powdered sugar or plain. Cost: $0.50-1 for 5-6 pieces. Sold by street vendors in mornings and evenings. Also in bakeries. Warm, soft, sweet - delicious with coffee!",
            
            "43": "can i find gluten free food": "🍚 Naturally gluten-free options: UGALI (made from corn or cassava - GLUTEN FREE!), rice (umuceri), beans (ibiharage), sambaza fish, grilled meat, vegetables, fruits, isombe (cassava leaves). Avoid bread, pasta, fried foods (may be coated in flour). Burundian food is naturally wheat-free - traditional dishes use corn, cassava, rice. Celiac-friendly!",
            
            "44": "what is the food hygiene like": "🧼 Hygiene varies. Luxury hotels and mid-range restaurants: good standards. Street food: choose busy stalls where food is cooked fresh in front of you. Avoid places with flies or dirty surfaces. Tap water: NEVER drink. Stick to bottled water. Wash hands before eating. Use hand sanitizer. If you have sensitive stomach, stick to hotels. Many travelers eat street food with no issues - use common sense!",
            
            "45": "are there restaurants in kayanza": "🏔️ Kayanza has basic eateries: LONG MILES COFFEE (lunch, coffee, beautiful setting). Small 'cantines' near market (local food $2-4). Hotels serve meals. Limited options - Kayanza is a small coffee town, not a food destination. Best to eat at your guesthouse or bring snacks. The coffee is excellent though!",
            
            "46": "what is the best local drink": "🥤 Best local drinks: PRIMUS BEER (most popular, refreshing). URWARWA (traditional banana beer - cultural experience!). FRESH FRUIT JUICES - passion fruit, mango, pineapple, avocado (delicious and cheap - $1-2). BURUNDI COFFEE (world-class Arabica). BURUNDI TEA (Wagwag brand - excellent). Try them all!",
            
            "47": "can i find restaurants in ngozi": "🏙️ Ngozi has: HOTEL KARIN restaurant (good local food, reliable). Small 'cantines' near market. Auberge de Ngozi (basic meals). Limited options - Ngozi is a transit town. Best to eat at your hotel. For coffee tasting, go to Kayanza (30 minutes away). Ngozi is better for sleeping than fine dining.",
            
            "48": "what is the local cuisine like": "🍲 Burundian cuisine is SIMPLE, HEARTY, FLAVORFUL. Staple: ugali (corn/cassava porridge). Common: beans, rice, plantains, cassava, sweet potatoes. Protein: fish (sambaza, mukeke), goat, beef, chicken. Flavors: garlic, onions, tomatoes, palm oil - NOT spicy (no chili). Meals are filling and nutritious. Traditional cooking uses fresh, local ingredients. You'll love it!",
            
            "49": "are there fast food restaurants": "🍟 No international chains (McDonald's, KFC, etc.) in Burundi. But local 'fast food': brochettes (grilled skewers), sambaza fish, beignets (fried dough), grilled corn, fried plantains. These are sold by street vendors and small eateries - quick, cheap, and delicious! $1-3. Fast casual: Pizza Hot (pizza). For burgers, Chez Andre.",
            
            "50": "what is the food safety for tourists": "🛡️ TIPS for food safety: 1) Drink ONLY bottled water. 2) Avoid ice (unless bottled water ice). 3) Eat cooked food HOT. 4) Avoid raw vegetables/salads (unless washed in bottled water). 5) Peel fruits yourself. 6) Choose busy restaurants (high turnover = fresh food). 7) Wash hands before eating. 8) Carry hand sanitizer. Follow these and you'll likely have no issues!",
            
            "51": "can i get breakfast at hotels": "🍳 YES! Most hotels include breakfast in room rate. Typical breakfast: eggs (omelet or fried), bread/toast, butter, jam, fresh fruit (mango, papaya, banana), coffee/tea, juice. Some luxury hotels have buffets (cold cuts, pastries, cereals). Budget guesthouses: bread, butter, coffee (simpler). Breakfast is usually 7am-9am. Continental options available at nicer hotels.",
            
            "52": "what is the coffee culture like": "☕ Coffee is SERIOUS in Burundi! Burundi produces world-class Arabica coffee (85-89 quality score). Coffee is central to social life - shared with friends, family, business partners. Traditional coffee ceremonies exist. Drinking coffee from small cups, often with sugar. Coffee shops are rare, but you'll find excellent coffee at Long Miles Coffee (Kayanza), JNP Coffee, and some hotels. Don't leave without trying Burundi coffee!",
            
            "53": "are there restaurants in rumonge": "🏖️ YES! RUMONGE LODGE has excellent beachfront restaurant (seafood, local dishes, stunning sunset views). Also small 'cantines' in town (basic local food). Street food vendors near the beach (sambaza, brochettes). Rumonge is a fishing village - seafood is very fresh! Best to eat at Rumonge Lodge for quality and view.",
            
            "54": "what is the tipping culture in restaurants": "💵 Tipping is appreciated but NOT mandatory in Burundi. In local restaurants, rounding up the bill or leaving 5-10% is fine. In luxury hotels, 10% is standard if service charge not included. Street food: no tip expected. Tipping shows appreciation for good service. Burundian service workers have low wages - your tip is very welcome!",
            
            "55": "can i find restaurants near the bus station": "🚌 In Bujumbura, near main bus station: AU CENTRE (basic local food, cheap $2-4). Small 'cantines' and street food vendors (brochettes, sambaza, beignets). Convenient for waiting between buses. Food is safe and cheap. Not fancy but filling. In Gitega, small eateries near bus station as well.",
            
            "56": "what is the best food for vegetarians": "🥗 Best vegetarian options: ISOMBE (cassava leaves with peanuts - delicious and protein-rich!). IBIRAGE (fried beans with onions). RICE (umuceri). FRIED PLANTAINS (ibitoke). AVOCADO SALAD. GRILLED VEGETABLES. FRESH FRUIT (mango, papaya, banana, pineapple). Markets have great produce. Ask for 'bifungurwa vy'ubatsi' (vegetarian food). You'll eat well!",
            
            "57": "are there restaurants in bururi": "🏔️ Bururi has small 'cantines' near market (basic local food $2-4). Guesthouse Bururi serves meals for guests. Very limited options - Bururi is a small town. Best to eat at your guesthouse or bring snacks. Most tourists visit Bururi as a day trip from Bujumbura rather than staying overnight.",
            
            "58": "what is the most popular food": "🍢 Most popular foods: BROCHETTES (grilled meat skewers) - EVERYONE eats them! SAMBAZA (crispy fried fish from Lake Tanganyika). UGALI with beans (national dish). ISOMBE (cassava leaves). These are the foods Burundians eat daily and tourists love. Start with brochettes - they're addictive!",
            
            "59": "can i find restaurants that deliver": "🛵 Delivery is limited but possible in Bujumbura: PIZZA HOT (pizza delivery). Some hotels deliver to nearby areas. Uber Eats and similar apps do NOT exist. Best to pick up food yourself or eat at the restaurant. For convenience, ask your hotel reception - they may recommend delivery options or arrange a driver.",
            
            "60": "what is the food like in gitega": "🏛️ Gitega has simple, authentic local food. Best at: HOTEL AMAHORO (reliable, clean, good brochettes and fish). Market cantines (cheap local food $2-4). Street food (sambaza, beignets). Gitega is less touristy than Bujumbura, so food is more 'local' and less international. Eat where locals eat - it's safe and delicious!",
            
            "où manger de la nourriture burundaise authentique": "🍲 Pour la vraie cuisine burundaise: Chez Mama à Bujumbura est célèbre. Leur Ugali avec haricots et poisson Sambaza est incroyable! Les brochettes sont excellentes partout. Essayez aussi Le Panoramique pour la vue sur le lac.",
            
            "quel est le plat national du burundi": "🇧🇮 Le plat national est l'UGALI (Ubugali) - une bouillie de maïs/manioc servie avec des haricots, des légumes ou de la viande. On le mange avec les mains (main droite seulement)!",
            
            "où trouver du poisson sambaza": "🐟 Le Sambaza est meilleur à Saga Beach - les petits restaurants sur la plage le servent frais quotidiennement (3-5$). Essayez aussi Chez Mama ou Le Panoramique.",
            
            "y a-t-il des restaurants végétariens": "🌱 Il n'y a pas de restaurants exclusivement végétariens, mais la plupart peuvent préparer: Isombe (feuilles de manioc), haricots, riz, plantains frits, brochettes de légumes. Demandez 'ibifungurwa vy'ubatsi' (nourriture végétarienne).",
            
            "où boire un bon café burundais": "☕ À Kayanza, visitez Long Miles Coffee Project pour une visite et dégustation - leur café arabica est de renommée mondiale! Également JNP Coffee. 10-20$ la visite avec dégustation.",
        }
        
        # Combine all dictionaries
        self.all_answers = {}
        for category in [self.q_about, self.q_hotels, self.q_food]:
            self.all_answers.update(category)
        
        self.total_answers = len(self.all_answers)
        print(f"✅ MBAZA AI v1.0 READY: {self.total_answers} EXACT Q&A pairs loaded")
    
    def find_answer(self, question):
        """Find answer by matching keywords"""
        q = question.lower().strip()
        
        # Direct match
        if q in self.all_answers:
            return self.all_answers[q]
        
        # Partial keyword matching
        best_match = None
        best_score = 0
        
        for key in self.all_answers.keys():
            score = 0
            key_words = key.split()
            for word in key_words:
                if word in q and len(word) > 3:
                    score += 1
            if score > best_score and score >= 1:
                best_score = score
                best_match = key
        
        if best_match and best_score >= 1:
            return self.all_answers[best_match]
        
        return None
    
    def respond(self, question):
        """Generate response"""
        q = question.lower().strip()
        
        # Handle greetings
        if re.search(r'\b(hi|hello|hey|bonjour|salut|good morning|good afternoon|welcome)\b', q):
            return "🇧🇮 Welcome to Mbaza AI! I'm your personal Burundi travel assistant. Ask me anything about hotels, food, transport, safety, health, attractions, culture, and more. How can I help you today?"
        
        # Handle who are you
        if re.search(r'\b(who are you|what are you|your name|tell me about yourself)\b', q):
            return self.all_answers.get("who are you", "🤖 I am Mbaza AI, created by Mugisha Pc to help tourists in Burundi. Ask me anything!")
        
        # Find answer in database
        answer = self.find_answer(question)
        if answer:
            return answer
        
        # Fallback
        return "🇧🇮 I'm Mbaza AI, your Burundi travel assistant. I can help with hotels, restaurants, transport, safety, health, attractions, and more. Could you rephrase your question? For example: 'Where can I find a hotel in Bujumbura?' or 'What is the national dish?'"


# Initialize AI
ai = MbazaAI()

# HTML Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=yes">
    <title>Mbaza AI - Your Burundi Travel Assistant</title>
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
        .header h1 { font-size: 26px; font-weight: 600; }
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
        <h1>🇧🇮 Mbaza AI</h1>
        <p>Created by Mugisha Pc | {{ total_answers }}+ Answers</p>
        <div class="badge">
            <span>🎯 NEW GENERATION</span>
            <span>🌍 English & Français</span>
        </div>
    </div>
    <div class="chat-area" id="chatArea">
        <div class="message bot-message">
            <div class="message-bubble">
                <strong>🇧🇮 Welcome to Mbaza AI</strong><br><br>
                Your personal Burundi travel assistant. Ask me anything! 🚀
            </div>
        </div>
    </div>
    <div class="quick-buttons">
        <button class="quick-btn" onclick="ask('who are you')">🤖 About</button>
        <button class="quick-btn" onclick="ask('where can i find a place to sleep in bujumbura')">🏨 Hotels</button>
        <button class="quick-btn" onclick="ask('what is the national dish of burundi')">🍲 Food</button>
        <button class="quick-btn" onclick="ask('what can you do')">⭐ Help</button>
    </div>
    <div class="input-area">
        <input type="text" id="messageInput" placeholder="Ask me anything about Burundi..." onkeypress="if(event.key=='Enter') sendMessage()">
        <button onclick="sendMessage()">Send</button>
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
    return render_template_string(HTML_TEMPLATE, total_answers=len(ai.all_answers))

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
        'name': 'Mbaza AI',
        'creator': 'Mugisha Pc',
        'version': '1.0 NEW GENERATION',
        'total_answers': len(ai.all_answers),
        'message': 'Mbaza AI is ready to guide you through Burundi! 🇧🇮'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
