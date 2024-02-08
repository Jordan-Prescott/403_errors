

# filed lists of sites
ALL_SITES = []
MARRIOTT_SITES = []
HYATT_SITES = []
VACATION_CLUB_SITES = []
HILTON_SITES = []
CHOICE_SITES = []

# FourteenIP and others not assigned to brand
OTHER_SITES = []


# files site into correct list
def file_group(site):
    ALL_SITES.append(site)

    if site.brand == "Marriott":
        MARRIOTT_SITES.append(site)
    elif site.brand == "Hyatt":
        HYATT_SITES.append(site)
    elif site.brand == "Vacation Club":
        VACATION_CLUB_SITES.append(site)
    elif site.brand == "Choice":
        CHOICE_SITES.append(site)
    elif site.brand == "Hilton":
        HILTON_SITES.append(site)
    else:
        OTHER_SITES.append(site)




class MagicGroup:
    """ Hotel

        TODO: Comment this!!

        Parameters:
            See EVA Object

    """

    def __init__(self, group_name, group_id, ent_srp, brand, solution_type, trunk_capacity, external_live, external_sandbox, internal_live, internal_sandbox) -> None:

        self.group_name = group_name
        self.group_id = group_id
        self.ent_srp = ent_srp
        self.brand = brand
        self.solution_type = solution_type
        self.trunk_capacity = trunk_capacity

        self.external_live = external_live
        self.external_sandbox = external_sandbox
        self.internal_live = internal_live
        self.internal_sandbox = internal_sandbox

    def __str__(self):
        return f"Hotel - Group Name: {self.group_name}, Group ID: {self.group_id}, Ent/SP: {self.ent_sp}, Brand: {self.brand}, EV Type: " \
               f"{self.solution_type}, Trunk Capacity: {self.trunk_capacity}, EL: {self.external_live}, ES: {self.external_sandbox}, IL: " \
               f"{self.internal_live}, IS: {self.internal_sandbox} "


class EVA(MagicGroup):
    """ EVA

    TODO: Comment this!!

    Parameters:
        variant_id (str): Unique ID of variant on Poly Platform.
    """
    def __init__(self, variant_id, account_id, project_id, project_name, group_name, ent_srp, brand, solution_type, trunk_capacity, external_live, external_sandbox, internal_live, internal_sandbox) -> None:

        super().__init__(variant_id, group_name, ent_srp, brand, solution_type, trunk_capacity, external_live, external_sandbox, internal_live, internal_sandbox)

        self.variant_id = variant_id
        self.account_id = account_id
        self.project_id = project_id
        self.project_name = project_name

        file_group(self)

    def __str__(self):
        return super().__str__() + f"EVA - Variant ID: {self.variant_id}, Account ID: {self.account_id}, " \
                                   f"Project ID: {self.project_id}, Project Name: {self.project_name} "


# EVA SITES: sectioned by project in PolyAI
    
# EVA US    
# Gaylord
MCOGP = EVA("MCOGP", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "Gaylord Palms Resort & Convention Center", "GaylordUS_EV_Full", "Marriott", "EV", 9, 4075860000, 4075860054,4075860053, 4075860055)
DALGT = EVA("DALGT", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "Gaylord Texan Resort & Convention Center", "GaylordUS_EV_Full", "Marriott", "EV", 8, 8177781000, 8177782650, 8177781153, 8177782651)
BNAGO = EVA("BNAGO", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "Gaylord Opryland Resort & Convention Center", "GaylordUS_EV_Full", "Marriott", "EV", 9, 6158891000, 4234568724, 4234568723, 4234568725)
WASGN = EVA("WASGN", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "Gaylord National Resort", "GaylordUS_EV_Full", "Marriott", "EV", 9, 3019654000, 2402699237, 2402699236, 2402699240)
DENGR = EVA("DENGR", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "Gaylord Rockies Resort & Convention Center", "GaylordUS_EV_Full", "Marriott", "EV", 7, 7204526900, 7194089303, 7194089302, 7194089304)
BNAGI = EVA("BNAGI", "ACCOUNT-d9a69212", "PROJECT-33659193", "Gaylord", "The Inn at Opryland A Gaylord Hotel", "GaylordUS_EV_Full", "Marriott", "EV", 2, 6158890800, 4234568727, 4234568726, 4234568728)

# AC Hotels
LAXAV = EVA("LAXAV", "ACCOUNT-d9a69212", "ac-hotels--usp", "AC Hotels", "AC Hotel by Marriott Los Angeles Downtown", "MarriottUS_EV_Select", "Marriott", 3, "EV", 2092801859, 2093895218, 2093895217, 2093895219)

# Moxy
LAXOX = EVA("LAXOX", "ACCOUNT-d9a69212", "moxy-usp", "Moxy", "Moxy Los Angeles Downtown", "MarriottUS_EV_Select", "Marriott", "EV", 3, 2092801846, 2092801855, 2092801854, 2093895216)

# Marriott 
AGSMC = EVA("AGSMC", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "Augusta Marriott at the Convention Centre", "MarriottUS_EV_Full", "Marriott", "EV", 1, 7067228900, 4783519220, 4783519219, 4783519221)
MCOSW = EVA("MCOSW", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "Marriott Orlando at SeaWorld", "Marriott_Lite", "Marriott", "EV", 2,  4073133600, 6896107607, 6896107606, 6896107608)
MSYLA = EVA("MSYLA", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "New Orleans Marriott", "Marriott_USA", "Marriott", "SIP Trunks", 5,  5045811000, 2254279117, 2254279116, 2254279118)
MCOWC = EVA("MCOWC", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "Orlando World Center Marriott", "Marriott_USA", "Marriott", "SIP Trunks", 6,  4072394200, 3215218002, "N/A", "N/A")
SATRC = EVA("SATRC", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "San Antonio Riverwalk", "Marriott_USA", "Marriott", "EV", 5, 2102231000, 3866959325, 3866959324, 3866959326)
SATDT = EVA("SATDT", "ACCOUNT-d9a69212", "Marriott-new-multi-variant-usp-usp", "Marriott", "San Antonio Marriott Riverwalk", "Marriott_USA", "Marriott", "EV", 3, 2102244555, 3866959329, 3866959328, 3866959330)

# 14IP Internal
FourteenIPUSA = EVA("FourteenIPUSA", "ACCOUNT-d9a69212", "PROJECT-661d852b", "14IP Internal", "FourteenIPUSA", "FourteenIPEV", "Internal", "EV", "" ,4072049014, 2393658474, 2393658466, 2393658478)
FourteenIPUK = EVA("FourteenIP UK", "ACCOUNT-d9a69212", "PROJECT-661d852b", "14IP Internal", "FourteenIP UK", "FourteenIPEV", "Internal", "EV", "", 1942369197, 2030028758,2037578432, 2039078442)

# Delta Hotel By Marriott
YLWOK = EVA("YLWOK", "ACCOUNT-d9a69212", "delta-marriott-grand-usp", "Delta Hotel By Marriott", "Marriott's Grand Okanagan Resort", "Marriott_Lite", "Delta Hotels", "EV", 2, 2507634500, 6042836472, 6042836477, 6042836488)
YVRDB = EVA("YVRDB", "ACCOUNT-d9a69212", "delta-marriott-grand-usp", "Delta Hotels by Marriott", "Delta Hotels by Marriott Burnaby Conference Center", "Marriott_Lite", "Delta Hotels", "EV", 2, 6044530750, 7864850768, 6044530751, 7867967864)
# NOT LIVE YET - YOWDM = EVA("YOWDM", )
# NOT LIVE YET - YYCBV = EVA("YYCBV", )

# Courtyard Canada
YYZCY = EVA("YYZCY", "ACCOUNT-d9a69212", "courtyard-canada-usp", "Courtyard Canada", "Courtyard by Marriott Toronto Downtown", "MarriottUS_EV_Select", "Marriott", "EV", 5, 4169240611, 2393661014, 2393661013, 2393661017)

# Aloft
CHIAA = EVA("CHIAA", "ACCOUNT-d9a69212", "Aloft-multi-variant-usp", "Aloft", "Aloft Chicago Magnificent Mile", "Tishman", "Marriott", "EV", 2, 3124296600, 2172107062, 2172107057, 2172107068)

# Vacation Club
MCOGV = EVA("MCOGV", "ACCOUNT-d9a69212", "Vacation-club-multi-variant-usp", "Vacation Club", "Marriott's Grande Vista", "Marriott_Vacation_US_EV_Full", "Marriott Vacation Club", "EV", 2, 4072387676, 2393661980, 2393661979, 2393661981)
HHHVI = EVA("HHHVI", "ACCOUNT-d9a69212", "Vacation-club-multi-variant-usp", "Vacation Club", "Marriott's Grande Ocean", "Hilton_Head_USA", "Marriott Vacations Worldwide", "EV", 3, 8436867343, 8036319157, 8036319156, 8036319158)
CTDDS = EVA("CTDDS", "ACCOUNT-d9a69212", "Vacation-club-multi-variant-usp", "Vacation Club", "Marriott Vacation Club Desert Springs Villas", "Marriott_Vacation_US_EV_Full", "Marriott Vacations Worldwide", "EV", 3, 7607791200, 2093895224, 2093895223, 2093895225)
RNOTL = EVA("RNOTL", "ACCOUNT-d9a69212", "Vacation-club-multi-variant-usp", "Vacation Club", "Marriott Vacation Club Timber Lodge", "Marriott_Vacation_US_EV_Full", "Marriott Vacation Club", "EV", 5, 5305426600, 5305426798, 5305426797, 5305426799)

# Sheraton
CHIGS = EVA("CHIGS", "ACCOUNT-d9a69212", "Sheraton-multi-variant-usp", "Sheraton", "Sheraton Grand Chicago", "Tishman", "Marriott", "EV", 5, 3124641000, 2172831854, 2172831853, 2172831855)

# JW (new)
WASJW = EVA("WASJW", "ACCOUNT-d9a69212", "JW-usp", "JW (new)", "JW Marriott Washington", "Marriott_USA", "JW Marriott", "SIP Trunks", 4, 2023932000, 7712085033, 7712085032, 7712085314)

# Westin
MCODW = EVA("MCODW", "ACCOUNT-d9a69212", "Westin-multi-variant-usp", "Westin", "Walt Disney World Swan", "Tishman", "Marriott", "EV", 6, 4079343000, 2393619569, 2393619568, 2393619570)
MCOSI = EVA("MCOSI", "ACCOUNT-d9a69212", "Westin-multi-variant-usp", "Westin", "Walt Disney World Dolphin", "Tishman", "Marriott", "EV", 7, 4079344000, 6892368002, 6892368001, 6892368003)

# Double Tree
EWRNA = EVA("EWRNA", "fourteen_ip_hilton-us", "doubletree-usp", "Double Tree", "DoubleTree by Hilton Hotel Newark Airport", "Hilton_EV_US", "Hilton", "SIP Trunks", 4, 3213061523, 5512481704, 5512481702, 5512481705)

# Autograph
SUXAK = EVA("SUXAK", "ACCOUNT-d9a69212", "autograph-usp", "Autograph", "The Warrior Hotel Autograph Collection", "MarriottUS_EV_Select", "Marriott International", "EV", 2, 7123171011, 7122509497, 7122509489, 7122509877)


# EVA EU
#InterContinental
#NOT LIVE YET: BERHA = EVA("BERHA", "14IP-uk", "intercontinental-ukp", "InterContinental", "InterContinental Berlin", "Standalone_SIPTrunks", "MISSING", "SIP Trunks", 3, 3031196233, 3031196263, 3031196242, 3031196264)

#Marriott France
PARGL = EVA("PARGL", "14IP-uk", "marriott-french-ukp", "Marriott France", "CY Paris Gare de Lyon Bercy SAS", "MarriottEU_EV_Select", "Courtyard", "EV", 2, 180206300, 188831091, 188831090, 188831092)

#Marriott Spain
BIOLC = EVA("BIOLC", "14IP-uk", "marriott-spainish-ukp", "Marriott Spain", "Hotel Marques de Riscal", "MarriottEU", "Luxury Collection", "EV", 2, 945180880, 945880568, 945880567, 945880569)

#Sea Containers
#External numbers here for TLGSEACI are those listed in Broadworks group however EVA is only live with Internal calls
TLGSEACI = EVA("TLGSEACI", "14IP-uk", "sea-containers-ukp", "Sea Containers", "Sea Containers London", "Lore_Group", "Other", "EV", 2, 2038611732, 2038611734, 2038611733, 2038611735)


# Deactivated sites:
# DEACTIVATED: ABVIWIN = EVA("ABVIWIN", "ACCOUNT-d9a69212", "americas-best-value-inn", "Americas Best Vallue Inn", "America's Best Value Inn Winnemucca", "Choice_Hotels", "Choice", "EV", 7756235281, 7754609212, 7754609211, 7754609213)

# DEACTIVATED: RDWYMCD = EVA("RDWYMCD", "ACCOUNT-d9a69212", "choice-multi-variant-usp", "Choice", "Rodeway Inn McDermitt", "Choice_Hotels", "Choice", "EV", 7754381183, 2393738911, 2393738910, 2393738912)
# DEACTIVATED: ECNLWIN = EVA("ECNLWIN", "ACCOUNT-d9a69212", "choice-multi-variant-usp", "Choice", "Econo Lodge Winnemucca", "Choice_Hotels", "Choice", "EV", 7756233661, 4072040010, 3213061513, 6478481032)
# DEACTIVATED: RDWYWIN = EVA("RDWYWIN", "ACCOUNT-d9a69212", "choice-multi-variant-usp", "Choice", "Rodeway Inn Winnemucca", "Choice_Hotels", "Choice", "EV", 7756231119, 7754609209, 7754609208, 7754609210)

# DEACTIVATED: MCOBUHH = EVA("MCOBUHH", "ACCOUNT-d9a69212", "hilton-multi-variant-usp", "Hilton", "MISSING", "MISSING", "Hilton", "EV", "MISSING", "MISSING", "MISSING", "MISSING")

# DEACTIVATED: PHLDV = EVA("PHLDV", "ACCOUNT-d9a69212", "courtyard-canada-usp", "Courtyard Canada", "Courtyard Devona/Villanova", "Marriott_Lite", "Marriott", "EV", 6106876633, 6104702646, 6104702626, 6104702673)
