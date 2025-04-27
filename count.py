# Count the number of successful and failed data fetches from the provided logs
log = """
Data fetched for station: Secretariat, Amaravati - APPCB
Data fetched for station: Gulzarpet, Anantapur - APPCB
Data fetched for station: Anand Kala Kshetram, Rajamahendravaram - APPCB
Data fetched for station: Vaikuntapuram, Tirupati - APPCB
Data fetched for station: HB Colony, Vijayawada - APPCB
Data fetched for station: Kanuru, Vijayawada - APPCB
Data fetched for station: PWD Grounds, Vijayawada - APPCB
Data fetched for station: Rajiv Gandhi Park, Vijayawada - APPCB
Data fetched for station: Rajiv Nagar, Vijayawada - APPCB
Data fetched for station: GVM Corporation, Visakhapatnam - APPCB
Data fetched for station: Naharlagun, Naharlagun - APSPCB
Data fetched for station: IITG, Guwahati - PCBA
Data fetched for station: LGBI Airport, Guwahati - PCBA
Data fetched for station: Pan Bazaar, Guwahati - PCBA
Data fetched for station: Railway Colony, Guwahati - PCBA
Data fetched for station: Girls College, Sivasagar - PCBA
Data fetched for station: Kharahiya Basti, Araria - BSPCB
Data fetched for station: New DM Office, Arrah - BSPCB
Data fetched for station: Gurdeo Nagar, Aurangabad - BSPCB
Data fetched for station: Lohiyanagar, Begusarai - BSPCB
Data fetched for station: Kamalnath Nagar, Bettiah - BSPCB
Data fetched for station: DM Office_Kachari Chowk, Bhagalpur - BSPCB
Data fetched for station: Mayaganj, Bhagalpur - BSPCB
Data fetched for station: D M Colony, Bihar Sharif - BSPCB
Data fetched for station: Charitra Van, Buxar - BSPCB
Data fetched for station: Darshan Nagar, Chhapra - BSPCB
Data fetched for station: Town Hall - Lal Bagh, Darbhanga - BSPCB
Data fetched for station: Collectorate, Gaya - BSPCB
Data fetched for station: Kareemganj, Gaya - BSPCB
Data fetched for station: SFTI Kusdihra, Gaya - BSPCB
Data fetched for station: Industrial Area, Hajipur - BSPCB
Data fetched for station: Mirchaibari, Katihar - BSPCB
Data fetched for station: SDM Office_Khagra, Kishanganj - BSPCB
Data fetched for station: Forest Rest House, Manguraha - BSPCB
Data fetched for station: Gandak Colony, Motihari - BSPCB
Data fetched for station: Town Hall, Munger - BSPCB
Data fetched for station: Buddha Colony, Muzaffarpur - BSPCB
Data fetched for station: MIT-Daudpur Kothi, Muzaffarpur - BSPCB
Data fetched for station: Muzaffarpur Collectorate, Muzaffarpur - BSPCB
Data fetched for station: DRM Office Danapur, Patna - BSPCB
Data fetched for station: Govt. High School Shikarpur, Patna - BSPCB
Data fetched for station: IGSC Planetarium Complex, Patna - BSPCB
Data fetched for station: Muradpur, Patna - BSPCB
Data fetched for station: Rajbansi Nagar, Patna - BSPCB
Data fetched for station: Samanpura, Patna - BSPCB
Data fetched for station: Mariam Nagar, Purnia - BSPCB
Data fetched for station: Dangi Tola, Rajgir - BSPCB
Data fetched for station: Police Line, Saharsa - BSPCB
Data fetched for station: DM Office_Kasipur, Samastipur - BSPCB
Data fetched for station: Dada Peer, Sasaram - BSPCB
Data fetched for station: Chitragupta Nagar, Siwan - BSPCB
Data fetched for station: Sector 22, Chandigarh - CPCC
Data fetched for station: Sector-25, Chandigarh - CPCC
Data fetched for station: Sector-53, Chandigarh - CPCC
Data fetched for station: 32Bungalows, Bhilai - CECB
Data fetched for station: Civic Center, Bhilai - Bhilai Steel Plant
Data fetched for station: Hathkhoj, Bhilai - CECB
Data fetched for station: Mangala, Bilaspur - NTPC
Data fetched for station: AIIMS, Raipur - CECB
Data fetched for station: Bhatagaon New ISBT, Raipur - CECB
Data fetched for station: Krishak Nagar, Raipur - CECB
Data fetched for station: Siltara Phase-II, Raipur - CECB
Data fetched for station: Alipur, Delhi - DPCC
Data fetched for station: Anand Vihar, Delhi - DPCC
Data fetched for station: Ashok Vihar, Delhi - DPCC
Data fetched for station: Aya Nagar, Delhi - IMD
Data fetched for station: Bawana, Delhi - DPCC
Data fetched for station: Burari Crossing, Delhi - IMD
Data fetched for station: CRRI Mathura Road, Delhi - IMD
Data fetched for station: Chandni Chowk, Delhi - IITM
Data fetched for station: DTU, Delhi - CPCB
Data fetched for station: Dr. Karni Singh Shooting Range, Delhi - DPCC
Data fetched for station: Dwarka-Sector 8, Delhi - DPCC
Data fetched for station: IGI Airport (T3), Delhi - IMD
Data fetched for station: IHBAS, Dilshad Garden, Delhi - CPCB
Data fetched for station: ITO, Delhi - CPCB
Data fetched for station: Jahangirpuri, Delhi - DPCC
Data fetched for station: Jawaharlal Nehru Stadium, Delhi - DPCC
Data fetched for station: Lodhi Road, Delhi - IITM
Data fetched for station: Lodhi Road, Delhi - IMD
Data fetched for station: Major Dhyan Chand National Stadium, Delhi - DPCC
Data fetched for station: Mandir Marg, Delhi - DPCC
Data fetched for station: Mundka, Delhi - DPCC
Data fetched for station: NSIT Dwarka, Delhi - CPCB
Data fetched for station: Najafgarh, Delhi - DPCC
Data fetched for station: Narela, Delhi - DPCC
Data fetched for station: Nehru Nagar, Delhi - DPCC
Data fetched for station: North Campus, DU, Delhi - IMD
Data fetched for station: Okhla Phase-2, Delhi - DPCC
Data fetched for station: Patparganj, Delhi - DPCC
Data fetched for station: Punjabi Bagh, Delhi - DPCC
Data fetched for station: Pusa, Delhi - DPCC
Data fetched for station: Pusa, Delhi - IMD
Data fetched for station: R K Puram, Delhi - DPCC
Data fetched for station: Rohini, Delhi - DPCC
Data fetched for station: Shadipur, Delhi - CPCB
Data fetched for station: Sirifort, Delhi - CPCB
Data fetched for station: Sonia Vihar, Delhi - DPCC
Data fetched for station: Sri Aurobindo Marg, Delhi - DPCC
Data fetched for station: Vivek Vihar, Delhi - DPCC
Data fetched for station: Wazirpur, Delhi - DPCC
Data fetched for station: Chandkheda, Ahmedabad - IITM
Data fetched for station: Gyaspur, Ahmedabad - IITM
Data fetched for station: Maninagar, Ahmedabad - GPCB
Data fetched for station: Raikhad, Ahmedabad - IITM
Data fetched for station: Rakhial, Ahmedabad - IITM
Data fetched for station: SAC ISRO Bopal, Ahmedabad - IITM
Data fetched for station: SAC ISRO Satellite, Ahmedabad - IITM
Data fetched for station: SVPI Airport Hansol, Ahmedabad - IITM
Data fetched for station: Sardar Vallabhbhai Patel Stadium, Ahmedabad - IITM
Data fetched for station: GIDC, Ankleshwar - GPCB
Data fetched for station: GIFT City, Gandhinagar - IITM
Data fetched for station: IIPHG Lekawada, Gandhinagar - IITM
Data fetched for station: Sector-10, Gandhinagar - GPCB
Data fetched for station: Phase-1 GIDC, Vapi - GPCB
Data fetched for station: Phase-4 GIDC, Vatva - GPCB
Data fetched for station: Patti Mehar, Ambala - HSPCB
Data fetched for station: Arya Nagar, Bahadurgarh - HSPCB
Data fetched for station: H.B. Colony, Bhiwani - HSPCB
Data fetched for station: Mini Secretariat, Charkhi Dadri - HSPCB
Data fetched for station: Municipal Corporation Office, Dharuhera - HSPCB
Data fetched for station: New Industrial Town, Faridabad - HSPCB
Data fetched for station: Sector 11, Faridabad - HSPCB
Data fetched for station: Sector 30, Faridabad - HSPCB
Data fetched for station: Sector-16A, Faridabad - HSPCB
Data fetched for station: Huda Sector, Fatehabad - HSPCB
Data fetched for station: Urban Estate-II, Hisar - HSPCB
Data fetched for station: Police Lines, Jind - HSPCB
Data fetched for station: Rishi Nagar, Kaithal - HSPCB
Data fetched for station: Sector-12, Karnal - HSPCB
Data fetched for station: Shastri Nagar, Narnaul - HSPCB
Data fetched for station: Shyam Nagar, Palwal - HSPCB
Data fetched for station: Sector-6, Panchkula - HSPCB
Data fetched for station: MD University, Rohtak - HSPCB
Data fetched for station: F-Block, Sirsa - HSPCB
Data fetched for station: Murthal, Sonipat - HSPCB
Data fetched for station: Gobind Pura, Yamuna Nagar - HSPCB
Data fetched for station: HIMUDA Complex Phase-1, Baddi - HPPCB
Data fetched for station: Rajbagh, Srinagar - JKSPCB
Data fetched for station: Mohalbani Ghat, Pathardih - DMC
Data fetched for station: Vidayagiri, Bagalkot - KSPCB
Data fetched for station: Ramteerth Nagar, Belgaum - KSPCB
Data fetched for station: BTM Layout, Bengaluru - CPCB
Data fetched for station: BWSSB Kadabesanahalli, Bengaluru - CPCB
Data fetched for station: Bapuji Nagar, Bengaluru - KSPCB
Data fetched for station: City Railway Station, Bengaluru - KSPCB
Data fetched for station: Hebbal, Bengaluru - KSPCB
Data fetched for station: Hombegowda Nagar, Bengaluru - KSPCB
Data fetched for station: Jayanagar 5th Block, Bengaluru - KSPCB
Data fetched for station: Jigani, Bengaluru - KSPCB
Data fetched for station: Kasturi Nagar, Bengaluru - KSPCB
Data fetched for station: Peenya, Bengaluru - CPCB
Data fetched for station: RVCE-Mailasandra, Bengaluru - KSPCB
Data fetched for station: Sanegurava Halli, Bengaluru - KSPCB
Data fetched for station: Shivapura_Peenya, Bengaluru - KSPCB
Data fetched for station: Silk Board, Bengaluru - KSPCB
Data fetched for station: Chikkaballapur Rural, Chikkaballapur - KSPCB
Data fetched for station: Kalyana Nagara, Chikkamagaluru - KSPCB
Data fetched for station: Devaraj Urs Badavane, Davanagere - KSPCB
Data fetched for station: Panchal Nagar, Gadag - KSPCB
Data fetched for station: B.Katihalli, Hassan - KSPCB
Data fetched for station: Ashwini Nagar, Haveri - KSPCB
Data fetched for station: Deshpande Nagar, Hubballi - KSPCB
Data fetched for station: Lingaraj Nagar, Hubballi - KSPCB
Data fetched for station: Lal Bahadur Shastri Nagar, Kalaburagi - KSPCB
Data fetched for station: Mahatma Basaveswar Colony, Kalaburgi - KSPCB
Data fetched for station: Tamaka Ind. Area, Kolar - KSPCB
Data fetched for station: Diwator Nagar, Koppal - KSPCB
Data fetched for station: Stuart Hill, Madikeri - KSPCB
Data fetched for station: Kadri, Mangalore - KSPCB
Data fetched for station: Hebbal 1st Stage, Mysuru - KSPCB
Data fetched for station: Haji Colony, Raichur - KSPCB
Data fetched for station: Vijay Nagar, Ramanagara - KSPCB
Data fetched for station: Vinoba Nagara, Shivamogga - KSPCB
Data fetched for station: Brahmagiri, Udupi - KSPCB
Data fetched for station: Ibrahimpur, Vijayapura - KSPCB
Data fetched for station: Collector Office, Yadgir - KSPCB
Data fetched for station: Udyogamandal, Eloor - Kerala PCB
Data fetched for station: Thavakkara, Kannur - Kerala PCB
Data fetched for station: Vyttila, Kochi - Kerala PCB
Data fetched for station: Polayathode, Kollam - Kerala PCB
Data fetched for station: Palayam, Kozhikode - Kerala PCB
Data fetched for station: Kariavattom, Thiruvananthapuram - Kerala PCB
Data fetched for station: Plammoodu, Thiruvananthapuram - Kerala PCB
Data fetched for station: Corporation Ground, Thrissur - Kerala PCB
Data fetched for station: Idgah Hills, Bhopal - MPPCB
Data fetched for station: Paryavaran Parisar, Bhopal - MPPCB
Data fetched for station: T T Nagar, Bhopal - MPPCB
Data fetched for station: Shrivastav Colony, Damoh - MPPCB
Data fetched for station: Bhopal Chauraha, Dewas - MPPCB
Data fetched for station: City Center, Gwalior - MPPCB
Data fetched for station: Deen Dayal Nagar, Gwalior - MPPCB
Data fetched for station: Maharaj Bada, Gwalior - MPPCB
Data fetched for station: Phool Bagh, Gwalior - Mondelez Ind. Food
Data fetched for station: Chhoti Gwaltoli, Indore - MPPCB
Data fetched for station: Govindh Bhavan Colony, Jabalpur - JMC
Data fetched for station: Gupteshwar, Jabalpur - JMC
Data fetched for station: Marhatal, Jabalpur - MPPCB
Data fetched for station: Suhagi, Jabalpur - JMC
Data fetched for station: Gole Bazar, Katni - MPPCB
Data fetched for station: Sahilara, Maihar - KJS Cements
Data fetched for station: Sector-D Industrial Area, Mandideep - MPPCB
Data fetched for station: Sector-2 Industrial Area, Pithampur - MPPCB
Data fetched for station: Shasthri Nagar, Ratlam - IPCA Lab
Data fetched for station: Civil Lines, Sagar - MPPCB
Data fetched for station: Deen Dayal Nagar, Sagar - MPPCB
Data fetched for station: Bandhavgar Colony, Satna - Birla Cement
Data fetched for station: Mahakaleshwar Temple, Ujjain - MPPCB
Data fetched for station: MIDC Chilkalthana, Aurangabad - MPCB
Data fetched for station: More Chowk Waluj, Aurangabad - MPCB
Data fetched for station: Rachnakar Colony, Aurangabad - MPCB
Data fetched for station: Gokul Nagar, Bhiwandi - MPCB
Data fetched for station: Chauhan Colony, Chandrapur - MPCB
Data fetched for station: MIDC Khutala, Chandrapur - MPCB
Data fetched for station: Khadakpada, Kalyan - MPCB
Data fetched for station: Pimpleshwar Mandir, Kalyan - MPCB
Data fetched for station: Bandra Kurla Complex, Mumbai - IITM
Data fetched for station: Bandra Kurla Complex, Mumbai - MPCB
Data fetched for station: Bandra, Mumbai - MPCB
Data fetched for station: Borivali East, Mumbai - IITM
Data fetched for station: Borivali East, Mumbai - MPCB
Data fetched for station: Byculla, Mumbai - BMC
Data fetched for station: Chakala-Andheri East, Mumbai - IITM
Data fetched for station: Chembur, Mumbai - MPCB
Data fetched for station: Chhatrapati Shivaji Intl. Airport (T2), Mumbai - MPCB
Data fetched for station: Colaba, Mumbai - MPCB
Data fetched for station: Deonar, Mumbai - IITM
Data fetched for station: Ghatkopar, Mumbai - BMC
Data fetched for station: Kandivali East, Mumbai - MPCB
Data fetched for station: Kandivali West, Mumbai - BMC
Data fetched for station: Kherwadi_Bandra East, Mumbai - MPCB
Data fetched for station: Khindipada-Bhandup West, Mumbai - IITM
Data fetched for station: Kurla, Mumbai - MPCB
Data fetched for station: Malad West, Mumbai - IITM
Data fetched for station: Mazgaon, Mumbai - IITM
Data fetched for station: Mindspace-Malad West, Mumbai - MPCB
Data fetched for station: Mulund West, Mumbai - MPCB
Data fetched for station: Navy Nagar-Colaba, Mumbai - IITM
Data fetched for station: Powai, Mumbai - MPCB
Data fetched for station: Sewri, Mumbai - BMC
Data fetched for station: Shivaji Nagar, Mumbai - BMC
Data fetched for station: Siddharth Nagar-Worli, Mumbai - IITM
Data fetched for station: Sion, Mumbai - MPCB
Data fetched for station: Vasai West, Mumbai - MPCB
Data fetched for station: Vile Parle West, Mumbai - MPCB
Data fetched for station: Worli, Mumbai - MPCB
Data fetched for station: Ambazari, Nagpur - MPCB
Data fetched for station: Mahal, Nagpur - MPCB
Data fetched for station: Opp GPO Civil Lines, Nagpur - MPCB
Data fetched for station: Ram Nagar, Nagpur - MPCB
Data fetched for station: Gangapur Road, Nashik - MPCB
Data fetched for station: Hirawadi, Nashik - MPCB
Data fetched for station: MIDC Ambad, Nashik - MPCB
Data fetched for station: Pandav Nagari, Nashik - MPCB
Data fetched for station: Airoli, Navi Mumbai - MPCB
Data fetched for station: Kopripada-Vashi, Navi Mumbai - MPCB
Data fetched for station: Mahape, Navi Mumbai - MPCB
Data fetched for station: Nerul, Navi Mumbai - MPCB
Data fetched for station: Sanpada, Navi Mumbai - MPCB
Data fetched for station: Sector-19A Nerul, Navi Mumbai - IITM
Data fetched for station: Sector-2E Kalamboli, Navi Mumbai - MPCB
Data fetched for station: Tondare-Taloja, Navi Mumbai - MPCB
Data fetched for station: Alandi, Pune - IITM
Data fetched for station: Bhosari, Pune - IITM
Data fetched for station: Bhumkar Nagar, Pune - IITM
Data fetched for station: Dhankawadi, Pune - IITM
Data fetched for station: Hadapsar, Pune - IITM
Data fetched for station: Karve Road, Pune - MPCB
Data fetched for station: Katraj Dairy, Pune - MPCB
Data fetched for station: MIT-Kothrud, Pune - IITM
Data fetched for station: Mhada Colony, Pune - IITM
Data fetched for station: Panchawati_Pashan, Pune - IITM
Data fetched for station: Revenue Colony-Shivajinagar, Pune - IITM
Data fetched for station: Savitribai Phule Pune University, Pune - MPCB
Data fetched for station: Transport Nagar-Nigdi, Pune - IITM
Data fetched for station: Dnyaneshwar Nagar, Solapur - MPCB
Data fetched for station: Ratandeep Housing Society, Solapur - MPCB
Data fetched for station: Solapur, Solapur - MPCB
Data fetched for station: Kasarvadavali, Thane - MPCB
Data fetched for station: Upvan Fort, Thane - MPCB
Data fetched for station: Sidhi Vinayak Nagar, Ulhasnagar - MPCB
Data fetched for station: Bolinj, Virar - MPCB
Data fetched for station: DM College of Science, Imphal - Manipur PCB
Data fetched for station: Manipur University, Imphal - Manipur PCB
Data fetched for station: JN Stadium, Shillong - Meghalaya PCB
Data fetched for station: Lumpyngngad, Shillong - Meghalaya PCB
Data fetched for station: Sikulpuikawn, Aizawl - Mizoram PCB
Data fetched for station: PWD Juction, Kohima - NPCB
Data fetched for station: GM Office, Brajrajnagar - OSPCB
Data fetched for station: Talcher Coalfields,Talcher - OSPCB
Data fetched for station: Jawahar Nagar, Puducherry - PPCC
Data fetched for station: Golden Temple, Amritsar - PPCB
Data fetched for station: Hardev Nagar, Bathinda - PPCB
Data fetched for station: Civil Line, Jalandhar - PPCB
Data fetched for station: Kalal Majra, Khanna - PPCB
Data fetched for station: Punjab Agricultural University, Ludhiana - PPCB
Data fetched for station: RIMT University, Mandi Gobindgarh - PPCB
Data fetched for station: Model Town, Patiala - PPCB
Data fetched for station: Ratanpura, Rupnagar - Ambuja Cements
Data fetched for station: Civil Lines, Ajmer - RSPCB
Data fetched for station: Moti Doongri, Alwar - RSPCB
Data fetched for station: RIICO Ind. Area III, Bhiwadi - RSPCB
Data fetched for station: Vasundhara Nagar_UIT, Bhiwadi - RSPCB
Data fetched for station: Subash Chowk, Churu - RSPCB
Data fetched for station: Adarsh Nagar, Jaipur - RSPCB
Data fetched for station: Mansarovar Sector-12, Jaipur - RSPCB
Data fetched for station: Police Commissionerate, Jaipur - RSPCB
Data fetched for station: RIICO Sitapura, Jaipur - RSPCB
Data fetched for station: Sector-2 Murlipura, Jaipur - RSPCB
Data fetched for station: Shastri Nagar, Jaipur - RSPCB
Data fetched for station: Collectorate, Jodhpur - RSPCB
Data fetched for station: Digari Kalan, Jodhpur - RSPCB
Data fetched for station: Jhalamand, Jodhpur - RSPCB
Data fetched for station: Mandor, Jodhpur - RSPCB
Data fetched for station: Samrat Ashok Udhyan, Jodhpur - RSPCB
Data fetched for station: Dhanmandi, Kota - RSPCB
Data fetched for station: Nayapura, Kota - RSPCB
Data fetched for station: Shrinath Puram, Kota - RSPCB
Data fetched for station: Indira Colony Vistar, Pali - RSPCB
Data fetched for station: Ashok Nagar, Udaipur - RSPCB
Data fetched for station: Zero Point GICI, Gangtok - SSPCB
Data fetched for station: Crescent University, Chengalpattu - TNPCB
Data fetched for station: Alandur Bus Depot, Chennai - CPCB
Data fetched for station: Arumbakkam, Chennai - TNPCB
Data fetched for station: Gandhi Nagar_Ennore, Chennai - TNPCB
Data fetched for station: Kodungaiyur, Chennai - TNPCB
Data fetched for station: Manali Village, Chennai - TNPCB
Data fetched for station: Manali, Chennai - CPCB
Data fetched for station: Perungudi, Chennai - TNPCB
Data fetched for station: Royapuram, Chennai - TNPCB
Data fetched for station: Velachery Res. Area, Chennai - CPCB
Data fetched for station: PSG College of Arts and Science, Coimbatore - TNPCB
Data fetched for station: SIDCO Kurichi, Coimbatore - TNPCB
Data fetched for station: Mendonsa Colony, Dindigul - TNPCB
Data fetched for station: Anthoni Pillai Nagar, Gummidipoondi - TNPCB
Data fetched for station: SIPCOT Phase-1, Hosur - TNPCB
Data fetched for station: Bombay Castel, Ooty - TNPCB
Data fetched for station: Chalai Bazaar, Ramanathapuram - TNPCB
Data fetched for station: Sona College of Technology, Salem - TNPCB
Data fetched for station: Meelavittan, Thoothukudi - TNPCB
Data fetched for station: Kumaran College, Tirupur - TNPCB
Data fetched for station: Bollaram Industrial Area, Hyderabad - TSPCB
Data fetched for station: Central University, Hyderabad - TSPCB
Data fetched for station: ECIL Kapra, Hyderabad - TSPCB
Data fetched for station: ICRISAT Patancheru, Hyderabad - TSPCB
Data fetched for station: IDA Pashamylaram, Hyderabad - TSPCB
Data fetched for station: IITH Kandi, Hyderabad - TSPCB
Data fetched for station: Kokapet, Hyderabad - TSPCB
Data fetched for station: Kompally Municipal Office, Hyderabad - TSPCB
Data fetched for station: Nacharam_TSIIC IALA, Hyderabad - TSPCB
Data fetched for station: New Malakpet, Hyderabad - TSPCB
Data fetched for station: Ramachandrapuram, Hyderabad - TSPCB
Data fetched for station: Sanathnagar, Hyderabad - TSPCB
Data fetched for station: Somajiguda, Hyderabad - TSPCB
Data fetched for station: Zoo Park, Hyderabad - TSPCB
Data fetched for station: Bardowali, Agartala - Tripura SPCB
Data fetched for station: Kunjaban, Agartala - Tripura SPCB
Data fetched for station: Manoharpur, Agra - UPPCB
Data fetched for station: Rohta, Agra - UPPCB
Data fetched for station: Sanjay Palace, Agra - UPPCB
Data fetched for station: Sector-3B Avas Vikas Colony, Agra - UPPCB
Data fetched for station: Shahjahan Garden, Agra - UPPCB
Data fetched for station: Shastripuram, Agra - UPPCB
Data fetched for station: New Collectorate, Baghpat - UPPCB
Data fetched for station: Sardar Patel Inter College, Baghpat - UPPCB
Data fetched for station: Civil Lines, Bareilly - UPPCB
Data fetched for station: Rajendra Nagar, Bareilly - UPPCB
Data fetched for station: Yamunapuram, Bulandshahr - UPPCB
Data fetched for station: Nagla Bhau, Firozabad - UPPCB
Data fetched for station: Vibhab Nagar, Firozabad - UPPCB
Data fetched for station: Indirapuram, Ghaziabad - UPPCB
Data fetched for station: Loni, Ghaziabad - UPPCB
Data fetched for station: Sanjay Nagar, Ghaziabad - UPPCB
Data fetched for station: Vasundhara, Ghaziabad - UPPCB
Data fetched for station: Madan Mohan Malaviya Univ. of Tech, Gorakhpur - UPPCB
Data fetched for station: Knowledge Park - III, Greater Noida - UPPCB
Data fetched for station: Knowledge Park - V, Greater Noida - UPPCB
Data fetched for station: Anand Vihar, Hapur - UPPCB
Data fetched for station: Shivaji Nagar, Jhansi - UPPCB
Data fetched for station: FTI Kidwai Nagar, Kanpur - UPPCB
Data fetched for station: IITK, Kanpur - IITK
Data fetched for station: NSI Kalyanpur, Kanpur - UPPCB
Data fetched for station: Nehru Nagar, Kanpur - UPPCB
Data fetched for station: Kalindi Kunj, Khurja - UPPCB
Data fetched for station: B R Ambedkar University, Lucknow - UPPCB
Data fetched for station: Gomti Nagar, Lucknow - UPPCB
Data fetched for station: Kendriya Vidyalaya, Lucknow - CPCB
Data fetched for station: Kukrail Picnic Spot-1, Lucknow - UPPCB
Data fetched for station: Lalbagh, Lucknow - CPCB
Data fetched for station: Nishant Ganj, Lucknow - UPPCB
Data fetched for station: Talkatora District Industries Center, Lucknow - CPCB
Data fetched for station: Ganga Nagar, Meerut - UPPCB
Data fetched for station: Jai Bhim Nagar, Meerut - UPPCB
Data fetched for station: Pallavpuram Phase 2, Meerut - UPPCB
Data fetched for station: Buddhi Vihar, Moradabad - UPPCB
Data fetched for station: Eco Herbal Park, Moradabad - UPPCB
Data fetched for station: Employment Office, Moradabad - UPPCB
Data fetched for station: Jigar Colony, Moradabad - UPPCB
Data fetched for station: Kashiram Nagar, Moradabad - UPPCB
Data fetched for station: Lajpat Nagar, Moradabad - UPPCB
Data fetched for station: Transport Nagar, Moradabad - UPPCB
Data fetched for station: New Mandi, Muzaffarnagar - UPPCB
Data fetched for station: Sector - 125, Noida - UPPCB
Data fetched for station: Sector - 62, Noida - IMD
Data fetched for station: Sector-1, Noida - UPPCB
Data fetched for station: Sector-116, Noida - UPPCB
Data fetched for station: Jhunsi, Prayagraj - UPPCB
Data fetched for station: Motilal Nehru NIT, Prayagraj - UPPCB
Data fetched for station: Nagar Nigam, Prayagraj - UPPCB
Data fetched for station: Ardhali Bazar, Varanasi - UPPCB
Data fetched for station: Bhelupur, Varanasi - UPPCB
Data fetched for station: IESD Banaras Hindu University, Varanasi - UPPCB
Data fetched for station: Maldahiya, Varanasi - UPPCB
Data fetched for station: Omex Eternity, Vrindavan - UPPCB
Data fetched for station: Doon University, Dehradun - UKPCB
Data fetched for station: Asansol Court Area, Asansol - WBPCB
Data fetched for station: Evelyn Lodge, Asansol - WBPCB
Data fetched for station: Mahabir Colliery, Asansol - WBPCB
Data fetched for station: Trivenidevi Bhalotia College, Asansol - WBPCB
Data fetched for station: Mahishkapur Road_B-Zone, Durgapur - WBPCB
Data fetched for station: PCBL Residential Complex, Durgapur - WBPCB
Data fetched for station: Sidhu Kanhu Indoor Stadium, Durgapur - WBPCB
Data fetched for station: Priyambada Housing Estate, Haldia - WBPCB
Data fetched for station: Belur Math, Howrah - WBPCB
Data fetched for station: Botanical Garden, Howrah - WBPCB
Data fetched for station: Dasnagar, Howrah - WBPCB
Data fetched for station: Ghusuri, Howrah - WBPCB
Data fetched for station: Padmapukur, Howrah - WBPCB
Data fetched for station: Ballygunge, Kolkata - WBPCB
Data fetched for station: Bidhannagar, Kolkata - WBPCB
Data fetched for station: Fort William, Kolkata - WBPCB
Data fetched for station: Jadavpur, Kolkata - WBPCB
Data fetched for station: Rabindra Bharati Univ., Kolkata - WBPCB
Data fetched for station: Rabindra Sarobar, Kolkata - WBPCB
Data fetched for station: Victoria, Kolkata - WBPCB
Data fetched for station: Ward-32 Bapupara, Siliguri - WBPCB
"""

# Count the number of data fetched and failed
data_fetched = log.count("Data fetched for station")
data_failed = log.count("Failed to retrieve data for station")

data_fetched, data_failed

print(data_fetched)
print(data_failed)
print(data_fetched+data_failed)

# Extract the list of failed stations from the logs
failed_stations = [line.split(": ", 1)[1] for line in log.splitlines() if "Failed to retrieve data for station" in line]
for station in failed_stations:
     print(station)
