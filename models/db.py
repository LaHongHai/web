import pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
client = pymongo.MongoClient("mongodb+srv://admin:kudo_321@cluster0-kafj1.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
mydb=client["places"]
mycoll = mydb["places list"]
mylist =[
    {"Id":1, 
    "Place":"Co To Island",
    "Region":"Northern Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal","Mountainous"],
    "Location":"Co To island is an archipelago located in the Gulf of Tonkin, including a large Co To Island, a small Co islands, the island of Thanh Lam, Tran and countless islands and small island.",
    "Description":"Co To Island in Quang Ninh Province is probably one of the most beautiful and romantic beaches in Vietnam with transparent blue sea, white smooth sand, golden sunshine, and green mountains and forest. Tourists who have never been to Co To may hardly imagine how fascinatingly and charmingly beautiful it is. Visiting Co To, tourists would not only have a chance to become one with the nature in a relaxing and fresh environment of blue clean seawater, but also to visit primitive forests, the impressive lighthouse of Co To, Ho Chi Minh’s Monument, Co To Pier, fishing village and natural reefs and islets."
    },
    {"Id":2, 
    "Place":"Cat Ba",
    "Region":"Northern Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal","Mountainous"],
    "Location":"Cat Ba Island, located in Hai Phong province, comprises the Cat Ba Archipelago, which makes up the southeastern edge of Lan Ha Bay in Northern Vietnam.",
    "Description":"A small island just off the North West coast, Cat Ba is one of the most popular places in Vietnam. Cat Ba island has a surface area of 285 km2 (110 square miles) and maintains the dramatic and rugged features of Ha Long Bay. Dominating the Gulf of Tonkin, Cat Ba is the largest of 367 islands making up the Cat Ba Archipelago. The topography is made up of sheltered bays dotted along sweeping coastlines with lush green forest flowing over steep hills and valleys. With its overnight cruise tours, rock climbing activities, open air markets, Cat Ba boast a broad range of recreational activities that cater for most people who visit this wonderful island. You can easily rent a motorbike from any hotel for $5 (standard) per day or less if you look around or visit in the low season. Buy your petrol at an official petrol station (Petrolimex) so you pay the official price. A small one is located in Cat Ba Town and a bigger one on the left side when you leave the town. The other option is to get petrol in bottles along the streets but it's much more expensive. Don't pay more than 50,000 VND for a 1.5L bottle of petrol, which can be bought in some of the small towns as well as near the port area near the end of the town. Anyone you hire a bike from should give you a photocopied map of the island which will help you with planning. Local buses across the island leave from the western edge of Cat Ba town, on the water near the market intersection."
    },
    {"Id":3, 
    "Place":"Sa Pa",
    "Region":"Northern Vietnam",
    "Season":["Summer","Winter"],
    "Geography":["Mountainous"],
    "Location":"Sapa is a frontier township and capital of Sa Pa District in Lào Cai Province in north-west Vietnam. It is one of the main market towns in the area.",
    "Description":"Located at 1500 meters (4921 feet) above sea level in Vietnam's remote northwest mountains, Sapa is famous for both its fine, rugged scenery and also its rich cultural diversity. Sapa is an incredibly picturesque town that lies in the Hoang Lien Son mountain range near the Chinese border in northwestern Vietnam, known as 'the Tonkinese Alps'. Sapa and its surrounding region is host to many hill tribes, as well as rice terraces, lush vegetation, and Fansipan, the highest peak in Vietnam. Other great mountains like Aurora & J, where Sa Pa sees the first rays of sun, make up a very steep valley. Many ethnic minorities live in and around Sapa. Excluding the Kinh people or ethnic Vietnamese, eight different ethnic minority groups are found in Sapa. They include H'mong (pronounced Mong), Dao (pronounced Yao), Tay, Giay (pronounced Zai), Muong, Thai, Hoa (ethnic Chinese) and Xa Pho (a denomination of the Phu La minority group). However, the last four groups comprise less than 500 people in total. The population of the district is estimated at 31,652 (1993) of which 52% are H'mong, 25% are Dao, 15% are Kinh, 5% are Tay and 2% are Giay. Around 3,300 people live in Sapa town, and the remainder are peasant farmers distributed unevenly throughout the district. The billboard in Sapa states proudly of its weather: 'Four seasons in one day'. Chilly winter in the early morning, spring time after sunrise, summer in afternoon and cold winter at night. Anywhere in the main village of Sapa can be reached on foot, and the town is small enough that you're not likely to get lost. A basic map will be good enough for most travellers."
    },
    {"Id":4, 
    "Place":"Tam Dao",
    "Region":"Northern Vietnam",
    "Season":["Summer","Winter","Spring","Autumn"],
    "Geography":["Mountainous"],
    "Location":"Tam Dao is a rural district of Vinh Phuc Province in the Red River Delta region of northern Vietnam.",
    "Description":"Tam Dao was founded by French colonialists in 1907 as a summer retreat from the heat of Hanoi. Today, Tam Dao is a popular summer resort for Hanoi residents & tourists thanks to its temperate climate.However during weekends, the hill station is very crowded & room prices double in the many hotels in town,so try to come only on weekdays & avoid public holidays. Tam Dao is a small mountainous town in Vinh Phuc Province. Regarded as the Da Lat in the North, Tam Dao possesses the cool weather all year round. Tourists can go to Tam Dao in any season in a year due to its wonderful weather. Especially, the temperature in Tam Dao is always lower than the temperature in Hanoi. Thus, most of travelers come here to enjoy the pleasant and cool atmosphere in summer. In winter, you can see a romantic and quite beauty with thick mist in this place. In addition, its location being just 70km from Hanoi has made it an attractive destination for visitors on weekends and holidays."
    },
    {"Id":5, 
    "Place":"Ba Na Hills",
    "Region":"Central Vietnam",
    "Season":["Summer","Winter","Spring","Autumn"],
    "Geography":["Mountainous"],
    "Location":"Ba Na Hills is a hill station and resort located in the Truong Son Mountains west of the city of Da Nang, in central Vietnam.",
    "Description":"Ba Na Hills is a hill station and resort located in the Truong Son Mountains west of the city of Da Nang, in central Vietnam. The station, advertised as 'the Da Lat of Danang province' by local tourism authorities, was founded in 1919 by French colonists. The colonists had built a resort to be used as a leisure destination for French tourists. Being located above 1500 meters above sea level, it has a view of the East Sea and the surrounding mountains. Ba Na Hills is one of the newest and most exciting projects in Vietnam. It’s a mountaintop resort complex that looks like a medieval castle, but inside these stone walls are modern accommodations, world class restaurants and a Fantasy Park full of exciting rides. The Ba Na Hills ticket price includes the entry ticket as well as cable cars for both ways to and from the park. Ticket price for an adult is 700,000 VND, including transfers by cable car, most games in Fantasy Park: 105 games and the Legendary Knight (tube slide), Family Entertainment Center (FEC), Linh Ung Pagoda, Linh Phong Tu Tower, Debay Wine Cellar, French Village, Le Jardin D’Amour, Tombstone Temple, Linh Chua Linh Tu Temple, Campanile, Ba Shrine, Funicular, Alpine Coaster."
    },
    {"Id":6, 
    "Place":"Hoi An",
    "Region":"Central Vietnam",
    "Season":["Spring"],
    "Geography":["Plain"],
    "Location":"Hoi An is a city with a population of approximately 120,000 in Vietnam's Quảng Nam Province",
    "Description":"Hoi An, once known as ‘Faifo’, with more than 2,000 years history, was the principal port of the Cham Kingdom, which controlled the strategic spice trade with Indonesia from the 7th to the 10th century and was a major international port in the 16th and 17th centuries - and the foreign influences are discernible to this day. Located on the coast of the Vietnam’s Central Sea, in the downstream of Thu Bon River, Quang Nam province, far from about 30 kilometers south of Da Nang, Hoi An Ancient Town is well-known as an crowded international commercial port where is the trade gateway between local people with merchant ships from Japan, China and the West during the 17th and 18th centuries. There are approximately 1,360 relics and landscapes, especially that relics are divided into 11 categories including 1,068 ancient houses, 19 pagoda, 43 divine shrine, 23 houses, 38 pagodas minority, 5 assembly halls, 11 old wells, 1 bridge, 44 ancient tombs. Hoi An Ancient Town recognized as a World Heritage Site by UNESCO in December 1999 becomes one of the most attractive destination in Vietnam. The centre of Hoi An is very small and pedestrianised, so you will be walking around most of the time. Motorbikes are only banned from the centre of town during certain times of day, so keep an eye out for them; even in the most narrow alleys. Evenings are especially busy with motorbikes two, or even three abreast competing with pedestrians for even the smallest space on the street!"
    },
    {"Id":7, 
    "Place":"Quy Nhon",
    "Region":"Central Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal"],
    "Location":"Quy Nhon is a coastal city in Binh Dinh Province in central Vietnam. It is composed of 16 wards and five communes with a total of 284 km². Quy Nhon is the capital of Binh Dinh Province.",
    "Description":"Quy Nhon is a lively and pleasant city virtually half way between the popular cities of Nha Trang and Hoi An. The city is known for its beautiful surroundings, Cham temples, and nearby beaches. The fact that this little corner of Viet Nam has been undiscovered by the majority of travelers means an authentic experience awaits those who come here. Unlike in the larger cities, the locals are extremely hospitable are genuinely glad to see visitors. Quy Nhon is surrounded by green mountains on three sides and the ocean on the fourth. Nestled in a bay, the city is protected from the effects of the worst hurricanes that batter the coast further north. The bay also provides for the livelihood of many as witnessed by fishermen bringing their catch, women cleaning and selling the product of their work, and patrons enjoying some of the freshest and tastiest seafood in restaurants. Quy Nhon is fantastic for cycling. The main promenade runs directly next to the beach and has very little traffic. Bicycles are also great for exploring the nearby temples and beaches, which are too far to walk to."
    },
    {"Id":8, 
    "Place":"Nha Trang",
    "Region":"Central Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal"],
    "Location":"Nha Trang is a coastal city and capital of Khanh Hoa Province, on the South Central Coast of Vietnam. It is bounded on the north by Ninh Hoa district, on the south by Cam Ranh town and on the west by Dien Khanh District.",
    "Description":"Traces of human settlement in Nha Trang date back to the Cham Empire, though in times of Vietnamese rule, there wasn’t much more than small fishing villages. The French recognized that this beautiful bay, with its islands and white sand beaches, made for a perfect bathing spot, and began the transformation into a resort town. American soldiers agreed, and Nha Trang became a favorite vacation stop during the war. The monsoon season is from October to mid December. Sea winds can be heavy, and sometimes the weather can get pretty chilly. Summer, naturally, brings many vacation goers into town and hotel rooms get somewhat more difficult to find. Nha Trang beach city is well known for its pristine beaches and excellent scuba diving and is fast becoming a popular destination for international tourists, attracting large numbers of backpackers as well as more affluent travelers on the Southeast Asia circuit. It is already very popular with Vietnamese tourists. Nha Trang Bay is widely considered as amongst the world's most beautiful bays. The possibly most beautiful street of Nha Trang is Tran Phu Street along the seaside, sometimes referred to as the Pacific Coast Highway of Vietnam."
    },
    {"Id":9, 
    "Place":"Phu Quoc Island",
    "Region":"Southern Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal"],
    "Location":"Phu Quoc is the largest island in Vietnam. Phu Quoc and nearby islands, along with distant Tho Chu Islands, is part of Kien Giang Province as Phu Quoc District.",
    "Description":"Phu Quoc island is a part of Kien Giang province. It is the largest island of Vietnam, with a total acreage of 574 square kilometers. Besides the charming beaches, this place is also famous for being the largest camp for prisoners of South Vietnam during the Vietnam War. Nowadays, many people come here for a quick escape to the beach town or to get closer to mother nature while trekking or camping in the national park. Phú Quốc Island has a tropical climate which has three seasons: High, Shoulder and Low Season. High Season: During the period between November to March, where the daily maximum temperature is typically and on average about 31 C, and the daily minimum temperatures (before sunrise) about 23 C. The skies are generally sunny, with possibly some light high cloud in early morning that clears by mid-morning, and the humidity is at it lowest throughout the year. Shoulder Season: During the period between April to June and late October, where the temperatures are a bit higher than during the high season, and the humidity around 80-85%. Crowds are less during this time and good chances of reasonable weather. Low Season: During the period between July to September, which is dominated by the monsoons."
    },
    {"Id":10, 
    "Place":"Cai Be floating market",
    "Region":"Southern Vietnam",
    "Season":["Spring","Summer","Autumn","Winter"],
    "Geography":["Plain"],
    "Location":"Cai Be is a river-land mixed town in Vietnam. It is a rural district of Tien Giang Province in the Mekong Delta region of Vietnam.",
    "Description":"Together with Cai Rang, Phung Hiep, Phong Dien Floating Markets, Cai Be Floating Market stands out as one of the noticeable and influential markets in Mekong Delta. Although its origin is still unknown, many people still consider that the market was formed by those from the central of the country in 17th to 18th centuries, during time of the formation of the delta. They were known as the first founders who cultivated and settled down the delta for a long time. As per what Gia Dinh Thanh Thong Chi recorded, in 1732, Nguyen Lord declared to start constructing Long Ho Town at Cai Be Town. Every day, lots of boats and rafts in the delta gather here to trade and do business. Although the market is often open all day, the liveliest time is at sunrise. Some sellers visit the market to purchase products from the merchant. Then, these will be brought back the markets on land for sale.The floating market lies in the area where the Tien River shares the border between 3 provinces of Tien Giang, Vinh Long as well as Ben Tre. Mingling with the bustling vibe and robust atmosphere of the market, visitors’ mind will feel the rhythm of the brandishing water flow and be mesmerized by the vastness of the Mekong River."
    },
    {"Id":11, 
    "Place":"Mui Ne",
    "Region":"Southern Vietnam",
    "Season":["Summer"],
    "Geography":["Coastal"],
    "Location":"Mui Ne is a coastal fishing town in the south-central Binh Thuan Province of Vietnam. The town, with approximately 25,000 residents, is a ward of the city of Phan Thiet.",
    "Description":"22 kilometers North Eastern Phan Thiet, Binh Thuan Province, Mui Ne is a group of beaches, such as Ong Dia beach, Front beach and Back Beach. The name “Mui Ne” derived from the fact that fishersmen get in here to hide the storm on their fishing days. “Mui” means cape, and “Ne” means hiding. Tourists can easily be attracted by the deep blue of the sea, the goldern of the sun and sand, all converging in warmth and purity. Mui Ne ward itself has two beaches; Ganh Beach and Suoi Nuoc Beach, both with an increasing number of resorts, shops and restaurants. Strong sea breezes make all the beaches of Phan Thiet very popular for kitesurfing and windsurfing. Rang Beach in Ham Tien ward was first discovered by many foreigners when they descended on the area on October 24, 1995 to watch a solar eclipse. Scientists had predicted that one of the best places in the world to see the total eclipse was on the beaches northeast of the Phan Thiet city center."
    },
    {"Id":12, 
    "Place":"Vung Tau",
    "Region":"Southern Vietnam",
    "Season":["Summer","Spring","Autumn","Winter"],
    "Geography":["Coastal","Mountainous"],
    "Location":"Vung Tau is the largest city and former capital of Ba Ria–Vung Tau Province in Vietnam.",
    "Description":"Located in the South of Viet Nam, 125 km away from Ho Chi Minh, Vung Tau is now considered the most popular destination for weekends from Ho Chi Minh. Vung Tau lies on a peninsula separated from the mainland by a gulf river called Co May river. It is a common saying that Vung Tau is naturally endowed of beautiful beaches, mountains around the city and cool climate throughout the year. Tourists cannot miss the extremely beautiful shore, the old famous light house, the statue of Jesus Christ with outstretched arms, unending delicious food and many more recreational venues. Located in Southern Vietnam, Vung Tau has only two seasons in a year. Dry season (November - April) is dry and slightly cooler during winter months and around Tet Holiday. The weather gets hotter in April. Rainy season (May - October) is rainy, but less than Ho Chi Minh City, usually hot at noon till 3PM. Summer is ideal for sea bathing. Vung Tau is rather small in size, so don't hesitate to take a walk. Recommended ways are: Bacu street (the city's downtown), Đo Chieu Street (food center), Trung Trac and Trung Nhị Square, Front Beach park and pavements along the coastline."
    }

]
x = mycoll.insert_many(mylist)

