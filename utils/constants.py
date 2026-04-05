import os
import random

from config import SERVER_ID

# Server flag emojis
SERVER_FLAGS = {
    'us1': '🇺🇸 US1', 'us2': '🇺🇸 US2', 'us3': '🇺🇸 US3',
    'nl': '🇳🇱 NL', 'neth': '🇳🇱 NETH',
    'sg': '🇸🇬 SG', 'jp': '🇯🇵 JP',
    'de': '🇩🇪 DE', 'uk': '🇬🇧 UK', 'fr': '🇫🇷 FR',
    'id': '🇮🇩 ID', 'in': '🇮🇳 IN', 'au': '🇦🇺 AU',
    'co': '🌐 BOT',
}
SERVER_DISPLAY = SERVER_FLAGS.get(SERVER_ID, f'🌐 {SERVER_ID.upper()}')
CMD_NAME = SERVER_ID

PROXY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "proxies.json")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  Browser Profiles — TLS + UA always matched
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Each entry maps a curl_cffi TLS profile to its compatible User-Agent strings.
# This ensures the TLS fingerprint (JA3/JA4) matches the UA being sent.
BROWSER_PROFILES = [
    # ── Chrome 136 (latest stable, March 2026) ──
    {"tls": "chrome136", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"},
    {"tls": "chrome136", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"},
    {"tls": "chrome136", "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"},
    # ── Chrome 134 ──
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"},
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"},
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"},
    # ── Chrome 133 ──
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"},
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"},
    # ── Chrome 131 (still common) ──
    {"tls": "chrome131", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"},
    {"tls": "chrome131", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"},
    # ── Edge 136 (latest, Chromium-based) ──
    {"tls": "chrome136", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"},
    {"tls": "chrome136", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"},
    # ── Edge 134 ──
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"},
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"},
    # ── Firefox 137 (latest stable) ──
    {"tls": "firefox135", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"},
    {"tls": "firefox135", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0"},
    {"tls": "firefox135", "ua": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0"},
    # ── Firefox 135 ──
    {"tls": "firefox135", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0"},
    {"tls": "firefox135", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0"},
    {"tls": "firefox135", "ua": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"},
    # ── Safari 18.3 (macOS Sequoia, latest) ──
    {"tls": "safari18_0", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15"},
    {"tls": "safari18_0", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3 Safari/605.1.15"},
    # ── Safari 18.1 ──
    {"tls": "safari18_0", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15"},
    {"tls": "safari18_0", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15"},
    # ── Opera 117 (latest, Chrome 136 based) ──
    {"tls": "chrome136", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 OPR/117.0.0.0"},
    {"tls": "chrome133a", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/116.0.0.0"},
    {"tls": "chrome131", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0"},
]

# Derived lists for backward compatibility
USER_AGENTS = [p["ua"] for p in BROWSER_PROFILES]
TLS_PROFILES = list(set(p["tls"] for p in BROWSER_PROFILES))

# Stripe.js version patterns
STRIPE_JS_VERSIONS = [
    "v3", "v3.1", "v3.2", "v3.3", "v3.4", "v3.5",
]


def get_random_browser_profile() -> dict:
    """Pick a random browser profile with matched TLS + UA.
    Returns dict with 'tls' and 'ua' keys."""
    return random.choice(BROWSER_PROFILES)

# Pool of realistic billing addresses organized by country code
BILLING_ADDRESSES_BY_COUNTRY = {
    "US": [
        {"name": "James Wilson", "line1": "742 Evergreen Terrace", "city": "Springfield", "state": "IL", "zip": "62704"},
        {"name": "Sarah Johnson", "line1": "1520 Oak Street", "city": "San Francisco", "state": "CA", "zip": "94117"},
        {"name": "Michael Brown", "line1": "308 Meadow Lane", "city": "Austin", "state": "TX", "zip": "78701"},
        {"name": "Emily Davis", "line1": "2145 Birch Drive", "city": "Denver", "state": "CO", "zip": "80202"},
        {"name": "Robert Martinez", "line1": "987 Pine Avenue", "city": "Miami", "state": "FL", "zip": "33101"},
        {"name": "Jessica Taylor", "line1": "1100 Maple Road", "city": "Seattle", "state": "WA", "zip": "98101"},
        {"name": "David Anderson", "line1": "456 Cedar Boulevard", "city": "Portland", "state": "OR", "zip": "97201"},
        {"name": "Ashley Thomas", "line1": "2301 Elm Street", "city": "Chicago", "state": "IL", "zip": "60601"},
        {"name": "Christopher Lee", "line1": "789 Walnut Court", "city": "Boston", "state": "MA", "zip": "02101"},
        {"name": "Amanda White", "line1": "1435 Spruce Way", "city": "Nashville", "state": "TN", "zip": "37201"},
        {"name": "Daniel Harris", "line1": "562 Willow Lane", "city": "Phoenix", "state": "AZ", "zip": "85001"},
        {"name": "Stephanie Clark", "line1": "3200 Ash Drive", "city": "Las Vegas", "state": "NV", "zip": "89101"},
        {"name": "Matthew Lewis", "line1": "871 Poplar Street", "city": "Atlanta", "state": "GA", "zip": "30301"},
        {"name": "Jennifer Robinson", "line1": "1028 Magnolia Ave", "city": "Charlotte", "state": "NC", "zip": "28201"},
        {"name": "Andrew Walker", "line1": "445 Hickory Road", "city": "Minneapolis", "state": "MN", "zip": "55401"},
        {"name": "Lauren Hall", "line1": "1567 Chestnut Blvd", "city": "San Diego", "state": "CA", "zip": "92101"},
        {"name": "Joshua Allen", "line1": "2890 Sycamore Dr", "city": "Dallas", "state": "TX", "zip": "75201"},
        {"name": "Megan Young", "line1": "634 Dogwood Lane", "city": "Philadelphia", "state": "PA", "zip": "19101"},
        {"name": "Ryan King", "line1": "1750 Juniper Street", "city": "Columbus", "state": "OH", "zip": "43201"},
        {"name": "Brittany Wright", "line1": "903 Redwood Ave", "city": "San Antonio", "state": "TX", "zip": "78201"},
    ],
    "GB": [
        {"name": "Oliver Smith", "line1": "42 Baker Street", "city": "London", "state": "England", "zip": "W1U 7EU"},
        {"name": "Charlotte Davies", "line1": "15 Victoria Road", "city": "Manchester", "state": "England", "zip": "M1 1AA"},
        {"name": "George Wilson", "line1": "78 Queen Street", "city": "Edinburgh", "state": "Scotland", "zip": "EH2 1JX"},
        {"name": "Emily Taylor", "line1": "23 Castle Road", "city": "Birmingham", "state": "England", "zip": "B1 1BB"},
        {"name": "Harry Brown", "line1": "9 Park Lane", "city": "Bristol", "state": "England", "zip": "BS1 5AH"},
    ],
    "CA": [
        {"name": "Liam Thompson", "line1": "450 Yonge Street", "city": "Toronto", "state": "ON", "zip": "M5B 1T8"},
        {"name": "Sophie Martin", "line1": "1200 Rue Sainte-Catherine", "city": "Montreal", "state": "QC", "zip": "H3B 1K1"},
        {"name": "Ethan Wilson", "line1": "800 Robson Street", "city": "Vancouver", "state": "BC", "zip": "V6Z 3B7"},
        {"name": "Olivia Brown", "line1": "320 Portage Avenue", "city": "Winnipeg", "state": "MB", "zip": "R3C 0C4"},
        {"name": "Noah Davis", "line1": "156 Sparks Street", "city": "Ottawa", "state": "ON", "zip": "K1P 5B9"},
    ],
    "AU": [
        {"name": "Jack Mitchell", "line1": "120 Collins Street", "city": "Melbourne", "state": "VIC", "zip": "3000"},
        {"name": "Mia Johnson", "line1": "88 George Street", "city": "Sydney", "state": "NSW", "zip": "2000"},
        {"name": "William Taylor", "line1": "45 Adelaide Street", "city": "Brisbane", "state": "QLD", "zip": "4000"},
        {"name": "Ella Brown", "line1": "200 Murray Street", "city": "Perth", "state": "WA", "zip": "6000"},
    ],
    "DE": [
        {"name": "Lukas Mueller", "line1": "Friedrichstraße 43", "city": "Berlin", "state": "Berlin", "zip": "10117"},
        {"name": "Anna Schmidt", "line1": "Maximilianstraße 15", "city": "Munich", "state": "Bayern", "zip": "80539"},
        {"name": "Felix Weber", "line1": "Hohe Straße 78", "city": "Cologne", "state": "NRW", "zip": "50667"},
        {"name": "Sophie Fischer", "line1": "Mönckebergstraße 22", "city": "Hamburg", "state": "Hamburg", "zip": "20095"},
    ],
    "FR": [
        {"name": "Lucas Dubois", "line1": "25 Rue de Rivoli", "city": "Paris", "state": "Île-de-France", "zip": "75001"},
        {"name": "Emma Martin", "line1": "14 Rue de la République", "city": "Lyon", "state": "Auvergne-Rhône-Alpes", "zip": "69001"},
        {"name": "Hugo Bernard", "line1": "8 Rue Paradis", "city": "Marseille", "state": "PACA", "zip": "13001"},
        {"name": "Chloé Moreau", "line1": "32 Rue du Faubourg", "city": "Toulouse", "state": "Occitanie", "zip": "31000"},
    ],
    "JP": [
        {"name": "Takeshi Yamamoto", "line1": "1-2-3 Shibuya", "city": "Shibuya-ku", "state": "Tokyo", "zip": "150-0002"},
        {"name": "Yuki Tanaka", "line1": "4-5-6 Umeda", "city": "Kita-ku", "state": "Osaka", "zip": "530-0001"},
        {"name": "Kenji Suzuki", "line1": "2-8-1 Nishiki", "city": "Naka-ku", "state": "Aichi", "zip": "460-0003"},
        {"name": "Sakura Watanabe", "line1": "3-1-1 Tenjin", "city": "Chuo-ku", "state": "Fukuoka", "zip": "810-0001"},
    ],
    "SG": [
        {"name": "Wei Ming Tan", "line1": "1 Raffles Place", "city": "Singapore", "state": "Singapore", "zip": "048616"},
        {"name": "Li Hua Lim", "line1": "391 Orchard Road", "city": "Singapore", "state": "Singapore", "zip": "238872"},
        {"name": "Jun Jie Wong", "line1": "80 Marine Parade Road", "city": "Singapore", "state": "Singapore", "zip": "449269"},
    ],
    "NL": [
        {"name": "Daan de Vries", "line1": "Kalverstraat 92", "city": "Amsterdam", "state": "Noord-Holland", "zip": "1012 PH"},
        {"name": "Emma Jansen", "line1": "Lijnbaan 45", "city": "Rotterdam", "state": "Zuid-Holland", "zip": "3012 EL"},
        {"name": "Sem Bakker", "line1": "Lange Viestraat 12", "city": "Utrecht", "state": "Utrecht", "zip": "3511 BK"},
    ],
    "IN": [
        {"name": "Rahul Sharma", "line1": "45 MG Road", "city": "Mumbai", "state": "Maharashtra", "zip": "400001"},
        {"name": "Priya Patel", "line1": "12 Brigade Road", "city": "Bangalore", "state": "Karnataka", "zip": "560001"},
        {"name": "Amit Kumar", "line1": "78 Park Street", "city": "Kolkata", "state": "West Bengal", "zip": "700016"},
        {"name": "Sneha Gupta", "line1": "23 Connaught Place", "city": "New Delhi", "state": "Delhi", "zip": "110001"},
    ],
    "BR": [
        {"name": "Lucas Silva", "line1": "Av. Paulista 1578", "city": "São Paulo", "state": "SP", "zip": "01310-200"},
        {"name": "Ana Oliveira", "line1": "Rua Visconde de Pirajá 330", "city": "Rio de Janeiro", "state": "RJ", "zip": "22410-002"},
        {"name": "Pedro Santos", "line1": "SQS 308 Bloco A", "city": "Brasília", "state": "DF", "zip": "70356-010"},
    ],
    "IT": [
        {"name": "Marco Rossi", "line1": "Via del Corso 112", "city": "Rome", "state": "Lazio", "zip": "00186"},
        {"name": "Giulia Bianchi", "line1": "Via Montenapoleone 8", "city": "Milan", "state": "Lombardia", "zip": "20121"},
        {"name": "Alessandro Ferrari", "line1": "Via Roma 45", "city": "Florence", "state": "Toscana", "zip": "50123"},
    ],
    "ES": [
        {"name": "Carlos García", "line1": "Calle Gran Vía 32", "city": "Madrid", "state": "Madrid", "zip": "28013"},
        {"name": "María López", "line1": "Passeig de Gràcia 55", "city": "Barcelona", "state": "Cataluña", "zip": "08007"},
        {"name": "Pablo Martínez", "line1": "Calle Sierpes 70", "city": "Seville", "state": "Andalucía", "zip": "41004"},
    ],
    "IE": [
        {"name": "Sean Murphy", "line1": "45 Grafton Street", "city": "Dublin", "state": "Dublin", "zip": "D02 VK60"},
        {"name": "Aoife O'Brien", "line1": "12 Patrick Street", "city": "Cork", "state": "Cork", "zip": "T12 X70A"},
        {"name": "Conor Kelly", "line1": "8 Shop Street", "city": "Galway", "state": "Galway", "zip": "H91 XR85"},
    ],
    "SE": [
        {"name": "Erik Lindberg", "line1": "Drottninggatan 53", "city": "Stockholm", "state": "Stockholm", "zip": "111 21"},
        {"name": "Astrid Johansson", "line1": "Vallgatan 12", "city": "Gothenburg", "state": "Västra Götaland", "zip": "411 16"},
        {"name": "Oscar Andersson", "line1": "Södra Förstadsgatan 24", "city": "Malmö", "state": "Skåne", "zip": "211 43"},
    ],
    "CH": [
        {"name": "Thomas Müller", "line1": "Bahnhofstrasse 21", "city": "Zurich", "state": "Zürich", "zip": "8001"},
        {"name": "Laura Weber", "line1": "Rue du Rhône 48", "city": "Geneva", "state": "Genève", "zip": "1204"},
        {"name": "Marc Schneider", "line1": "Marktgasse 15", "city": "Bern", "state": "Bern", "zip": "3011"},
    ],
    "NZ": [
        {"name": "James Taylor", "line1": "125 Queen Street", "city": "Auckland", "state": "Auckland", "zip": "1010"},
        {"name": "Sophie Williams", "line1": "88 Lambton Quay", "city": "Wellington", "state": "Wellington", "zip": "6011"},
        {"name": "Ben Martin", "line1": "45 Colombo Street", "city": "Christchurch", "state": "Canterbury", "zip": "8013"},
    ],
    "HK": [
        {"name": "Kevin Chan", "line1": "1 Queen's Road Central", "city": "Central", "state": "Hong Kong", "zip": "999077"},
        {"name": "Amy Wong", "line1": "100 Nathan Road", "city": "Tsim Sha Tsui", "state": "Kowloon", "zip": "999077"},
        {"name": "David Lau", "line1": "68 Hennessy Road", "city": "Wan Chai", "state": "Hong Kong", "zip": "999077"},
    ],
    "MY": [
        {"name": "Ahmad bin Ibrahim", "line1": "Lot 10, Jalan Bukit Bintang", "city": "Kuala Lumpur", "state": "WP KL", "zip": "55100"},
        {"name": "Siti Nurhaliza", "line1": "22 Jalan Sultan Ismail", "city": "Kuala Lumpur", "state": "WP KL", "zip": "50250"},
        {"name": "Tan Wei Ming", "line1": "Gurney Drive 88", "city": "George Town", "state": "Penang", "zip": "10250"},
    ],
    "MX": [
        {"name": "Carlos Hernández", "line1": "Av. Reforma 222", "city": "Mexico City", "state": "CDMX", "zip": "06600"},
        {"name": "María González", "line1": "Calle Morelos 45", "city": "Guadalajara", "state": "Jalisco", "zip": "44100"},
        {"name": "Juan López", "line1": "Av. Constitución 800", "city": "Monterrey", "state": "Nuevo León", "zip": "64000"},
    ],
    "MO": [
        {"name": "Wong Ka Ming", "line1": "Rua de S. Paulo No. 45", "city": "Macau", "state": "Macau", "zip": "999078"},
        {"name": "Chan Mei Ling", "line1": "Av. de Almeida Ribeiro 128", "city": "Macau", "state": "Macau", "zip": "999078"},
        {"name": "Ho Siu Wai", "line1": "Rua do Campo No. 78", "city": "Macau", "state": "Macau", "zip": "999078"},
        {"name": "Leong Chi Keong", "line1": "Estrada do Repouso 32", "city": "Taipa", "state": "Macau", "zip": "999078"},
        {"name": "Lam Pui San", "line1": "Rua de Pedro Coutinho 56", "city": "Macau", "state": "Macau", "zip": "999078"},
    ],
    "DK": [
        {"name": "Magnus Nielsen", "line1": "Strøget 28", "city": "Copenhagen", "state": "Hovedstaden", "zip": "1050"},
        {"name": "Freja Hansen", "line1": "Søndergade 14", "city": "Aarhus", "state": "Midtjylland", "zip": "8000"},
    ],
    "NO": [
        {"name": "Lars Eriksen", "line1": "Karl Johans gate 22", "city": "Oslo", "state": "Oslo", "zip": "0159"},
        {"name": "Nora Larsen", "line1": "Torgallmenningen 8", "city": "Bergen", "state": "Vestland", "zip": "5014"},
    ],
    "FI": [
        {"name": "Mikko Virtanen", "line1": "Aleksanterinkatu 17", "city": "Helsinki", "state": "Uusimaa", "zip": "00100"},
        {"name": "Aino Korhonen", "line1": "Hämeenkatu 12", "city": "Tampere", "state": "Pirkanmaa", "zip": "33100"},
    ],
    "AT": [
        {"name": "Maximilian Gruber", "line1": "Kärntner Straße 38", "city": "Vienna", "state": "Wien", "zip": "1010"},
        {"name": "Anna Huber", "line1": "Getreidegasse 9", "city": "Salzburg", "state": "Salzburg", "zip": "5020"},
    ],
    "BE": [
        {"name": "Lucas Peeters", "line1": "Meir 47", "city": "Antwerp", "state": "Antwerpen", "zip": "2000"},
        {"name": "Emma Dubois", "line1": "Rue Neuve 123", "city": "Brussels", "state": "Bruxelles", "zip": "1000"},
    ],
    "PT": [
        {"name": "Miguel Santos", "line1": "Rua Augusta 274", "city": "Lisbon", "state": "Lisboa", "zip": "1100-053"},
        {"name": "Ana Ferreira", "line1": "Rua de Santa Catarina 112", "city": "Porto", "state": "Porto", "zip": "4000-442"},
    ],
    "PL": [
        {"name": "Jakub Kowalski", "line1": "Nowy Świat 46", "city": "Warsaw", "state": "Mazowieckie", "zip": "00-363"},
        {"name": "Zofia Nowak", "line1": "Floriańska 14", "city": "Kraków", "state": "Małopolskie", "zip": "31-021"},
    ],
    "TH": [
        {"name": "Somchai Prasert", "line1": "123 Sukhumvit Road", "city": "Bangkok", "state": "Bangkok", "zip": "10110"},
        {"name": "Ploy Srisai", "line1": "45 Nimman Road", "city": "Chiang Mai", "state": "Chiang Mai", "zip": "50200"},
    ],
    "PH": [
        {"name": "Juan dela Cruz", "line1": "123 Ayala Avenue", "city": "Makati", "state": "Metro Manila", "zip": "1226"},
        {"name": "Maria Santos", "line1": "45 Osmeña Boulevard", "city": "Cebu City", "state": "Cebu", "zip": "6000"},
    ],
    "ID": [
        {"name": "Budi Santoso", "line1": "Jl. Sudirman Kav. 52", "city": "Jakarta", "state": "DKI Jakarta", "zip": "12190"},
        {"name": "Siti Rahayu", "line1": "Jl. Malioboro 56", "city": "Yogyakarta", "state": "DIY", "zip": "55271"},
    ],
    "AE": [
        {"name": "Ahmed Al Maktoum", "line1": "Sheikh Zayed Road Tower 1", "city": "Dubai", "state": "Dubai", "zip": "00000"},
        {"name": "Fatima Al Nahyan", "line1": "Corniche Road Villa 23", "city": "Abu Dhabi", "state": "Abu Dhabi", "zip": "00000"},
    ],
}

# Flat list for backward compatibility
BILLING_ADDRESSES = []
for _country, _addrs in BILLING_ADDRESSES_BY_COUNTRY.items():
    for _a in _addrs:
        BILLING_ADDRESSES.append({**_a, "country": _country})

CARD_SEPARATOR = "━ ━ ━ ━ ━ ━━━ ━ ━ ━ ━ ━"
STATUS_EMOJIS = {
    'CHARGED': '😎', 'LIVE': '✅', 'DECLINED': '🥲', '3DS': '😡',
    'ERROR': '💀', 'FAILED': '💀', 'UNKNOWN': '❓'
}

# Decline codes that mean the card is LIVE (valid number, wrong details)
LIVE_DECLINE_CODES = {
    'incorrect_cvc', 'incorrect_zip', 'insufficient_funds',
    'invalid_cvc', 'card_velocity_exceeded', 'do_not_honor',
    'try_again_later', 'not_permitted', 'withdrawal_count_limit_exceeded',
}


def get_random_billing(country: str = None) -> dict:
    """Get a random billing address, matched to country if available.
    
    Priority:
    1. If country is provided and we have addresses for it → use that country
    2. If country not found → fallback to US
    """
    if country:
        country = country.upper().strip()
        if country in BILLING_ADDRESSES_BY_COUNTRY:
            addr = random.choice(BILLING_ADDRESSES_BY_COUNTRY[country])
            return {**addr, "country": country}
    # Fallback to US
    addr = random.choice(BILLING_ADDRESSES_BY_COUNTRY["US"])
    return {**addr, "country": "US"}


def get_currency_symbol(currency: str) -> str:
    symbols = {
        "USD": "$", "EUR": "€", "GBP": "£", "INR": "₹", "JPY": "¥",
        "CNY": "¥", "KRW": "₩", "RUB": "₽", "BRL": "R$", "CAD": "C$",
        "AUD": "A$", "MXN": "MX$", "SGD": "S$", "HKD": "HK$", "THB": "฿",
        "VND": "₫", "PHP": "₱", "IDR": "Rp", "MYR": "RM", "ZAR": "R",
        "CHF": "CHF", "SEK": "kr", "NOK": "kr", "DKK": "kr", "PLN": "zł",
        "TRY": "₺", "AED": "د.إ", "SAR": "﷼", "ILS": "₪", "TWD": "NT$"
    }
    return symbols.get(currency, "")


def format_time(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.2f}s"
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins}m {secs:.2f}s"
